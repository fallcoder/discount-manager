def calculate_discount(age, is_student, initial_price):
    if age <= 18: 
        discount_rate = 0.20 if is_student == "oui" else 0.10
    elif age >= 60:
        discount_rate = 0.15
    else:
        discount_rate = 0.0

    discounted_price = initial_price * (1 - discount_rate)

    if discount_rate > 0:
        print(f"réduction de {int(discount_rate * 100)}% appliquée")
    else:
        print("pas de réduction appliquée")

    print(f"prix après réduction : {discounted_price:.2f}€")
    return discounted_price