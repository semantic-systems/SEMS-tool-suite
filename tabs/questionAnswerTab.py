from gradio_graph import gradio as gr


with gr.Blocks() as questionAnswerTab:
    with gr.Row():
        gr.TextArea(label='Question')
        gr.TextArea(label='Answer', interactive=False)
    with gr.Row():
        gr.Text(label="URL")
        gr.Button()