太好了，購物平台成功完成 🎉
今天的內容其實涵蓋了 **Streamlit 基礎介面、圖片處理、狀態管理、AI API 串接、聊天機器人製作** 幾個重要主題。我幫你整理成一份筆記，方便之後複習。

# Streamlit + OpenAI API 學習筆記

---

# 一、Streamlit 基礎

## 1. 匯入 Streamlit

```python
import streamlit as st
```

Streamlit 是一個可以快速建立網頁介面的 Python 套件。

執行方式：

```bash
streamlit run 檔案名稱.py
```

例如：

```bash
streamlit run class4-3.py
```

---

# 二、Streamlit 常用元件

## 1. 標題

```python
st.title("標題文字")
```

顯示網頁的大標題。

範例：

```python
st.title("🛒 購物平台")
```

結果：

```
🛒 購物平台
```

---

## 2. 文字顯示

### 一般文字

```python
st.write("文字內容")
```

例如：

```python
st.write("價格：10元")
```

---

### 成功提示

```python
st.success("購買成功！")
```

顯示綠色提示框。

---

### 錯誤提示

```python
st.error("庫存不足")
```

顯示紅色錯誤框。

---

### 分隔線

```python
st.divider()
```

建立水平分隔線。

---

# 三、圖片元件

## 1. 顯示圖片

```python
st.image("圖片路徑", width=寬度)
```

範例：

```python
st.image(
    "image/apple.png",
    width=300
)
```

---

## 2. 讀取資料夾圖片

需要：

```python
import os
```

取得資料夾：

```python
image_folder = "image"
```

取得所有檔案：

```python
image_files = os.listdir(image_folder)
```

例如：

```python
st.write(image_files)
```

結果：

```
apple.png
banana.png
orange.png
```

---

## 3. 使用迴圈顯示所有圖片

```python
for image_file in image_files:

    st.image(
        f"{image_folder}/{image_file}",
        width=100
    )
```

可以一次顯示資料夾內所有圖片。

---

## 4. 圖片大小控制

### 固定寬度

```python
width=300
```

---

### 使用容器寬度

```python
use_container_width=True
```

圖片會自動符合欄位大小。

---

# 四、Streamlit 使用者輸入元件

---

## 1. 數字輸入框

```python
st.number_input()
```

範例：

```python
size = st.number_input(
    "圖片大小",
    min_value=50,
    max_value=500,
    step=50,
    value=100
)
```

參數：

| 參數      | 功能         |
| --------- | ------------ |
| min_value | 最小值       |
| max_value | 最大值       |
| step      | 每次增加多少 |
| value     | 預設值       |

---

## 2. 下拉選單

```python
st.selectbox()
```

範例：

```python
product = st.selectbox(
    "選擇商品",
    ["蘋果","香蕉"]
)
```

---

## 3. 按鈕

```python
st.button()
```

範例：

```python
if st.button("購買"):

    st.success("成功")
```

按下按鈕後執行程式。

---

# 五、版面配置 Layout

## columns 欄位

```python
st.columns()
```

範例：

```python
cols = st.columns(4)
```

建立四個欄位。

搭配：

```python
for col in cols:

    with col:

        st.write("內容")
```

可以製作商品卡片。

---

# 六、Path 圖片路徑管理

使用：

```python
from pathlib import Path
```

取得目前程式位置：

```python
BASE_DIR = Path(__file__).resolve().parent
```

取得上一層：

```python
IMAGE_DIR = BASE_DIR.parent / "image"
```

好處：

- 不怕換電腦
- 不怕執行位置不同
- 避免 FileNotFoundError

例如：

```python
IMAGE_DIR / "apple.png"
```

會自動組成：

```
pythonXAI/image/apple.png
```

---

# 七、session_state 狀態保存

Streamlit 每次操作都會重新執行程式。

如果要保存資料，需要：

```python
st.session_state
```

---

