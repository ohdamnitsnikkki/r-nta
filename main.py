# Startkapital satt till 100'000 kronor

startkapital = 100000

# Be användare fylla i räntesatsen, samt felhantera ogiltigt format

while True:
    try:
        # Be användaren om räntesats
        ranta = float(input("Fyll i din årliga räntesat: "))
        break # Avsluta om räntesatsen är i korrekt format
    except ValueError: # Be användaren försöka igen om räntesatsen är felaktig
        print("Ogiltigt format. Försök igen, exempel 3.5")