# Chỉ đường Học viện

Ứng dụng chỉ đường trong khuôn viên Học viện, chạy bằng Streamlit. Giao diện HTML/CSS/JavaScript được lưu trong `app.html` và hiển thị qua component của Streamlit.

## Chạy trên máy cá nhân

Yêu cầu Python 3.13 trở lên. Có thể chạy bằng `uv`:

```bash
uv sync
uv run streamlit run streamlit_app.py
```

Hoặc cài dependencies bằng pip:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy lên Streamlit Community Cloud

1. Đẩy repository lên GitHub.
2. Vào [Streamlit Community Cloud](https://share.streamlit.io/) và chọn **Create app**.
3. Chọn repository, branch cần deploy và đặt **Main file path** là `streamlit_app.py`.
4. Trong **Advanced settings**, chọn Python 3.13 trở lên nếu được yêu cầu, rồi chọn **Deploy**.

Giữ `streamlit_app.py`, `app.html` và `requirements.txt` trong cùng repository. Nếu sửa giao diện, cập nhật `app.html`; không dán trực tiếp HTML vào file Python.
