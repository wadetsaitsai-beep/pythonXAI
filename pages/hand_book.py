import streamlit as st
with st.expander("Class 1 課堂筆記" ):

    st.write(
        """

# 🐍 Python 基礎筆記（國小版）

## 1. `print()`：把內容顯示出來

`print()` 就像是在跟電腦說：「請把這段內容秀給我看！」

```python
print("Hello World!")
print("蔡承佑")
```

畫面會顯示：

```
Hello World!
蔡承佑
```

### 換行 `\n`

如果想要讓文字分成兩行，可以使用 `\n`。

```python
print("不要低頭\n雙下巴會出來")
```

畫面：

```
不要低頭
雙下巴會出來
```

---

# 2. 註解（給人看的說明）

註解是寫給自己或其他人看的，**電腦不會執行**。

### 單行註解

```python
# 這是一行註解
```

### 多行註解

```python
'''
這是第一行
這是第二行
'''
```

💡 小技巧：

按 **Ctrl + /** 可以快速註解或取消註解。

---

# 3. 資料種類（資料型態）

Python 裡有很多種資料。

| 型態    | 名稱                 | 範例             |
| ------- | -------------------- | ---------------- |
| `int`   | 整數                 | `1`、`100`、`-5` |
| `float` | 小數                 | `3.14`、`1.5`    |
| `str`   | 文字（字串）         | `"Apple"`        |
| `bool`  | 布林值（只有對或錯） | `True`、`False`  |

例如：

```python
print(1)
print(3.14)
print("Apple")
print(True)
```

---

# 4. 變數（資料的小盒子）

變數就像一個貼了名字的小盒子，可以把資料放進去。

```python
a = 10
print(a)
```

畫面：

```
10
```

也可以換內容：

```python
a = "Apple"
print(a)
```

畫面：

```
Apple
```

💡 一個變數裡的資料可以改變。

---

# 5. 數學運算

Python 可以像計算機一樣算數學。

```python
1 + 1
```

常見運算：

| 符號 | 功能   | 範例      |
| ---- | ------ | --------- |
| `+`  | 加法   | `3+2=5`   |
| `-`  | 減法   | `5-2=3`   |
| `*`  | 乘法   | `3*4=12`  |
| `/`  | 除法   | `8/2=4.0` |
| `//` | 整除   | `7//2=3`  |
| `%`  | 取餘數 | `7%2=1`   |
| `**` | 次方   | `2**3=8`  |

---

# 6. 運算順序

算式有先後順序：

1. `()` 括號
2. `**` 次方
3. `* / // %`
4. `+ -`

例如：

```python
print((2+3)*4)
```

答案是：

```
20
```

---

# 7. 字串（文字）的運算

### 把文字接起來

```python
print("Hello" + "World")
```

結果：

```
HelloWorld
```

---

### 重複文字

```python
print("Hi!" * 3)
```

結果：

```
Hi!Hi!Hi!
```

---

# 8. f 字串（把資料放進句子）

可以把變數放進一句話裡。

```python
name = "Apple"
age = 18

print(f"我的名字是{name}，我今年{age}歲。")
```

結果：

\```
我的名字是Apple，我今年18歲。
```

💡 變數要放在 `{\}` 裡。

---

# 9. `len()`：算長度

可以算文字有幾個字。

```python
print(len("apple"))
```

結果：

```
5
```

---

# 10. `type()`：看看資料是什麼種類

```python
print(type(1))
print(type("apple"))
```

結果：

```
<class 'int'>
<class 'str'>
```

可以知道資料是哪一種型態。

---

# 11. 型態轉換

有時候要把資料變成另一種型態。

```python
int(1.9)
```

結果：

```
1
```

常用轉換：

| 指令      | 功能             |
| --------- | ---------------- |
| `int()`   | 變整數           |
| `float()` | 變小數           |
| `str()`   | 變文字           |
| `bool()`  | 變 True 或 False |

例如：

```python
print(float(5))
```

結果：

```
5.0
```

⚠️ 不是所有資料都能轉換，例如：

```python
int("apple")
```

會發生錯誤。

---

# 12. `input()`：請使用者輸入資料

可以請使用者輸入內容。

```python
name = input("請輸入名字：")
```

如果要輸入數字，通常要加上 `int()` 或 `float()`。

例如：

```python
age = int(input("請輸入年齡："))
```

---

# 13. 範例：計算圓面積

圓面積公式：

**圓面積 = π × 半徑²**

```python
r = float(input("請輸入半徑："))

print(f"圓的面積是：{3.14 * r ** 2}")
```

---

# 14. 範例：計算平均

```python
a = float(input("請輸入期中成績："))
b = float(input("請輸入期末成績："))

print(f"平均成績是：{(a+b)/2}")
```

---

# 🌐 Streamlit（做網頁）

Streamlit 可以把 Python 做成漂亮的網頁。

先匯入：

```python
import streamlit as st
```

---

## `st.title()`

顯示最大的標題。

```python
st.title("我的第一個網頁")
```

---

## `st.write()`

可以顯示很多種類的資料，例如：

- 文字
- 數字
- 表格
- Markdown

```python
st.write("Hello")
```

---

## `st.text()`

只能顯示普通文字。

```python
st.text("Hello")
```

---

## `st.markdown()`

可以使用 Markdown 做漂亮的排版。

例如：

```python
st.markdown(\"""
# 大標題

## 小標題

- 蘋果
- 香蕉
- 西瓜

**粗體**

*斜體*
\""")
```

可以做出：

- 大標題
- 小標題
- 項目清單
- 粗體文字
- 斜體文字
- 程式碼
- 分隔線
- 超連結

---

# 🎯 今天學到的重點

✅ `print()`：把內容顯示出來

✅ 註解：寫說明，不會執行

✅ 四種基本資料型態：

- `int`（整數）
- `float`（小數）
- `str`（文字）
- `bool`（True、False）

✅ 變數：裝資料的小盒子

✅ 數學運算：`+ - * / // % **`

✅ 字串可以相加、重複

✅ `f""`：把變數放進句子

✅ `len()`：算文字長度

✅ `type()`：看資料種類

✅ `int()`、`float()`、`str()`、`bool()`：資料型態轉換

✅ `input()`：請使用者輸入資料

✅ 練習做：

- 計算圓面積
- 計算平均分數

✅ Streamlit 常用指令：

- `st.title()`：標題
- `st.write()`：顯示各種資料
- `st.text()`：純文字
- `st.markdown()`：美化排版

---

"""
    )

