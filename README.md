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
XML: Bahasa markup yang dirancang untuk mendefinisikan, menyimpan, dan mentransfer data terstruktur antara sistem yang berbeda. Ini digunakan terutama untuk pertukaran data antara aplikasi. XML memiliki struktur hierarkis dengan elemen, atribut, dan teks yang diapit oleh tag. Ini membuat xml sangat fleksibel dalam merepresentasikan berbagai jenis data yang terstruktur.

JSON: JSON adalah format pertukaran data ringan yang digunakan terutama untuk pertukaran data antara aplikasi, terutama di lingkungan web. Ini digunakan untuk mengirim data antara server dan browser, serta antara server dan server. JSON menggunakan struktur objek yang lebih mudah dibaca dan juga ditulis oleh manusia.

HTML: HTML adalah bahasa markup yang digunakan untuk membuat struktur dan tampilan halaman web. Ini digunakan terutama untuk menggambarkan struktur dan tampilan konten web yang ditampilkan di browser.

Seperti yang telah dijabarkan di atas, penggunaan ketiganya tergantung pada kebutuhan aplikasi kita masing-masing dan juga tergantung pada konteks penggunaannya.

**3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**
- Ringan dan Mudah Dibaca
JSON memiliki format yang ringan dan mudah dibaca oleh manusia. Hal ini membuat kita lebih mudah untuk membuat, membaca, dan memahami data dalam format JSON.
- Dukungan Browser Bawaan
Banyak bahasa pemrograman yang memiliki dukungan bawaan untuk mengurai JSON. Ini membuat pengolahan data JSON di browser menjadi lebih mudah dan juga efisien. Sebagai hasilnya, JSON sering digunakan dalam pengiriman data dari server ke browser dan sebaliknya dalam pengembangan aplikasi web.
- Crossplatform
JSON adalah format independen platform, sehingga data yang dibentuk dalam format JSON dapat lebih mudah untuk dipahami dan digunakan oleh berbagai bahasa pemrograman dan juga sistem operasi. Ini membuat json lebih ideal untuk pertukaran data antara aplikasi yang berjalan di platform yang berbeda.

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



# **TUGAS 4**
## 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah salah satu form bawaan yang disediakan oleh Django, yang dirancang khusus untuk membantu dalam proses pembuatan user baru dalam aplikasi web yang dibangun dengan Django. Form ini digunakan untuk mengumpulkan informasi yang diperlukan untuk membuat akun seperti username, password, dan konfirmasi password.
### Kelebihan UserCreationForm:
- Mudah digunakan
Dapat langsung diintegrasikan dengan mudah ke dalam aplikasi Django Anda tanpa harus menulis kode form secara manual.
- Validasi otomatis
Memiliki validasi otomatis yang memastikan bahwa pengguna mengisi data dengan benar dan mematuhi aturan keamanan yang umum, seperti contohnya memeriksa kekuatan password dan memeriksa apakah username sudah ada.
- Kompatibilitas dengan Django Authentication
Form ini secara langsung terkait dengan sistem otentikasi yang disediakan oleh Django.
### Kekurangan UserCreationForm:
- Tidak dapat disesuaikan sepenuhnya
UserCreationForm adalah form bawaan yang sederhana, sehingga jika ingin menambah fitur custom dalam proses pendaftaran mungkin memerlukan lebih banyak kode.
- Tidak termasuk fitur keamanan tingkat lanjut
Meskipun UserCreationForm menyediakan beberapa tingkat validasi dan keamanan dasar, kita mungkin perlu menambahkan lapisan keamanan tambahan seperti CAPTCHA atau verifikasi email untuk mengatasi risiko keamanan yang lebih tinggi.

## 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi adalah proses verifikasi identitas pengguna, sementara otorisasi adalah proses mengatur hak akses atau izin pengguna dalam aplikasi. Autentikasi memastikan identitas, sedangkan otorisasi mengontrol apa yang dapat dilakukan oleh pengguna yang telah terautentikasi. Keduanya sangatlah penting untuk menjaga keamanan dan kontrol akses dalam aplikasi web.

