import gradio as gr
from twitter import TwitterFunctions
import requests

def ee(q):
    try:
        url = 'http://sems-kg-1.informatik.uni-hamburg.de:5278/'
        headers = {'Content-Type': 'application/json',}
        return requests.post(url, data={'message' : q}, headers=headers)
    except Exception as e:
        return e
        

with gr.Blocks() as eventExtractionTab:
    # Inputs
    eeInputText = gr.TextArea(label='Input text', value='there was an earthquake in Hamburg last night man damn hot noodles.', interactive=True)
    with gr.Row():
        with gr.Column(scale=1):
            gr.Text(label='Query for Tweets')
            with gr.Row():
                gr.Button("Query Tweet")
                gr.Button("Delete")
        with gr.Column(scale=1):
            runKEButton = gr.Button("Run Event Extraction", variant='primary')
    # Results
    with gr.Row():
        test = gr.Text(label='Event Type', interactive=False, visible=True)
        gr.Text(label='Arguments', interactive=False, visible=False)
        gr.Text(label='Links', interactive=False, visible=False)

    # Functions
    # getTweetButton.click(fn=twitterFunctions.getTweet, inputs=tweetQueryText, outputs=inputText)
    # deleteTextButton.click(fn=lambda:"", inputs=[], outputs=inputText)
    
    runKEButton.click(fn=ee, inputs=eeInputText, outputs=test)
