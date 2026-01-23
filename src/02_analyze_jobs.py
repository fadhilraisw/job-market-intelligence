# Aggregation pipeline
# $match: Saring bahan baku (Cuma ambil mobil warna merah).
# $group: Rakit/Kelompokkan (Hitung ada berapa mobil merah per merk).
# $sort: Urutkan hasil akhir (Dari yang paling mahal).

from db_connection import get_db_connection
import pandas as pd

def analyze_market():
    db = get_db_connection()
    collection = db['jobs']

    # --- KASUS 1 : Rata Rata Gaji per Lokasi ---
    # Kita ingin tahu: "di kota mana gaji paling tinggi?"
    pipeline_salary = [
        # Stage 1 : Filter data yang gajinya tidak null/kosong
        { "$match" : { "salary": { "$ne": None } } },

        # Stage 2: Grouping (Sama kayak GROUP BY di SQL)
        {
            "$group": {
                "_id": "$location", # Group berdasarkan kolom 'location'
                "avg_salary": { "$avg": "$salary" }, # Hitung Rata Rata
                "total_jobs": {"$sum": 1 } # Hitung jumlah lowongan 
            }
        },

        # Stage 3: Sorting (Urutkan dari gaji tertinggi)
        {"$sort": {"avg_salary": -1 }} # -1 artinya Descending (Besar ke Kecil)

    ]

    print("\n📊 ANALISA 1: Rata rata Gaji per Lokasi")
    results = list(collection.aggregate(pipeline_salary))

    # Biar outputnya cantik/rapi, kita bungkus pakai Pandas DataFrame
    df_result = pd.DataFrame(results)

    # Format angka gaji biar gak muncul e+07 (scientific notation)
    pd.options.display.float_format = '{:,.0f}'.format
    print(df_result)

    # --- KASUS 2: Mencari Keyword "Python" ---
    # Mencari lowongan yang deskripsinya mengandung kata 'Python'
    count_python = collection.count_documents({
        "description": { "$regex": "Python", "$options": "i"} # i = case insensitive (huruf besar dan kecil sama saja)
    })

    print(f"\n🐍 Jumlah Lowongan yang butuh Python: {count_python}")

if __name__ == "__main__" :
    analyze_market()

# python src/02_analyze_jobs.py