import os

PASSWORD = "admin123"

# Fungsi untuk meminta password
def ask_password():
    password = input("Masukkan password: ")
    return password == PASSWORD # Password default


# Fungsi untuk memeriksa apakah file pertanyaan sudah ada
def check_file():
    if not os.path.exists("quiz_questions.txt"):
        with open("quiz_questions.txt", "w") as file:
            file.write("")
#Fungsi untuk mengecek file Pilihan Ganda 
def check_file_PG():
    if not os.path.exists("quiz_questions_PG.txt"):
        with open("quiz_questions_PG.txt", "w") as file:
            file.write("")
#Fungsi untuk mengecek file True or False
def check_file_TF():
    if not os.path.exists("quiz_questions_TF.txt"):
        with open("quiz_questions_TF.txt", "w") as file:
            file.write("")
