import gradio as gr
from gradio_graph import gradio as gr

with gr.Blocks() as kgVisualizationTab:
    with gr.Row():
        with gr.Column(scale=1):
            value = gr.Textbox(
                value="http://www.wikidata.org/entity/Q84263196", label="Root")
        with gr.Column(scale=1):
            endpoint = gr.Dropdown(
                label='Endpoint', value='https://skynet.coypu.org/wikidata/', choices=['https://skynet.coypu.org/wikidata/', 'https://query.wikidata.org/sparql'])

    with gr.Row():
        with gr.Column(scale=1):
            with gr.Row(elem_id="row"):
                rate_limit = gr.Textbox(
                    value=20,
                    label="Rate Limit",
                    elem_id="row"
                )
                size_limit = gr.Textbox(
                    value=100,
                    label="Size Limit"
                )
        with gr.Column(scale=1):
            reset_button = gr.Button("Reset")
            submit_button = gr.Button("Submit", variant="primary")

    graph = gr.Graph()

    def bundle(value, endpoint, rate, size):
        return {"value": value, "endpoint": endpoint, "rate_limit": rate, "size_limit": size}
    submit_button.click(fn=bundle, inputs=[value, endpoint, rate_limit,
                 size_limit], outputs=graph)
    def reset():
        return ["http://www.wikidata.org/entity/Q84263196", "https://skynet.coypu.org/wikidata/", "20", "100"]
    reset_button.click(fn=reset, outputs=[value, endpoint, rate_limit, size_limit])
