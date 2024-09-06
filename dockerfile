ARG IMAGE

FROM ${IMAGE}
LABEL maintainer="Brad Larson"

#USER root

ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN --mount=type=cache,target=/var/cache/apt \ 
    apt update -y && apt install -y --no-install-recommends \
        python3 \
        python3-pip \
         && \
    rm -rf /var/lib/apt/lists/*

        # build-essential \
        # nodejs \
        # npm \
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

#RUN curl -fsSL https://code-server.dev/install.sh | sh

#USER 1000

COPY requirements.txt .
RUN --mount=type=cache,target=/var/cache/apt \
      pip3 install -r requirements.txt


RUN mkdir /var/run/sshd

EXPOSE 22 3000 5000 6006 8080 8888

WORKDIR /config/workspace
ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED=1
RUN echo 'alias py=python3' >> ~/.bashrc

# RUN /app/code-server/bin/code-server --install-extension ms-python.python \
#     --install-extension eamodio.gitlens

# ENV PUID=1000 
# ENV PGID=1000 
# ENV PASSWORD=${PASSWORD}
COPY server.py server.py
COPY config/ /config/
COPY templates/ templates/
COPY static/ static/

# Launch container
CMD ["py server.py"]
#CMD ["/bin/bash"]
#CMD ["/usr/sbin/sshd", "-D"]
#CMD ["code-server" "--auth none" "--disable-telemetry" "--bind-addr 0.0.0.0:8080" "--disable-update-check" "--user-data-dir /data"]
