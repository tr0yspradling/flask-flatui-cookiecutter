FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  git \
  python3 \
  python3-pip \
  python3-dev

RUN pip3 install --upgrade pip

RUN pip install -r ./requirements.txt

ARG UID
RUN useradd docker -l -u $UID -s /bin/bash -m
USER docker

WORKDIR {{cookiecutter.project_dir}}

ENTRYPOINT ["/bin/bash"]