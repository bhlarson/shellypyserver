# shelly_server_program_spec.md Program Specification

- **Program Name**: Shelly Server
- **Generated Program Main File**: `shelly_server.py`
- **Author**: Brad Larson
- **Date**: 2026-01-04

## Table of Contents
- [Introduction](#introduction)
- [Specification Description](#specification-description)
- [Creator Interview](#creator-interview)
- [Program Generation Process](#program-generation-process)
- [Program Generation Report](#program-generation-report)
- [Program](#program)
  - [Program Description](#program-description)
  - [Program Structure](#program-structure)
  - [Program Environment](#program-environment)
- [Functional Requirements](#functional-requirements)
- [Acceptance Criteria](#acceptance-criteria)
- [Prompts](#prompts)
- [Tests](#tests)
- [Issues](#issues)
  - [Open Issues](#open-issues)
  - [Resolved Issues](#resolved-issues)

## Introduction
This document specifies **ShellyServer**, an HTTP + MQTT server that interfaces with Shelly devices to enable home automation sequences and provide a web UI for status, control, and configuration. The server will be implemented in Python using FastAPI for the web interface and paho-mqtt for MQTT communication. It will run in a Docker container on a Linux host.  It provides device visibility, control, and user-defined automation sequences based on device states and events.

## Creator Interview

**Date**: 2026-01-04  
**Creator**: Brad Larson  
**Interviewer/Model**: GPT-5.2 Thinking  

### Transcript (condensed but faithful)
- **Program file name**: `shelly_server.py`
- **Purpose**: “HTTP server exposing Shelly lighting control.”
- **Primary user/integration**: Server is **both an MQTT server and a web server**; interfaces with Shelly devices to provide home automation sequences and a web interface for status, control, and configuration.
- **Device support**: Variety of Shelly devices; details provided via config. Can span Shelly versions and device types (relays/lighting).
- **Device management/discovery**: **Config-driven only**, no auto discovery. Config includes device address, credentials, name, MQTT topic, switch type, etc.
- **Deployment**: Runs in a **Docker container on a Linux host**.
- **Operations**: 
  - View devices in web UI
  - View current state via MQTT
  - Control device state
  - View/add/delete “control sequences” (if-this-then-that)
  - Detect device loss/offline + show communication failures
- **Logging**: Structured **JSON logs**, daily rotated (date-stamped). Log **sequence events and failures**, not every MQTT event/state change.
- **Web interface**: Use **FastAPI**, provide REST API + web UI; include `static/` for assets and `index.html`.
- **MQTT library**: `import paho.mqtt.client as mqtt`
- **Sequencing/automation**:
  - Actions support **lists of steps** affecting multiple devices
  - Trigger is a **boolean logical condition** over system state (not a single token)
  - Maintain internal **system state** (perceived state of all devices)
  - On startup, query devices to initialize state
  - On any MQTT event, update system state
  - Support state snapshot save/restore (for testing/evaluation)
  - Periodic “refresh cycle” to reconcile perceived vs actual state, with staggered device polling:
    - Parameter A: refresh cycle start interval (e.g., every N minutes)
    - Parameter B: per-device polling delay within cycle (e.g., every M seconds)

## Program Generation Process
Use a Plan → Act → Critique → Revise loop:
1. Translate requirements to a function/object table and request/response schemas.
2. Implement tests that cover requirements.
3. Implement code to satisfy tests.
4. Iterate until acceptance criteria pass.
5. Record each iteration in the generation report.

## Program Generation Report
Maintain a report file (e.g., `ShellyServer_generation_report.md`) containing per-iteration:
- date, prompts, model, commit/tag
- plan (design, endpoints/topics, data models, risks)
- changes made
- test results
- critique and next revision plan

## Specification Description
This program specification describes a collaborative program generation process.  A programmer will update this specification to direct AI agents to create the desired program.  The agent will create, validate, describe the program generation and the program.  The programmer will review the generated program and tests, update the specification and program to improve the implementation.  The programmer will then re-execute the AI agent to refine the program based on the updated specification.  This process will continue until the program meets all functional requirements and passes all tests.  

This specification:
- defines the program as shelly_server.py
- is not created or modified by the AI agent.  It is only modified by the programmer to direct the AI agent.
- defines the [Program Generation Process](#program-generation-process) to generate the python program shelly_server.py.  Follow this program generation process on each iteration to successfully accomplish the users request.
- defines the [AI Program Generation Report](#ai-program-generation-report) to document each iteration of the program generation process.
- describes the iterative program generation process, we expect to converge reliably to a program that meets all functional requirements and passes all tests through human and AI collaboration.
- describes how the program specification must be connected to the plan, implementation and evaluation artifacts  enabling effective collaboration and convergence
- describes in [Program Generation Report](#program-generation-report) how the design must traceably identify the instructions and requirements from this file it is implementing.
- The [Program Generation Process](#program-generation-process) describes the process to plan generate and evaluate the program while tieing back to this specification.  Each iteration of the program generation process must follow this process.
- The [Functional Requirements](#functional-requirements) describes the required capabilities of this program.  Each of these must be implemented or the failure to implement must be documented in the [AI Program Generation Report](#ai-program-generation-report) section.
- The [Program](#program) provides required structure, libraries, methods, and constraints of the program to be generated.  If the program deviates from this structure, the deviation must be documented in the [AI Program Generation Report](#ai-program-generation-report) section.  
- The [Prompts](#prompts) section describes how prompts and in-context learning are to be created and used in the program.  It also specifies specific prompts and in-context learning configuration files to use. If the prompt implementation deviates from these instructions, the deviation must be documented in the [AI Program Generation Report](#ai-program-generation-report) for this iteration.
- Follow the process in [AI Program Generation Report](#ai-program-generation-report) on each AI Agent iteration to describe and document the program generation process.  Each iteration must be documented as described in that section.
- [Issues](#issues) section describes open and resolved issues in the program generation process or the generated program.  AI agents may be directed to resolve specific open issues in subsequent iterations of the program generation process.  Only focus on the issues that are specifically requested in the agent prompt for each iteration.

## Program

### Program Description

**One sentence**: An HTTP (FastAPI) + MQTT (paho) server that controls and monitors Shelly lighting/relay devices and runs user-defined automation sequences, with a web UI for status/control/config.

#### Inputs
- **Device configuration file**: `config/shelly_devices/devices.yaml`
  - Contains: device id/name, IP/hostname, credentials (optional per device), MQTT topic info, capabilities/switch channels, etc.
- **Sequence configuration**: within the config (either in the same YAML or separate config section/file; see [Sequencing](#sequencing-and-automation)).
- **Runtime parameters** (env vars or CLI flags; to be finalized in implementation):
  - MQTT broker host/port/credentials (if broker is external)
  - web host/port
  - refresh cycle interval and per-device polling delay
  - log directory

#### Outputs
- **REST API** (JSON) for programmatic control and management.
- **Web UI** served by FastAPI:
  - `index.html` UI page
  - `static/` assets
- **MQTT interactions**:
  - subscribe to device topics for events/state
  - publish commands to control devices (as applicable)
- **Logs**:
  - daily JSON log files of sequence executions and failures.
- **System state snapshots**:
  - saved/restored snapshots for testing/evaluation (storage format TBD).

#### Processing
1. Load config from `config/shelly_devices/devices.yaml`.
2. Initialize MQTT client and subscribe to configured topics.
3. Initialize **SystemState** by querying all configured devices (startup sync).
4. Serve FastAPI endpoints and web UI.
5. Update SystemState on MQTT events.
6. Evaluate sequencing conditions when relevant state changes occur.
7. Execute sequence actions (lists of commands), and log results.
8. Run periodic refresh cycles:
   - every `refresh_cycle_interval`, step through devices
   - wait `per_device_poll_delay` between device polls
   - reconcile discrepancies between actual device state and stored state

### Program Structure

#### Suggested directory layout
- `shelly_server.py` (entry point)
- `app/`
  - `api/` (FastAPI routers)
  - `mqtt/` (paho client wrapper, topic mapping)
  - `state/` (SystemState + persistence)
  - `sequences/` (sequence models + evaluator + executor)
  - `devices/` (device abstractions, config parsing)
  - `logging/` (JSON logger + daily rotation)
- `web/`
  - `index.html`
  - `static/` (js/css/assets)
- `config/`
  - `shelly_devices/`
    - `devices.yaml`
- `tests/` (unit + integration)

(Exact layout may be adjusted, but FastAPI must serve `index.html` and a static directory.)

### Program Environment
- **Runtime**: Docker container on Linux host
- **Python**: 3.11+ recommended
- **Web framework**: FastAPI + ASGI server (uvicorn)
- **MQTT**: `paho.mqtt.client` (import as `mqtt`)
- **Config parsing**: YAML (library TBD; e.g., PyYAML or ruamel.yaml)
- **Logging**: structured JSON logs, daily rotation
- **Testing**: pytest

### Shelly MQTT Reference
```text
https://shelly-api-docs.shelly.cloud/gen2/ComponentsAndServices/Mqtt/
```

## Sequencing and Automation

### Sequence model (proposed YAML shape)
```yaml
sequences:
  - id: "sync_press_evening"
    name: "Sync controller press (evening)"
    condition: "events.sync_controller.button_down AND state.living_room_light.on == true"
    actions:
      - type: "set"
        device_id: "kitchen_light"
        channel: 0
        value: "on"
      - type: "toggle"
        device_id: "lamp"
        channel: 0
      - type: "set_level"
        device_id: "dimmer1"
        channel: 0
        value: 35
```

### Condition language
- Boolean expression over SystemState (and optional recent events)
- Operators: AND/OR/NOT, comparisons, and state/event accessors
- Must be sandboxed (no arbitrary code execution)

### System State
- Startup initialization: query all devices to populate initial state
- Event updates: MQTT events update state immediately
- Periodic reconciliation:
  - `refresh_cycle_interval_seconds`
  - `per_device_poll_delay_seconds`
  - Iterate devices one-by-one with delay and reconcile mismatches

### Sequence execution logging
Daily JSON logs record sequence executions and failures (including per-action results), not every MQTT message.

## Functional Requirements

| ID | Requirement | Verification |
|---|---|---|
| FR-001 | Load config from `config/shelly_devices/devices.yaml` and validate required fields. | Unit tests for config parsing and validation. |
| FR-002 | No device auto-discovery; only devices in config are managed. | Integration test confirms only configured devices appear. |
| FR-003 | Run FastAPI server providing REST API + serving `index.html` and `static/`. | Integration test: `/` returns html; `/static/*` works; `/api/health` responds. |
| FR-004 | Use MQTT via `paho.mqtt.client` to subscribe/publish per config. | Integration test with mocked broker; verify subscriptions and publishes. |
| FR-005 | Maintain SystemState and update on MQTT events. | Unit test for event → state update. |
| FR-006 | Initialize SystemState at startup by querying devices. | Integration test verifies startup polling and state populated. |
| FR-007 | Provide device visibility and state in API/UI. | Integration test checks device list includes states. |
| FR-008 | Provide device control operations via REST and routed to MQTT publish. | Integration test validates publish messages created. |
| FR-009 | Provide sequence management: list/add/delete sequences. | Integration test validates CRUD via REST. |
| FR-010 | Sequences support boolean condition triggers and list-of-actions execution. | Unit test for condition eval + action order. |
| FR-011 | Detect device loss/offline and record communication failures; expose in API/UI. | Integration test simulates offline device; verify output. |
| FR-012 | Daily JSON logs record sequence events and failures (not every MQTT event). | Test verifies log content + rotation naming. |
| FR-013 | Periodic reconciliation refresh cycle with staggered polling. | Test verifies scheduling and delays. |
| FR-014 | Save/restore SystemState snapshots for testing/evaluation. | Unit test: save → load equals. |

## Acceptance Criteria

| ID | Description | Criteria for Completion |
|---|---|---|
| AC-1 | Device visibility in Web UI | All configured devices appear with correct status. |
| AC-2 | Device control via REST/UI | Controls publish correct MQTT commands and update state/UI. |
| AC-3 | Sequence execution | Defined sequence executes correctly and is logged. |
| AC-4 | Offline handling | Offline devices detected, displayed, and failures logged. |
| AC-5 | Daily JSON logs | One file per day; logs include sequence events/failures only. |
| AC-6 | Reconciliation refresh | Refresh runs at configured interval and polls devices with per-device delay. |

## Tests

### Unit Tests (starter)
| Test ID | Description | Expected Outcome |
|---|---|---|
| UT-001 | Load/validate `devices.yaml` | Valid passes; invalid fails clearly |
| UT-002 | MQTT event → SystemState update | State matches expected |
| UT-003 | Condition evaluation | Boolean results correct |
| UT-004 | Sequence action list execution | Ordered execution + results captured |
| UT-005 | Daily JSON logging | Correct schema + rotation |
| UT-006 | Refresh staggering | Correct per-device spacing |
| UT-007 | State snapshot roundtrip | Restored equals saved |

### Integration Tests (starter)
| Test ID | Description | Expected Outcome |
|---|---|---|
| IT-001 | Server starts; `/` UI loads; `/api/health` OK | UI + API respond |
| IT-002 | Mock broker; verify subscriptions | Correct topics subscribed |
| IT-003 | Command via REST; verify publish + state | Publish correct; state updates |
| IT-004 | Sequence CRUD via REST | List reflects changes |
| IT-005 | Offline device simulation | Failure detected + exposed |
| IT-006 | Refresh cycle behavior | Polls staggered by delay |

## Issues

### Open Issues
- OI-001: Exact Shelly generations/models and topic mappings to be finalized from real `devices.yaml` examples.
- OI-002: Whether startup queries use HTTP, MQTT request/response, or hybrid.
- OI-003: Final condition language syntax and safe evaluator design.
- OI-004: Advanced sequence features (repeat-while, long-press timing, dim step intervals) final representation.
- OI-005: REST/UI auth model not specified yet.

### Resolved Issues
- RI-001: Program file name set to `shelly_server.py`.
- RI-002: FastAPI chosen for REST/UI; paho chosen for MQTT (`import paho.mqtt.client as mqtt`).
