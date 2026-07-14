import streamlit as st #匯入streamlit模組並取名為st

# st.number_input()可以讓使用者輸入數字，設定step=1可以讓使用者只能輸入整數
# min_value=0可以設定最小值為0，max_value=100可以設定最大值，value=50可以設定預設值
number = st.number_input("請輸入一個整數", step=1, min_value=0, max_value=100)
# st.markdown()可以在網頁中使用Markdown語法顯示文字
st.markdown(f"您輸入的數字是：{number}")

st.markdown("---")
st.markdown("### 練習")
number2 = st.number_input("請輸入另一個整數", step=1, min_value=0, max_value=100)
if number2 > 90:
    st.markdown('你的等級是A')
elif number2 > 80:
    st.markdown('你的等級是B')
elif number2 > 70:
    st.markdown('你的等級是C')
elif number2 > 60:
    st.markdown('你的等級是D')
else:
    st.markdown('你的等級是F')

import streamlit as st #匯入streamlit模組並取名為st

st.markdown("---")
st.markdown("### 按鈕練習")
#st.button()可以在網頁中顯示一個按鈕，使用者可點擊按鈕
#key式按鈕的識別名稱，可用於區分不同按鈕
#當使用者點擊按鈕時，會回傳True，否則回傳False
st.button("點擊我", key="button1")
if st.button("點擊我", key="toggle"):
    st.toggle("切換")
if st.button("點擊我", key="balloon"):
    st.balloons()