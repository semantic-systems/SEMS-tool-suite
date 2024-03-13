import gradio as gr
from tabs import kgVisualizationTab, eventExtractionTab, questionAnswerTab, UniversalEventDetectorTab, eventVisualizationTab, esgClassificationTab

title = "Coypu MoD"

css = """
#row {height: 100%} 
.gradio-container {background-color: #E8E8DC}
.custom-footer {    
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    font-size: 16px;
    font-weight: 600;
    --tw-text-opacity: 1;
    color: rgb(209 213 219 / var(--tw-text-opacity));}
"""

'''main gradio function that defines all tabs'''
with gr.Blocks(css=css, title=title) as demo:
    with gr.Row():
        img_funny_coy = gr.Image("./images/colored_top_image.svg")
    with gr.Tab('KG Connect & Visualization'):
        kgVisualizationTab.render()
    #with gr.Tab('Knowledge Extraction'):
    #    knowledgeExtractionTab.render()
    with gr.Tab('Event Extraction'):
        eventExtractionTab.render()
    with gr.Tab('Universal Event Detection'):
        UniversalEventDetectorTab.render()
    # with gr.Tab('Event Visualization'):
    #     eventVisualizationTab.render()
    with gr.Tab('Question Answering'):
        questionAnswerTab.render()

    with gr.Tab('ESG Classification'):
        esgClassificationTab.render()

    with gr.Row():
        footer_links = gr.HTML("""
                               <div class='custom-footer'>
                                    <a href='https://www.hitec-hamburg.de/impressum/' target='_blank' rel='noreferrer' class='group hover:text-gray-400 dark:hover:text-gray-400 transition-colors'>Impressum</a>
                                    &nbsp; • &nbsp;
                                    <a href='https://www.hitec-hamburg.de/datenschutz/' target='_blank' rel='noreferrer' class='group hover:text-gray-400 dark:hover:text-gray-400 transition-colors'>Datenschutz</a>  
                               </div>
                                """)
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")
