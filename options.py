from verification import *

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
