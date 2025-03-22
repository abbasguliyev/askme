# Python tabanlı bir Docker imajı kullan
FROM python:3.9  

# Çalışma dizini oluştur
WORKDIR /app  

# Gerekli bağımlılıkları yükle
COPY requirements.txt requirements.txt  
RUN pip install -r requirements.txt  

# Proje dosyalarını kopyala
COPY . .  

# Django uygulamasını başlat
CMD ["gunicorn", "askme.wsgi:application", "--bind", "0.0.0.0:8000"]  
