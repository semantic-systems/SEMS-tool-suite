from typing import List
import gradio as gr
from pipelines import KnowledgeExtractionPipeline
from feeds import TwitterFunctions

knowledgeExtractionPipeline = KnowledgeExtractionPipeline()
twitterFunctions = TwitterFunctions()


def callPipeline(inputText: str, model: str):
    result = knowledgeExtractionPipeline.testExtract(inputText)
    return result


with gr.Blocks() as knowledgeExtractionTab:

    # Inputs
    keInputText = gr.TextArea(label='Input text')
    with gr.Row():
        with gr.Column(scale=1):
            tweetQueryText = gr.Text(label='Query for Tweets', elem_id='test')
            with gr.Row():
                getTweetButton = gr.Button("Query Tweet")
                deleteTextButton = gr.Button("Delete")

        with gr.Column(scale=1):
            dropdownKEModel = gr.Dropdown(
                label='Model for Knowledge Extraction', value='spacy', choices=['spacy', 'rebel'])
            runKEButton = gr.Button("Run Knowledge Extraction")

    # Results
    with gr.Row():
        kgInJSONLD = gr.Json('{}', label='KG in JSON-LD')
        gr.Label(label='Visualization of the constructed Knowledge Graph...')

    # Functions
    getTweetButton.click(fn=twitterFunctions.getTweet,
                         inputs=tweetQueryText, outputs=keInputText)
    deleteTextButton.click(fn=lambda: "", inputs=[], outputs=keInputText)
    runKEButton.click(fn=callPipeline, inputs=[
                      keInputText, dropdownKEModel], outputs=kgInJSONLD)
