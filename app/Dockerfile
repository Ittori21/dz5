FROM python:3.9-slim

# Ставим nginx, supervisor и зависимости для postgres
RUN apt-get update && apt-get install -y nginx supervisor gcc libpq-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . /app

# Подкидываем конфиги
COPY nginx-container.conf /etc/nginx/nginx.conf
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80

CMD ["/usr/bin/supervisord"]