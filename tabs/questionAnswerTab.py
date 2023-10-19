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
        print(question)
        url = 'https://turbo.skynet.coypu.org/'
        request = requests.post(url, json={"messages": [{"role": "user",
               "content": f"You are a question answering system expert. Please reformulate the following sentence into a reasonable question for a LLM. /n/n {question} /n/n "}],
                                "temperature": 0.1,
                                "key": "M7ZQL9ELMSDXXE86"
        }).json()
        print("request", request)

        reforumated_question = request[0].get('choices')[0].get("message").get("content")
        print("reforumated_question", reforumated_question)
        request = requests.post(url, json={"messages": [{"role": "user",
                                                "content": reforumated_question}],
                                "temperature": 0.1,
                                "max_new_tokens": 120,
                                 "key": "M7ZQL9ELMSDXXE86"}).json()
        print("answer", request[0].get('choices')[0].get("message").get("content"))
        return reforumated_question, request[0].get('choices')[0].get("message").get("content")
    except Exception as e:
        return e, e


# with gr.Blocks() as questionAnswerTab:
#     with gr.Row():
#         gr.Markdown(f"{description}")
#     with gr.Row():
#         with gr.Column():
#             question_box = gr.TextArea(label='Question')
#             gr.Examples(examples, inputs=question_box, label='Example questions')
#             qaRun = gr.Button(variant='primary')
#         with gr.Column():
#             answer_box = gr.JSON(label='Answer', interactive=False)
#             reformulated_question_box = gr.JSON(label='Reformulated question', interactive=False)
#
#     qaRun.click(fn=qa, inputs=question_box, outputs=[reformulated_question_box, answer_box])


if __name__ == "__main__":
    qa("What is the population of Germany?")