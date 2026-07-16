import streamlit as st
import time

if st.button("重新整理", key="button1"):
    st.success("準備重新整理")
    time.sleep(3)
    st.rerun()

if "cart" not in st.session_state:
    st.session_state.cart = []

st.title('點餐機')

col1, col2 = st.columns(2)

with col1:
    c = st.text_input('請輸入餐點', key='input1')

with col2:
    if st.button('加入購物籃', key='button2'):
        if c != "":
            st.session_state.cart.append(c)
            st.rerun()

st.title('購物籃')

for i, b in enumerate(st.session_state.cart):
    col1, col2 = st.columns([4, 1])

    with col1:
        st.write(b)

    with col2:
        if st.button("刪除", key=f"delete_{i}"):
            st.session_state.cart.pop(i)
            st.rerun()