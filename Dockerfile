FROM python:3.9.15 AS builder
COPY ["gradio_graph/", "install.sh", "./"]
RUN bash install.sh

FROM python:3.9.15

COPY --from=builder ["gradio", "gradio/"]
COPY --from=builder [".venv", ".venv/"]
COPY . ./
RUN pip install tweepy
ENV NODE_OPTIONS=--max_old_space_size=4096

EXPOSE 7860
CMD [".venv/bin/python",  "main.py"]
