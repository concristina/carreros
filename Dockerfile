FROM python:3.7-alpine as build
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED=1
RUN apk add --update build-base python-dev py-pip git jpeg-dev zlib-dev postgresql-dev
RUN pip install -U pip
ENV LIBRARY_PATH=/lib:/usr/lib
COPY . .
RUN pip install -qr requirements.txt

FROM python:3.7-alpine
RUN apk add postgresql-dev jpeg-dev zlib-dev
COPY --from=build /usr/src/app /usr/src/app
COPY --from=build /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages
WORKDIR /usr/src/app

EXPOSE 8000
ENV DEBUG ${DEBUG}
ENV DB_URL ${DB_URL}
CMD gunicorn carreros.wsgi:application -w 2 -b 0.0.0.0:8000