python -m venv .venv
source .venv/bin/activate

git clone https://github.com/sch-28/gradio_graph
cd gradio_graph
bash scripts/install_gradio.sh
bash scripts/build_frontend.sh
