import gradio as gr
import requests


examples=[
    "Does Tokyo have a sea port?",
    "How many sea ports are there in China?",
    "What is the risk level of Germany?",
    "What is the international acronym of Saudi Arabia?"
    ]

description = """- SPARQL Structure Prediction
                 - SPARQL Content Population -> Query Generation"""


def qa(question, kb):
    try:
        url = 'http://coypu_kgqa_container:12000/'
        if kb == "CoyPuKG":
            kb_val = "coypukg"
        elif kb == "DBpedia":
            kb_val = "dbpedia"
        elif kb == "Freebase":
            kb_val = "freebase"
        request = requests.post(url, json={"text": question, "kb": kb_val}, headers={"Content-Type": "application/json"}).json()
        return request.get('answers'), {"sparql": request.get('sparql')}
    except Exception as e:
        return e,e


with gr.Blocks() as questionAnswerTab:
    with gr.Row():
        gr.Markdown(f"{description}")
    with gr.Row():
        with gr.Column():
            question_box = gr.TextArea(label='Question')
            kb_dropdown = gr.Dropdown(choices=["CoyPuKG"],
                                      value="CoyPuKG",
                                      label="Target KG")
            gr.Examples(examples, inputs=question_box, label='Example questions')
            qaRun = gr.Button(variant='primary')
        with gr.Column():
            answer_box = gr.JSON(label='Answer', interactive=False)
            sparql_box = gr.JSON(label='SPARQL', interactive=False)

    qaRun.click(fn=qa, inputs=[question_box, kb_dropdown], outputs=[answer_box, sparql_box])
