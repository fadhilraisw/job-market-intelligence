import pandas as pd
from db_connection import get_db_connection


class JobMarketAnalyzer :
    def __init__(self):
        """
        Konstruktor : bagian ini dijalankan saat class dipanggil
        Tugasnya menyiapkan connection ke database.
        """
        self.db = get_db_connection()
        self.collection = self.db['jobs']
        print("🤖 System Initialized: Database Connected.")
    
    def load_data(self, csv_path) :
        """
        Method untuk membaca CSV dan upload ke MongoDB
        """
        try :
            df = pd.read_csv(csv_path)
            data_json = df.to_dict('records')

            # Reset data lama (opsional, biar bersih saat testing)
            self.collection.delete_many({})

            # Insert data baru
            self.collection.insert_many(data_json)
            print(f"✅ Data Loaded: {len(data_json)} records inserted.")
        
        except FileNotFoundError:
            print(f"❌ Error: File {csv_path} tidak ditemukan.")
    
    def get_salary_summary(self):
        """
        Method untuk analisa gaji (Aggregation)
        """
        pipeline = [
            {"$match" : {"salary": {"$ne": None}}},
            {
                "$group": {
                    "_id": "$location",
                    "avg_salary": {"$avg": "$salary"},
                    "job_count": {"$sum": 1}
                }
            },
            {"$sort": {"avg_salary": -1 }}
        ]

        results = list(self.collection.aggregate(pipeline))
        # Return sebagai DataFrame biar cantik, tapi jangan print disini
        # Biarkan 'Main Program' yang nge-print
        return pd.DataFrame(results)
    
    def get_top_companies(self, limit=5):
        """
        Method untuk mencari perusahaan mana yang paling banyak membuka lowongan
        """
        pipeline = [
            #Stage Bersih bersih
            {"$match" : {"company": {"$ne": None}}},
            #Stage grouping
            {
                "$group": {
                    "_id" : "$company",
                    "avg_salary": {"$avg": "$salary"},
                    "job_count" : {"$sum": 1}
                }
            },
            
            #Stage sorting
            {"$sort": {"job_count": -1}},

            #Stage Limit
            {"$limit": limit}
        ]
        results = list(self.collection.aggregate(pipeline))
        return pd.DataFrame(results)
    
# --- UJI COBA CLASS (Main Program) ---
if __name__ == "__main__" :
    #1. Instansiasi (Menghidupkan Robot)
    bot = JobMarketAnalyzer()

    #2. Suruh Robot Kerja: Load Data 
    bot.load_data('data_raw/big_job_data.csv')

    #3. Suruh Robot Kerja: Analisa
    print("\n📊 Laporan Gaji (Big Data Analysis):")
    df_salary = bot.get_salary_summary()

    #Format angka
    pd.options.display.float_format = '{:,.0f}'.format
    print(df_salary)

    # 4. Cetak Laporan 2: Top Companies
    print("\n🏆 LAPORAN 2: Top 5 Perusahaan Paling Aktif")
    df_top = bot.get_top_companies(limit=5)
    print(df_top)

# python src/job_analyzer.py

