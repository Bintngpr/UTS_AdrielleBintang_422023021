# Case Study : UKRIDA E-Library Management System

# System Requirment (FURPS)

## Functionalty
-   **Autentikasi**: Pengguna harus dapat membuat akun dengan nama pengguna dan kata sandi. Mereka juga harus dapat masuk dengan kredensial mereka.
-   **Manajemen Perpustakaan**:
        o   Pengguna harus dapat menampilkan daftar buku yang tersedia.
        o   Pengguna harus dapat meminjam buku dari perpustakaan.
        o   Pengguna harus dapat mengembalikan buku ke perpustakaan.
        o   Pengguna harus dapat menambahkan buku baru ke perpustakaan.

## Usability
-   **Antarmuka Pengguna**: Sistem harus memiliki antarmuka pengguna yang intuitif untuk melakukan operasi perpustakaan.
-   **Penanganan Kesalahan**: Pesan kesalahan yang jelas harus diberikan kepada pengguna dalam hal input yang tidak valid atau kesalahan sistem.
-   **Aksesibilitas**: Sistem harus dapat diakses oleh pengguna dengan disabilitas, jika berlaku.

## Responsibility
-   **Keamanan Autentikasi**: Kredensial pengguna harus disimpan dan diotentikasi secara aman.
-   **Integritas Data**: Informasi buku dan transaksi pengguna harus dipelihara dengan akurat tanpa kehilangan data.

## Performance
-   **Waktu Respons**: Sistem harus merespons dengan cepat terhadap tindakan pengguna seperti masuk, menampilkan daftar buku, meminjam, dan mengembalikan buku.
-   **Skalabilitas**: Sistem harus dapat menangani peningkatan jumlah pengguna dan buku tanpa degradasi kinerja yang signifikan.

## Supportability
-   **Kemudahan Pemeliharaan**: Kode harus terstruktur dengan baik dan didokumentasikan untuk kemudahan pemeliharaan oleh pengembang.
-   **Ekstensibilitas**: Sistem harus dirancang untuk dengan mudah mengakomodasi peningkatan atau perubahan di masa depan, seperti fitur tambahan atau integrasi.
-   **Kompatibilitas**: Sistem harus kompatibel dengan berbagai platform dan browser yang umum digunakan oleh pengguna target.

## Other Considerations
-   **Keamanan**: Pastikan komunikasi dan penyimpanan data sensitif seperti kredensial pengguna dan informasi transaksi aman.
-   **Kepatuhan Regulasi**: Pastikan kepatuhan dengan regulasi perlindungan data yang relevan, terutama mengenai privasi pengguna dan keamanan data.


# Identify Component

## User Authentication Component
-   Bertanggung jawab untuk mengelola akun pengguna, termasuk registrasi dan login.
-   Class Involved : 'Authenticator', 'User'

## Library Management Component
-   Menangani operasi yang berkaitan dengan pengelolaan koleksi buku perpustakaan
-   Class Involved : 'Library','Book'

## Book Management Subcomponents

-   **Display Books**
-    Bertanggung jawab untuk menampilkan daftar buku yang tersedia.
-    Class Involved : 'Display_books'


-   **Issue Books**
-    Menangani proses peminjaman buku kepada user.
-    Class Involved : 'Issue_books'


-   **Return Books**
-    Mengelola proses pengembalian buku ke e-library
-    Class Involved : 'Return_books'


-   **Add Books**
-    Mengelola penambahan buku baru ke e-library
-    Class Involved : 'Add_books'


-   **Load Books**
-    Memuat daftar awal buku dari sebuah file
-    Class Involved : 'Load_books'

## Main Component
-   Mengkoordinasikan interaksi antara antarmuka pengguna dan sistem manajemen perpustakaan
-   Class Involved : 'Main'

## User Interface Component
-   Menyediakan antarmuka bagi pengguna untuk berinteraksi dengan sistem
-   Tidak didefinisikan secara eksplisit dalam kode yang disediakan, tetapi dianggap sebagai bagian dari implementasi antarmuka pengguna di main.py


# User Roles

-   **Administrator**:
        •   Bertanggung jawab atas pengelolaan umum perpustakaan, termasuk manajemen pengguna dan buku.
        •   Memiliki akses penuh ke semua fitur sistem.

-   **Mahasiswa/User**:
        •   Pengguna yang dapat menggunakan layanan perpustakaan, seperti meminjam dan mengembalikan buku.
        •   Memiliki akses terbatas tergantung pada kebijakan perpustakaan.

# User Stories

-   **Administrator**:
        •   Menambahkan Buku
        •   Memastikan Informasi Peminjaman Benar
        •   Menerima Notifikasi
    
-   **Mahasiswa**:
        •   Melihat Daftar Buku
        •   Meminjam Buku
        •   Mengembalikan Buku
        •   Menerima Notifikasi

## Use Case

-   **Autentikasi Pengguna**
-   **Proses Peminjaman**
-   **Pengembalian Buku**
-   **Penambahan Buku**
-   **Melihat Data Peminjaman**

## Class Diagram
