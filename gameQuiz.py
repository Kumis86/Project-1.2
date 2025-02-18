import os

# Password default
PASSWORD = "admin123"

# Fungsi untuk memeriksa apakah file pertanyaan sudah ada
def check_file():
    if not os.path.exists("quiz_questions.txt"):
        with open("quiz_questions.txt", "w") as file:
            file.write("")

# Fungsi untuk membaca pertanyaan dari file
def read_questions():
    questions = []
    with open("quiz_questions.txt", "r") as file:
        for line in file:
            question, answer = line.strip().split("|")
            questions.append({"question": question, "answer": answer})
    return questions

# Fungsi untuk menampilkan semua pertanyaan
def show_questions():
    questions = read_questions()
    if not questions:
        print("Tidak ada pertanyaan yang tersedia!")
    else:
        print("=== Daftar Pertanyaan ===")
        for i, q in enumerate(questions, 1):
            print(f"{i}. Pertanyaan: {q['question']} | Jawaban: {q['answer']}")

# Fungsi untuk meminta password
def ask_password():
    password = input("Masukkan password: ")
    return password == PASSWORD

# Fungsi untuk menambahkan pertanyaan baru
def add_question():
    if ask_password():
        question = input("Masukkan pertanyaan baru: ")
        answer = input("Masukkan jawaban: ")
        with open("quiz_questions.txt", "a") as file:
            file.write(f"{question}|{answer}\n")
        print("Pertanyaan berhasil ditambahkan!")
    else:
        print("Password salah! Akses ditolak.")

# Fungsi untuk mengedit pertanyaan
def edit_question():
    if ask_password():
        questions = read_questions()
        show_questions()
        try:
            question_number = int(input("Pilih nomor pertanyaan yang ingin diubah: ")) - 1
            if 0 <= question_number < len(questions):
                new_question = input("Masukkan pertanyaan baru: ")
                new_answer = input("Masukkan jawaban baru: ")
                questions[question_number] = {"question": new_question, "answer": new_answer}
                with open("quiz_questions.txt", "w") as file:
                    for q in questions:
                        file.write(f"{q['question']}|{q['answer']}\n")
                print("Pertanyaan berhasil diubah!")
            else:
                print("Nomor pertanyaan tidak valid!")
        except ValueError:
            print("Input harus berupa angka!")
    else:
        print("Password salah! Akses ditolak.")

# Fungsi untuk menghapus pertanyaan
def delete_question():
    if ask_password():
        questions = read_questions()
        show_questions()
        try:
            question_number = int(input("Pilih nomor pertanyaan yang ingin dihapus: ")) - 1
            if 0 <= question_number < len(questions):
                questions.pop(question_number)
                with open("quiz_questions.txt", "w") as file:
                    for q in questions:
                        file.write(f"{q['question']}|{q['answer']}\n")
                print("Pertanyaan berhasil dihapus!")
            else:
                print("Nomor pertanyaan tidak valid!")
        except ValueError:
            print("Input harus berupa angka!")
    else:
        print("Password salah! Akses ditolak.")

# Fungsi untuk memainkan quiz
def play_quiz():
    questions = read_questions()
    if not questions:
        print("Tidak ada pertanyaan yang tersedia untuk dimainkan!")
        return

    score = 0
    print("=== Selamat datang di Quiz Game! ===")
    for i, q in enumerate(questions, 1):
        print(f"\nPertanyaan {i}: {q['question']}")
        user_answer = input("Jawaban Anda: ")
        if user_answer.lower() == q['answer'].lower():
            print("Benar!")
            score += 1
        else:
            print(f"Salah! Jawaban yang benar adalah: {q['answer']}")
    print(f"\nGame selesai! Skor Anda: {score}/{len(questions)}")

# Fungsi utama game
def main():
    check_file()
    while True:
        print("\n=== Menu Quiz Game ===")
        print("1. Main Quiz")
        print("2. Lihat Pertanyaan")
        print("3. Tambah Pertanyaan")
        print("4. Edit Pertanyaan")
        print("5. Hapus Pertanyaan")
        print("6. Keluar")
        choice = input("Pilih menu (1-6): ")

        if choice == "1":
            play_quiz()
        elif choice == "2":
            show_questions()
        elif choice == "3":
            add_question()
        elif choice == "4":
            edit_question()
        elif choice == "5":
            delete_question()
        elif choice == "6":
            print("Terima kasih telah bermain! Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()