# ShellyPyServer

This projects creates a python [flask web server](https://flask.palletsprojects.com) to centralize and publish local control to [Shely lighting controllers](https://www.shelly.cloud/).  I've written this as a programming lesson for my children on collaborative python web server develelopment.

## Objectives
1. Work together on a programming project synchronized with git
1. Create a python web server from scratch serving static web pages
1. Add to the API of a joint web server
1. Add a new Shelly device interface to the the web server
1. Add an on/off device control to the server web page
1. Receive device events
1. Publish the device event though the web interface
1. Display the device event on the web page

## Instructions

### Setup
Setup the following packages on your development computer:
1. Create a github account: [https://github.com/](https://github.com/).
1. Install git on your computer (already installed on Linux): [https://git-scm.com/downloads](https://git-scm.com/downloads)
1. Install vscode on your computer: [https://code.visualstudio.com/](https://code.visualstudio.com/)
1. Install python and vscode python extensions:[python-tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
### Getting started with git
"[git](https://git-scm.com/)" is version control system that lets us sychronize development with other people and over time.  We will use it to make a local copy of the shellypyserver project, track our changes, and synchronize our work with each other. 

1. To get  our project, open a terminal to the location you want to work from (e.g." c:/data/git) and type:
    ```cmd
    https://github.com/bhlarson/shellypyserver.git
    ```
1. Next open the directory in [vscode](https://code.visualstudio.com/).
1. Add your name to the list in the "Developers" section below, add your changes to git, commit your changes, and push them to github.  If you are not one of my developers (children), branch this project and you can push into your branch.
    ```cmd
    git status
    git pull
    git add README.md
    git commit -m "Adding Brad Larson to developers"
    git push
    ```
1. In your github account, create and publish a static website with a simple static message: [github pages](https://pages.github.com/)

### Preparing the dockerimage
1. Prepare an Ubunt linux computer
1. On the development computer, enable DOCKER_BUILDKIT
```cmd
echo 'export DOCKER_BUILDKIT=1' >> ~/.bashrc
. ~/.bashrc
```

### Python Flask Server
### Python Django Server
You will first create a python web server from scratch based on django's [Getting Started](https://docs.djangoproject.com/en/4.1/intro/)  
1. Install django:
    ```cmd
    pip install Django
    ```
1. Create the text file 'ss.py' as a simple server
1. Use django-admin to create a starter application
    ```cmd
    django-admin startproject ss
    ```
1. Run your server
    ```cmd
    python ss/manage.py runserver
    ```
1. If not automatically launched your web server should be at [localhost:8000](http://localhost:8000).
1. Create a the base directoreis for a polls app:
    ```cmd
    cd ss
    python manage.py startapp polls
    ```
1. Open [ss/polls/views.py](ss/polls/views.py)
1. Add the following index response:
    ```python
    from django.http import HttpResponse


    def index(request):
        return HttpResponse("Hello, world. You're at the polls index.")
    ```
1. [ss/poles/urls.py](ss/urls.py)

VSCode web client [code-server](https://coder.com/docs/code-server)
[code-server](https://github.com/coder/code-server)
[vscode](https://github.com/Microsoft/vscode)
[](https://github.com/microsoft/vscode-dev-containers/)
[coder](https://github.com/coder/coder) platform to manage code-server
[How To Make a Web Application Using Flask in Python 3](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)
[FLASK Installation](https://flask.palletsprojects.com/en/2.2.x/installation/#install-flask)
[openvscode-server](https://github.com/gitpod-io/openvscode-server/)
[django server](https://code.visualstudio.com/docs/python/tutorial-django)
[production pythion server](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/)
[Django OpenAPI](https://hackernoon.com/openapi-30-schema-with-swagger-ui-for-django-restful-app-4w293zje)
[Django Authentication](https://docs.djangoproject.com/en/4.1/topics/auth/)
## Developers:
- Brad Larson