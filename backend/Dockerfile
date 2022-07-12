FROM python:3.8.3-alpine

#  ensures that Python output is logged to the terminal, making it possible to monitor Django logs in realtime.

ENV PYTHONUNBUFFERED 1

# prevents Python from copying pyc files to the container.
ENV PYTHONDONTWRITEBYTECODE 1  

RUN mkdir WPT/

RUN cd WPT && mkdir /backend
WORKDIR /WPT/backend


# RUN pip install --upgrade pip 
COPY . .
RUN pip install -r requirements.txt

# EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
