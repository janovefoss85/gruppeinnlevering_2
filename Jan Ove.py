# Prosjekt 2 IS-118
# Jan Ove`s interaktive spill med Erling i hovedrollen
# Din oppgave er å ta Erling sine valg.
print("Situasjon 1: Håndtering av konflikten mellom Silje og Elias")
print("Alternativ 1A Skjermet trepartssamtale")
print("Alternativ 1B Induviduel en til en samtale")

valg1 = input("Hva velger du? (Alternativ 1A eller 1B?) ")
poeng = 0

if valg1 == "1A" or valg1 == "1a":
    print("\n Du valgte skermet trepartssamtale.")
    poeng = poeng + 2
elif valg1 == "1B" or valg1 == "1b":
    print("\n Du valgte induviduel en til en samtale")
    poeng = poeng + 1
else:
    print("\n Du tastet inn et ugyldig valg, start på nytt")

print ("Du har hjulpet Erling til å ta første viktige avgjørelse")

print("Situasjon 2: Forbygge den ulmende saken melllom Hamdi og Hallgeir")
print("Alternativ 2A:Innkalle til et avklaringsmøte om innbyggerdialogen")
print("Alternativ 2B:Avvente situasjonen og la partene finne ut av det selv")

valg2 = input("Hva velger du? (alternativ 2A eller 2B?)")

if valg2 == "2A" or valg2 == "2a":
    print("\\nDu valgte avklaringsmøte. Uenigheten stoppet tidlig. Bra jobbet!")
    poeng = poeng + 2
elif valg2 == "2B" or valg2 == "2b":
    print("\\nDu valgte å avvente. Frustrasjonen ligger fortsatt under overflaten.")
    poeng = poeng + 0
else:
    print("\n Du tastet inn et ugyldig valg, start på nytt")

print("Du har hjulpet Erling å ta enda en viktig avgjørlse")

print("Situasjon 3: Bevare motivasjonen og samholdet i teamet mot prototypefristen")
print("Alternativ 3A: Prioritere relasjonsbygging og teambygging")
print("Alternativ 3B: Prioritere stram fremdrift og faglige referanser")

valg3 = input("Hva velger du? (alternativ 3A eller 3B? )")

if valg3 == "3A" or valg3 == "3a":
    print("\nDu valgte teambuilding. Tilliten og tryggheten øker i gruppen.")
    poeng = poeng + 2
elif valg3 == "3B" or valg3 == "3b":
    print("\nDu valgte stram fremdrift. Prototypen blir ferdig, men teamet er slitt.")
    poeng = poeng + 1
else:
    print("\n Du tastet inn et ugyldig valg, start på nytt")

print("Det var siste avgjørese Erling takker deg for hjelpen.")

print("Sluttresultat")
print("Din totale poengsum er:", poeng)

if poeng >= 5:
    print("Resultat: Erling har gjennvunnet prosjektgruppens tillitt," \
    "prosjektet blir levert i tide")
elif poeng >= 3:
    print("Prosjektet blir delvis levert, men det skurrer enda mellom prosjektmedlemmene")
else:
    print("Prosjektet ble ikke levert og flere prosjektmedlemmer sluttet")

print("Takk for du du hjalp Erling")



