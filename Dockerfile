FROM python:3.9.1
RUN apt-get update
RUN apt-get upgrade -y
RUN pip install elasticsearch
RUN pip install psutil
ADD . /zen-tasks
WORKDIR /zen-tasks
CMD [ "python", "./main_app.py" ]