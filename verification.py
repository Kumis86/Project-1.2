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

