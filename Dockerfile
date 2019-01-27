FROM ubuntu:latest
MAINTAINER Don Gourley "gourley@wrlc.org"
RUN apt-get update -y
# Q: this seems to install python2.7 ???
RUN apt-get install -y python-pip python-dev build-essential
COPY . /redirects
WORKDIR /redirects
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_ENV development
ENTRYPOINT ["python"]
CMD ["app.py"]
