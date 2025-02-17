def DiscountCalculator(original_price, discount_percentage):
    discount_amount = original_price * (discount_percentage / 100)
    final_price = original_price - discount_amount
    print(f"Original Price: {original_price:.2f} €")
    print(f"Discount Amount: {discount_amount:.2f} €")
    print(f"Final Price after {discount_percentage}% discount: {final_price:.2f} €")

while True:
    print("Welches Programm wollen Sie nutzen?")
    print("1. Prozentrechner")
    print("2. MwSt. Rechner")
    print("3. Rabattrechner")
    programm = int(input("Bitte geben Sie eine 1, 2 oder 3 ein: "))    
    if programm == 1:
        try:
            LP = float(input("Listenpreis: ").replace(",", ".").replace("€", "").replace(" EUR", ""))
            EP = float(input("Einkaufspreis: ").replace(",", ".").replace("€", "").replace(" EUR", ""))
            Prozentrechner(LP, EP)
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine gültige Zahl ein.")
    
    elif programm == 2:
        try:
            wert = float(input("Bitte geben Sie einen Bruttowert ein: ").replace(",", ".").replace("€", ""))
            land = input("Bitte geben Sie ein Landeskürzel ein:")
            MwSt_Rechner(wert, land)
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine gültige Zahl ein.")
    
    elif programm == 3:
        try:
            original_price = float(input("Originalpreis: ").replace(",", ".").replace("€", ""))
            discount_percentage = float(input("Rabattprozentsatz: ").replace(",", "."))
            DiscountCalculator(original_price, discount_percentage)
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine gültige Zahl ein.")
    
    nochmal = input("Möchten Sie eine weitere Berechnung durchführen? (Y/N): ").lower()
    if nochmal != "y":
        print("Das Programm wird beendet.")
        break