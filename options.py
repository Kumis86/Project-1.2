from verification import *
#fungsi untuk memilih mode Lihat Pertanyaan
def show_questions_mode():
    os.system('cls')
    print("Silahkan untuk memilih mode")
    print("1. Lihat Pertanyaan Essay")
    print("2. Lihat Pertanyaan Pilihan Ganda")
    print("3. Lihat Pertanyaan True or False")
    print("4. Kembali")
    choice = input("Masukkan Nomor (1-4): ")

    if choice == "1":
        show_questions()
    elif choice == "2":
        show_questions_PG()
    elif choice == "3":
        show_questions_TF()
    elif choice == "4":
        return "back"  # Kembali ke menu utama
    else:
        print("Nomor tidak valid. Coba Lagi")

#fungsi untuk menambah mode Pertanyaan
def add_question_mode():
    os.system('cls')
    
    print("Silahkan untuk memilih mode")
    print("1.Add Pertanyaan Essay")
    print("2.Add Pertanyaan Pilihan Ganda")
    print("3.Add Pertanyaan True or False")
    print("4.Kembali")
    choice = input("Masukkan Nomor (1-4): ")

    if choice == "1":
        add_question()
    elif choice == "2":
        add_question_PG()
    elif choice == "3":
        add_question_TF()
    elif choice == "4":
        return "back"
    else :
        print("nomor tidak valid. Coba Lagi")


#fungsi untuk menghapus mode Pertanyaan
def delete_question_mode():
    os.system('cls')
    
    print("Silahkan untuk memilih mode")
    print("1.Hapus Pertanyaan Essay")
    print("2.Hapus Pertanyaan Pilihan Ganda")
    print("3.Hapus Pertanyaan True or False")
    print("4.kembali")
    choice = input("Masukkan Nomor (1-4): ")

    if choice == "1":
       delete_question()
    elif choice == "2":
       delete_question_pg()
    elif choice == "3":
        delete_question_TF()
    elif choice == "4":
        return "back"
    else :
        print("nomor tidak valid. Coba Lagi")


#fungsi untuk mengedit mode Pertanyaan
def edit_question_mode():
    os.system('cls')
    
    print("Silahkan untuk memilih mode")
    print("1.Edit Pertanyaan Essay")
    print("2.Edit Pertanyaan Pilihan Ganda")
    print("3.Edit Pertanyaan True or False")
    print("4.Kembali")
    choice = input("Masukkan Nomor (1-4): ")

    if choice == "1":
        edit_question()
    elif choice == "2":
        edit_question_PG()
    elif choice == "3":
        edit_queation_tf()
    elif choice == "4":
        return "back"
    else :
        print("nomor tidak valid. Coba Lagi")

        
#fungsi untuk memilih Game mode
def mode_quiz():
    os.system('cls')
    
    print("Silahkan untuk memilih mode")
    print("1.Essay")
    print("2.Pilihan Ganda")
    print("3.True or False")
    print("4.kembali")
    choice = input("Masukkan Nomor (1-4): ")

    if choice == "1":
        play_quiz()
    elif choice == "2":
        Pilihan_Ganda()
    elif choice == "3":
        True_False()
    elif choice == "4":
        return "back"
    else :
        print("nomor tidak valid. Coba Lagi")



#Essay
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

#PG
#fungsi untuk membaca
def read_questions_PG():
    questions_PG = []
    with open("quiz_questions_PG.txt", "r") as file:
        for line in file:
            question, answer = line.strip().split("|")
            questions_PG.append({"question": question, "answer": answer})
    return questions_PG

#fungsi untuk melihat pertanyaan yang ada
def show_questions_PG():
    questions = read_questions_PG()
    if not questions:
        print("Tidak ada pertanyaan yang tersedia!")
    else:
        print("=== Daftar Pertanyaan ===")
        for i, q in enumerate(questions, 1):
            print(f"{i}. Pertanyaan: {q['question']} | Jawaban: {q['answer']}")

#Fungsi untuk menambahkan pertanyaan
def add_question_PG():
    if ask_password():
        question = input("Masukkan pertanyaan baru: ")
        question2 = input("Masukkan pilihan ganda dengan format a._ b._ dst.:")
        answer = input("Masukkan jawaban: ")
        with open("quiz_questions_PG.txt", "a") as file:
            file.write(f"{question}{question2}|{answer}\n")
        print("Pertanyaan berhasil ditambahkan!")
    else:
        print("Password salah! Akses ditolak.")

#Fungsi untuk mengedit pertanyaan
def edit_question_PG():
    if ask_password():
        questions_PG = read_questions_PG()
        show_questions_PG()
        try:
            question_number = int(input("Pilih nomor pertanyaan yang ingin diubah: ")) - 1
            if 0 <= question_number < len(questions_PG):
                new_question = input("Masukkan pertanyaan baru: ")
                new_answer = input("Masukkan jawaban baru: ")
                questions_PG[question_number] = {"question": new_question, "answer": new_answer}
                with open("quiz_questions_PG.txt", "w") as file:
                    for q in questions_PG:
                        file.write(f"{q['question']}|{q['answer']}\n")
                print("Pertanyaan berhasil diubah!")
            else:
                print("Nomor pertanyaan tidak valid!")
        except ValueError:
            print("Input harus berupa angka!")
    else:
        print("Password salah! Akses ditolak.")

