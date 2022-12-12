import gradio as gr
import requests


examples=[
    "What is the capital of Denmark?",
    "What is the population of Germany?",
    "Of which country is Berlin the capital?",
    "Where is the birthplace of Angela Merkel?"
    ]
def qa(question):
    try:
        url = 'http://tebaqa-controller:8080/qa-simple'
        request = requests.post(url, data={"query": question, "lang": "en"}).json()
        return request.get('answers'), request.get('sparql')
    except Exception as e:
        return e,e 
    
   

with gr.Blocks() as questionAnswerTab:
    with gr.Row():
        with gr.Column():
            question_box = gr.TextArea(label='Question')
            gr.Examples(examples, inputs=question_box, label='Example questions')
            qaRun = gr.Button(variant='primary')
        with gr.Column():
            answer_box = gr.JSON(label='Answer', interactive=False)
            sparql_box = gr.JSON(label='SPARQL', interactive=False)

    qaRun.click(fn=qa, inputs=question_box, outputs=[answer_box, sparql_box])
