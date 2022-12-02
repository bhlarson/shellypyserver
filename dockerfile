ARG IMAGE

FROM ${IMAGE}
LABEL maintainer="Brad Larson"

USER root

ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN --mount=type=cache,target=/var/cache/apt \ 
     apt-get update -y && apt-get install -y --no-install-recommends \
        build-essential \
        python3 \
        python3-pip \
        nodejs \
        npm \
        && \
     rm -rf /var/lib/apt/lists/*

        # cusrl \
        # unzip \
        # git \
        # nodejs \
        # npm \
#         autofs \
#         net-tools \
#         iproute2 \
#         pciutils \
#         tzdata \
#         rsync \
#         tree \
#         htop \
#         expect \
#         apt-utils \
#         software-properties-common \
#         ca-certificates \
#         gnupg \
#         lsb-release \
#         apt-transport-https \
#         daemonize \
#         dbus-user-session \
#         fontconfig && \
        # openssh-server \
        # sudo \
        # nano \

RUN curl -fsSL https://code-server.dev/install.sh | sh

COPY requirements.txt .
RUN --mount=type=cache,target=/var/cache/apt \
    pip3 install -r requirements.txt


RUN mkdir /var/run/sshd

EXPOSE 22 3000 5000 6006 8080 8888

WORKDIR /app
ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED=1
RUN echo 'alias py=python3' >> ~/.bashrc

RUN code-server --install-extension ms-python.python && \
    code-server --install-extension eamodio.gitlens && \
    code-server --install-extension ms-toolsai.jupyter && \
    code-server --install-extension redhat.vscode-yaml

RUN git clone https://github.com/bhlarson/shellypyserver.git

# Launch container
#CMD ["/bin/bash"]
#CMD ["/usr/sbin/sshd", "-D"]
CMD ["/bin/bash", "/app/shellypyserver/sstartup.sh"]
