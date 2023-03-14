import webbrowser

import gradio as gr
import plotly
import requests
from feeds import GdeltFunctions
import json
from ipywidgets import Output


api = GdeltFunctions()

out = Output()
@out.capture(clear_output=True)
def do_click(trace, points, state):
    print("hey i am here")
    if points.point_inds:
        print("hey you clicked me!")
        ind = points.point_inds[0]
        url = trace["customdata"][ind][1]
        # url = df.link.iloc[ind]
        webbrowser.open_new_tab(url)

        
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
        with open("./fig_cls.json", "w") as f:
            json.dump(output.get('fig_cls'), f)
        with open("./fig_cluster.json", "w") as f:
            json.dump(output.get('fig_cluster'), f)
        fig_cls = plotly.io.read_json("./fig_cls.json")
        fig_cluster = plotly.io.read_json("./fig_cluster.json")
        trace_cls = fig_cls.data[0]
        trace_cluster = fig_cluster.data[0]
        trace_cls.on_click(do_click)
        trace_cluster.on_click(do_click)
        return descriptions, fig_cls, fig_cluster
    except Exception as e:
        return e, e, e


with gr.Blocks() as eventVisualizationTab:
    with gr.Row():
        gr.Markdown(
            value="Event visualizer in MoD aims to visualize news queired with a keyword from the past 24 hours. "
                  "An event type classifier is used to generate the scatter plot (left), "
                  "which offers a fast overview on the event types in the past 24 hours. "
                  "However, the classifier is not error-free. Therefore, a clustering algorithm is used to create "
                  "event clusters as shown in the scatter plot (right)."
                  " Please enter a keyword to search for news from GDELT. "
                  "The following steps will happen once you click the submit botton. \n "
                  "- 250 articles are queried from the GDELT API, and only English articles are filtered in.\n"
                  "- Titles of the articles are used as features for the classifier and the clustering algorithm. \n"
                  "- DBSCAN (eps=3, min_samples=2) clusters the PCA-reduced features. \n"
                  "- Visualization of both the classified and clustered result are displayed. \n"
                  "(try \"Hamburg\" to see what happened in Hamburg in the past 24 hours!)")
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
            with gr.Column():
                plot_cls = gr.Plot(label="Classification Result").style()
            with gr.Column():
                plot_cluster = gr.Plot(label="Clustering Result").style()

        # Functions
        delete_input_button.click(fn=lambda:"", inputs=[], outputs=input_box)
        runEEButton.click(fn=ee, inputs=input_box, outputs=[output_box_description, plot_cls, plot_cluster])

