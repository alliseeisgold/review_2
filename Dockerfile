FROM ubuntu:latest

COPY . /app

WORKDIR /app

RUN apt-get -y update

RUN apt-get install -y python3 && apt-get install -y python3-pip

# RUN pip install -r requirements.txt

# ENTRYPOINT [ "python3"]

CMD [ "./run.sh"]