with st.expander("Class 2 課堂筆記" ):
    st.write(
        """

# 🐍 Python 基礎筆記（二）

## 今天學會：比較、判斷、按鈕和重複做事情

---

# 1. 比較運算子（比一比）

比較運算子可以幫助電腦判斷兩個東西是不是一樣，或是哪一個比較大。

比較完後，答案只有兩種：

- `True`（對、是真的）
- `False`（錯、不是）

| 符號 | 意思       | 範例     | 結果  |
| ---- | ---------- | -------- | ----- |
| `==` | 等於       | `5 == 5` | True  |
| `!=` | 不等於     | `5 != 5` | False |
| `>`  | 大於       | `8 > 5`  | True  |
| `<`  | 小於       | `3 < 2`  | False |
| `>=` | 大於或等於 | `5 >= 5` | True  |
| `<=` | 小於或等於 | `5 <= 5` | True  |

例如：

```python
print(8 > 5)
```

結果：

```
True
```

💡 小提醒：

通常要比較**同一種類**的資料，例如數字跟數字、文字跟文字。

---

# 2. 邏輯運算子（一起判斷）

有時候，一個條件還不夠，需要一次判斷很多條件。

這時可以使用：

- `and`
- `or`
- `not`

---

## （1）and（而且）

兩個條件都要成立，答案才會是 `True`。

就像：

👉「今天是星期六，而且沒有下雨。」

兩件事情都要是真的。

```python
print(True and True)
```

結果：

```
True
```

但是：

```python
print(True and False)
```

結果：

```
False
```

### 小口訣

✅ 全部都對 → True

❌ 只要有一個錯 → False

---

## （2）or（或者）

只要有一個條件成立就可以。

例如：

👉「今天吃披薩或漢堡。」

有其中一個就可以。

```python
print(True or False)
```

結果：

```
True
```

### 小口訣

✅ 有一個對 → True

❌ 全部都錯 → False

---

## （3）not（相反）

`not` 就是把答案反過來。

```python
print(not True)
```

結果：

```
False
```

```python
print(not False)
```

結果：

```
True
```

---

# 3. 運算順序

Python 也有計算順序。

1. `()` 括號
2. `**` 次方
3. `* / // %`
4. `+ -`
5. `== != > < >= <=`
6. `not`
7. `and`
8. `or`

先算前面的，再算後面的。

---

# 4. if 判斷（如果……就……）

生活中每天都在做判斷。

例如：

- 如果下雨，就帶雨傘。
- 如果肚子餓，就吃飯。

Python 也是一樣。

```python
if 條件:
    要做的事情
```

例如：

```python
score = 90

if score >= 60:
    print("及格")
```

---

# 5. if、elif、else

可以讓電腦做很多種選擇。

例如密碼檢查：

```python
password = input("請輸入密碼：")

if password == "1234":
    print("歡迎cy")
elif password == "5678":
    print("歡迎cy2")
elif password == "0000":
    print("歡迎cy3")
else:
    print("密碼錯誤")
```

意思就是：

先檢查第一個。

不是，再檢查第二個。

再不是，就檢查第三個。

全部都不是，就執行 `else`。

---

## if 和 elif 的差別

### 多個 if

每一個都會檢查。

```
if
if
if
```

全部都要看一次。

---

### if + elif + else

找到正確答案後，就不再往下檢查。

```
if
↓
elif
↓
elif
↓
else
```

所以速度比較快，也比較省時間。

---

# 6. Streamlit 輸入數字

可以在網頁做一個數字輸入框。

```python
number = st.number_input("請輸入數字")
```

還可以設定：

- `min_value`：最小值
- `max_value`：最大值
- `value`：預設值
- `step`：每次增加多少

例如：

```python
number = st.number_input(
    "請輸入一個整數",
    min_value=0,
    max_value=100,
    step=1
)
```

代表：

- 最小 0
- 最大 100
- 一次加 1

---

# 7. 成績等級判斷

利用 if 做成績分類。

```python
if number > 90:
    st.markdown("你的等級是A")
elif number > 80:
    st.markdown("你的等級是B")
elif number > 70:
    st.markdown("你的等級是C")
elif number > 60:
    st.markdown("你的等級是D")
else:
    st.markdown("你的等級是F")
```

例如：

| 成績 | 等級 |
| ---- | ---- |
| 95   | A    |
| 84   | B    |
| 76   | C    |
| 63   | D    |
| 40   | F    |

---

# 8. 按鈕（Button）

可以做一個按鈕。

```python
st.button("點擊我")
```

使用者按下去時，就會回傳 `True`。

例如：

```python
if st.button("點我"):
    st.balloons()
```

按下按鈕，就會放氣球🎈。

---

## Toggle（開關）

```python
st.toggle("切換")
```

像燈的開關一樣。

可以：

- 開（True）
- 關（False）

---

# 9. for 迴圈（一直重複）

如果有很多事情要重複做，就不用一直寫很多次。

例如：

```
請說五次你好
```

不用寫：

```python
print("你好")
print("你好")
print("你好")
print("你好")
print("你好")
```

可以寫：

```python
for i in range(5):
    print("你好")
```

---

# 10. range()

`range()` 可以產生一串數字。

## range(5)

```python
range(5)
```

會產生：

```
0
1
2
3
4
```

不會包含 5。

---

## range(5,10)

```python
range(5,10)
```

結果：

```
5
6
7
8
9
```

---

## range(5,10,2)

第三個數字代表每次跳幾格。

```python
range(5,10,2)
```

結果：

```
5
7
9
```

一次跳 2。

---

# 11. 迴圈變數 i

在 for 裡面的 `i`，每次都會拿到不同的數字。

```python
for i in range(5):
    print(i)
```

畫面：

```
0
1
2
3
4
```

可以把 `i` 想成一位正在數數的小幫手。

---

# 12. 在迴圈中計算

例如：

```python
for i in range(5):
    a = i * 2
```

每一次：

| i   | a   |
| --- | --- |
| 0   | 0   |
| 1   | 2   |
| 2   | 4   |
| 3   | 6   |
| 4   | 8   |

最後：

```python
print(a)
```

答案是：

```
8
```

因為 `a` 每一次都被更新，最後留下的是最後一次的結果。

---

# 🎯 今天重點整理

✅ 比較運算子

- `==` 等於
- `!=` 不等於
- `>`
- `<`
- `>=`
- `<=`

答案只有：

- `True`
- `False`

---

✅ 邏輯運算子

- `and`：全部都要對
- `or`：有一個對就可以
- `not`：答案相反

---

✅ if 判斷

可以讓電腦依照不同情況做不同事情。

---

✅ elif

找到符合的條件就停止，不用繼續檢查。

---

✅ Streamlit

- `st.number_input()`：輸入數字
- `st.button()`：按鈕
- `st.toggle()`：開關
- `st.balloons()`：放氣球動畫
- `st.markdown()`：顯示文字

---

✅ for 迴圈

可以重複做很多次事情。

---

✅ range()

- `range(5)` → 0～4
- `range(5,10)` → 5～9
- `range(5,10,2)` → 5、7、9

---
""")

