# {{program_file_name}} Program Specification
- **Program Name**: {{program_name}}
- **Description**: {{program_description}}
- **Author**: {{author_name}}
- **Date**: {{date}}

## Table of Contents
- [Introduction](#introduction): introduce this program specification
- [Specification Description](#specification-description): describes this specification and how to interpret it
- [Creator Interview](#creator-interview): interview with the program creator
- [Program Generation Process](#program-generation-process): process to generate the program
- [Program Generation Report](#program-generation-report): describes the report for each program generation iteration
- [Program](#program): describes the generated program
    - [Program Description](#program-description): describes the program inputs, outputs, and processing
    - [Program Structure](#program-structure): describe the structure, program objects, and functions
    - [Program Environment](#program-environment): describe the environment, credentials, libraries, and standards
- [Functional Requirements](#functional-requirements): list the program functional requirements and evaluation criteria
- [Prompts](#prompts): list the prompts and in-context learning to be used in the program
- [Tests](#tests): describe the unit, integration, and end to end tests
- [Issues](#issues): List issues in this program generation process or the generated program
    - [Open Issues](#open-issues): List open issues
    - [Resolved Issues](#resolved-issues): List resolved issues

## Introduction
This document is a program specification template for the program [{{program_file_name}}]({{program_file_name}}).  Using an AI-assisted interview with the program creator (human or agent) ths template creates a program specification.  During this program specification creation, replace each template value enclosed with curled brackets ""{{<teplate value>}}"" with the value for the program specification.  If the template value is not completely from the interview context, ask the program creature explicitly for the template value or verify the uncertain template value.   After the initial program specification creation, the program creator will refine this specification progressively to create and refine the program.  A program generation agent will use this template to implement this program and verify program functionally.  [{{program_file_name}}]({{program_file_name}}) is {{program_description}}.  It is generated in collaboration with AI generated code and tests.  This program specification describes the program generation process and the resulting program.

## Creator Interview
The first step in program generation is a crater interview to define the program specification.  The full transcript of each interview must be included in this section with the date of the interview, name of the program creator, the name or model of the interviewer, an a transcript of the interview.   On this first interview, import the [program_specification_template.md](./program_specification_template.md) into and chat agent program like ChatGPT to perform and interview to define the program.  On subsequent interviews, import the already specialized program specification to be updated during he interview.  

The purpose of the interview is to complete the program specification.  The interview could be through voice wor written chat. During the interview:
1.  the LLM chat agent asks the program creator to capture the information to fully define one or more features of the program being specified.  
1. the LLM chat agent ask follow up questions.  
1. the LLM chat agent ask multiple probing questions about various aspects of each issue to capture details 
1. If the program creature continues to provide useful details about the program specification, continue to asks follow questions to fully capture the program context.
1. If the program creator indicates that the topic is complete.  
1. The LLM chat agent includes include information from supplied product documentations, software libraries, and web searches to generate useful follow up question from related technologies and software libraries to formulate effective questions. 
1. If the program creature continues to provide useful details about the program specification, continue to asks follow up questions.
1. Generate new questions as needed to fully capture the program context.  
1. Perform internet searches to provide questions based on existing product documentation, software libraries, and web searches to generate useful follow up question from related technologies and software libraries to formulate effective questions.     
1. Document the full interview below below in markdown format.
1. Each interview transcript must include the date of the interview, name of the program creator, the name or model of the interviewer, and a transcript of the interview.
1. Based on the interview, complete the program specification template by replacing each template value enclosed with curled brackets ""{{<teplate value>}}"" with the value for the program specification.
1. Based on the interview, update the [Functional Requirements](#functional-requirements), [Program](#program), [Prompts](#prompts), and [Tests](#tests) sections of this program specification to fully define the program to be generated.
1. Based on the interview, update the [Issues](#issues) section to list any open issues in the program specification or the generated program.

Example Interview Transcript:
### Creator Interview Example:
**Date**: 2024-06-15 <br>
**Creator**: Jane Doe <br>
**Interviewer**: GPT-5.1 <br>

**Transcript**: <br>
**Q:** What is the program purpose? <br> 
**A:** The program is designed to generate embeddings for engineering drawing features extracted from PDF files. <br>
**Q:** What is the program name?  <br>
**A:** design_embeddings.py <br>
**Q:** Describe the program inputs? <br>
**A:** The program takes as input:

    1. a list of PDF files containing engineering drawings
    2. a configuration files for Azure OpenAI credentials
    3. drawing feature classifications
    4. in-context learning examples for feature detection

**Q:** Describe the program outputs? <br>
**A:** The program outputs:

    1. A NetworkX graph representation of each drawing view
    2. A list of text section for each drawing feature neighborhood
    3. A list of metadata for each drawing feature including drawing information
    4. A list of embedding vectors for each drawing feature
    5. logs of API usage and costs

**Q:** Describe the program processing? <br>
**A:** The program processes the input PDF files to extract drawing features using a SwarmFeatureDetector.  For each drawing feature, it creates text sections and metadata.  It then generates embedding vectors for each text section using the Azure OpenAI embedding model.  The program also tracks API usage and costs.

**Q:** What are the functional requirements for the program?** <br>
**A:** The functional requirements are:

    1. Extract drawing features from PDF files
    2. Create text sections for each drawing feature neighborhood
    3. Create metadata for each drawing feature
    4. Generate embedding vectors for each text section
    5. Track API usage and costs

**Q:** What libraries should be used?** <br>
**A:** The program should use the following libraries:

    1. docgraph.openapi for Azure OpenAI API access
    2. fitz for PDF processing
    3. networkx for graph representation
    4. asyncio for asynchronous processing
    5. argparse for command line argument parsing

**Q:** Are there any specific error handling requirements?** <br>
**A:** The program should handle errors related to API calls, file I/O, and data processing gracefully.  It should log errors and continue processing other files when possible.

...

### Creator Interview Transcripts

## Specification Description
This program specification describes a collaborative program generation process.  A programmer will update this specification to direct AI agents to create the desired program.  The agent will create, validate, describe the program generation and the program.  The programmer will review the generated program and tests, update the specification and program to improve the implementation.  The programmer will then re-execute the AI agent to refine the program based on the updated specification.  This process will continue until the program meets all functional requirements and passes all tests.  

This specification:
- defines the program as {{program_file_name}}
- is not created or modified by the AI agent.  It is only modified by the programmer to direct the AI agent.
- defines the [Program Generation Process](#program-generation-process) to generate the python program {{program_file_name}}.  Follow this program generation process on each iteration to successfully accomplish the users request.
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

## Program Generation Process
**Request**
- The user requests the AI agent to create/modify/evaluate the [{{program_file_name}}]({{program_file_name}}) using this specification.
- Input for each iteration includes:
    - The original request
    - This specification file [{{program_name}}_ai_instructions.md]({{program_name}}_ai_instructions.md)
    - The current program [{{program_file_name}}]({{program_file_name}})
    - Prompts and in-context learning files described in the [Prompts](#prompts) section
    - The current tests described in the [Tests](#tests) section
    - The previous AI agent iteration report sections in [{{program_name}}_implementation.md]({{program_name}}_implementation.md)
- Output for each iteration includes:
    - Updated program [{{program_file_name}}]({{program_file_name}})
    - Updated prompts and in-context learning files described in the [Prompts](#prompts) section
    - Updated tests described in the [Tests](#tests) section
    - Updated program generation report section appended to [{{program_name}}_implementation.md]({{program_name}}_implementation.md) containing the details of this iteration as described in the [AI Program Generation Report](#ai-program-generation-report) section and test results.

**Each iteration of the program generation process must execute one or more iterations of the Plan → Act → Critique → Revise (PACR) loop as described below:**

- **Plan** — given the iteration inputs document a complete strategy to accomplish the request:

    Document the plan as described in [AI Program Generation Report](#ai-program-generation-report) describing each step of the plan in detail.  At each iteration, the current plans should address the limitations and critiques of previous iteration.
    The plan priorities in order are:
    1. describe the request and objective
    1. describe the new or changed functionality to be implemented
    1. From previous AI Program Generation Report Critique or Test sections, describe how to address previous issues that are unaddressed
    1. **Proposal**: describe a proposal to implement the requested functionality and address unaddressed issues from previous critiques
    1. **Function/Object Table**: Create/update table describing each function and object in the program:

        | Function/Object | Purpose | Inputs | Outputs | Memory Used | Processing Steps | Libraries Used | Requirement Addressed | Type (New/Modified/Existing) |
        |----------------|---------|--------|---------|-------------|------------------|----------------|-----------------------|-------------------------------|
        |                |         |        |         |             |                  |                |                       |                               |
    
    1. **Relationships**: Describe the relationships between the functions and objects in the table
    1. **Program Flow Graph**:  Based on the function/object table, [{{program_file_name}}]({{program_file_name}}), defines the program_flow_graph function to reflect the full program structure and relationships between objects and functions in the program:
    ```python
        import networkx as nx
        from pyvis.network import Network
        import matplotlib.pyplot as plt

        def program_flow_graph(html_graph_path: str = "program_flow_graph.html", png_graph_path: str = None) -> str:

        # List all top-level functions and classes
        # Top-level functions & orchestrators (kept updated per Edit 9/24/2025: 3:19 follow-up graph maintenance)
        nodes = [
            "parse_args",
            "main",
            # Additional nodes
        ]
        # Links between modules - this represents the program flow and dependencies
        edges = [
            # Main program flow
            {"source": "parse_args", "target": "main"},
            # Additional edges
        ]
        
        graph_data = {
            "directed": True,
            "multigraph": False,
            "nodes": nodes,
            "edges": edges
        }
        
        # Create HTML visualization
        graph = nx.node_link_graph(graph_data, edges="edges")

        if png_graph_path:
            plt.figure(figsize=(12, 8))
            pos = nx.spring_layout(graph)
            nx.draw(graph, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold", arrows=True)
            plt.savefig(png_graph_path)

        net = Network(notebook=True, cdn_resources='remote', directed=True, height='1000px', width='100%', bgcolor="#222222", font_color="white", select_menu=True)
        net.from_nx(graph)

        net.write_html(html_graph_path)

    ```
    1. Output the program structure graph as an HTML and PNG file using pyvis.network and provide a link to the file in the plan.
    1. Display an image of the program structure graph image in the program report for this iteration.
    1. List potential shortcomings of the proposed structure
    1. Identify libraries that are not included in requirements.txt
    1. Evaluate if the necessary libraries in requirements.txt
    1. Describe the [Functional Requirements](#functional-requirements) that are not addressed by the plan
    1. Describe the [Functional Requirements](#functional-requirements) that partially addressed by the plan
    1. Describe error scenarios and how they will be handled in the plan
    1. Describe errors that are not handled in the plan
    1. Evaluate the limitations of the current plan
    1. Propose refinements to address the limitations

    After planning the program implementation, plan the unit, integration, end to end tests needed to validate the program implementation:
    1. **Test table**: Create/Update the table with the tests to perform:

        |Requirement/Feature/Error| Type | Function/Class | Input | Expected Output | Description |
        |---|---|---|---|---|---|
        |   |   |   |   |   |   |

        - Requirement/Feature/Error: The specification requirement, feature, or error being tested
        - Type: unit/integration/end to end
        - Function/Class: The function or class being tested
        - Input: The input to the function or class
        - Expected Output: The expected output from the function or class
        - Description: A description of the test
    
    1. Each test identified in the specification must be implemented in the tests section
    1. Define additional tests so each function and class is tested
    1. Write each function and class in the main program experiments/swarm_feature_detection.py
    1. Verify each function and class with the unit tests
    1. Rewrite each the function and class that does not pass the unit tests to address the issues
    1. Verify that all unit tests pass
    1. Integrate the functions and classes as per the program graph
    1. Create integration tests in the file "experiments/test/swarm_feature_detection_integration.py" that test the following:
        a. Tests the program with the default PDF and verify the output json file
        b. Verify the saved page image from the default PDF
        c. Tests the Azure OpenAI API call with to the Azure OpenAI server using the provided credentials and verify the output JSON structure
        d. Tests error handling by providing invalid inputs and verifying that the program handles them gracefully
    1. Create the end to end test "experiments/test/swarm_feature_detection_end_to_end.py" for the  full program with the default PDF and verify the output
    1. Rewrite and re-test any part of the program that does not work as expected
    1. Create a program report "experiments/swarm_feature_detection_implementation.md" that lists: 
        - all steps performed in the program generation process, 
        - tests command line to run the unit tests, integration tests, and end to end tests,
        - issues found for each test,
        - how each issue was resolved
        - the final status of the program
        - limitations of the program
        - next steps for improving the program
    1. For subsequent program changes, update, "experiments/swarm_feature_detection_implementation.md" with a new section
        at the end of the document that lists:
        - the date of the changes
        - the prompt the initiated the changes
        - the model used to make the changes
        - list each file and the line numbers that were changed
        - the changes made to the program
        - issues found
        - how each issue was resolved
        - tests command line to run the unit tests, integration tests, and end to end tests
        - the final status of the program after the changes
    
    **Judge**: Judge the plan quality based on:
    1. It addresses all aspects of the request
    1. it addresses all unaddressed issues from previous critiques
    1. it addresses all [Functional Requirements](#functional-requirements)
    1. it addresses all program structure requirements in the [Program](#program) section
    1. it addresses all error handling requirements
    1. it provides a simple implementation than can be reliably implemented
    1. it provides a simple implementation can be fully tested
    1. it makes the fewest changes to the existing program

    Iteratively improve the plan is until it is their or no future improvements noted or a maximum number of plan iterations is reached (default 5)


- **Act** — Execute: using the selected AI model and evaluation mode, 
    1. Update the tests, programs, and prompts as per the plan.
    1. Execute the tests.
    1. Document the test results. 
- **Critique** — Evaluate the results against the expected outcomes and identify any discrepancies or areas for improvement.
    1. Describe the critique of the changes made in this iteration
    1. Describe the test results of this iteration
    1. Describes how well the request was satisfied
    1. List the implementation's shortcomings in satisfying the request
    1. Describe any new issues that arose during the implementation
    1. Describe shortcomings accomplishing the functional requirements
    1. Describe shortcomings accomplishing the program structure requirements
    1. Describe shortcomings in error handling
    1. Describe how the program structure can be improved to better satisfy the request and simplify the implementation
    1. Describe how the tests can be improved to better validate the implementation
- **Revise** — 
    1. Determine if a next iteration is needed.  
    1. Restate the original objective.  
    1. Define a refined prompt that encompasses the original objective and addresses the critique, and plan based on the critique and 
       test results. Iterate the PACR loop until the requested functionality is implemented and tests are successful or a maximum number of iterations is reached.  
  If the program is not satisfactory after the maximum number of iterations (default=5), document the limitations and next steps in the AI Program Generation Report.
  Document the revised request textin the AI Program Generation Report.
- **Iterate** — Repeat the PACR loop until the program meets all functional requirements and passes all tests or a maximum number of iterations is reached (default 7).

## Program Generation Report
[{{program_name}}_implementation.md]({{program_name}}_implementation.md) is an AI generated, human edited report of the program generation process. Each run of the AI program generation, will add a new section to the end of the file experiments/{{program_name}}_implementation. The report should be structured as follows:

    # Design Embeddings Implementation

    ## Introduction
    <Describe the objective of this program generation iteration based on the program specification>

    ## Program Generation Iterations
    ### <Iteration Name>
    1. **Request**
        - **date**: <date of the change>
        - **prompt**: <prompt that initiated the change>
        - **git_tag**: <the git tag this change is applied to>
        - **model**: <model used to make the change>

    #### Plan <Plan Iteration Description>
    1. **Functionality**: describe the new or changed functionality to be implemented
    1. **Critique**: describe unaddressed issues from previous iterations addressed in [{{program_name}}_implementation.md]({{program_name}}_implementation.md) that are being considered in in this 1. **Proposal**: reasoning proposal to implement the requested functionality and address unaddressed issues from previous critiques
    1. **Relationships**: Describe the relationships between the functions and objects in the table
    1. **Function/Object Table**: Report the function/object table for each reasoning iteration as described in the [Program Generation Process](#program-generation-process) section
    1. **Program Flow Graph**: Display the program structure graph image for each reasoning iteration created as per the [Program Generation Process](#program-generation-process) section
    1. List potential shortcomings of the proposed structure
    1. Identify libraries that are not included in requirements.txt
    1. Evaluate if the necessary libraries in requirements.txt
    1. Describe the [Functional Requirements](#functional-requirements) that are not addressed by the plan
    1. Describe the [Functional Requirements](#functional-requirements) that partially addressed by the plan
    1. Describe error scenarios and how they will be handled in the plan
    1. Describe errors that are not handled in the plan
    1. Evaluate the limitations of the current plan
    1. Propose refinements to address the limitations
    1. **Test table**: Create/Update the table with the tests to perform as described in the [Program Generation Process](#program-generation-process)
    1. **Judge**: report the plan judgement based on the criteria in the [Program Generation Process](#program-generation-process) section

    #### Act
    **Change List** List each program changes in the following table
    |File| Lines | Requirement/Feature/Error | Description |
    |---|---|---|---|
    |   |   |   |   |

    #### Test Results
    - Test commands to run the tests
    - Unit test final results
    - Integration test final results
    - End to end test final results

    #### Critique
    1. Describe the critique of the changes made in this iteration
    1. Describe the test results of this iteration
    1. Describes how well the request was satisfied
    1. List the implementation's shortcomings in satisfying the request
    1. Describe any new issues that arose during the implementation
    1. Describe shortcomings accomplishing the functional requirements
    1. Describe shortcomings accomplishing the program structure requirements
    1. Describe shortcomings in error handling
    1. Describe how the program structure can be improved to better satisfy the request and simplify the implementation
    1. Describe how the tests can be improved to better validate the implementation
    #### Revise
    - Restate the original objective
    - Why is the current program not satisfactory
    - What is the current iteration number and has the maximum number of iterations been reached
    - Should the PACR loop continue (yes/no)
    - How should the request be revised based on the critique to address the issues found and satisfy the original request

    the section contents are describe in the [AI Program Generation Report](#ai-program-generation-report) section as shown in the following example: 

        # Design Embeddings Implementation

        ## Intial program creation

        ### Request

        - **date**: 10/6/2025
        - **prompt**: Create a Python program to generate embeddings for engineering drawing features.
        - **git_tag**: v1.0.0
        - **model**: gpt-5

        ### Plan
        Create a Python program named experiments/{{program_name}}.py that implements the following capabilities:
        1. feature_sections: ...

## Program


### Program Description

- {{program_name}}.py defines the class "DesignEmbeddings" with function interface with following capabilities in the program:
    1. feature_sections: Given a PDF file containing engineering drawings, create a list of text sections containing: 
        - drawing feature neighborhoods extracted from the drawing views
        - drawing metadata containing title block, revision block, and drawing notes as JSON metadata
        - section text: combine the drawing feature neighborhoods and drawing metadata into text sections for embedding generation:
            ```json
            {
                "metadata": {
                    "drawing" : filename or identifier,
                    "page": <page number>,
                    "title_block": "<title block data>",
                    "revision_table": <revision table data>,
                    "notes": [<list of drawing notes>],
                },
                "text": "<JSON text of feature neighborhood>",
            }
            ```
    1. DesignEmbeddings.embedding: given a feature section text, create an embedding vector using the docgraph.common.openapi.embedding method with the embedding model configured in the DesignEmbeddings class constructor.

    1. create_index(index:str, pdf_files:List[str]): 
        - given an index name and a list of PDF files containing engineering drawings, 
        - create a vector database index 
        - for each drawing, create embedding sections using feature_sections
        - for each feature section, create embedding vectors
    1. DesignEmbeddings.delete_index(index:str): Delete the entire vector database index and all associated storage
    1. DesignEmbeddings.search(query:str): Given query text, create an embedding vector and search the vector database index for similar embeddings.  Return the top N results with metadata and similarity scores.
- parse_args: command line argument parser
    - input_pdf: default data/TPDexamples/CASE003_30_items/ExamplesToTeachAI/1262184_NOK_corrected.pdf
    - creds: path to json file containing Azure OpenAI credentials.  Default config/creds.yaml
    - drawing_list: json file containing a list of drawings to process.  Default experiments/config/drawing_list.json
    - classifications: json file containing the drawing feature classifications.  Default experiments/config/classifications.json
    - feature_detection_examples: json file containing in context learning examples of drawing feature detection.  Default experiments/config/swarm_feature_detection_examples.json
    - title_block_extraction_examples: default experiments/config/extract_title_block.json
    - table_extraction_examples: default experiments/config/extract_tables.json
    - note_extraction_examples: default experiments/config/extract_notes.json
    - view_extraction_examples: default experiments/config/extract_views.json
    - results_path: path to save results.  Default: output_embeddings
    - model: model to use for feature detection.  Default: gpt-5
    - timeout: timeout for model calls in seconds.  Default: 2000.0
    - max_iterations: maximum number of iterations to perform for feature detection.  Default: 3
    - max_retries: maximum number of retries for model calls.  Default: 3
    - input_token_price: default=1.25e-6
    - output_token_price: default=10e-6
    - dpi: full page image dots per inch default=72
    - feature_crop_dpi: default=216

        
- main: command line interface to evaluate the above functions


### Program Structure

**feature_sections**: 

input: 
- {{list and describe the program inputs here}}

output:
- {{list and describe all program outputs here}}

processing:
- {{describe the program processing here}}

### Program Environment

**Credentials**
{{Describe the credentials and credential management here}}

**Libraries**
- {{list and describe the libraries, versions, and usage patterns here.  Include specific usage patterns and examples that will be needed in the program implementation.}}

**Standards**
- {{list and describe any coding standards, documentation standards, or other standards to be followed in the program implementation here.}}

## Prompts
- {{List and describe prompt and in context learning files to be used in the program implementation here.  Include specific prompt templates and in-context learning examples that will be needed in the program implementation.}}

## Functional Requirements

| Requirement ID | Requirement Description | Requirement Verification |
|----------------|-------------------------|--------------------------|
| FR-001 | {{Describe the first functional requirement}} | {{Describe the functional requirement verification}} |
| FR-002 | {{Describe the second functional requirement}} | {{Describe the functional requirement verification}} |. |

{{add additional functional requirements as needed}}

## Tests

### Unit Tests
- {{List and describe specific unit tests for each function and class in the program here.  Include test inputs, expected outputs, and test descriptions.}}

### Integration Tests
- {{List and describe specific integration tests for the program here.  Include test inputs, expected outputs, and test descriptions.}}

### End-to-End Tests
- {{List and describe specific end-to-end tests for the program here.  Include test inputs, expected outputs, and test descriptions.}}


## General Program Structure

### {{Identify each general program structure here}}

{{Describe and prove examples examples of the general program structure here}}

### {{Additional general program structure here}}

{{Describe and prove examples examples of the additional general program structure here}}

...


## Program Capabilities
1. {{List and describe the pogram capabilities here}}

## Issues
List of program issues from testing and evaluation.

### Open Issues
- Issue 1: Description of the issue
- Issue 2: Description of the issue

### Resolved Issues
- Issue 3: Description of the issue
- Issue 4: Description of the issue