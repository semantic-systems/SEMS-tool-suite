from gradio_graph import gradio as gr


def test(a):
    print(a)

    return a


demo = gr.Interface(
    test,
    gr.Textbox(placeholder="Enter sentence here..."),
    "graph",
    examples=[
        ["Example"],
    ],
)


if __name__ == "__main__":
    demo.launch()
