import pandas as pd 
import os

# Data pura pura (dummy data)
# Bayangkan ini adalah data yang biasanya kita download dari Kaggle/Internet

data = [
    {
        "job_title" : "Data Analyst",
        "company" : "Gojek",
        "location" : "Jakarta",
        "description" : "Dibutuhkan ahli SQL dan Python. Mengerti MongoDB adalah nilai plus.",
        "salary": 15000000
    },
    {
        "job_title" : "Software Engineer",
        "company": "Tokopedia",
        "location": "Remote",
        "description": "Dicari programmer Java dan Springboot. Tahan tekanan tinggi.",
        "salary": 20000000
    },
    {
        "job_title": "Admin",
        "company": "CV Maju Mundur",
        "location": "Bekasi",
        "description": "Bisa Excel dan Word. Rajin dan Teliti.",
        "salary": 500000
    },
    {
        "job_title": "AI Engineer",
        "company": "OpenAI Cabang Indonesia",
        "location": "Jakarta",
        "description": "Menguasai NLP, Python, dan TensorFlow. Pengalaman NoSQL.",
        "salary": 35000000
    }

]

def create_csv():
    #1. Ubah list dictionary di atas menjadi DataFrame (Tabel Pandas)
    df = pd.read_json(pd.io.json.dumps(data)) if False else pd.DataFrame(data)
    # ^ Cara simpelnya: pd.DataFrame(data)

    #2. Tentukan mau simpan dimana
    # KIta mundur satu folder lalu masuk ke data_raw
    file_path = os.path.join("data_raw", "job_postings.csv")

    #3. Simpan jadi CSV
    df.to_csv(file_path, index=False)
    print(f"✅ File CSV berhasil dibuat di : {file_path}")
    print("Isi data preview: ")
    print(df.head())

if __name__ == "__main__":
    create_csv()

# python src/00_generate_dummy_data.py