FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
