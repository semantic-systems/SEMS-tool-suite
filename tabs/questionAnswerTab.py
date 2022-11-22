import gradio as gr
import requests


def test(link, query):
    req = link + query + '?&lang=en'
    response = requests.post('http://localhost:8080/qa?query=Where is the birthplace of Angela Merkel?&lang=en')
    return response

with gr.Blocks() as questionAnswerTab:
    with gr.Row():
        question = gr.TextArea(
            label='Question', value='Where is the birthplace of Angela Merkel')
        result = gr.JSON(label='Answer', interactive=False)
    with gr.Row():
        link = gr.Text(label="URL", value='http://localhost:8080/qa?query=')
        qaRun = gr.Button(variant='primary')

    qaRun.click(fn=test, inputs=None, outputs=result)
