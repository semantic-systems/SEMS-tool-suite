import gradio as gr
import requests
from twitter import TwitterFunctions

def ee(q):
    try:
        url = 'http://coypu-eventextraction-event_extractor-1:5278'
        headers = {'Content-Type': 'application/json'}
        output = requests.post(url, json={'message': q}, headers=headers).json()
        return output.get('event type'), output.get('event arguments'), output.get('event graph')
    except Exception as e:
        return e,e,e

examples=[
    "A preliminary 6.20 magnitude #earthquake has occurred near Taft, Eastern Visayas, #Philippines.",
    "A shooting has been reported at Saugus High School in Santa Clarita just north of Los Angeles.",
    "Six Vicpol officers have tested positive this month #COVID19",
    "One person was missing following a large explosion at an apparent industrial building in Houston Friday. The blast damaged nearby buildings and homes."
    ]


with gr.Blocks() as eventExtractionTab:
    with gr.Row():
        # Inputs
        with gr.Column():
            input_box = gr.TextArea(label='Input text')    
            with gr.Accordion("Examples", open=False):
                gr.Examples(examples, inputs=input_box, label='')
            with gr.Accordion("Get examples from Twitter", open=False, visible=True):
                twitter_input_box = gr.Text(label='Query for Tweets')
                getTweetButton = gr.Button("Query Tweet")
            with gr.Row():
                with gr.Column():
                    delete_input_button = gr.Button("Delete", elem_id='delete')
                with gr.Column():
                    runEEButton = gr.Button("Run Event Extraction", variant='primary')

        # Results
        with gr.Column():
            output_box_event_type = gr.Textbox(label="Event type:", interactive=False)
            output_box_entities = gr.JSON(label="Extracted entities:", interactive=False)
            output_box_graph = gr.JSON(label="Event graph:", interactive=False)

    # Functions
    getTweetButton.click(fn=TwitterFunctions.getTweet, inputs=twitter_input_box, outputs=input_box)  
    delete_input_button.click(fn=lambda:"", inputs=[], outputs=input_box)
    runEEButton.click(fn=ee, inputs=input_box, outputs=[output_box_event_type, output_box_entities, output_box_graph])
