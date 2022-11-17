import gradio as gr
from twitter import TwitterFunctions

#knowledgeExtractionPipeline = KnowledgeExtractionPipeline()
twitterFunctions = TwitterFunctions()

# def callPipeline(inputText : str, model : str):
#     result = knowledgeExtractionPipeline.testExtract(inputText)
#     return result


with gr.Blocks() as eventExtractionTab:
    # Inputs
    gr.TextArea(label='Input text')
    with gr.Row():
        with gr.Column(scale=1):
            gr.Text(label='Query for Tweets')
            with gr.Row():
                gr.Button("Query Tweet")
                gr.Button("Delete")
        with gr.Column(scale=1):
            runKEButton = gr.Button("Run Event Extraction")
    # Results
    with gr.Row():
        gr.Text(label='Event Type', interactive=False)
        gr.Text(label='Arguments', interactive=False)
        gr.Text(label='Links', interactive=False)
    gr.Label(label='Visualization of the constructed Knowledge Graph...')

    # Functions
    # getTweetButton.click(fn=twitterFunctions.getTweet, inputs=tweetQueryText, outputs=inputText)
    # deleteTextButton.click(fn=lambda:"", inputs=[], outputs=inputText)
    # #runKEButton.click(fn=callPipeline, inputs=[inputText, dropdownKEModel], outputs=kgInJSONLD)
