FROM ubuntu:latest
RUN apt-get update && apt-get -y update
RUN apt-get install -y build-essential python3.8 python3-pip python3-dev
RUN pip3 install flask
RUN pip3 install flask-wtf
COPY . ./app
WORKDIR /app
CMD ["python3", "flask_app.py"]