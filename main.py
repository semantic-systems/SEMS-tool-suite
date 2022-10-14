from gradio_graph import gradio as gr


def test(a):
    print(a)

    return a




with gr.Blocks() as demo:
    with gr.Row( elem_id='test'):
        with gr.Tab('KG Connect & Visualization'):
            examples = gr.Radio(["http://rdf.freebase.com/ns/aviation.aircraft", "http://rdf.freebase.com/ns/m.03jmrzx"])
            graph = gr.Graph()
            examples.change(fn=test, inputs=examples, outputs=graph)
            pass
        with gr.Tab('Knowledge Extraction'):
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Text(label='Input Text')
                    gr.Dropdown(label='Model', choices=['Model 1','Model 2'], interactive=True)
                with gr.Column(scale=1):
                    gr.Text(label='KG in JSON-LD', Interactive=False)
                    gr.Label('Visualization of the constructed Knowledge Graph...')
        with gr.Tab('Event Detection/ Argument Extraction'):
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Text(label='Input')
                    gr.Dropdown(choices=['Model Event Detection 1','Model Event Detection 2'], label='Event Detection Model', interactive=True)
                    gr.Dropdown(choices=['Model Argument 1','Model Argument 2'], label='Argument Extraction Model', interactive=True)
                with gr.Column(scale=1):
                    gr.Text(label='Event Type', Interactive=False)
                    gr.Text(label='Arguments', Interactive=False)
                    gr.Text(label='Links', Interactive=False)
                    gr.Label('Visualization of the Event Knowledge Graph...')
        with gr.Tab('Maximum Damage'):
            pass
        
        with gr.Tab('Question Answering'):
            with gr.Row():
                with gr.Column():
                    gr.Text(label='Question')
                with gr.Column():
                    gr.Text(label='Answer', Interactive=False)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")