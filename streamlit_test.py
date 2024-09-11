import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 创建 Streamlit 应用
st.title("数学函数绘图")

# 创建输入框
function_input = st.text_input("请输入数学函数（例如：np.sin(x)）:")

# 创建提交按钮
if st.button("绘制"):
    try:
        # 定义 x 轴数据
        x = np.linspace(-10, 10, 400)
        # 计算 y 轴数据
        y = eval(function_input)
        
        # 创建图形
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title(f"函数: {function_input}")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        
        # 显示图形
        st.pyplot(fig)
    except Exception as e:
        st.write(f"错误: {e}")
print("done")