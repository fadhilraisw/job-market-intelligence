import pandas as pd
from db_connection import get_db_connection #kita panggil fungsi koneksi yang tadi sudah dibuat

def ingest_data():
    # 1. Buka Koneksi ke Database
    db = get_db_connection()
    if db is None:
        return #Berhenti kalau gagal konek
    
    # 2. Baca Data CSV (Bahan Baku)
    try:
        # Membaca file CSV yang kita buat di langkah sebelumnya
        df = pd.read_csv('data_raw/job_postings.csv')
        print(f"📖 Berhasil membaca {len(df)} data dari CSV.")
    except FileNotFoundError:
        print("❌ File CSV tidak ditemukan! Jalankan script 00 dulu.")
        return
    # 3. Transformasi: CSV (DataFrame) -> JSON (List of Dictionaries)
    # df.to_dict('records') adalah mantra ajaib Pandas untuk mengubah tabel jadi JSON
    data_json = df.to_dict('records')

    # Debugging: Intip 1 data untuk memastikan bentuknya benar
    print("🧐 Contoh data yang akan masuk: ")
    print(data_json[0])

    # 4. Loading: Masukkan ke MongoDB
    # Kita buat 'Collection' (Folder) baru bernama 'jobs'
    collection = db['jobs']

    # Bersihkan data lama biar tidak duplikat (Opsional, untuk tahap belajar)
    collection.delete_many({})

    # Masukkan data baru 
    collection.insert_many(data_json)

    print(f"✅ Sukses! {len(data_json)} lowongan kerja telah tersimpan di MongoDB")

if __name__ == "__main__":
    ingest_data()

# python src/01_ingest_data.py