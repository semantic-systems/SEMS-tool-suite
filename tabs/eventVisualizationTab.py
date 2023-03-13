import gradio as gr
import plotly
import requests
from feeds import GdeltFunctions
import json
import plotly.graph_objects as go
import pandas as pd


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
        with open("./fig_cls.json", "w") as f:
            json.dump(output.get('fig_cls'), f)
        with open("./fig_cluster.json", "w") as f:
            json.dump(output.get('fig_cluster'), f)
        fig_cls = plotly.io.read_json("./fig_cls.json")
        fig_cluster = plotly.io.read_json("./fig_cluster.json")
        fig_timeline = get_event_timeline_plot()
        return descriptions, fig_cls, fig_cluster, fig_timeline
    except Exception as e:
        return e,e,e, e


def get_event_timeline_plot():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

    fig = go.Figure(go.Scatter(
        x=df['Date'],
        y=df['mavg']
    ))

    fig.update_xaxes(
        rangeslider_visible=True,
        tickformatstops=[

            dict(dtickrange=[86400000, 604800000], value="%e. %b d"),
            dict(dtickrange=[604800000, "M1"], value="%e. %b w"),
            dict(dtickrange=["M1", "M12"], value="%b '%y M"),
            dict(dtickrange=["M12", None], value="%Y Y")
        ]
    )
    return fig


with gr.Blocks() as eventVisualizationTab:
    with gr.Row():
        gr.Markdown(
            value="Please enter a keyword to search for news from GDELT. The following steps will happen once you click the submit botton. \n "
                  "- 250 articles are queried from the GDELT API, and only English articles are filtered in.\n"
                  "- Titles of the articles are used as features. \n"
                  "- DBSCAN (eps=3, min_samples=2) clusters the PCA-reduced features. \n"
                  "- Visualization of both the classified and clustered result are displayed.")
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
            gr.Markdown("Yet, your clustering algorithm might tell you another story.")
            plot_cluster = gr.Plot(label="Clustering Result").style()
        with gr.Row():
            gr.Markdown("...")
        with gr.Row():
            plot_timeline = gr.Plot(label="Event Timeline").style()

        # Functions
        delete_input_button.click(fn=lambda:"", inputs=[], outputs=input_box)
        runEEButton.click(fn=ee, inputs=input_box, outputs=[output_box_description, plot_cls, plot_cluster, plot_timeline])