#fungsi untuk menghapus pertanyaan
def delete_question_pg():
        if ask_password():
            questions_PG = read_questions_PG()
            show_questions_PG()
            try:
                question_number = int(input("Pilih nomor pertanyaan yang ingin dihapus: ")) - 1
                if 0 <= question_number < len(questions_PG):
                    questions_PG.pop(question_number)
                    with open("quiz_questions_PG.txt", "w") as file:
                        for q in questions_PG:
                            file.write(f"{q['question']}|{q['answer']}\n")
                    print("Pertanyaan berhasil dihapus!")
                else:
                    print("Nomor pertanyaan tidak valid!")
            except ValueError:
                print("Input harus berupa angka!")
        else:
            print("Password salah! Akses ditolak.")

#fungsi untuk bermain
def Pilihan_Ganda():
    questions_PG = read_questions_PG()
    if not questions_PG:
        print("Tidak ada pertanyaan yang tersedia untuk dimainkan!")
        return

    score = 0
    print("=== Selamat datang di Quiz Game! ===")
    for i, q in enumerate(questions_PG, 1):
        print(f"\nPertanyaan {i}: {q['question']}")
        user_answer = input("Jawaban Anda: ")
        if user_answer.lower() == q['answer'].lower():
            print("Benar!")
            score += 1
        else:
            print(f"Salah! Jawaban yang benar adalah: {q['answer']}")
    print(f"\nGame selesai! Skor Anda: {score}/{len(questions_PG)}")

#Truth or False section
#fungsi untuk membaca
def read_questions_TF():
    questions = []
    with open("quiz_questions_TF.txt", "r") as file:
        for line in file:
            question, answer = line.strip().split("|")
            questions.append({"question": question, "answer": answer})
    return questions

#fungsi untuk melihat pertanyaan yang ada
def show_questions_TF():
    questions = read_questions_TF()
    if not questions:
        print("Tidak ada pertanyaan yang tersedia!")
    else:
        print("=== Daftar Pertanyaan ===")
        for i, q in enumerate(questions, 1):
            print(f"{i}. Pertanyaan: {q['question']} | Jawaban: {q['answer']}")

#Fungsi untuk menambahkan pertanyaan
def add_question_TF():
    if ask_password():
        question = input("Masukkan pertanyaan baru: ")
        answer = input("Masukkan jawaban: ")
        with open("quiz_questions_TF.txt", "a") as file:
            file.write(f"{question}|{answer}\n")
        print("Pertanyaan berhasil ditambahkan!")
    else:
        print("Password salah! Akses ditolak.")

#Fungsi untuk mengedit pertanyaan
def edit_queation_tf():
    if ask_password():
        questions_TF = read_questions_TF()
        show_questions_TF()
        try:
            question_number = int(input("Pilih nomor pertanyaan yang ingin diubah: ")) - 1
            if 0 <= question_number < len(questions_TF):
                new_question = input("Masukkan pertanyaan baru: ")
                new_answer = input("Masukkan jawaban baru: ")
                questions_TF[question_number] = {"question": new_question, "answer": new_answer}
                with open("quiz_questions_TF.txt", "w") as file:
                    for q in questions_TF:
                        file.write(f"{q['question']}|{q['answer']}\n")
                print("Pertanyaan berhasil diubah!")
            else:
                print("Nomor pertanyaan tidak valid!")
        except ValueError:
            print("Input harus berupa angka!")
    else:
        print("Password salah! Akses ditolak.")

#fungsi untuk menghapus pertanyaan
def delete_question_TF():
    if ask_password():
        questions_TF = read_questions_TF()
        show_questions_TF()
        try:
            question_number = int(input("Pilih nomor pertanyaan yang ingin dihapus: ")) - 1
            if 0 <= question_number < len(questions_TF):
                questions_TF.pop(question_number)
                with open("quiz_questions_TF.txt", "w") as file:
                    for q in questions_TF:
                        file.write(f"{q['question']}|{q['answer']}\n")
                print("Pertanyaan berhasil dihapus!")
            else:
                print("Nomor pertanyaan tidak valid!")
        except ValueError:
            print("Input harus berupa angka!")
    else:
        print("Password salah! Akses ditolak.")

#fungsi untuk bermain
def True_False():
    questions_TF = read_questions_TF()
    if not questions_TF:
        print("Tidak ada pertanyaan yang tersedia untuk dimainkan!")
        return

    score = 0
    print("=== Selamat datang di Quiz Game! ===")
    for i, q in enumerate(questions_TF, 1):
        print(f"\nPertanyaan {i}: {q['question']}")
        user_answer = input("Jawaban Anda(tekan (1) untuk benar dan tekan (0)untuk salah): ")
        if user_answer.lower() == q['answer'].lower():
            print("Benar!")
            score += 1
        else:
            print(f"Salah! Jawaban yang benar adalah: {q['answer']}")
    print(f"\nGame selesai! Skor Anda: {score}/{len(questions_TF)}")
