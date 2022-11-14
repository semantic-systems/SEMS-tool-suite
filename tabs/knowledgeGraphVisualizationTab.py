from gradio_graph import gradio as gr


with gr.Blocks() as kgVisualizationTab:
    examples = gr.Radio(["http://rdf.freebase.com/ns/aviation.aircraft", "http://rdf.freebase.com/ns/m.03jmrzx"])
    graph = gr.Graph()
    examples.change(fn=None, inputs=examples, outputs=graph)