FROM python:3.8

ENV FLASK_APP=wsgi.py
ENV FLASK_ENV=development

EXPOSE 5000/tcp
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT ["python"]

CMD ["wsgi.py"]
