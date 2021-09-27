# Zenatix Task
This repo contains the solution to the task

The code can be runned both on a local machine or a docker container.
To get the best results(Better visualisations in Kibana) please run the code on the local machine as there you will have several process running in background but in docker container there won't be enough process to visualise.

Below are the steps to run the code on both Docker Container as well as Local Machine

## Steps to run on Docker
Step 1 - Clone the repo
```git clone https://github.com/rajpratyush/zenatix.git```

Step 2 - Ensure that Docker is installed
```docker -v```

Step 3 - Ensure that Docker Compose is installed 
```docker-compose --version```

If any of these is not installed then follow the steps to install them from the links given below

Docker - https://docs.docker.com/engine/install/ubuntu/

Docker Compose - https://docs.docker.com/compose/install/

Step 4 - Cd into the cloned repo

Step 5 -  Run the docker-compose file
```docker-compose up```


## Steps to run on Local Machine
Step 1 - Clone the repo
```git clone https://github.com/Akshat1903/zenatix-task.git```

Step 2 - Ensure that Elasticsearch and kibana are installed and their services are running, in case any error follow their official documentation to install and run these

Step 3 - Cd into the cloned repo

Step 4 - Create a python virtual env and activate it.

```python -m venv venv```

```source venv/bin/activate```

Step 5 - Install the requirements
```pip install -r requirements.txt```

Step 6 - Run the python file
```python main-app.py```
