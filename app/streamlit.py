import streamlit as st
from services.plan_excute import PlanExcute, SEOpt # 确保路径正确
import asyncio

# 定义一个同步包装器，用于调用异步函数
def sync_plan_execute(user_message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(PlanExcute(user_message))
    loop.close()
    return result

def sync_SEOpt(user_message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(SEOpt(user_message))
    loop.close()
    return result

# 初始化或更新session_state
if 'show_dialogue' not in st.session_state:
    st.session_state.show_dialogue = None

def show_dialogue_1():
    st.session_state.show_dialogue = 1

def show_dialogue_2():
    st.session_state.show_dialogue = 2

st.set_page_config(page_title="企业应用指南：Plan and Execute", layout="wide")

col1, col2 = st.columns([2.5,4])

with col1:
    st.image("logo.jpg", width=200)  # 确保路径正确

with col2:
    st.title("企业应用指南")

# 侧边栏按钮
st.sidebar.button('AI助手小度', on_click=show_dialogue_1)
st.sidebar.button('出海商家SEO助手', on_click=show_dialogue_2)

# 根据选择显示不同的对话
if st.session_state.show_dialogue == 1:
    st.markdown("<h2 style='text-align: center;'>AI助手小度</h2>", unsafe_allow_html=True)
    user_message = st.text_input('问题', '请问你需要我帮助你什么：', key="dialogue_1")
    if st.button('提问'):
        with st.spinner('小度正在思考...'):
            answer = sync_plan_execute(user_message)
            st.markdown(f"<div style='color: blue; font-size: 20px;'>{answer}</div>", unsafe_allow_html=True)
elif st.session_state.show_dialogue == 2:
    st.markdown("<h2 style='text-align: center;'>商品SEO优化</h2>", unsafe_allow_html=True)
    user_message = st.text_input('问题', '请输入你需要优化的商品描述：', key="dialogue_2")
    if st.button('优化'):
        with st.spinner('正在优化SEO...'):
            answer = sync_SEOpt(user_message)
            st.markdown(f"<div style='color: blue; font-size: 20px;'>{answer}</div>", unsafe_allow_html=True)

st.sidebar.header("关于")
st.sidebar.info("这是基于文心大模型使用Streamlit构建的企业应用指南示例。\n\n 你可以点击左侧按钮与智能助手小度对话，或者使用右侧按钮优化商品描述。\n\n\n\n\n\n\n\n 贡献自Tritonix团队")
