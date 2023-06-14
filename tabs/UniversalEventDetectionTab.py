import gradio as gr
import requests
from feeds import GdeltFunctions


def utc(message, scheme):
    try:
        url = 'https://sc.hitec.skynet.coypu.org'
        headers = {'Content-Type': 'application/json'}
        output = requests.post(url, json={'message': message, "key": "GBGBE3THWLF9FB2U", "scheme": scheme}, headers=headers).json()
        return output
    except Exception as e:
        return e


examples=["\"One-in-100-year flood event\" devastates Western Australia",
          "118th United States Congress convenes; House of Representatives adjourns without electing Speaker for first time in 100 years.",
          "UK Treasury considering plans for digital pound, economic secretary says.",
          "Troops freed by Mali return to Ivory Coast."]


with gr.Blocks() as UniversalEventDetectorTab:
    with gr.Row():
        gr.Markdown(f"Enter your a list of labels (separated by , ) in the 'scheme' field. The Universal Event Detector (UED) will pay attention to them and try to do zero-shot classification for you."
                    f"The default value is 'Earthquake, Flooding, Tropical storm, Explosion, Shooting, Wildfire, Hostage, Pandemic, War, Inflation'."
                    f"Have fun!")
    with gr.Row():
        # Inputs
        with gr.Column():
            input_box = gr.TextArea(label='Input text')    
            with gr.Accordion("Examples", open=False):
                gr.Examples(examples, inputs=input_box, label='')
            with gr.Accordion("Get examples from Gdelt", open=False, visible=True):
                twitter_input_box = gr.Text(label='Query for Feeds')
                getFeedButton = gr.Button("Query Feed")
            with gr.Row():
                with gr.Column():
                    delete_input_button = gr.Button("Delete", elem_id='delete')
                with gr.Column():
                    runEEButton = gr.Button("Run UED", variant='primary')

        # Results
        with gr.Column():
            output_box_label = gr.JSON(label="Label:", interactive=False)

    # Functions
    getFeedButton.click(fn=GdeltFunctions.get_feed, inputs=twitter_input_box, outputs=input_box)
    delete_input_button.click(fn=lambda:"", inputs=[], outputs=input_box)
    runEEButton.click(fn=utc, inputs=input_box, outputs=output_box_label)
