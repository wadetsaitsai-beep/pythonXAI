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
