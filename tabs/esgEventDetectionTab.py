import gradio as gr
import requests
from twitter import TwitterFunctions

def ee(q):
    try:
        url = 'https://esg-classifier.skynet.coypu.org'
        headers = {'Content-Type': 'application/json'}
        output = requests.post(url, json={'message': q, "key": "4QT4B4JNCL5SLJM5"}, headers=headers).json()
        return output.get('label'), output.get('wikidata')
    except Exception as e:
        return e,e

examples=["\"One-in-100-year flood event\" devastates Western Australia",
          "118th United States Congress convenes; House of Representatives adjourns without electing Speaker for first time in 100 years.",
          "UK Treasury considering plans for digital pound, economic secretary says.",
          "Troops freed by Mali return to Ivory Coast."]


with gr.Blocks() as esgEventExtractionTab:
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
            output_box_event_type_link = gr.Textbox(label="Event type link:", interactive=False)

    # Functions
    getTweetButton.click(fn=TwitterFunctions.getTweet, inputs=twitter_input_box, outputs=input_box)  
    delete_input_button.click(fn=lambda:"", inputs=[], outputs=input_box)
    runEEButton.click(fn=ee, inputs=input_box, outputs=[output_box_event_type, output_box_event_type_link])
