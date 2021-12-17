# pull official base image
FROM python:3.8.3-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#COPY ./requirement.txt .

# install psycopg2 dependencies
RUN apt-get update && apt-get -y install apt-utils gcc python3-dev musl-dev g++ unixodbc-dev unixodbc

# install dependencies
RUN pip3 install --upgrade pip
COPY ./requirement.txt .
RUN pip install -r requirement.txt

#copy entrypoint.sh

# COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
#CMD /usr/src/app/entrypoint.sh

CMD ["python", "myapp/manage.py", "runserver", "0.0.0.0:8080"]
