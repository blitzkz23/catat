from module.display import *
from module.display import *

income = []
outcome = []

def main():
    # Show welcome menu
    show_welcome_menu()
    
    is_transaction_done = False
    
    while not is_transaction_done:
        menu_choice = input("Masukkan pilihan menu (1-6): \n")
        try:
            if menu_choice == "1":
                print("1")
            elif menu_choice == "2":
                print("2")
            elif menu_choice == "3":
                print("3")
            elif menu_choice == "4":
                print("4")
            elif menu_choice == "5":
                print("5")
            elif menu_choice == "6":
                print("6")
            else:
                print("Maaf, menu tidak tersedia silahkan pilih dari nomor (1-6)")      
        except Exception as e:
            print(f"--- ERROR: Terjadi kesalahan: {e}. ---\n")
            
    
    

if __name__ == "__main__":
    main()