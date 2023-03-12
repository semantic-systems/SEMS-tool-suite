import gradio as gr
import plotly
import requests
from feeds import GdeltFunctions


api = GdeltFunctions()


def ee(q):
    try:
        url = 'http://event_visualizer_container:5281'
        headers = {'Content-Type': 'application/json'}
        output = requests.post(url, json={'message': q}, headers=headers).json()
        descriptions = output.get('descriptions')
        descriptions += "\n Note:\n " \
                        "- oos refers to an out-of-scope class.\n" \
                        "- DBSCAN is used as the clustering algorithm.\n" \
                        "- PC 1 and PC 2 refers to the first and the second principal components of the sentence embeddings, when reduced to two dimensions.\n"
        fig_cls = plotly.io.read_json('fig_cls')
        fig_cluster = plotly.io.read_json('fig_cluster')
        return descriptions, fig_cls, fig_cluster
    except Exception as e:
        return e,e,e


with gr.Blocks() as eventVisualizationTab:
    with gr.Row():
        gr.Markdown(
            value="This process takes about 10 seconds to complete. The following steps are executed if you click the submit botton. \n "
                  "- It queries 250 articles from GDELT (the max. for a single query in GDELT).\n"
                  "- Only articles written in English are selected for further analyses. \n "
                  "- Titles of the articles will be fed into the event type detector. \n"
                  "- A unsupervised clustering algorithm takes sentence embeddings as input and output cluster assignments. \n"
                  "- Visualization of both the classified result and clustering result will be displayed.")
    # Inputs
    with gr.Column():
        input_box = gr.Text(placeholder="Enter a keyword here...", label="Keyword to query GDELT")
        with gr.Row():
            with gr.Column():
                delete_input_button = gr.Button("Delete", elem_id='delete')
            with gr.Column():
                runEEButton = gr.Button("Submit", variant='primary')
        with gr.Row():
            output_box_description = gr.Markdown(label="Description")
        with gr.Row():
            plot_cls = gr.Plot(label="Classification Result").style()
        with gr.Row():
            plot_cluster = gr.Plot(label="Clustering Result").style()

        # Functions
        delete_input_button.click(fn=lambda:"", inputs=[], outputs=input_box)
        runEEButton.click(fn=ee, inputs=input_box, outputs=[output_box_description, plot_cls, plot_cluster])
