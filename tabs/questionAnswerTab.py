import gradio as gr
import requests


def qa(link, query):
    request = link + query + '&lang=en'
    try:
        return requests.post(request).json()
    except Exception as e:
        return e
    
   

with gr.Blocks() as questionAnswerTab:
    with gr.Row():
        question = gr.TextArea(
            label='Question', value='Where is the birthplace of Angela Merkel')
        result = gr.JSON(label='Answer', interactive=False)
    with gr.Row():
        link = gr.Text(label="URL", value='http://localhost:8080/qa?query=')
        qaRun = gr.Button(variant='primary')

    qaRun.click(fn=qa, inputs=[link, question], outputs=result)
