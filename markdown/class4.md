以下是依照你的程式整理的一份 **Python + Streamlit 課程筆記**，將內容依照主題分類，方便日後複習。

---

# Python & Streamlit 課程筆記

## 一、Streamlit 基本功能

### 1. 載入套件

```python
import streamlit as st
import time
import random
```

- `streamlit`：建立網頁介面
- `time`：控制時間，例如延遲
- `random`：產生亂數

---

### 2. 按鈕(Button)

```python
if st.button("重新整理"):
    st.success("準備重新整理")
    time.sleep(3)
    st.rerun()
```

按下按鈕後會：

1. 顯示成功訊息
2. 等待 3 秒
3. 重新整理頁面

---

### 3. 文字輸入(Text Input)

```python
c = st.text_input("請輸入餐點")
```

可以讓使用者輸入文字。

---

### 4. 數字輸入(Number Input)

```python
guess = st.number_input(
    "請輸入數字",
    min_value=1,
    max_value=100,
    step=1
)
```

限制只能輸入指定範圍的整數。

---

### 5. 標題

```python
st.title("點餐機")
st.subheader("猜數字")
```

常用：

- `st.title()`：大標題
- `st.subheader()`：次標題
- `st.write()`：輸出資料
- `st.warning()`：警告訊息
- `st.success()`：成功訊息

---

### 6. 分欄

```python
col1, col2 = st.columns(2)
```

左右分成兩欄。

例如：

```python
with col1:
    st.text_input(...)

with col2:
    st.button(...)
```

---

## 二、Session State（重要）

### 建立購物車

```python
if "cart" not in st.session_state:
    st.session_state.cart = []
```

第一次進入網站才建立購物車。

否則每次重新整理都會清空資料。

---

### 新增商品

```python
st.session_state.cart.append(c)
```

加入購物車。

---

### 刪除商品

```python
st.session_state.cart.pop(i)
```

依照索引刪除資料。

例如：

```python
for i, b in enumerate(st.session_state.cart):
    if st.button("刪除", key=f"delete_{i}"):
        st.session_state.cart.pop(i)
        st.rerun()
```

---

### 重新整理頁面

```python
st.rerun()
```

重新執行整支程式。

---

## 三、猜數字遊戲

### 初始化資料

```python
if "target" not in st.session_state:
    st.session_state.target = random.randint(1,100)
```

第一次執行時：

- 建立答案
- 建立上下限
- 建立遊戲狀態

---

### 產生亂數

```python
random.randint(1,100)
```

產生：

```
1~100（包含100）
```

---

### 判斷答案

```python
if guess < target:
```

太小

```python
elif guess > target:
```

太大

```python
else:
```

猜對

---

### 更新範圍

```python
st.session_state.low = guess
```

或

```python
st.session_state.high = guess
```

讓下一次只能猜新的範圍。

---

### 慶祝效果

```python
st.balloons()
```

畫面會出現氣球。

---

## 四、指定運算子

```python
a += 1
```

等於

```python
a = a + 1
```

常用：

| 運算子 | 意思     |
| ------ | -------- |
| +=     | 加       |
| -=     | 減       |
| \*=    | 乘       |
| /=     | 除       |
| %=     | 取餘數   |
| //=    | 整數除法 |
| \*\*=  | 次方     |

---

## 五、運算子優先順序

```
()
**
* / // %
+ -
== != > < >= <=
not
and
or
=
+=
-=
*=
...
```

最先算：

```
()
```

最後算：

```
=
```

---

## 六、while 迴圈

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

流程：

```
判斷條件

↓

成立

↓

執行程式

↓

回去判斷
```

直到條件變成 False。

---

### break

```python
if i == 3:
    break
```

立即離開迴圈。

---

## 七、for 迴圈

```python
for i in range(5):
    print(i)
```

輸出

```
0
1
2
3
4
```

---

### range()

```
range(5)
```

```
0~4
```

```
range(1,6)
```

```
1~5
```

```
range(1,6,2)
```

```
1 3 5
```

---

## 八、random 模組

```python
random.randrange(7)
```

結果：

```
0~6
```

---

```python
random.randrange(1,6)
```

結果：

```
1~5
```

---

```python
random.randrange(1,6,2)
```

結果：

```
1 3 5
```

---

## 九、Dictionary（字典）

建立：

```python
d = {
    "a":1,
    "b":2
}
```

格式：

```
key : value
```

特色：

- Key 不可重複
- Key 必須不可變
- Value 可以重複

---

### 取得 Key

```python
d.keys()
```

---

### 取得 Value

```python
d.values()
```

---

### 取得 Key、Value

```python
d.items()
```

例如：

```python
for key, value in d.items():
    print(key, value)
```

---

### 新增

```python
d["d"] = 4
```

---

### 修改

```python
d["a"] = 5
```

---

### 刪除

```python
d.pop("a")
```

如果不存在：

```python
d.pop("e","not found")
```

回傳

```
not found
```

---

### 檢查 Key

```python
"a" in d
```

True

```python
"e" in d
```

False

---

## 十、巢狀 Dictionary

例如：

```python
grade = {
    "小明":{
        "國文":[90,80,70],
        "數學":[85,75,65]
    }
}
```

取得資料：

```python
grade["小明"]["數學"]
```

得到

```
[85,75,65]
```

取得第一次成績：

```python
grade["小明"]["數學"][0]
```

得到

```
85
```

---

## 十一、計算平均

### 單科平均

```python
avg = sum(scores) / len(scores)
```

例如：

```python
avg = sum(chinese) / len(chinese)
```

---

### 全部科目平均

```python
total = 0

for scores in subjects.values():
    total += sum(scores)

avg = total / (len(subjects) * 3)
```

---

## 十二、整理所有科目成績

建立：

```python
avg_grade = {
    "國文":[],
    "數學":[],
    "英文":[]
}
```

利用：

```python
for subjects in grade.values():
    for subject, scores in subjects.items():
        avg_grade[subject] += scores
```

得到：

```
{
    "國文":[...],
    "數學":[...],
    "英文":[...]
}
```

---

## 十三、len()

List 長度：

```python
len(cart)
```

Dictionary Key 數量：

```python
len(avg_grade)
```

結果：

```
3
```

---

# 本次學習重點

- Streamlit 基本元件（Button、Text Input、Number Input、Columns）
- `st.session_state` 保存資料
- `st.rerun()` 重新整理畫面
- 購物車新增與刪除功能
- 猜數字遊戲邏輯
- 指定運算子與運算子優先順序
- `while`、`for`、`break`
- `random` 亂數函式
- Dictionary（建立、查詢、新增、修改、刪除）
- 巢狀 Dictionary 的資料存取
- 平均值計算與資料整理
