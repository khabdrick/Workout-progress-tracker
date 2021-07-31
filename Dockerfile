FROM python:3.8.3-alpine

#  ensures that Python output is logged to the terminal, making it possible to monitor Django logs in realtime.

ENV PYTHONUNBUFFERED 1

# prevents Python from copying pyc files to the container.
ENV PYTHONDONTWRITEBYTECODE 1  

# RUN pip install --upgrade pip 
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /WPT
WORKDIR /WPT

COPY . /WPT

# EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
