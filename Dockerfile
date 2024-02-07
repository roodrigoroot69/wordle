FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev \
      gcc make libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir app/
RUN mkdir common/

WORKDIR app/

COPY common/ common/
COPY wordle/ .

EXPOSE 8000

CMD ["uvicorn", "wordle.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
