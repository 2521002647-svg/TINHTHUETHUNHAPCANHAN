import streamlit as st
st.image("IMAGE_0613.jpeg")
# 1. Cấu hình trang giao diện
st.set_page_config(
    page_title="Tính Thuế TNCN - Đề tài 4", 
    page_icon="💰", 
    layout="centered"
)

# Chèn ảnh tiêu đề từ file của bạn

st.title("💰 App tính Thuế Thu Nhập Cá Nhân_Đề Tài4_Nguyễn Gia Huy")

# 2. Nhập dữ liệu đầu vào (Giao diện nhập liệu trực quan)
thu_nhap = st.number_input(
    "Nhập thu nhập trước thuế (VNĐ):",
    min_value=0.0,
    value=20_000_000.0,
    step=500_000.0,
    format="%0.f"
)

nguoi_phu_thuoc = st.number_input(
    "Nhập số người phụ thuộc:",
    min_value=0,
    value=0,
    step=1
)

st.markdown("---")

# 3. Xử lý tính toán (Hệ thống chạy ngầm tự động phản hồi khi thay đổi dữ liệu)
giam_tru_ban_than = 15_500_000
giam_tru_phu_thuoc = nguoi_phu_thuoc * 6_200_000
bao_hiem = thu_nhap * 0.105

tong_giam_tru = giam_tru_ban_than + giam_tru_phu_thuoc + bao_hiem

# Thu nhập tính thuế
thu_nhap_tinh_thue = max(0.0, thu_nhap - tong_giam_tru)

# Tính thuế lũy tiến từng phần (7 bậc chuẩn theo dữ liệu của bạn)
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

thu_nhap_sau_thue = thu_nhap - bao_hiem - tax

# 4. Xuất kết quả ra màn hình UI chuyên nghiệp
st.subheader("📊 Kết quả tính toán")

# Chia thành 3 cột hiển thị các thông số chính bằng st.metric
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Thu nhập tính thuế", value=f"{thu_nhap_tinh_thue:,.0f} đ")
with col2:
    st.metric(label="Thuế TNCN phải nộp", value=f"{tax:,.0f} đ")
with col3:
    st.metric(label="Thu nhập sau thuế (Net)", value=f"{thu_nhap_sau_thue:,.0f} đ")

st.markdown(" ")

# Gom các thông tin chi tiết vào một bảng mở rộng (Expander) cho giao diện gọn gàng
with st.expander("🔍 Xem chi tiết các khoản giảm trừ và chi phí"):
    st.write(f"Thu nhập trước thuế: **{thu_nhap:,.0f} VNĐ**")
    st.write(f"Giảm trừ bản thân: **{giam_tru_ban_than:,.0f} VNĐ**")
    st.write(f"Giảm trừ người phụ thuộc: **{giam_tru_phu_thuoc:,.0f} VNĐ**")
    st.write(f"Bảo hiểm bắt buộc (10.5%): **{bao_hiem:,.0f} VNĐ**")
    st.write(f"Tổng các khoản được giảm trừ: **{tong_giam_tru:,.0f} VNĐ**")

# Banner thông báo tổng kết dưới cùng
if tax > 0:
    st.success(f"Số thuế TNCN bạn cần nộp là **{tax:,.0f} VNĐ**. Thu nhập thực nhận (Net) của bạn là **{thu_nhap_sau_thue:,.0f} VNĐ**.")
else:
    st.info("Thu nhập của bạn chưa đến mức phải nộp thuế TNCN sau khi trừ các khoản giảm trừ và bảo hiểm.")
