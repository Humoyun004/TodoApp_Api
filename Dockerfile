FROM python:3.11-slim-bullseye

WORKDIR /todo_app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /todo_app/

CMD ["python", "manage.py","runserver","0.0.0.0:8000"]






