from gradio_graph import gradio as gr


def test(a):
    print(a)

    return a


demo = gr.Interface(
    test,
    gr.Textbox(placeholder="Enter sentence here..."),
    "graph",
    examples=[
        "http://rdf.freebase.com/ns/aviation.aircraft", "http://rdf.freebase.com/ns/m.03jmrzx",
    ],
)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")