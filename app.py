import streamlit as st

# 1. Cấu hình trang giao diện
st.set_page_config(
    page_title="Tính Thuế TNCN", 
    page_icon="💰", 
    layout="centered"
)

# 2. Định nghĩa hàm tính thuế (giữ nguyên logic của bạn)
def tinh_thue_tncn_chuan(tong_thu_nhap_vnd, muc_giam_tru_vnd=15_000_000):
    thu_nhap_tinh_thue_vnd = tong_thu_nhap_vnd - muc_giam_tru_vnd
    
    if thu_nhap_tinh_thue_vnd <= 0:
        return 0
        
    thu_nhap = thu_nhap_tinh_thue_vnd / 1_000_000
    thue_trieu_dong = 0
    
    if thu_nhap <= 10:
        thue_trieu_dong = thu_nhap * 0.05
    elif thu_nhap <= 30:
        thue_trieu_dong = (10 * 0.05) + (thu_nhap - 10) * 0.10
    elif thu_nhap <= 60:
        thue_trieu_dong = (10 * 0.05) + (20 * 0.10) + (thu_nhap - 30) * 0.20
    elif thu_nhap <= 100:
        thue_trieu_dong = (10 * 0.05) + (20 * 0.10) + (30 * 0.20) + (40 * 0.30) + (thu_nhap - 60) * 0.30
    else:
        thue_trieu_dong = (10 * 0.05) + (20 * 0.10) + (30 * 0.20) + (40 * 0.30) + (thu_nhap - 100) * 0.35
        
    return thue_trieu_dong * 1_000_000

# 3. Tạo giao diện ứng dụng (UI)
st.title("💰 Ứng Dụng Tính Thuế Thu Nhập Cá Nhân")

# Ô nhập Tổng thu nhập
tong_thu_nhap = st.number_input(
    "Tổng thu nhập cá nhân / tháng (VNĐ):", 
    min_value=0.0, 
    value=16_000_000.0,  # Giá trị hiển thị mẫu ban đầu
    step=500_000.0,
    format="%0.f"
)

# Cố định mức giảm trừ trong code, chạy ngầm bên dưới
MUC_GIAM_TRU_CO_DINH = 15_000_000

st.markdown("---")

# 4. Xử lý tính toán và xuất kết quả
thue_phai_nop = tinh_thue_tncn_chuan(tong_thu_nhap, MUC_GIAM_TRU_CO_DINH)
thu_nhap_tinh_thue = max(0.0, tong_thu_nhap - MUC_GIAM_TRU_CO_DINH)

st.subheader("📊 Kết quả tính toán")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Thu nhập tính thuế (Sau giảm trừ)", value=f"{thu_nhap_tinh_thue:,.0f} VNĐ")
with col2:
    st.metric(label="Thuế TNCN phải nộp", value=f"{thue_phai_nop:,.0f} VNĐ")

# Thông báo trực quan dưới cùng
if thue_phai_nop > 0:
    st.success(f"Tổng thu nhập: **{tong_thu_nhap:,.0f} VNĐ** -> Thuế phải nộp: **{thue_phai_nop:,.0f} VNĐ**")
else:
    st.info("Thu nhập của bạn chưa vượt quá mức giảm trừ 15 triệu. Bạn **không cần phải nộp thuế**.")
