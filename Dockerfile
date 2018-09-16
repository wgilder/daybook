FROM jazzdd/alpine-flask:python3

RUN apk add --no-cache libffi-dev gcc python3-dev musl-dev libressl-dev

ADD requirements.txt /tmp_ins/
RUN pip install -r /tmp_ins/requirements.txt 
RUN rm -rf /tmp_ins/

ADD app.py /app/
ADD templates/ /app/templates/
ADD streifen/ /app/streifen/
