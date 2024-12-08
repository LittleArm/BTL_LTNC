# Bước 1: Chọn image Python chính thức
FROM python:3.9-slim

# Cài đặt các thư viện cần thiết
WORKDIR /app
COPY ./be/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy mã nguồn vào container
COPY ./be /app

# Expose port cho Flask
EXPOSE 5000

# Chạy ứng dụng Flask
CMD ["python", "app.py"]
