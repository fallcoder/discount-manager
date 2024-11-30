from discount import calculate_discount
from input_handler import get_user_input

def main():
    print("**** BIENVENUE ****")

    user_input = get_user_input()
    if user_input is not None:
        age, is_student, initial_price = user_input
        calculate_discount(age, is_student, initial_price)
    else:
        print("données invalides, impossible de calculer la réduction") 
        
        

if __name__ == "__main__":
    main()