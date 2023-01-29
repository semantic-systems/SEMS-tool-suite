import gradio as gr

with gr.Blocks() as kgVisualizationTab:
    with gr.Row():
        # the onload function is used to pass the theme parameter to the iframe - kinda clunky, but it works. If someone has a better way of doing this, please let me know!
        html = gr.HTML(
            '<iframe src="https://sch-28.github.io/kg-vis" style="height:80vh; width:100%;" id="k-graph" onload="const query = window.location.search;const url_params = new URLSearchParams(query);const theme = url_params.get(`__theme`);if(theme){const iframe = document.querySelector(`gradio-app`).shadowRoot.getElementById(`k-graph`);if(iframe.src !== `https://sch-28.github.io/kg-vis/?theme=${theme}`) iframe.src = `https://sch-28.github.io/kg-vis/?theme=${theme}`}"></iframe>')
