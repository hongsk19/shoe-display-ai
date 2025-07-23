
import streamlit as st
import pandas as pd
from ai_model import calculate_priority
from optimizer import optimize_display

# Simple login (hardcoded)
def login(username, password):
    return username == "admin" and password == "1234"

# Login screen
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("👟AI 신발 진열 시스템 Proto- 로그인")
    username = st.text_input("아이디")
    password = st.text_input("비밀번호", type="password")
    login_button = st.button("로그인")

    if login_button:
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("로그인 성공!")
            st.rerun()  # 🔁 로그인 성공 후 앱 재시작
        else:
            st.error("아이디 또는 비밀번호가 잘못되었습니다.")
    st.stop()

# Main app after login
st.title("👟 신발 매장 진열 추천")

uploaded_file = st.file_uploader("CSV 파일 업로드", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📦 원본 데이터")
    st.dataframe(df)

    df = calculate_priority(df)
    df = optimize_display(df)

    st.subheader("🤖 AI 추천 결과")
    st.dataframe(df[['product_id', 'priority', 'display_qty', 'recommended_zone']])