## 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah potongan data kecil yang disimpan pada perangkat pengguna saat mereka mengunjungi situs web. Cookies digunakan dalam konteks aplikasi web untuk menyimpan informasi pada sisi klien (browser pengguna) yang dapat diakses dan dikirimkan kembali ke server web ketika pengguna mengunjungi situs tersebut lagi. Hal ini memungkinkan aplikasi web untuk mengenali pengguna, menyimpan preferensi, dan melacak sesi pengguna.
Django menggunakan cookies untuk mengelola data sesi pengguna dengan cara berikut:
1. Session Cookies
Ketika seorang pengguna mengakses situs web yang menggunakan Django, server akan membuat sebuah sesi unik untuk pengguna tersebut. Informasi sesi ini kemudian disimpan dalam session cookies di browser pengguna.
2. Session Framework
Django memiliki sistem sesi bawaan yang memungkinkan kita untuk menyimpan dan mengelola data sesi pengguna dengan mudah. Data sesi ini dapat diakses di berbagai bagian aplikasi, seperti views dan juga templates. Django secara otomatis mengelola siklus hidup dari sebuah sesi, termasuk pembuatan dan penghapusan sesi, serta menyimpan data sesi ke dalam cookies.
3. Konfigurasi
Kita dapat mengonfigurasi pengaturan sesi di dalam berkas settings.py Django. Kita dapat menentukan bagaimana sesi harus disimpan misalnya dalam database, dalam cookies, atau di server, berapa lama sesi harus bertahan, dan lain-lain.

## 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies dalam pengembangan web bisa menjadi aman jika dikelola dengan benar. Namun, terdapat beberapa risiko potensial yang harus diwaspadai. Risiko tersebut diantaranya terdapat pencurian data, session hijacking, serangan XSS, pelacakan yang invasif, dan komplikasi hukum. Sehingga untuk mengamankan cookies, hal yang dapat kita lakukan adalah menggunakan HTTPS, menyesuaikan pengaturan keamanan, enkripsi data sensitif, validasi data, berikan privasi dan juga opsi penggunaan cookies. Hal ini disebabkan karena keamanan adalah prioritas utama dalam pengembangan web.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
Pada tahap ini, saya mengimport library django berikut pada views.py di main
~~~
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
~~~
Lalu saya menambahkan fungsi register ke dalam file views.py untuk menghasilkan form registrasi secara otomatis
~~~
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
~~~
Selanjutnya, saya menambahkan file html baru bernama register.html agar dapat membuat tampilan website
~~~
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
~~~
Lalu, saya menambahkan import register pada urls.py dan menambahkan "path('register/', register, name='register')," pada urlpatterns

Untuk login, saya menambahkan import authenticate dan login pada file views.py lalu menambahkan potongan kode untuk autentikasi pengguna saat login
~~~
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
~~~
Lalu, saya juga membuat kode html di file baru bernama login.html agar terdapat display saat kita ingin login di web seperti berikut
~~~
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
~~~
Lalu, saya menambahkan import login_user pada urls.py dan menambahkan "path('login/', login_user, name='login')," pada urlpatterns

Untuk Logout, saya menambahkan import logout pada file views.py lalu menambahkan potongan kode untuk melakukan mekanisme logout
~~~
def logout_user(request):
    logout(request)
    return redirect('main:login')
~~~
Lalu, saya menambahkan potongan kode pada berkas main.html
~~~
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
~~~
Lalu, saya menambahkan import logout_user pada urls.py dan menambahkan "path('logout/', logout_user, name='logout')," pada urlpatterns

### Restriksi Akses Main agar Login Required dan Menggunakan Data dari Cookies
Saya mengimport login_required pada views.py, Lalu saya menambahkan potongan kode berikut ini agar halaman main hanya dapat diakses setelah proses login berhasil
~~~
...
@login_required(login_url='/login')
def show_main(request):
...
~~~

Lalu, saya mengimport datetime pada file views.py. Kemudian mengubah fungsi login_user pada views.py sehingga dapat melihat kapan pengguna melakukan kegiatan login
~~~
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
~~~

