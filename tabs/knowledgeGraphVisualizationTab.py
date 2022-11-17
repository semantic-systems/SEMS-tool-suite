import gradio as gr


with gr.Blocks() as kgVisualizationTab:
    input = gr.Textbox(
        value="http://www.wikidata.org/entity/Q84263196", label="Root")
    submit = gr.Button(value="Submit", variant="primary")
    graph = gr.Graph()
    submit.click(fn=None, inputs=input, outputs=graph)
