import streamlit as st
import random
import time # 匯入時間模組，用來做一點點小延遲增加張力

# 設定網頁標題和圖示 (這是瀏覽器標籤頁上的標題)
st.set_page_config(page_title="終極密碼王", page_icon="🎯")

# 1. 初始化遊戲狀態 (只在第一次載入網頁時執行)
if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, 100) # 隨機挑選 1-100 的答案
    st.session_state.low = 1                         # 目前範圍的下限
    st.session_state.high = 100                      # 目前範圍的上限
    st.session_state.game_over = False               # 紀錄遊戲是否結束
    st.session_state.message = None                  # 一開始不預設任何提示訊息

# 網頁大標題
st.title("猜數字遊戲")

# 2. 顯示目前的數字範圍
st.subheader(f"請輸入 :red[{st.session_state.low}] 到 :red[{st.session_state.high}] 的整數")

# 3. 提示訊息顯示區 (只有在玩家猜錯、有警告訊息時才會顯示)
if st.session_state.message:
    st.warning(st.session_state.message)

# 4. 遊戲輸入與邏輯判定
if not st.session_state.game_over:
    # 💡 關鍵改動：加入 label_visibility="collapsed" 來徹底隱藏提示字且不留白！
    guess = st.number_input(
        "請輸入你猜的數字：",
        min_value=st.session_state.low,
        max_value=st.session_state.high,
        value=st.session_state.low,  # 預設值自動貼齊當前最小值
        step=1,
        key="guess_input",
        label_visibility="collapsed"  # 👈 隱藏標籤字樣
    )

    # 建立按鈕版面
    col1, col2 = st.columns([1, 3])
    with col1:
        submit_button = st.button("提交答案", use_container_width=True)

    if submit_button:
        if guess < st.session_state.target:
            st.session_state.low = guess 
            st.session_state.message = f"🤔 【{guess}】太小了！範圍縮小囉！"
            st.rerun() 
            
        elif guess > st.session_state.target:
            st.session_state.high = guess 
            st.session_state.message = f"🧐 【{guess}】太大了！範圍縮小囉！"
            st.rerun()
            
        else:
            # === 🎉 猜對了！驚喜效果爆發 🎉 ===
            st.session_state.game_over = True
            
            # 顯示大號的慶祝 Markdown 文字
            st.markdown(f"""
                <h1 style='text-align: center; color: #FF4B4B; font-size: 50px;'>
                    🎉🎊 恭喜！你猜對了！ 🎊🎉
                </h1>
                <h2 style='text-align: center; color: #31333F;'>
                    答案就是 {st.session_state.target}
                </h2>
            """, unsafe_allow_html=True)
            
            st.balloons() # 呼叫氣球效果！
            time.sleep(1) # 稍微延遲讓驚喜感留存
            st.rerun()    # 重新整理以更新畫面

# 5. 猜對之後，顯示「再玩一次」的按鈕與精美勝利面板
else:
    st.markdown(f"""
        <div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px; text-align: center;'>
            <h1 style='color: #4CAF50;'>🏆 勝利！🏆</h1>
            <h3>最終答案：{st.session_state.target}</h3>
        </div>
        <br>
    """, unsafe_allow_html=True)
    
    if st.button("再來一局！挑戰你的直覺", use_container_width=True, type="primary"):
        # 重設所有遊戲狀態，開啟全新一局
        st.session_state.target = random.randint(1, 100)
        st.session_state.low = 1
        st.session_state.high = 100
        st.session_state.game_over = False
        st.session_state.message = None # 新遊戲開始一樣不顯示提示
        st.rerun()