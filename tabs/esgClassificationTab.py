import gradio as gr
import requests


examples=[
    "CDP Climate Change Response : To meet our commitment to achieve netzero emissions by 2025, we are focusing first on actual reductions across our Scope 1, 2 and 3 emissions. • We plan to meet our office energy needs with 100% renewable electricity by 2023 and equip our people to make climate smart travel decisions. In fiscal 2021, we were already powering our offices and centers globally with 53% renewable electricity. • We will require 90% of our key suppliers (defined as vendors that represent a significant portion of our 2019 Scope 3 emissions) to disclose their environmental targets and actions being taken to reduce emissions by 2025. • To address remaining emissions, we are investing in nature-based carbon removal solutions that will directly remove carbon from the atmosphere.",
    "Biodiversity : Biodiversity Enhancement and Compensation Programme As part of its strategy on mitigation hierarchy, ACCIONA has a programme for the design and execution of voluntary initiatives that go beyond governmental requirements and the aim of which is to contribute to the Net Positive Impact on Biodiversity, favouring the situation of certain threatened species and/or ecosystems.",
    "Eliminating Deforestation : Hershey commits to eliminating commodity-driven deforestation from our entire supply chain by 2030 while respecting and protecting the human rights of individuals. Guided by our No Deforestation Policy, we will work within our individual commodity supply chains to drive sustainable practices with our suppliers and within the industry to achieve this.",
    ]

description = """- Vicuna 1.5-based ESG Classification (only three classes) """


def esg(question):
    try:
        url = 'https://turbo.skynet.coypu.org/'
        request = requests.post(url, json={"messages": [{"role": "user",
                                                "content": f"Which class does this text best fall into? Environment, Social or Governance? Answer with a single word.\n\n{question}"}],
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
            gr.Examples(examples, inputs=question_box, label='Example text')
            esgRun = gr.Button(variant='primary')
        with gr.Column():
            # reformulated_question_box = gr.JSON(label='Reformulated question', interactive=False)
            answer_box = gr.JSON(label='Result', interactive=False)

    esgRun.click(fn=esg, inputs=input_box, outputs=[answer_box])

