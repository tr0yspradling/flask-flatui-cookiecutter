#!/usr/bin/env bash

AUTOAPP=autoapp.py
ENV={{cookiecutter.virtual_env}}

if [[ ! -x "$AUTOAPP" ]]
then
    chmod +x $AUTOAPP
fi
if [ ! -d $ENV ]; then
    python3 -m venv $ENV
fi

# activate virtualenv
source {{cookiecutter.virtual_env}}/bin/activate
pip install -r requirements.txt

# set debug flag
export FLASK_DEBUG=TRUE

./$AUTOAPP --host 127.0.0.1 --port 8080 --debug=True
