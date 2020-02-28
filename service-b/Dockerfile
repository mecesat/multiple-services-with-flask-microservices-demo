FROM python:2.7-alpine

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD . /app

EXPOSE 5000

CMD ["python", "app.py"]