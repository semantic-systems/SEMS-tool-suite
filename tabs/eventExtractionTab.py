import gradio as gr
from twitter import TwitterFunctions
import requests

def ee(q):
    try:
        url = 'http://event_extractor:5278'
        headers = {'Content-Type': 'application/json'}
        return requests.post(url, json={'message': q}, headers=headers).json()
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
        event_type = gr.Text(label='Event Type', interactive=False, visible=True)
        entities = gr.Text(label='Entities', interactive=False, visible=False)
        graph = gr.Text(label='Graph', interactive=False, visible=False)

    # Functions
    # getTweetButton.click(fn=twitterFunctions.getTweet, inputs=tweetQueryText, outputs=inputText)
    # deleteTextButton.click(fn=lambda:"", inputs=[], outputs=inputText)
    
    runKEButton.click(fn=ee, inputs=eeInputText, outputs=event_type)
    runKEButton.click(fn=ee, inputs=eeInputText, outputs=entities)
    runKEButton.click(fn=ee, inputs=eeInputText, outputs=graph)
