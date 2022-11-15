from gradio_graph import gradio as gr
import requests


def test(link, query):
    req = link + query + '?&lang=en'
    response = requests.post(req)
    print(response)
    return response


with gr.Blocks() as questionAnswerTab:
    with gr.Row():
        question = gr.TextArea(label='Question', value='Where is the birthplace of Angela Merkel')
        result = gr.JSON(label='Answer', interactive=False)
    with gr.Row():
        link  =gr.Text(label="URL", value='http://localhost:8080/qa?query=')
        qaRun = gr.Button()

    qaRun.click(fn=test, inputs=[link,question], outputs=result)

        