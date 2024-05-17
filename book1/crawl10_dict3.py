# 萌典 Web App
# [Hugging Face](https://huggingface.co/)
# pip install gradio
# http://127.0.0.1:7860/
# https://609f0dd05ce375b555.gradio.live/
import gradio as gr
import requests
import json

def rStr(word):
    reStr = ""
    url = f"https://www.moedict.tw/uni/{word}"
    resp = requests.get(url)
    if resp and resp.status_code == 200:
        info = json.loads(resp.text)
        print(f"查詢字詞:{info['title']}\n")
        reStr += f"查詢字詞:{info['title']}\n"
        reStr += f"部首:{info['radical']}\n"
        reStr += f"筆畫:{info['stroke_count']}\n"
        for index, data in enumerate(info['heteronyms']):
            reStr += f"[{index+1}]"
            reStr += f"  注音:{data['bopomofo']}\n"
            reStr += f"  羅馬拼音:{data['bopomofo2']}\n"
            reStr += f"  漢語拼音:{data['pinyin']}\n"
            for i, item in enumerate(data['definitions']):
                reStr += f"  ({i+1}):{item['def']}\n"
                if "type" in item:
                    reStr += f"    詞性：{item['type']}\n"
                if "example" in item:
                    reStr += f"    解釋：{item['example']}\n"
                if "quote" in item:
                    reStr += f"    引用：{item['quote']}\n"
                if "link" in item:
                    reStr += f"    參考\n"
                    for ref in item['link']:
                        reStr += f"      {ref}\n"

    return reStr

# 建立 gradio
grobj = gr.Interface(fn = rStr,
            inputs = gr.Textbox(),
            outputs = gr.Textbox())
# 啟動 gradio
# share=True : public 執行
# grobj.launch(share=True)
grobj.launch()