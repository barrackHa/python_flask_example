FROM python:3.7.4-alpine

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app

ENTRYPOINT ["python"]

CMD ["app.py"]


