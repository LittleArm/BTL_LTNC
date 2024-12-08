# Bước 1: Sử dụng image node để build ứng dụng
FROM node:18 AS build

WORKDIR /app
COPY ./sao-ke-frontend/package*.json ./
RUN npm install
COPY ./sao-ke-frontend ./
RUN npm run build

# Bước 2: Sử dụng image Nginx để phục vụ tệp build
FROM nginx:alpine

# Copy build files từ bước trước vào thư mục mặc định của Nginx
COPY --from=build /app/build /usr/share/nginx/html

# Expose cổng 80 để truy cập từ bên ngoài
EXPOSE 80

# Chạy Nginx
CMD ["nginx", "-g", "daemon off;"]
