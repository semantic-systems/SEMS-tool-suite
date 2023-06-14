import gradio as gr
import requests
from feeds import GdeltFunctions


def utc(message, scheme='Earthquake, Flooding, Tropical storm, Explosion, Shooting, Wildfire, Hostage, Pandemic, War, Inflation'):
    try:
        url = 'https://sc.hitec.skynet.coypu.org'
        headers = {'Content-Type': 'application/json'}
        scheme = [element.strip() for element in scheme.split(',')]
        output = requests.post(url, json={'message': message, "key": "GBGBE3THWLF9FB2U", "scheme": scheme}, headers=headers).json()
        return output
    except Exception as e:
        return e


text_examples=["\"One-in-100-year flood event\" devastates Western Australia",
          "118th United States Congress convenes; House of Representatives adjourns without electing Speaker for first time in 100 years.",
          "UK Treasury considering plans for digital pound, economic secretary says.",
          "Troops freed by Mali return to Ivory Coast."]

scheme_examples=["Environmental event, Societal event, Governmental event",
          "Exchange, Buy in, Payment, Sell out, Expressing publicly, Institutionalization, Bankruptcy",
          "Feeling happy, Feeling sad, Feeling angry, Feeling melancholic, Feeling calm, Feeling like a child",
          "Exposition, Rising action, Climax, Falling action, Resolution"]

api = GdeltFunctions()

with gr.Blocks() as UniversalEventDetectorTab:
    with gr.Row():
        gr.Markdown(f"- Enter your a list of labels (separated by , ) in the 'scheme' field.\n"
                    f"- The Universal Event Detector (UED) will pay attention to them and try to do zero-shot classification for you.\n"
                    f"- The default value is 'Earthquake, Flooding, Tropical storm, Explosion, Shooting, Wildfire, Hostage, Pandemic, War, Inflation'.\n"
                    f"- And have fun!\n")
    with gr.Row():
        # Inputs
        with gr.Column():
            input_box = gr.TextArea(label='Input text')    
            scheme_box = gr.TextArea(label='Scheme',
                                     placeholder="Earthquake, Flooding, Tropical storm, Explosion, Shooting, Wildfire, Hostage, Pandemic, War, Inflation",
                                     value="Earthquake, Flooding, Tropical storm, Explosion, Shooting, Wildfire, Hostage, Pandemic, War, Inflation")
            with gr.Accordion("Text Examples", open=False):
                gr.Examples(text_examples, inputs=input_box, label='')
            with gr.Accordion("Scheme Examples", open=False):
                gr.Examples(scheme_examples, inputs=scheme_box, label='')
            with gr.Accordion("Get real news from Gdelt", open=False, visible=True):
                twitter_input_box = gr.Text(label='Query for Feeds')
                getFeedButton = gr.Button("Query Feed")
            with gr.Row():
                with gr.Column():
                    delete_input_button = gr.Button("Delete text", elem_id='delete')
                with gr.Column():
                    delete_scheme_button = gr.Button("Delete scheme", elem_id='delete')
                with gr.Column():
                    runEEButton = gr.Button("Run UED", variant='primary')

        # Results
        with gr.Column():
            output_box_label = gr.JSON(label="Label:", interactive=False)

    # Functions
    getFeedButton.click(fn=api.get_feed, inputs=twitter_input_box, outputs=input_box)
    delete_input_button.click(fn=lambda:"", inputs=[], outputs=input_box)
    delete_scheme_button.click(fn=lambda:"", inputs=[], outputs=scheme_box)
    runEEButton.click(fn=utc, inputs=[input_box, scheme_box], outputs=output_box_label)
