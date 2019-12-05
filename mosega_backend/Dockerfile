FROM ubuntu

RUN apt-get update
RUN yes | apt-get -y install python3.6
RUN yes | apt-get install python3-pip

# create root directory for our project in the container
RUN mkdir /backend

# Set the working directory to /backend
WORKDIR /backend

# Copy the current directory contents into the container at /backend
ADD . /backend/

# Install any needed packages specified in requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
