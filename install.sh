python -m venv .venv
source .venv/bin/activate

cd gradio_graph
bash scripts/install_gradio.sh
bash scripts/build_frontend.sh
