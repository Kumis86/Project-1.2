from options import *
from verification import *

check_file()
def main():
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
            mode_quiz()
        elif choice == "2":
            result = show_questions_mode()
            if result == "back":
                continue  # Kembali ke menu utama
        elif choice == "3":
            add_question_mode()
        elif choice == "4":
            edit_question_mode()
        elif choice == "5":
            delete_question_mode()
        elif choice == "6":
            print("Terima kasih telah bermain! Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
        