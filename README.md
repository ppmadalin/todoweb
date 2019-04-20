
# Simple TODO App

Just a simple web TODO app made with Python and Flask.

Requires python 3.7 installed.

## Instalation

- Create a Docker image:
    - clone repository ` git clone https://github.com/ppmadalin/todoweb.git`
    - change directory `cd todoweb`
    - build docker image `docker build -t todoweb-image`
    - run docker image `docker run -d -p 5000:5000 --name todoweb-server todoweb-image`
    - go to http://localhost:5000

- Runing without docker
    - clone repository ` git clone https://github.com/ppmadalin/todoweb.git`
    - change directory `cd todoweb`
    - create python env `python -m venv venv`
    - switch to env:
        - Linux `source /venv/bin/activate`
        - Windwos `.\venv\Scripts\activate`
    - install requirements `pip -r install requirements.txt`
    - setup environments: 
        - Linux: `export FLASK_APP=manage.py`
        - Windows: `set FLASK_APP=manage.py` or `$env:FLASK_APP="manage.py"`
    - run app: `flask run`

