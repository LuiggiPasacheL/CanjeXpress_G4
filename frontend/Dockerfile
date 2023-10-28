
# Paso 1: Construye la aplicación Vue.js
FROM node:21 AS build
WORKDIR /app
ARG VITE_API_URL=http://service-login:5000
ENV VITE_API_URL=$VITE_API_URL
RUN echo "VITE_API_URL=$VITE_API_URL" > .env
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Paso 2: Utiliza una imagen base de Nginx
FROM nginx:latest
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

