FROM python:3.8-slim-buster
RUN apt update

ENV DHOMEDIR=/app

COPY . $DHOMEDIR/
WORKDIR $DHOMEDIR
RUN pip install -r requirements.txt

CMD ["python", "./main.py"]