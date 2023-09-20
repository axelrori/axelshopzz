### Nama    : Serafino Theodore Axel Rori
### NPM     : 2206082644
### Kelas   : PBP F

# **TUGAS 2**

Link aplikasi Adaptable:
https://axelshopzz.adaptable.app/main/

**1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

- Membuat sebuah proyek Django baru.
Di checklist ini, pertama-tama saya membuat direktori baru di local files dengan nama axelshopzz, lalu saya juga membuat repository di Github dengan nama axelshopzz. Kemudian saya menghubungkan repository di GitHub dengan direktori di local files. Setelah itu, saya mengkonfigurasi git sedemikian rupa lalu membuat virtual environment, lalu dilanjutkan dengan menginstall django dengan menambahkan beberapa dependencies di dalam requirements.txt. Setelah itu, proyek django dijalankan dengan menggunakan perintah "django-admin startproject axelshopzz .". Setelah ini dilakukan, maka dilanjutkan dengan beberapa konfigurasi pada settings.py dan membuat berkas .gitignore.

- Membuat aplikasi dengan nama main pada proyek tersebut.
Pada checklist ini, app main dibuat dengan menjalankan perintah "python manage.py startapp main" pada command prompt. Perintah ini membuat terbuatnya direktori aplikasi baru di dalam direktori proyek axelshopzz yang bernama main. Setelah itu saya menambahkan 'main' pada INSTALLED_APPS di dalam settings.py agar aplikasi main terdaftar ke dalam proyek.

- Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
Di checklist ini, saya membuat berkas urls.py baru di dalam direktori main lalu di dalamnya didefinisikan fungsi show_main, kemudian file urls.py yang terletak di direktori proyek juga ditambahkan include main.urls

- Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
-- name sebagai nama item dengan tipe CharField.
-- amount sebagai jumlah item dengan tipe IntegerField.
-- description sebagai deskripsi item dengan tipe TextField.
Pada checklist ini, di berkas models.py, membuat "from django.db import models". Lalu, membuat class Product dimana di dalamnya diletakkan atribut name dengan tipe CharField dan dibuat max length=255. Lalu dibuat juga atribut amount dengan tipe IntegerField. Selanjutnya dibuat juga atribut description dengan tipe TextField. Setelah models berhasil dibuat, saya melakukan migrasi model agar perubahan dapat dilacak oleh Django.

- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Setelah menambahkan models, saya membuat fungsi show_main yang memiliki atribut seperti appname, nama, dan kelas yang akan terkoneksi dengan template di file main.html

- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
Pada checklist ini, saya mengisi urls.py di dalam aplikasi main dengan kode sebagai berikut
<img src="/READMEIMG/URLSMAIN.png" alt="Gambar Kode urls.py di aplikasi main">

- Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Sesudah mengkonfigurasi django dan membuat .gitignore di awal tadi, saya sudah mulai melakukan deployment ke Adaptable dengan memilih branch main di repository axelshopzz. Lalu, menggunakan Python App Template beserta PostgreSQL sebagai tipe basis data. Selanjutnya memasukan start command "python manage.py migrate && gunicorn axelshopzz.wsgi", lalu mencentang bagian HTTP Listener on PORT. Dengan ini, axelshopzz sudah mulai di deploy. Namun, pada kasus saya sebelumnya, saya mendapati deployment failed. Meskipun deployment pertama gagal, saya tetap melanjutkan semua step yang harus dilakukan dan sembari tiap progress dipush ke GitHub, app axelshopzz akan mendeploy ulang dan akhirnya deployment app berhasil setelah semua step dan checklist berhasil dibuat.


**2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
<img src="/READMEIMG/BAGAN.png" alt="Bagan">


**3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
Virtual environment (venv) digunakan untuk mengisolasi dependensi proyek Python, termasuk aplikasi web berbasis Django, dengan alasan Venv memungkinkan kita untuk mengisolasi dependensi setiap proyek, menghindari konflik paket dan memastikan konsistensi. Lalu, venv juga membuat pengelolaan dependensi lebih mudah proyek seperti instalasi, pembaruan, dan penghapusan paket. Selain itu, venv memungkinkan pencatatan dependensi proyek dalam file requirements.txt untuk replikasi yang konsisten. Jadi, sebenarnya kita bisa saja membuat aplikasi web Django tanpa venv, tetapi penggunaan venv lebih disarankan untuk pengelolaan yang lebih baik dan menghindari potensi masalah dengan dependensi.

