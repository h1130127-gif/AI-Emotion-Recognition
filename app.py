import gradio as gr
from deepface import DeepFace

# 情緒分析主程式
def multimodal_emotion_ai(user_text, input_image):
    # ---- 1. 處理文字 ----
    # 這裡先用簡單的關鍵字邏輯代替
    text_result = "正向" if "開心" in user_text or "棒" in user_text else "未知"
    
    # ---- 2. 處理影像（防爆機制） ----
    face_result = "未偵測到人臉"
    if input_image is not None:
        try:
            # Gradio 傳進來的 input_image 直接就是一個 NumPy 矩陣，可以直接餵給 DeepFace
            predictions = DeepFace.analyze(img_path=input_image, actions=['emotion'], enforce_detection=False)
            face_result = predictions[0]["dominant_emotion"]
        except Exception as e:
            face_result = f"分析失敗: {str(e)}"
            
    # ---- 3. 結合結果 ----
    final_output = f"【文字分析】：講話內容偏向 {text_result}\n【臉部表情】：偵測到 {face_result}"
    return final_output

# 建立 Gradio 介面
demo = gr.Interface(
    fn=multimodal_emotion_ai,
    # 定義兩個輸入組件：一個文字框、一個影像上傳框
    inputs=[
        gr.Textbox(label="第一步：請輸入說的話", placeholder="例如：我今天好高興！"),
        gr.Image(label="第二步：請上傳測試大頭照（或用網頁相機拍照）")
    ],
    # 定義輸出組件
    outputs=gr.Textbox(label="系統多模態辨識結果"),
    title="🎭 高中生專題：多模態情緒辨識系統",
    description="請同時輸入文字與照片，系統將結合兩者判斷您的真實心境！"
)

# 啟動網頁
if __name__ == "__main__":
    demo.launch()
