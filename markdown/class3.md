當然可以！我幫你整理成適合複習的筆記，保留重點、語法和容易搞混的地方。

---

# Python & Streamlit 學習筆記

## 一、number_input 數字輸入

```python
import streamlit as st

number = st.number_input(
    "請輸入一個整數 (1-9)",
    step=1,
    min_value=1,
    max_value=9
)
```

### 參數

| 參數      | 用途         |
| --------- | ------------ |
| step      | 每次增加多少 |
| min_value | 最小值       |
| max_value | 最大值       |

---

## 二、for 迴圈

```python
for i in range(1, number+1):
    st.write(str(i)*i)
```

### 輸入 5

```
1
22
333
4444
55555
```

### 重點

```python
str(i) * i
```

代表把數字轉成字串後重複 i 次。

例如

```
str(4) * 4
```

結果

```
4444
```

---

# 三、List（串列）

## 建立 List

```python
[]
```

空的 list

```python
[1,2,3]
```

三個元素

```python
[1,2,3,'a','b']
```

不同型態可以混合

```python
[1,2,3,['a','b']]
```

List 裡面可以放 List。

---

## 取得元素

```python
L=[1,2,3,'a','b','c']
```

| 程式 | 結果 |
| ---- | ---- |
| L[0] | 1    |
| L[1] | 2    |
| L[3] | 'a'  |

### 注意

index 從 **0** 開始。

---

# 四、List 切片 (Slice)

假設

```python
L=[1,2,3,'a','b','c']
```

## 全部

```python
L[:]
```

```
[1,2,3,'a','b','c']
```

---

## 每隔一個取

```python
L[::2]
```

結果

```
[1,3,'b']
```

---

## 指定範圍

```python
L[1:4]
```

結果

```
[2,3,'a']
```

> 不包含 index 4

---

## 範圍+間隔

```python
L[1:4:2]
```

結果

```
[2,'a']
```

### 記法

```
[start : end : step]
```

和

```
range(start,end,step)
```

很像。

---

# 五、append()

新增元素

```python
L=[1,2,3]

L.append(4)
```

結果

```
[1,2,3,4]
```

永遠加到最後面。

---

# 六、remove()

刪除指定元素

```python
L=['a','b','c','d','a']

L.remove('a')
```

結果

```
['b','c','d','a']
```

### 注意

remove()

只刪除第一個找到的元素。

---

若要刪全部

```python
for i in L:
    if i=="a":
        L.remove(i)
```

> ⚠️ 不建議在走訪 list 時直接刪除元素，可能會跳過部分元素。較安全的方法是建立新 list，例如：
>
> ```python
> L = [x for x in L if x != "a"]
> ```

---

# 七、pop()

依照 index 刪除

```python
L.pop(0)
```

刪第一個

```python
L.pop()
```

刪最後一個

---

# 八、sort()

排序

```python
L=[3,1,5,2]

L.sort()
```

結果

```
[1,2,3,5]
```

### 注意

sort()

會直接修改原本的 List。

---

# 九、List 走訪

## 方法一：利用 index

```python
for i in range(len(L)):
    print(L[i])
```

適合需要知道位置。

---

## 方法二：直接走訪

```python
for i in L:
    print(i)
```

適合只需要元素。

---

# 十、Streamlit Columns

建立欄位

```python
col1,col2=st.columns(2)
```

放按鈕

```python
col1.button("按鈕1")
col2.button("按鈕2")
```

---

## 設定比例

```python
st.columns([2,1])
```

代表

```
■■
■
```

左邊比較寬。

---

## 三欄

```python
st.columns([1,2,3])
```

比例

```
1 : 2 : 3
```

---

## with 用法

```python
with col1:
    st.button("按鈕")
    st.write("文字")
```

可以把很多元件放進同一欄。

---

## 用 for 建立很多欄

```python
cols=st.columns(4)

for i in range(4):
    with cols[i]:
        st.button(f"按鈕{i+1}")
```

適合大量元件。

---

# 十一、文字輸入

```python
text=st.text_input(
    "輸入文字",
    value="預設文字"
)
```

取得輸入

```python
st.write(text)
```

---

# 十二、session_state

## 問題

如果寫

```python
ans=1
```

按按鈕

```python
ans+=1
```

畫面重新整理後

```
ans
```

又變回

```
1
```

因為 Streamlit 每次都重新執行程式。

---

## 解法

```python
if "ans" not in st.session_state:
    st.session_state.ans=1
```

增加

```python
st.session_state.ans +=1
```

顯示

```python
st.write(st.session_state.ans)
```

這樣數值就能保留。

---

# 十三、st.rerun()

重新執行整個程式

```python
st.rerun()
```

用途：

- 強制刷新畫面
- 更新 session_state 後立即重新整理
- 某些元件更新時很有用

---

# 今日重點整理 ⭐

✅ `number_input()`：建立數字輸入框，並限制輸入範圍。
✅ `range(start, end, step)`：控制 for 迴圈的起點、終點（不包含 end）與間隔。
✅ `List`：可存放不同型態資料，也能巢狀存放其他 List。
✅ `append()`：新增元素到 List 尾端。
✅ `remove()`：刪除第一個符合的元素；走訪時直接刪除要特別小心。
✅ `pop()`：依索引刪除元素，未指定索引時刪除最後一個。
✅ `sort()`：將 List 原地排序。
✅ `Slice`：`[start:end:step]` 用於擷取 List 的部分內容。
✅ `st.columns()`：建立多欄版面，可搭配 `with` 管理元件。
✅ `st.text_input()`：建立文字輸入框。
✅ `st.session_state`：保存資料，避免每次重新執行程式時變數重設。
✅ `st.rerun()`：強制重新執行整個 Streamlit 程式。
