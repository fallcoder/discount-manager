def get_user_input():
    try:
        age = int(input("entrez votre age : "))
        if age < 0:
            print("l'age ne peut pas etre négatif")
            return None

        initial_price = float(input("entrez le prix initial : "))
        if initial_price < 0:
            print("le prix ne peut pas etre négatif")
            return None

        is_student = input("etes-vous étudiant ? (oui/non) : ").strip().lower()
        
        if is_student not in ['oui', 'non']:
            print("réponse invalide pour le statut étudiant")
            return None
        #is_student = is_student_input
        print(f"\nAge: {age}, Statut étudiant: {is_student}, Prix initial: {initial_price}")
        return age, is_student, initial_price
    
    except ValueError:
        print("entrée invalide. Veuillez saisir des nombres valides")
        return None
        