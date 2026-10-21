#IS-118 - Gruppeinnlevering 2 
#interaktiv historie om prosjektleder Erling

# Poengsystem: A gir 1 poeng, men B gir 0 poeng
# Antall poeng bestemmer hvilken avsluttning spilleren får
poeng = 0

print ("Velkommen til Erlings prosjekt!")
print ("Du er prosjektleder for kommunens digitale medborgerportal")
print ("Det har gått seks uker siden prosjektstart.")
print ("Teamet opplever konflikter, og du må ta tre viktige beslutninger. ") 

# Situalsjon 1: konlflikten Mellom Silje og ELias

print ("\nSituasjon 1: Konflikten mellom Silje og Elias")
print ("Silje ønsker bedre brukervennlighet, men Elias prioriterer sikkerhet og kostnader.")
print ("Uenigheten har utviklet seg til en personkonflikt.")
print ("Hvordan vil du håndtere konflikten?")

print ("\nA: Arrangere en felles samtale med Silje og Elias.")
print ("B: Ha individuelle samtaler med dem.")
valg1 =input("\nSkriv inn A eller B: ").upper()

while valg1 != "A" and valg1 != "B": 
    print("Ugyldig valg! Du må velge A eller B")
    valg1 = input ("Prøv igjen (A eller B): ").upper()
           

if valg1 == "A":
    poeng += 1
    print ("\nDu samler Silje og Elias til en felles samtale uten resten av teamet.")
    print ("Begge får forklart sine synspunkter, og dere forsøker å finne et kompromiss.")
    print ("Samtalen kan likevel bli opphetet og gjøre konflikten verre.")
elif valg1 == "B":
    print ("\nDu velger å snakke med Silje og Elias hver for seg.")
    print ("Dette gir begge mulighet til å forklare seg i rolige omgivelser.")
    print ("Samtalene tar lengre tid og kan oppfattes som beslutninger bak lukkede dører.")


# Situasjon 2: Konflikten mellom Hamdi og Hallgeir

print("\nSituasjon 2: Konflikten mellom Hamdi og Hallgeir")
print ("Hamdi ønsker at kommunen skal ha kontroll over den digitale plattformen.")    
print ("Hallgeir ønsker en mer åpen dialog med innbyggerne under digitale møter.")
print ("Uenigheten skaper spenning i teamet.")
print ("Prototypen skal være ferdig om tre uker, og tiden begynner å bli knapp.")
print ("Hvordan vil du håndtere situasjonen?")

print ("\nA: Arrangere et strukturert avklaringsmøte.")
print ("B: La Hamdi og Hallgeir forsøke å løse konflikten selv.")
valg2 =input("\nSkriv inn A eller B: ").upper()

while valg2 != "A" and valg2 != "B": 
    print("Ugyldig valg! Du må velge A eller B")
    valg2 = input ("Prøv igjen (A eller B): ").upper()
           
if valg2 == "A":
    poeng += 1
    print("\nDu arrangerer et strukturert avklaringsmøte mellom Hamdi og Hallgeir.")
    print("Begge får forklare sine synspunkter, og dere forsøker å hindre at konflikten eskalerer.")
    print("Møtet tar likevel verdifull arbeidstid, og prototypen skal være ferdig om tre uker.")
elif valg2 == "B":
    print("\nDu lar Hamdi og Hallgeir forsøke å løse konflikten selv.")
    print("Dette sparer tid og gir dem mulighet til å ta ansvar for samarbeidet.")
    print("Men misnøyen kan vokse og føre til en større konflikt senere.")

# Situasjon 3: Motivasjon og samarbeid

print("\nSituasjon 3: Motivasjon og samarbeid")
print(" Teamet har opplevd flere konflikter, og motivasjonen begynner å synke")
print("Prototypen skal leveres om tre uker.")
print("Som prosjektleder må du finne en balanse mellom samarbeid og fremdrift.")
print("Hvordan vil du prioritere?")

print("\nA: Arrangere teambuilding for å styrke tilliten og samarbeidet.")
print("B: Fokusere på tydelige oppgaver, fremdrift og leveranser.")
valg3 =input("\nSkriv inn A eller B: ").upper()

while valg3 != "A" and valg3 != "B": 
    print("Ugyldig valg! Du må velge A eller B")
    valg3 = input ("Prøv igjen (A eller B): ").upper()

if valg3 == "A":
    poeng += 1
    print("\nDu arrangerer teambuilding for å styrke samholdet i teamet.")
    print("Dette kan bygge tillit, skape trygghet og forbedre samarbeidet.")
    print("Samtidig bruker dere verdifull tid som kunne gått til utviklingen av prototypen.")
elif valg3 == "B":
    print("\nDu velger å prioritere fremdrift, tydelige oppgaver og leveranser.")
    print("Dette øker sjansen for at prototypen blir ferdig innen fristen.")
    print("Samtidig kan manglende fokus på samarbeid føre til økt press, misnøye og utmattelse i teamet.")

# Avslutning på historien

print ("\n--- Resultat av dine beslutninger")
# 0 poeng gir avsluttning 1,1 poeng gir avsluttning 2.
# 2 eller 3 poeng gir avsluttning 3.
if poeng == 0:
    print("\nGod fremdrift, men teamet blir mer presset.")
    print("Du har prioritert fremdrift og spart tid på konflikthåndtering.")
    print("Prototypen er på god vei, men flere konflikter er fortsatt uløste.")
    print("Presset på teamet øker, og samarbeidet kan bli vanskeligere fremover.") 

elif poeng == 1:
    print("\nTryggere samarbeid, men prototypefristen kan ryke.")
    print("Du har tatt grep for å forbedre samarbeidet i teamet.")
    print("Dette skaper mer trygghet, men enkelte konflikter er fortsatt utfordrende.")
    print("Tiden begynner å bli knapp, og prototypen står i fare for å bli forsinket.")
else:
    print("\nKonfliktene løses tidlig, men tidsbruken øker.")
    print("Du har prioritert konflikthåndtering og samarbeid gjennom prosjektet.")
    print("Teamet har fått bedre forståelse for hverandre og funnet løsninger på uenighetene.")
    print("Samtidig har møtene tatt verdifull tid fra utviklingen av prototypen.")