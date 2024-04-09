import streamlit as st
from utils.tmux_helper import TmuxHelper
from streamlit_autorefresh import st_autorefresh


# 设置页面配置为宽模式
st.set_page_config(layout="wide")


# 创建TmuxHelper实例
tmux_helper = TmuxHelper()

st_autorefresh(interval=5000, key='tmux_session_refresher')

# Streamlit应用标题
st.title("Tmux Sessions Outputs")

# 获取所有tmux会话
session_list = tmux_helper.get_session_list()

# 动态设置列数，例如根据会话数量来决定
columns_per_row = st.number_input("Enter the number of columns", min_value=1, max_value=10, value=3)

# 让用户自定义tmux会话的显示顺序
user_ordered_sessions = st.multiselect("Arrange the tmux sessions in the order you prefer:",
                                       options=session_list, default=session_list)


# 对于所有会话，动态创建行和列来展示输出
for i in range(0, len(user_ordered_sessions), columns_per_row):
    # 创建一行中的列
    cols = st.columns(columns_per_row)
    # 在每列中显示会话的输出
    for j in range(columns_per_row):
        # 计算当前会话的索引
        session_index = i + j
        # 如果当前索引小于会话列表长度，则显示该会话输出
        if session_index < len(user_ordered_sessions):
            session_name = user_ordered_sessions[session_index]
            # 使用cols[j]来指定列，展示会话名称和输出
            with cols[j]:
                st.markdown(f"**Session: {session_name}**")
                stdout = tmux_helper.get_stdout(session_name)
                if stdout:
                    st.text_area(f"Output of {session_name}", value=stdout, height=300, max_chars=None)
                else:
                    st.write("No output available.")
