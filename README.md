# Direct Messaege Instagram Menggunakan Python
   Hay.. Perkenalkan nama saya fembi nur ilham. saya merupakan mahasiswa universitas bengkulu di prodi Agribisnis. saya membangun ini untuk tujuan mempermudah penelitian saya mengenai followers yang ada di instagram. ini dibangun menggunakan python yaitu bahasa pemograman yang sangat populer di 2020 ini. semoga dengan ini bisa mempermudah penelitian saya dan membantu penelitian yang akan datang untuk meneliti tentang followers instagram sehingga akan lebih banyak penelitian kedepannya yang memanfaatkan teknologi untuk indenesia lebih maju.
        
## Tutorial
1. Instal Python di windows (https://www.python.org/) atau dapat kunjungi link berikut (https://www.petanikode.com/python-windows/)
2. Pastikan pip (perintah dasar terminal python) terbaca di terminal windows dengan cara ketik cmd di search windows masukkan
```
pip --version
```
3. Jika tidak muncul pip version, ulangi sampai bisa
4. Download file ini dengan klik code (tombol warna hijau) lalu download zip
5. Setelah download file tersebut. klik extrak (Kelurakan file data) file zip tersebut bebas dimana saja namun untuk lebih mudah letakan file hasil extrak tadi ke directory C. buat dulu folder di directory C misalkan dm-foll lalu letakan di folder itu. 
6. Setelah berhasil, Buka cmd ketik

```
cd /dm-foll
```
*Mengarahkan cmd ke folder program maka akan tampil C:\dm-foll>

7. Setelah itu masukkan perintah dibawah ke cmd folder atas
```
pip install -r requirements.txt
```
8. Buka file accounts.json untuk memasukkan akun instagram untuk login
```
[{
    "username": "username_ig",
    "password": "Pass"
}]
```
Ubah data sesuai akun untuk login, jika memiliki lebih dari 1 akun maka seperti berikut 
```
[
    {
    "username": "username_ig_1",
    "password": "Pass"
    },
    {
    "username": "username_ig_2",
    "password": "Pass"
    }


]
```
9. Buka file username.txt untuk tujuan pesan yang akan dirim yaitu berupa username instagram, enter untuk memisahkan username
10. Buka file message.txt untuk pesan yang akan di sampaikan ke username yang sudah diinput
11. Langkah Terakhir, jalankan run.py klik 2x bisa juga klik open with > python atau bisa juga di jalankan lewat terminal tadi pada C:\dm-foll> maka ketik :

```
run.py
```
