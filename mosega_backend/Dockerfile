#FROM ubuntu
#
#RUN apt-get update
#RUN yes | apt-get -y install python3.6
#RUN yes | apt-get install python3-pip
#
## create root directory for our project in the container
#RUN mkdir /backend
#
## Set the working directory to /backend
#WORKDIR /backend
#
## Copy the current directory contents into the container at /backend
#ADD . /backend/
#
## Install any needed packages specified in requirements.txt
#
#RUN pip3 install -r requirements.txt
#
#EXPOSE 8000
#STOPSIGNAL SIGINT
#ENTRYPOINT ["python3", "manage.py"]
#CMD ["runserver", "0.0.0.0:8000"]


FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /bend
WORKDIR /bend
COPY requirements.txt /bend/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /bend/
RUN chmod +x start.sh && ./start.sh
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