**4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.**
- MVC (Model-View-Controller)
Model tidak langsung berkomunikasi dengan View. Semua komunikasi antara Model dan View terjadi melalui Controller. MVC terutama digunakan dalam pengembangan aplikasi berbasis desktop dan web tradisional.

- MVT (Model-View-Template)
MVT adalah konsep yang digunakan khusus dalam Django, kerangka kerja web Python. Dalam MVT, Template mengambil peran tampilan, sementara View lebih berfokus pada mengatur logika aplikasi.

- MVVM (Model-View-ViewModel)
MVVM adalah arsitektur yang sering digunakan dalam pengembangan aplikasi berbasis perangkat lunak bergerak (mobile) dan aplikasi satu halaman (single-page applications) di web. ViewModel memainkan peran penting dalam mengelola tampilan dan interaksi pengguna.

Perbedaan utama antara ketiganya adalah bagaimana mereka memisahkan tugas-tugas dalam pengembangan perangkat lunak dan bagaimana mereka mengelola aliran data dan interaksi antara Model dan View. Pemilihan arsitektur tergantung pada jenis aplikasi yang sedang dikembangkan dan juga preferensi dari pengembang itu sendiri.



# **TUGAS 3**
**1. Apa perbedaan antara form POST dan form GET dalam Django?**
POST:
Metode POST mengirim data dari formulir sebagai bagian dari badan permintaan HTTP. Nantinya data akan dikirim secara tersembunyi, sehingga tidak terlihat di URL. Ini membuat POST lebih aman untuk mengirim data sensitif seperti contohnya kata sandi karena tidak bisa terlihat oleh orang lain.
GET:
Metode GET mengirim data dari formulir dengan melampirkannya ke URL sebagai parameter query string. Data ini dapat terlihat di URL dan dapat di-bookmark atau dibagikan dengan mudah. Metode ini lebih cocok digunakan untuk permintaan yang tidak mengubah keadaan dari server.

**2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?**

**3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
- Membuat input form untuk menambahkan objek model pada app sebelumnya
Membuat beberapa objek model pada file forms.py yang berisi name, amount, price, dan description. Objek date added tidak ditambah karena sudah didefinisikan secara otomatis pada file models.py. Berikut merupakan gambar kode input form:
<img src="/READMEIMG/FORMSPY.png" alt="Gambar Kode forms.py di aplikasi main">

- Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
Dalam checklist ini, yang dilakukan adalah menggunakan 6 function yang berbeda ke dalam file views.py, diantaranya terdapat show_main dan create_product untuk format HTML, show_xml, show_json, show_xml_by_id, dan show_json_by_id. Untuk funciton show_xml dan show_json, dibuat variabel data dengan mengambil semua product yang terdapat dalam database, kemudian return HttpResponse yang di serialize. Untuk function show_xml_by_id, dan show_json_by_id, dibuat variabel data yang memfilter product dengan id tertentu lalu mereturn HttpResponse yang diserialize juga. Berikut adalah gambar penggunaan 6 function tersebut dalam file views.py:
<img src="/READMEIMG/VIEWSPY.png" alt="Gambar Kode views.py di aplikasi main">

- Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
Untuk membuat routing URL dari masing-masing views, yang perlu dilakukan adalah mengubah isi dari urls.py yang terdapat di dalam aplikasi main, yaitu dengan mengimport tiap function yang terdapat di file views.py dan menambahkan pathnya di dalam list url_patterns. Berikut adalah gambaran kode import dan juga list url_patterns:
<img src="/READMEIMG/URLSPYIMPORT.png" alt="Gambar Kode import dalam urls.py di aplikasi main">
<img src="/READMEIMG/URLSPYCODE.png" alt="Gambar Kode urls.py di aplikasi main">

- Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
Postman HTML:
<img src="/READMEIMG/Postman_html.png" alt="Postman HTML">
Postman XML:
<img src="/READMEIMG/Postman_xml.png" alt="Postman XML">
Postman JSON:
<img src="/READMEIMG/Postman_json.png" alt="Postman JSON">
Postman XML by ID:
<img src="/READMEIMG/Postman_xmlid.png" alt="Postman XML BY ID">
Postman JSON by ID:
<img src="/READMEIMG/Postman_jsonid.png" alt="Postman JSON BY ID">