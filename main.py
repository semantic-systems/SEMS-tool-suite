from gradio_graph import gradio as gr
from tabs import *


def main() -> None:
   '''main gradio function that defines all tabs'''
   with gr.Blocks() as demo:
      with gr.Tab('KG Connect & Visualization'):
         kgVisualizationTab.render()
      with gr.Tab('Knowledge Extraction'):
         knowledgeExtractionTab.render()
      with gr.Tab('Event Extraction'):
         eventExtractionTab.render()
      with gr.Tab('Maximum Damage'):
         maximumDamageTab.render()
      with gr.Tab('Question Answering'):
         questionAnswerTab.render()
   demo.launch()


if __name__ == "__main__":
   main()