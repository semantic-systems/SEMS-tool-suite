FROM node:18

RUN apt-get update && \
    apt-get install -y software-properties-common &&\
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get install -y git python3.9 nodejs curl python-is-python3 && \
    npm install -g pnpm && \
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3.9 get-pip.py


RUN pip install tweepy

WORKDIR /usr/
ENV NODE_OPTIONS=--max_old_space_size=4096
RUN git clone --recurse-submodules -j8 --depth 1 https://github.com/semantic-systems/the-demo && \
    cd the-demo &&  \
    cd gradio_graph && \
    bash scripts/install_gradio.sh && \
    bash scripts/build_frontend.sh

EXPOSE 7860
CMD ["python",  "the-demo/main.py"]
