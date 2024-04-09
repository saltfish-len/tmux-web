import streamlit as st
from utils.tmux_helper import TmuxHelper
from streamlit_autorefresh import st_autorefresh

# 创建TmuxHelper实例
tmux_helper = TmuxHelper()

# 设置自动刷新，每5秒刷新一次
st_autorefresh(interval=5000, key='tmux_session_refresher')

# Streamlit应用标题
st.title("Tmux Sessions Manager")

# 获取所有tmux会话
session_list = tmux_helper.get_session_list()

# 在侧边栏中为每个会话创建一个链接
st.sidebar.title("Tmux Sessions")
if 'selected_session_name' not in st.session_state:
    st.session_state.selected_session_name = session_list[0] if session_list else None

for session_name in session_list:
    if st.sidebar.button(session_name):
        st.session_state.selected_session_name = session_name

# 根据用户选择的会话显示详细信息
if st.session_state.selected_session_name:
    st.header(f"Session: {st.session_state.selected_session_name}")

    # 显示当前会话的输出
    stdout = tmux_helper.get_stdout(st.session_state.selected_session_name)
    if stdout:
        st.text_area("Session Output", value=stdout, height=300)
    else:
        st.write("No output available.")
