#!/usr/bin/env bash

# Check for LEPP stack & install missing packages.
required_packages=("nginx", "uwsgi", "postgresql", "python3-pip")

for package in "${required_packages[@]}"
do
    PKG_OK=$(dpkg-query -W --showformat='${Status}\n' ${package}|grep "install ok installed")
    echo Checking for ${package}: $PKG_OK
    if ["" == "$PKG_OK"]; then
      echo "${package} not installed. Installing ${package}."
      sudo apt-get install ${package}
    fi
done

# Setup virtual environment
ENV={{cookiecutter.virtual_env}}
if [ ! -d $ENV ]; then
    python3 -m venv $ENV
fi

# Download requirements
source $ENV/bin/activate
pip install -r requirements.txt
deactivate

#sudo letsencrypt certonly -d {{cookiecutter.domain}}