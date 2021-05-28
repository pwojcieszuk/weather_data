FROM python:3.9
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src .
RUN export FLASK_ENV=development
ENTRYPOINT python app.py
