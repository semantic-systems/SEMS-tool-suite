FROM python:3.9.15 AS builder
COPY ["gradio_graph/", "install.sh", "./"]
RUN bash install.sh

FROM python:3.9.15

RUN \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y dist-upgrade && \
    apt-get -y autoremove && \
    apt-get -y install \
        git \
        curl \
    && \
    apt-get -y clean

COPY . /src/
RUN pip install -r /src/requirements.txt
WORKDIR src

ENV NODE_OPTIONS=--max_old_space_size=4096

EXPOSE 7860
ENTRYPOINT ["python"]
CMD ["/src/main.py"]
