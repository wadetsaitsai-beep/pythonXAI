print("hello world!")
print("蔡承佑")
print("不要低頭\n雙下巴會出來")
 
'''
 這是多行註解
'''

# 這是單行註解
print("hello world!") #print是在終端機顯示的指令
# ctrl + / 可以快速註解或取消註解

# 基本型態
print(1) # int這是整數, -1,0,1,2
print(1.0) # float這是浮點數
print(1.234) # float這是浮點數
print("APPLE") # string這是字串 "sad123", '1'
print(True) # bool這是布林值 True/False
print(False) # bool這是布林值 True/False

# 變數
a = 10 #新增一個儲存空間並取名為a, "="的功能是將右邊的值10存入左邊的a
print(a) # 在終端機顯示a所存的值
a = "apple" #將a的值改為"apple"
print(a) # 在終端機顯示a所存的值

# 運算子
print(1 + 1) #加法
print(1 - 1) #減法
print(1 * 1) #乘法
print(1 / 1) #除法
print(1 // 1) #整除
print(1 % 1) #取餘數
print(2 ** 3) #次方

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減

# 字串運算，+、*
print("hello" + "world") #字串相加
print("hello" * 3) #字串乘法

# 字串格式化
name = "apple"
age = 18
print(f"Hello, my name is {name}, I'm {age} years old.")  # f-string
# 可以將變數或其他型態的資料放到f字串裡面的{}，這樣就可以在字串中顯示

print(len("apple")) #len()是一個函式，可以計算字串的長度
print(len("，"))  #len()是一個函式，可以計算字串的長度
# type()，可以查看變數的型態
print(type(1)) #(class 'int')
print(type(1.0)) #(class 'float')
print(type("apple")) #(class 'str')
print(type(True)) #(class 'bool')

# 型態轉換
print(int(1.0)) #將浮點數轉為整數
print(float(1)) #將整數轉為浮點數
print(str(1)) #將整數轉為字串
print(bool(1)) #將整數轉為布林值
print(int(1.234)) #將浮點數轉為整數
print(float('1.234')) #將字串轉為浮點數
print(str(1.0)) #將浮點數轉為字串
print(bool(10.0)) #將浮點數轉為布林值
# print(int('apple')) #將字串轉為整數，會報錯

# 請使用者輸入半徑，計算園面積
r=float(input("請輸入半徑:")) #input()是輸入函式，會將使用者輸入的資料轉為字串
print(f"園的面積是: {3.14 * r ** 2}")

a = float(input("請輸入國文期中成績:"))
b = float(input("請輸入國文期末成績:"))
print(f"國文平均成績是: {(a + b) / 2}")