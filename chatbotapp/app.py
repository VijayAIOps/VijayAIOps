import gradio as gr
import requests
import spaces


def main():
    print("Hello from gradio-demo!")

@spaces.GPU
def chat_response(message , history):
    try:
        result = requests.post("http://localhost:8000/prompt",json={"message": message})
        result.raise_for_status()
        return result.json().get("message","No 'resonse' received")
    except requests.RequestException as e:
        return f"Request failed: {e}"
    
with gr.Blocks(theme="soft") as demo:
        gr.ChatInterface(
            title = "Simple Chat Assistant",
            description="A basic Gradio demo",
            examples=["Tell me a joke", "Give me motivational quote", "How are you?"],
            fn=chat_response
        )
if __name__ == "__main__":
    demo.launch(share=True)