with st.expander("Class 3 課堂筆記" ):
    st.write(
        '''


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

| 參數        | 用途     |
| --------- | ------ |
| step      | 每次增加多少 |
| min_value | 最小值    |
| max_value | 最大值    |

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

| 程式   | 結果  |
| ---- | --- |
| L[0] | 1   |
| L[1] | 2   |
| L[3] | 'a' |

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

* 強制刷新畫面
* 更新 session_state 後立即重新整理
* 某些元件更新時很有用

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
 '''
    )

with st.expander("Class 4 課堂筆記" ):

    st.write(
        '''

---

# Python & Streamlit 課程筆記

## 一、Streamlit 基本功能

### 1. 載入套件

```python
import streamlit as st
import time
import random
```

* `streamlit`：建立網頁介面
* `time`：控制時間，例如延遲
* `random`：產生亂數

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

* `st.title()`：大標題
* `st.subheader()`：次標題
* `st.write()`：輸出資料
* `st.warning()`：警告訊息
* `st.success()`：成功訊息

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

* 建立答案
* 建立上下限
* 建立遊戲狀態

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

| 運算子 | 意思   |
| --- | ---- |
| +=  | 加    |
| -=  | 減    |
| *=  | 乘    |
| /=  | 除    |
| %=  | 取餘數  |
| //= | 整數除法 |
| **= | 次方   |

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

* Key 不可重複
* Key 必須不可變
* Value 可以重複

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

* Streamlit 基本元件（Button、Text Input、Number Input、Columns）
* `st.session_state` 保存資料
* `st.rerun()` 重新整理畫面
* 購物車新增與刪除功能
* 猜數字遊戲邏輯
* 指定運算子與運算子優先順序
* `while`、`for`、`break`
* `random` 亂數函式
* Dictionary（建立、查詢、新增、修改、刪除）
* 巢狀 Dictionary 的資料存取
* 平均值計算與資料整理
'''
    )

with st.expander("Class 5 課堂筆記" ):

    st.write(
        '''

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

'''
    )