Lalu, saya mengubah fungsi show_main pada views.py agar dapat memproses last_login
~~~
if 'last_login' in request.COOKIES:
    last_login = request.COOKIES['last_login']
else:
    last_login = 'N/A'
~~~

### Menghubungkan Model Products dengan User
Pada tahap ini, saya mengimport user di file models.py. Kemudian, saya menambahkan atribut user pada model Products
~~~
class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
~~~
Kemudian, saya mengubah fungsi create_product pada file views.py seperti berikut:
~~~
def create_product(request):
    form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
    product = form.save(commit=False)
    product.user = request.user
    product.save()
    return HttpResponseRedirect(reverse('main:show_main'))
~~~

### Menambahkan Kode Bonus
Pertama-tama saya menambahkan 3 fungsi baru yaitu plus_product_amount, minus_product_amount, dan juga remove_product pada views.py seperti berikut:
~~~
def plus_product_amount(request, id):
    product = Product.objects.get(id=id)
    product.amount += 1
    product.save()
    response = HttpResponseRedirect(reverse("main:show_main"))
    return response

def minus_product_amount(request, id):
    product = Product.objects.get(id=id)
    if (product.amount > 0):
        product.amount -= 1
        product.save()
    response = HttpResponseRedirect(reverse("main:show_main"))
    return response

def remove_product(request, id):
    Product.objects.filter(pk=id).delete()
    response = HttpResponseRedirect(reverse("main:show_main"))
    return response
~~~
Kemudian saya mengimport fungsi di atas menuju urls.py dan menambahkan path ke dalam urls patterns seperti berikut:
~~~
...
path('plus_product_amount/<int:id>', plus_product_amount, name='plus_product_amount'),
path('minus_product_amount/<int:id>', minus_product_amount, name='minus_product_amount'),
path('remove_product/<int:id>', remove_product, name='remove_product'),
~~~

Setelah itu, saya menambahkan kode di main.html agar dapat terdisplay pada website seperti berikut:
~~~
<td class="d-flex align-items-center">
    <form method="post" action="{% url 'main:plus_product_amount' product.id %}">
        {% csrf_token %}
        <button class="btn btn-primary mx-1">+</button>
    </form>
    <form method="post" action="{% url 'main:minus_product_amount' product.id %}">
        {% csrf_token %}
        <button class="btn btn-primary mx-1">-</button>
    </form>
    <form method="post" action="{% url 'main:remove_product' product.id %}">
        {% csrf_token %}
        <button class="btn btn-primary mx-1">Delete</button>
    </form>
</td>
~~~



# **TUGAS 5**
## 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
Element selector berguna untuk mengkustomisasi semua elemen yang sama pada suatu file html. contoh penggunaannya adalah seperti berikut:
~~~
h2 {
    font-weight: 600;
    color: #fff;
}
~~~
Dalam potongan kode di atas, semua elemen di file html yang terbuat dari h2 akan mengikuti sifat yang telah ditentukan oleh element selector pada file css.

Waktu yang tepat untuk menggunakan element selector adalah jika ingin mengubah suatu style awal yang default yang kita diinginkan pada suatu halaman karena element selector akan mengubah semua elemen yang terlibat pada seluruh page HTML.

## 2. Jelaskan HTML5 Tag yang kamu ketahui.
HTML5 adalah versi terbaru dari bahasa HTML. Dalam versi ini ada beberapa fitur tag yang sering saya gunakan, diantaranya terdapat:
<header>: Tag ini digunakan untuk mendefinisikan bagian atas dari suatu halaman HTML.
<nav>: Tag ini biasanya digunakan untuk membuat navbar dan umumnya tag nav dimasukkan ke dalam tag header karena navbar berada di bagian teratas pada suatu halaman HTML.
<section>: Tag ini biasanya digunakan untuk mengelompokkan suatu konten yang terkait, contohnya di tugas ini pada halaman login, section memuat semua fitur mulai dari label, input box, dan juga login button.
<div>: Tag ini sering digunakan untuk mengelompokkan suatu fitur konten agar mudah untuk dikustomisasi sendiri.

