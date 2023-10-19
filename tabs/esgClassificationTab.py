import gradio as gr
import requests


examples=[
    "\"One-in-100-year flood event\" devastates Western Australia",
    "118th United States Congress convenes; House of Representatives adjourns without electing Speaker for first time in 100 years.",
    "UK Treasury considering plans for digital pound, economic secretary says.",
    "Troops freed by Mali return to Ivory Coast.",
    "Eliminating Deforestation : Hershey commits to eliminating commodity-driven deforestation from our entire supply chain by 2030 while respecting and protecting the human rights of individuals. Guided by our No Deforestation Policy, we will work within our individual commodity supply chains to drive sustainable practices with our suppliers and within the industry to achieve this.",
    ]

description = """- Vicuna 1.5-based ESG Classification (Classes: environmental event, societal event, governmental event and out-of-scope) """


def esg(question):
    try:
        url = 'https://turbo.skynet.coypu.org/'
        request = requests.post(url, json={"messages": [{"role": "user",
                                                "content": f"Which class does the following text best fall into? Environmental event, Societal event, Governmental event or out-of-scope? Note that out-of-scope refers to any class other than Environment, Social, Governance. Answer with a single word.\n\n{question}"}],
                                "temperature": 0.1,
                                "max_new_tokens": 10,
                                 "key": "M7ZQL9ELMSDXXE86"}).json()
        return request[0].get('choices')[0].get("message").get("content")
    except Exception as e:
        return e


with gr.Blocks() as esgClassificationTab:
    with gr.Row():
        gr.Markdown(f"{description}")
    with gr.Row():
        with gr.Column():
            input_box = gr.TextArea(label='Input text')
            gr.Examples(examples, inputs=input_box, label='Example text')
            esgRun = gr.Button(variant='primary')
        with gr.Column():
            answer_box = gr.JSON(label='Result', interactive=False)

    esgRun.click(fn=esg, inputs=input_box, outputs=[answer_box])

