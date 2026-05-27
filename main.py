pip install deepface opencv-python
import gradio as gr
def analyze_emotion(user_text):
    return f"系統收到的文字是：'{user_text}'，準備進行 NLP 分析！"
demo = gr.Interface(
    fn=analyze_emotion, 
    inputs=gr.Textbox(label="請輸入你想說的話（例如：我今天好開心）"), 
    outputs="text"
)
demo.launch()
