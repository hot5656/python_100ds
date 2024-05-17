# Gradio 1st example
# [Hugging Face](https://huggingface.co/)
# pip install gradio
# http://127.0.0.1:7860/
# https://609f0dd05ce375b555.gradio.live/
import gradio as gr

def rStr(text):
    return text.replace("morning", "night")

# 建立 gradio
# rStr : 處理函數
# inputs : 輸入欄位
 # outputs : 輸出欄位
grobj = gr.Interface(fn = rStr,
            inputs = gr.Textbox(),
            outputs = gr.Textbox())
# 啟動 gradio
# share=True : public 執行
# grobj.launch(share=True)
grobj.launch()