## 初始化資料

範例：

```python
if "products" not in st.session_state:

    st.session_state.products = {}
```

意思：

如果還沒有商品資料，就建立。

---

## 商品資料結構

本次購物平台：

```python
{
 "蘋果":{
    "price":10,
    "stock":10,
    "image":"apple.png"
 }
}
```

包含：

- 商品名稱
- 價格
- 庫存
- 圖片

---

# 八、購物平台製作重點

流程：

```
建立商品資料
        ↓
顯示商品圖片
        ↓
顯示價格
        ↓
顯示庫存
        ↓
按購買
        ↓
stock - 1
        ↓
重新整理畫面
```

---

## 扣庫存

```python
info["stock"] -= 1
```

等同：

```python
info["stock"] = info["stock"] - 1
```

---

## 重新整理

```python
st.rerun()
```

用途：

讓修改後的資料立即更新。

例如：

購買後：

```
庫存10
 ↓
購買
 ↓
庫存9
```

---

# 九、OpenAI API 基礎

安裝：

```bash
pip install openai
```

---

## 載入 API Key

使用：

```python
from dotenv import load_dotenv
```

讀取：

```python
load_dotenv()
```

取得：

```python
os.getenv("OPENAI_API_KEY")
```

---

# 十、OpenAI 基本對話

設定：

```python
openai.api_key = API_KEY
```

建立回答：

```python
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
        "role":"user",
        "content":"你好"
        }
    ]
)
```

---

取得 AI 回覆：

```python
response.choices[0].message.content
```

---

# 十一、AI 對話紀錄

AI 要記得之前聊天內容：

建立：

```python
messages=[]
```

---

加入使用者：

```python
messages.append(
{
"role":"user",
"content":text
}
)
```

---

加入 AI：

```python
messages.append(
{
"role":"assistant",
"content":reply
}
)
```

形成：

```
使用者
 ↓
AI
 ↓
使用者
 ↓
AI
```

---

# 十二、Streamlit 聊天介面

## 顯示聊天泡泡

使用：

```python
st.chat_message()
```

使用者：

```python
st.chat_message(
"user"
).write("你好")
```

AI：

```python
st.chat_message(
"assistant"
).write("您好")
```

---

## 使用者輸入框

```python
st.chat_input()
```

範例：

```python
prompt = st.chat_input(
"請輸入訊息"
)
```

---

# 十三、AI Chatbot 架構

完整流程：

```
使用者輸入
      |
      ↓
chat_input()
      |
      ↓
加入 history
      |
      ↓
送給 OpenAI API
      |
      ↓
取得 AI 回覆
      |
      ↓
加入 history
      |
      ↓
重新整理
```

---

# 十四、三欄排版

```python
st.columns([4,2,1])
```

代表：

```
第一欄 : 4
第二欄 : 2
第三欄 : 1
```

比例：

```
████████  ████  ██
```

常用於：

- 設定區
- 模型選擇
- 清除按鈕

---

# 十五、今日完成作品

## 🛒 Streamlit 購物平台

功能：

✅ 商品圖片顯示
✅ 商品價格
✅ 商品庫存
✅ 購買按鈕
✅ 自動扣庫存
✅ 新增庫存
✅ 商品選擇
✅ 即時更新

使用技術：

- Streamlit
- Path
- session_state
- columns
- button
- selectbox
- number_input

---

## 🤖 AI 聊天機器人

功能：

✅ 使用 OpenAI API
✅ 保存聊天紀錄
✅ 自訂 System Message
✅ 選擇 AI Model
✅ Streamlit 聊天泡泡介面

使用技術：

- OpenAI API
- dotenv
- session_state
- chat_message
- chat_input

---

# 今日重點整理（一句話版）

> Streamlit 可以快速建立互動式網站；利用 session_state 保存資料，再搭配 OpenAI API，就能製作具有記憶功能的 AI 網頁應用。
