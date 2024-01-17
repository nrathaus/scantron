# syntax=docker/dockerfile:1

FROM ubuntu:latest

RUN apt update
RUN apt install --yes python3-pip
RUN apt install --yes openssh-server openssh-client

ARG user=scantron
ARG group=scantron
ARG uid=1000
ARG gid=1000
RUN groupadd -g ${gid} ${group}
RUN useradd -u ${uid} -g ${group} -s /bin/sh -m ${user}
USER ${uid}:${gid}

# We want to run this as non-root
RUN pip3 install ansible\>=2.4.0.0

WORKDIR /home/${user}
COPY --chown=${user} . .

RUN ./initial_setup.sh

RUN console/scantron_secrets.json.empty console/scantron_secrets.json

