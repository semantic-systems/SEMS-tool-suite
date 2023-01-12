FROM python:3.9.15

RUN \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y dist-upgrade && \
    apt-get -y autoremove && \
    apt-get -y install curl && \
    apt-get -y clean

COPY . /src/
WORKDIR /src

RUN pip install -r /src/requirements.txt

EXPOSE 7860
ENTRYPOINT ["python"]
CMD ["/src/main.py"]
