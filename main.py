import gradio as gr
from tabs import kgVisualizationTab, eventExtractionTab, questionAnswerTab, esgEventExtractionTab

title = "Coypu MoD"

'''main gradio function that defines all tabs'''
with gr.Blocks(css="#row {height: 100%} .gradio-container {background-color: #E8E8DC}", title=title) as demo:
    with gr.Row():
        img_funny_coy = gr.Image("./images/colored_top_image.svg")
    with gr.Tab('KG Connect & Visualization'):
        kgVisualizationTab.render()
    #with gr.Tab('Knowledge Extraction'):
    #    knowledgeExtractionTab.render()
    with gr.Tab('Event Extraction'):
        eventExtractionTab.render()
    #with gr.Tab('Maximum Damage'):
    #    maximumDamageTab.render()
    with gr.Tab('Question Answering'):
        questionAnswerTab.render()
    with gr.Tab('ESG Event Type Detection'):
        esgEventExtractionTab.render()
    
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")
