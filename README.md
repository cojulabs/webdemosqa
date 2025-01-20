# Web Demo SQA

**Web Demo SQA** adalah sebuah aplikasi web contoh yang dirancang untuk digunakan dalam praktik pengujian otomatisasi (automation testing). Aplikasi ini dibangun menggunakan framework Django dan menyediakan elemen-elemen antarmuka yang sering digunakan dalam pengujian aplikasi web, seperti formulir, tombol, tabel, dan lain-lain.

Proyek ini bertujuan untuk membantu Software Quality Assurance (SQA) dalam memahami dan mempraktikkan berbagai skenario pengujian otomatisasi.

## Cara Menggunakan

Clone project ini dan masuk ke dalam direktorinya. Setelah itu jalankan
perintah berikut:

```
pip install -r requirements.txt
python manage.py migrate
```

Setelah itu, buat akun admin yang baru untuk masuk ke dalam halaman admin:

```
python manage.py createsuperuser
```

Isi kredensial seperti username, email dan password. Setelah selesai, jalankan development server dengan perintah berikut:

```commandline
python manage.py runserver
```

Server akan berjalan di http://localhost:8000. Untuk masuk ke halaman admin, akses URL http://localhost:8000/admin.



