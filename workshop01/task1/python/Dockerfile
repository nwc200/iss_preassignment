## Build
FROM python:3.8

LABEL maintaner=cheng

WORKDIR /app

COPY public public
COPY templates templates
COPY requirements.txt .
COPY run.sh .
COPY utils.py .
COPY main.py .

RUN pip install -r requirements.txt

## Run
ENV PORT=5000
ENV INSTANCE_NAME=MyApp
ENV INSTANCE_HASH=123
EXPOSE ${PORT}

ENTRYPOINT [ "python", "main.py" ]