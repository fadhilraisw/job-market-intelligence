import pandas as pd
import random
import os


# Bank Kata (Vocabulary) untuk diacak
TITLES = ["Data Analyst", "Data Scientist", "Backend Engineer", "Frontend Dev", "DevOps Engineer", "AI Specialist", "Fullstack Dev"]
COMPANIES = ["Gojek", "Tokopedia", "Traveloka", "Shopee", "Bukalapak", "Bank BCA", "Telkomsel", "Startup Stealth"]
LOCATIONS = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta", "Bali", "Remote", "Batam", "Medan"]
SKILLS = ["Python", "SQL", "MongoDB", "Excel", "Tableu", "React", "Docker", "AWS", "TensorFlow"]

def generate_description(title, skill_list):
    # Membuat deskripsi lowongan yang terlihat nyata
    required_skills = random.sample(skill_list, k=3) # Ambil 3 skill acak
    return f"We are looking for a{title}. Candidates must be proficient in {','.join(required_skills)}. Good salary and benefits."

def generate_dataset(num_rows=1000) :
    data = []
    print(f"🚀 Memulai generate {num_rows} data lowongan kerja...")

    for _ in range(num_rows):
        title = random.choice(TITLES)

        # Logika Gaji: Engineer biasanya lebih mahal dari Analyst (contoh kasar)
        base_salary = 5000000
        if "Engineer" in title or "Dev" in title or "AI" in title:
            base_salary = 100000000

        # Tambahkan variabel acak pada gaji
        salary = base_salary + random.randint(1000000, 20000000)

        item = {
            "job_title": title,
            "company": random.choice(COMPANIES),
            "location": random.choice(LOCATIONS),
            "description": generate_description(title, SKILLS),
            "salary": salary,
            "posted_at": "2026-01-24" #Anggap semua baru
        }
        data.append(item)
    
    # Simpan ke CSV
    df = pd.read_json(pd.io.json.dumps(data)) if False else pd.DataFrame(data)
    file_path = os.path.join("data_raw", "big_job_data.csv")
    df.to_csv(file_path, index=False)

    print(f"✅ Selesai! {num_rows} data tersimpan di: {file_path}")
    print("Contoh 5 data teratas")
    print(df.head())

#main
if __name__ == "__main__":
    #Kita buat 5000 data!
    generate_dataset(5000)

# python src/03_generate_big_data.py

