FROM python:3.8-slim-buster

LABEL version="0.0.1" \
    author="BikoCodes" \
    maintainer="Chapiana Inc <bikocodes@gmail.com>"

COPY . /opt/chapiana-api/
WORKDIR /opt/chapiana-api/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
ENV PATH=/usr/local/nginx/bin:$PATH

RUN pip install --upgrade pip 

COPY ./LICENSE LICENSE
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

VOLUME ["/opt/chapiana-api"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:$PORT"]

COPY ./opt/entrypoint.sh /
ENTRYPOINT ["sh", "/opt/chapiana-api/entrypoint.sh" ]
