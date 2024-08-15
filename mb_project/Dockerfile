#Use an official Python runtime as a parent image
FROM python:3.11-slim

#Set envionment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#Set the working directory
WORKDIR /app

#Copy the requirements 
COPY requirements.txt /app/

#Install the dependencies
RUN pip install --upgrade pip
RUN pip instal -r requirements.txt

#Copy the django project code to the container
COPY . /app/

#Collect the static files
RUN python manage.py collectstatic --noinput

#Expose the port app runs on
EXPOSE 8000


