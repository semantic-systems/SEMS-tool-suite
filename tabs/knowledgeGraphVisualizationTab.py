import gradio as gr

with gr.Blocks() as kgVisualizationTab:
    with gr.Row():
        html = gr.HTML('<iframe src="https://sch-28.github.io/rdf-vis" style="height:80vh; width:100%;"></iframe>')
