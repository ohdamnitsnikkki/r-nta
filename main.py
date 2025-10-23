# Startkapital satt till 100'000 kronor

startkapital = 100000

# Be användare fylla i räntesatsen, samt felhantera ogiltigt format

while True:
    try:
        # Be användaren om räntesats
        ranta = float(input("Fyll i din årliga räntesat: "))
        break # Avsluta om räntesatsen är i korrekt format
    except ValueError: # Fångar felaktigt format tillexempel bokstäver
        print("Ogiltigt format. Försök igen, exempel 3.5")


# Skriv ut tabellrubriker
print("\nÅr\tKapital (kr)\tÅrets ränta (kr)")
print("------------------------------------------")

# Loopa fem gånger (över fem år)

# Kopia av startkapitalet för beräkningar
kapital = startkapital  

for ar in range(1, 6):
    # Beräkna kapital med ränta
    nytt_kapital = kapital * (1 + ranta / 100)
    # Beräkna årets ränta (skillnaden från förra årets kapital)
    arets_ranta = nytt_kapital - kapital
    # Uppdatera kapital till de ya värdet
    kapital = nytt_kapital

    # Skriv ut året, totala kapitalet och årets ränta med två decimaler
    print(f"{ar}\t{kapital:.2f}\t\t{arets_ranta:.2f}")

# Avsluta programmet
print("\nBeräkningen är klar!")