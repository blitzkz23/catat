from module.display import *
from module.util import *

incomes = []
outcomes = []

def main():
    # Show welcome menu
    show_welcome_menu()
    
    is_transaction_done = False
    
    while not is_transaction_done:
        menu_choice = input("Masukkan pilihan menu (1-6): \n")
        try:
            if menu_choice == "1":
                # Add income
                try:
                    new_income = int(input("Silahkan masukkan pemasukkan baru: \n"))
                    input_income(incomes, new_income)
                    
                    for index, income in enumerate(incomes):
                        print(f"{index} - {income}")
                except ValueError as e:
                    print("Input salah.  Tolong masukkan angka yang valid")
                    continue
            elif menu_choice == "2":
                # Add outcome
                try:
                    new_outcome = int(input("Silahkan masukkan pengeluaran baru: \n"))
                    input_income(outcomes, new_outcome)
                    
                    for index, outcome in enumerate(outcomes):
                        print(f"{index} - {outcome}")
                except ValueError as e:
                    print("Input salah.  Tolong masukkan angka yang valid")
                    continue
            elif menu_choice == "3":
                # Sum income
                print(f"Total pemasukkan: {sum_list(incomes)}")
            elif menu_choice == "4":
                # Sum outcome
                print(f"Total pengeluaran: {sum_list(outcomes)}")
            elif menu_choice == "5":
                # Count gap between income and outcome
                total_incomes = sum_list(incomes)
                total_outcomes = sum_list(outcomes)
                
                print(f"Jumlah pemasukkan - pengeluaran: {total_incomes-total_outcomes}")
            elif menu_choice == "6":
                # exit program
                break
            else:
                print("Maaf, menu tidak tersedia silahkan pilih dari nomor (1-6)")      
        except Exception as e:
            print(f"--- ERROR: Terjadi kesalahan: {e}. ---\n")
            
    
    

if __name__ == "__main__":
    main()