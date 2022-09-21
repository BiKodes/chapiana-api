FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Adds our application code to the image

WORKDIR /opt/chapiana-api/
COPY . /opt/chapiana-api/
EXPOSE 8000

VOLUME ["/opt/chapiana-api"]
# Run the production server
CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - contacts.wsgi:application

ENTRYPOINT ["sh", "/opt/chapiana-api/entrypoint.sh" ] 