## 3. Jelaskan perbedaan antara margin dan padding.
Margin adalah ruang di sekitar suatu elemen pada HTML. Margin dapat digunakan untuk mengontrol jarak antara suatu elemen dengan elemen-elemen lainnya di dalam suatu page HTML. Margin dapat diatur dari segala sisi seperti margin-top, margin-left, margin-right, dan juga margin-bottom. Contoh penggunaan margin dalam css:
~~~
section {
  margin-top: 5px;
  margin-right: 20px;
  margin-bottom: 5px;
  margin-left: 20px;
}
~~~
Padding adalah ruang di dalam elemen HTML antara kontennya dan batas elemen itu sendiri. Padding dapat digunakan untuk mengontrol jarak antara konten elemen dan batas elemen tersebut. Padding juga dapat diatur dari segala sisi seperti padding-top, padding-left, padding-right, dan juga padding-bottom. Contoh penggunaan padding dalam css:
~~~
section {
  padding-top: 15px;
  padding-right: 30px;
  padding-bottom: 15px;
  padding-left: 30px;
}
~~~
Perbedaan utama antara margin dan padding adalah margin mengatur jarak di sekitar elemen, sedangkan padding mengatur ruang di dalam elemen antara kontennya dan batas elemen itu sendiri.

## 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Berikut merupakan perbedaan antara Tailwind dan Bootstrap:
| Deisgn | Customization | Ukuran |
|--------|:-------------:|--------|


## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Untuk mengkustomisasi, saya menggunakan file external css dengan cara mambuat folder baru static di dalam direktori aplikasi main, lalu membuat folder css di dalamnya yang berisi file-file css dari file html yang telah dibuat sebelumnya.
Untuk membuat file html terhubung dengan file css, saya menambahkan potongan kode berikut di bagian atas setiap file html:
~~~
{% load static %}

{% block meta %}
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="{% static 'css/filename.css' %}">
  <title>Title</title>
{% endblock meta %}
~~~
Selanjutnya, saya mengkustomisasi page login, register, main, edit_product, dan juga create_product. Dalam mengubah desain dari page, perlu dilakukan pembagian setiap bagian dari html ke dalam class yang berbeda agar dapat dikustomisasi masing-masing. Beberapa command yang sering digunakan adalah padding, margin, width, height, dan lain-lain. Saya juga mengganti background dari html menggunakan image dengan memasukkan imageurl ke dalam file css.

Lalu, saya menambahkan fitur card ke dalam halaman main. Untuk menambahkan fitur card, saya menambahkan lalu sedikit memodifikasi potongan kode dari website bootstrap seperti berikut:
~~~
<div class="card-container">
        {% for product in products %}
        <div class="card" style="width: 18rem; border-radius: 20px; padding-left: 10px; padding-right: 10px; align-items: center;">
          <img src={{product.image_url}} class="card-img" alt="productimage">
          <div class="card-body">
            <h5 class="card-title">{{product.name}}</h5>
            <p class="card-text">{{product.description}}</p>
          </div>
        </div>
    {% endfor %}
</div>
~~~
Dalam potongan kode bootstrap di atas, agar card dapat terhubung dengan product, elemen dari card dihubungkan dengan objek products, contohnya pada bagian card-title elemennya adalah {{product.name}} dan pada bagian card-text elemennya adalah {{product.description}}.
Setelah menambahkan potongan kode untuk card, selanjutnya saya mengkustomisasi card di file main.css dengan potongan kode sebagai berikut:
~~~
.card-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  grid-gap: 20px;
  margin: 40px;
  justify-content: center;
  justify-items: center;
  padding-bottom: 20px;
}

.card-container .card {
  max-width: 100%;
}

.card-container .card-title {
  font-weight: bold;
  color: #333;
}

.card-container .card-text {
  color: #555;
}

.card img {
  max-width: 100%;
  border-radius: 24px;
  height: 200px;
  object-fit: cover;
  margin: 10px;
}
~~~


