from options import *
from verification import *

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
