import streamlit as st
from pathlib import Path


# =========================
# 找到 image 資料夾
# =========================
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR.parent / "image"


# =========================
# 初始化商品
# =========================
if "products" not in st.session_state:

    st.session_state.products = {

        "蘋果": {
            "price": 10,
            "stock": 10,
            "image": IMAGE_DIR / "apple.png"
        },

        "橘子": {
            "price": 10,
            "stock": 10,
            "image": IMAGE_DIR / "orange.png"
        },

        "香蕉": {
            "price": 10,
            "stock": 10,
            "image": IMAGE_DIR / "banana.png"
        },

        "BG": {
            "price": 10,
            "stock": 10,
            "image": IMAGE_DIR / "bg.png"
        }

    }


products = st.session_state.products


# =========================
# 購物平台
# =========================
st.title("🛒 購物平台")


cols = st.columns(4)


for col, (name, info) in zip(cols, products.items()):

    with col:

        st.image(
            str(info["image"]),
            width=150
        )

        st.subheader(name)

        st.write(f"💰 價格：${info['price']}")

        st.write(f"📦 庫存：{info['stock']}")


        if st.button(f"購買{name}"):

            if info["stock"] > 0:

                info["stock"] -= 1

                st.success(f"成功購買{name}")

                st.rerun()

            else:

                st.error("庫存不足")


# =========================
# 新增庫存
# =========================
st.divider()

st.title("📦 新增商品庫存")


product = st.selectbox(
    "選擇商品",
    list(products.keys())
)


amount = st.number_input(
    "新增庫存數量",
    min_value=1,
    value=1
)



if st.button("新增庫存"):

    products[product]["stock"] += amount

    st.success(
        f"{product} 增加 {amount} 個庫存"
    )

    st.rerun()



# =========================
# 顯示目前庫存
# =========================
st.subheader("📦 目前各商品庫存")


for name, info in products.items():

    st.write(
        f"{name}：{info['stock']} 個"
    )