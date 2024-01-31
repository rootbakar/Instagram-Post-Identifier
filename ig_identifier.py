import instaloader
from datetime import datetime
import pytz

def convert_to_indonesian_time(date_str, time_str):
    # Konversi string tanggal ke objek datetime
    date_object = datetime.strptime(date_str, '%Y-%m-%d')

    # Konversi string waktu ke objek datetime
    time_object = datetime.strptime(time_str, '%H:%M:%S')

    # Gabungkan tanggal dan waktu
    combined_datetime = datetime.combine(date_object.date(), time_object.time())

    # Tentukan zona waktu Indonesia Barat (WIB)
    indonesia_west_timezone = pytz.timezone('Asia/Jakarta')

    # Konversi ke zona waktu Indonesia Barat
    local_datetime = pytz.utc.localize(combined_datetime).astimezone(indonesia_west_timezone)

    # Format tanggal dan waktu ke format yang diinginkan
    formatted_datetime = local_datetime.strftime('%d %B %Y %H:%M:%S WIB')

    return formatted_datetime

def identifikasi_postingan(post_url):
    L = instaloader.Instaloader()

    try:
        # Mendapatkan informasi postingan dari URL
        post = instaloader.Post.from_shortcode(L.context, post_url.split('/')[-2])

        # Mengonversi tanggal posting ke waktu lokal Indonesia
        local_time = convert_to_indonesian_time(post.date_utc.strftime('%Y-%m-%d'), post.date_utc.strftime('%H:%M:%S'))

        # Informasi postingan
        print("Informasi Postingan:")
        print("Username:", post.owner_username)
        print("Tanggal Posting (Waktu Lokal Indonesia):", local_time)
        print("Jumlah Komentar:", post.comments)
        print("Jumlah Like:", post.likes)
        print("Deskripsi:", post.caption)
        print("URL Gambar:", post.url)

    except Exception as e:
        print("Terjadi kesalahan:", e)

if __name__ == "__main__":
    # Meminta input URL postingan dari pengguna
    post_url = input("Masukkan URL postingan Instagram: ")
    
    identifikasi_postingan(post_url)

