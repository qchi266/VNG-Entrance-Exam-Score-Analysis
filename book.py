import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
from PIL import Image

df_tot = pd.read_csv('2024/danhsach-24.csv')
total = len(df_tot['STT'])
origin_counts = df_tot['Nơi sinh'].value_counts()

# Homepage: Overview of the entrance exam data

# Load the school logo
logo = Image.open('chuyen.jpg')
# Display the logo in the app
st.image(logo, width=800)
# Center the image
st.markdown("<div style='text-align: center;'><img src='school_logo.png' width='150'></div>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Tổng Quan Điểm Thi Đầu Vào THPT Chuyên Võ Nguyên Giáp 2024</h1>", unsafe_allow_html=True)


st.subheader("Overview")
st.write(f"Tổng số thí sinh tham gia kỳ thi đầu vào: {total}")

# Distribution of Origin: Bar chart or Pie chart
st.subheader("Phân bổ số lượng thí sinh theo vùng")
origin_fig = px.bar(origin_counts, x=origin_counts.index, y=origin_counts.values,
                    labels={'x': 'Nơi sinh', 'y': 'Số lượng học sinh'}, color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(origin_fig)

# Gender Breakdown: Pie or Bar chart
st.subheader("Tỉ lệ thí sinh tham dự tuyển sinh Chuyên Võ Nguyên Giáp (Nam : Nữ)")
gender_fig = px.pie(df_tot, names='Giới tính', title="Nam : Nữ", color_discrete_sequence=[px.colors.qualitative.Pastel[3], px.colors.qualitative.Pastel[4]])
st.plotly_chart(gender_fig)

# Score Visualization: Displaying scores per class
st.subheader("Phân phối tổng điểm thi của tất cả thí sinh tham dự")
fig_1 = px.histogram(df_tot, x="Điểm xét tuyển chuyên",
            color_discrete_sequence=px.colors.qualitative.Pastel )
fig_1.update_yaxes(title_text="Số lượng thí sinh")
st.plotly_chart(fig_1)

#Each class
anh = pd.read_csv('2024/anh-24.csv')
hoa = pd.read_csv('2024/hoa-24.csv')
ly = pd.read_csv('2024/ly-24.csv')
sinh = pd.read_csv('2024/sinh-24.csv')
su = pd.read_csv('2024/su-24.csv')
tin = pd.read_csv('2024/tin-24.csv')
toan = pd.read_csv('2024/toan-24.csv')
van = pd.read_csv('2024/van-24.csv')

classes_data = {
    'Toán': toan,
    'Lý': ly,
    'Anh': anh,
    'Hóa': hoa,
    'Sinh': sinh,
    'Sử': su,
    'Tin': tin,
    'Văn': van
}
# Select Box to choose the class
#st.title("VNG Gifted High School Class Scores Distribution")
st.subheader("Xem điểm đậu vào lớp Chuyên")

# Class selection using Streamlit's select box
class_choice = st.selectbox("Chọn lớp Chuyên", options=list(classes_data.keys()))

# Get the corresponding DataFrame based on class selection
selected_df = classes_data[class_choice].head(35)

# Define pastel colors
pastel_colors = ['#A4C3B2', '#FFD1BA', '#C7CEEA', '#e377c2']

# Display the selected class name
st.write(f"Điểm đậu Chuyên: **{class_choice}**")

# Display highest score
highest_score = selected_df[selected_df['STT'] == 1]
st.write(f"### Thủ Khoa Chuyên {class_choice}:")
st.write(f"**Toán**: {float(highest_score['Điểm thi môn Toán'])}")
st.write(f"**Văn**: {float(highest_score['Điểm thi môn Ngữ văn'])}")
st.write(f"**Anh**: {float(highest_score['Điểm thi môn Anh'])}")
st.write(f"**Điểm Chuyên**: {float(highest_score['Điểm thi môn Chuyên'])}")
st.write(f"**Tổng điểm**: {float(highest_score['Điểm xét tuyển chuyên'])}")

# Plot the distribution of scores for each test (Toán, Văn, Anh, Môn chuyên)
st.subheader("Phân phối điểm")
# Toán Score Distribution
mean_toan = selected_df['Điểm thi môn Toán'].mean()
toan_fig = px.histogram(selected_df, x="Điểm thi môn Toán", title="Phân phối điểm Toán", nbins=5)
toan_fig.update_traces(marker_color=pastel_colors[0])  # Pastel color
toan_fig.add_vline(x=mean_toan, line_dash="dash", line_color="red", annotation_text="Trung bình", annotation_position="top right")
st.plotly_chart(toan_fig)

# Văn Score Distribution
mean_van = selected_df['Điểm thi môn Ngữ văn'].mean()
van_fig = px.histogram(selected_df, x="Điểm thi môn Ngữ văn", title="Phân phối điểm Văn", nbins=5)
van_fig.update_traces(marker_color=pastel_colors[1])  # Pastel color
van_fig.add_vline(x=mean_van, line_dash="dash", line_color="red", annotation_text="Trung bình", annotation_position="top right")
st.plotly_chart(van_fig)

# Anh Score Distribution
mean_anh = selected_df['Điểm thi môn Anh'].mean()
anh_fig = px.histogram(selected_df, x="Điểm thi môn Anh", title="Phân phối điểm Anh", nbins=5)
anh_fig.update_traces(marker_color=pastel_colors[2])  # Pastel color
anh_fig.add_vline(x=mean_anh, line_dash="dash", line_color="red", annotation_text="Trung bình", annotation_position="top right")
st.plotly_chart(anh_fig)

# Chuyên Score Distribution
mean_chuyen = selected_df['Điểm thi môn Chuyên'].mean()
chuyen_fig = px.histogram(selected_df, x="Điểm thi môn Chuyên", title="Phân phối điểm Chuyên", nbins=5)
chuyen_fig.update_traces(marker_color=pastel_colors[3])  # Pastel color
chuyen_fig.add_vline(x=mean_chuyen, line_dash="dash", line_color="red", annotation_text="Trung bình", annotation_position="top right")
st.plotly_chart(chuyen_fig)
