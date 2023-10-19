import gradio as gr
import requests


examples=[
    "What is the capital of Denmark?",
    "What is the population of Germany?",
    "Of which country is Berlin the capital?",
    "Where is the birthplace of Angela Merkel?"
    ]

description = """- Vicuna 1.5-based QA system """


def qa(question):
    try:
        url = 'https://turbo.skynet.coypu.org/'
        request = requests.post(url, messages=[{"role": "user",
               "content": f"You are a question answering system expert. Please reformulate the following sentence into a reasonable question for a LLM."
                          "/n/n question /n/n "}],
                                temperature = 0.1
                                ).json()
        reforumated_question = request[0].get('choices')[0].get("message").get("content")
        request = requests.post(url, messages=[{"role": "user",
                                                "content": reforumated_question}],
                                temperature = 0.1,
                                max_tokens = 120).json()
        return request[0].get('choices')[0].get("message").get("content")
    except Exception as e:
        return e


with gr.Blocks() as questionAnswerTab:
    with gr.Row():
        gr.Markdown(f"{description}")
    with gr.Row():
        with gr.Column():
            question_box = gr.TextArea(label='Question')
            gr.Examples(examples, inputs=question_box, label='Example questions')
            qaRun = gr.Button(variant='primary')
        with gr.Column():
            answer_box = gr.JSON(label='Answer', interactive=False)
            sparql_box = gr.JSON(label='SPARQL', interactive=False)

    qaRun.click(fn=qa, inputs=question_box, outputs=[answer_box, sparql_box])
