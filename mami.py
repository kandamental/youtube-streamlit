import streamlit as st
import pandas as pd
import numpy as np
import time

# ２カラムレイアウトにする
left_column, right_column = st.beta_columns(2)

#  左側→ボタンを追加　右側→テキストを表示
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム") 

# プログレスバーの表示
st.write("プログレスバーの表示")
"Start!"
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done!!!"