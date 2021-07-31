FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

# RUN pip install --upgrade pip 
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /WPT
WORKDIR /WPT

COPY ./WPT /WPT

EXPOSE 8000
# CMD ["python", "manage.py", "runserver", ]
