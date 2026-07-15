import streamlit as st
with st.expander("Class 1 課堂筆記" ):

    st.write(
        """
以下是整理成**適合國小學生閱讀**的 Python 筆記，用簡單的說法搭配小例子，方便複習。

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
我將內容整理成一份**適合國小學生閱讀**的 Python 筆記，延續前一次的風格，加入生活化比喻與簡單範例，方便複習。

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