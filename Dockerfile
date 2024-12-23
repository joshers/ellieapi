FROM python:3.13.1-slim-bookworm

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD [ "python3", "-m" , "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]