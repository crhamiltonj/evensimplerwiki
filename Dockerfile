FROM python:3.8
ENV FLASK_APP=wsgi.py
EXPOSE 5000/tcp
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app

CMD ["flask", "run"]
