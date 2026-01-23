from pymongo import MongoClient

def get_db_connection() :
    try :
        # Menghubungkan Ke Mongo DB Docker
        # 'localhost' karena docker berjalan di laptop sendiri
        # '27017' karena merupakan pintu port standar mongo db
        client = MongoClient("mongodb://localhost:27017/")

        # Cek koneksi dengan perintah 'ping'
        client.admin.command('ping')

        print("✅ Berhasil terhubung ke MongoDB!")

        # kita akan pakai database bernama 'job_market_db'
        # Di MongoDB, kalau DB belum ada, dia bakal otomatis dibuat saat isi data
        db = client['job_market_db']
        return db
    except Exception as e :
        print(f"❌ Gagal koneksi: {e}")
        return None

# Test fungsi langsung saat file ini dijalankan
if __name__ == "__main__" :
    db = get_db_connection()


# command untuk connect
# python src/db_connection.py                       