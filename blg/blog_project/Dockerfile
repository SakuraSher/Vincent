FROM python:3.11-slim

ENV PYTHONBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE blog_project.settings

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/



EXPOSE 8000

CMD ["gunicorn" ,"--bind","0.0.0.0:8000", "blog_project.wsgi:application"]


