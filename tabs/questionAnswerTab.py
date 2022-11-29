import gradio as gr
import requests


def qa(q):
    try:
        url = http://tebaqa-controller:8080/qa
        return requests.post(url, data={"query": q, "lang": "en"}).json()
    except Exception as e:
        return e
    
   

with gr.Blocks() as questionAnswerTab:
    with gr.Row():
        with gr.Column():
            question = gr.TextArea(label='Question', value='Where is the birthplace of Angela Merkel')
            qaRun = gr.Button(variant='primary')
        with gr.Column():
            result = gr.JSON(label='Answer', interactive=False) 

    qaRun.click(fn=qa, inputs=question, outputs=result)
