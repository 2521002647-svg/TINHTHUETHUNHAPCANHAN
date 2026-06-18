import os
import streamlit as st

# 1. Cấu hình trang giao diện
st.set_page_config(
    page_title="Tính Thuế TNCN - Đề tài 6", 
    page_icon="💰", 
    layout="centered"
)

# Tự động kiểm tra file ảnh để chống sập giao diện nếu thiếu file



st.title("💰 TÍNH THUẾ THU NHẬP CÁ NHÂN_ĐỀ TÀI4_NGUYỄN GIA HUY")

# 2. Nhập dữ liệu đầu vào (Chỉ giữ lại ô nhập Thu nhập)
thu_nhap = st.number_input(
    "Nhập thu nhập trước thuế (VNĐ):",
    min_value=0.0,
    value=20_000_000.0,
    step=500_000.0,
    format="%0.f"
)

st.markdown("---")

# 3. Xử lý tính toán theo đúng quy tắc của bạn
giam_tru_ban_than = 15_500_000

# Thu nhập tính thuế = Thu nhập - Tiền miễn trừ cá nhân
thu_nhap_tinh_thue = max(0.0, thu_nhap - giam_tru_ban_than)

# Tính thuế lũy tiến từng phần (7 bậc) dựa trên Thu nhập tính thuế mới
tax = 0
if thu_nhap_tinh_thue <= 5_000_000:
    tax = thu_nhap_tinh_thue * 0.05
elif thu_nhap_tinh_thue <= 10_000_000:
    tax = 250_000 + (thu_nhap_tinh_thue - 5_000_000) * 0.10
elif thu_nhap_tinh_thue <= 18_000_000:
    tax = 750_000 + (thu_nhap_tinh_thue - 10_000_000) * 0.15
elif thu_nhap_tinh_thue <= 32_000_000:
    tax = 1_950_000 + (thu_nhap_tinh_thue - 18_000_000) * 0.20
elif thu_nhap_tinh_thue <= 52_000_000:
    tax = 4_750_000 + (thu_nhap_tinh_thue - 32_000_000) * 0.25
elif thu_nhap_tinh_thue <= 80_000_000:
    tax = 9_750_000 + (thu_nhap_tinh_thue - 52_000_000) * 0.30
else:
    tax = 18_150_000 + (thu_nhap_tinh_thue - 80_000_000) * 0.35

# Thu nhập thực nhận sau khi trừ thuế
thu_nhap_sau_thue = thu_nhap - tax

# 4. Xuất kết quả ra giao diện UI chuyên nghiệp
st.subheader("📊 Kết quả tính toán")

# Chia làm 3 cột thông số trực quan
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Thu nhập tính thuế", value=f"{thu_nhap_tinh_thue:,.0f} đ")
with col2:
    st.metric(label="Thuế TNCN phải nộp", value=f"{tax:,.0f} đ")
with col3:
    st.metric(label="Thu nhập sau thuế (Net)", value=f"{thu_nhap_sau_thue:,.0f} đ")

st.markdown(" ")

# Phần xem chi tiết phép tính khi cần bấm vào để mở rộng
with st.expander("🔍 Xem chi tiết công thức áp dụng"):
    st.write(f"Thu nhập của bạn: **{thu_nhap:,.0f} VNĐ**")
    st.write(f"Mức miễn trừ cá nhân cố định: **{giam_tru_ban_than:,.0f} VNĐ**")
    st.write(f"Thu nhập đem đi lũy tiến tính thuế: {thu_nhap:,.0f} - {giam_tru_ban_than:,.0f} = **{thu_nhap_tinh_thue:,.0f} VNĐ**")

# Hộp banner thông báo tổng kết dưới cùng
if tax > 0:
    st.success(f"Số thuế TNCN cần nộp là **{tax:,.0f} VNĐ**. Thu nhập thực nhận (Net): **{thu_nhap_sau_thue:,.0f} VNĐ**.")
else:
    st.info("Thu nhập chưa vượt quá mức miễn trừ cá nhân 15.5 triệu. Bạn không cần phải nộp thuế.")
