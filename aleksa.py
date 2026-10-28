# Interaktiv historie: Erlings prosjektteam
# IS-118 – Gruppeoppgave 2
# Kjor programmet i terminalen med: python erling_game.py
# Din valg har stor konsekvenser... Passe på godt på hvilken valg du gjør...

def get_choice(prompt, option_a, option_b):
    """Be brukeren velge A eller B, og kontroller input."""
    while True:
        print(prompt)
        print(f"A: {option_a}")
        print(f"B: {option_b}")
        choice = input("Velg A eller B: ").strip().upper()

        if choice in ("A", "B"):
            return choice
        else:
            print("Ugyldig valg. Skriv A eller B.\n")


def main():
    print("=" * 55)
    print("MEDBORGERPORTALEN: ERLINGS VANSKELIGE VALG")
    print("=" * 55)
    print(
        "\nDet har gått seks uker siden Erling startet prosjektet med å utvikle "
        "kommunens nye medborgerportal. Teamet har tre uker igjen til "
        "prototypefristen. Det har oppstått uenigheter, og Erling må ta tre "
        "viktige beslutninger. Valgene dine påvirker hvordan historien ender.\n"
    )

    # Beslutning 1: Konflikten mellom Silje og Elias
    print("\n--- SITUASJON 1: SILJE OG ELIAS ---")
    print(
        "Silje mener at Elias' tekniske forslag begrenser brukeropplevelsen. "
        "Elias mener Siljes forslag er usikre og for kostbare. Diskusjonene "
        "har blitt personlige.")
    
    choice1 = get_choice(
        "\nHva bør Erling gjøre?",
        "Møte sammen: samle Silje og Elias for å diskutere konflikten direkte.",
        "Møte hver for seg: snakke individuelt med dem for å roe ned situasjonen.")
    

    if choice1 == "A":
        print(
            "\nErling leder et felles møte. Begge får forklare synspunktene sine. "
            "Det kan føre til en tidlig avklaring, men samtalen krever god styring "
            "for å unngå at konflikten blir sterkere.")
        
    else:
        print(
            "\nErling snakker med dem hver for seg. De får et roligere rom til å "
            "forklare frustrasjonen sin, men prosessen tar mer tid og kan oppfattes "
            "som at Erling driver med bakromspolitikk.")
        

    # Beslutning 2: Uenigheten mellom Hamdi og Hallgeir
    print("\n--- SITUASJON 2: HAMDI OG HALLGEIR ---")
    print(
        "Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende "
        "plattform. Hallgeir ønsker en mer åpen løsning der innbyggerne kan "
        "komme med spontane innspill.")
    
    choice2 = get_choice(
        "\nHva bør Erling gjøre?",
        "Avklaringsmøte: samle Hamdi og Hallgeir for å avklare forventningene.",
        "Se det an: la dem forsøke å finne en løsning på egen hånd.")
    

    if choice2 == "A":
        print(
            "\nErling arrangerer et avklaringsmøte. Uenigheten kan løses før den "
            "vokser, men møtet tar verdifull tid fra arbeidet med prototypen.")

    else:
        print(
            "\nErling lar dem prøve selv. Det sparer tid nå, men misnøyen kan "
            "fortsette under overflaten og bli et større problem senere.")
        

    # Beslutning 3: Motivasjon eller prototypefrist
    print("\n--- SITUASJON 3: MOTIVASJON ELLER FRAMDRIFT ---")
    print(
        "Prototypefristen nærmer seg. Teamet trenger både framdrift og et "
        "bedre samarbeidsklima."
    )
    choice3 = get_choice(
        "\nHva bør Erling prioritere?",
        "Teambuilding: bruke tid på å bygge tillit og forbedre samarbeidet.",
        "Stram framdrift: prioritere koding, oppgavefordeling og fristen."
    )

    if choice3 == "A":
        print(
            "\nErling prioriterer teambuilding. Teamet får tid til å bygge tillit, "
            "men det blir mindre tid til koding."
        )
    else:
        print(
            "\nErling prioriterer framdrift. Teamet får mer tid til å utvikle "
            "prototypen, men stress og uavklarte konflikter kan øke."
        )

    # Avslutning: Valgene brukes til å avgjøre hvilket utfall som passer best.
    print("\n" + "=" * 55)
    print("SLUTTEN PÅ HISTORIEN")
    print("=" * 55)

    # Slutt 1: Alle konflikter håndteres aktivt, og relasjoner prioriteres.
    if choice1 == "A" and choice2 == "A" and choice3 == "A":
        print("\nSLUTT 1: KONFLIKTENE LØSES TIDLIG, MEN TIDEN ØKER")
        print(
            "Erling tar tak i begge uenighetene og prioriterer teamets "
            "samarbeid. Teamet får bedre forståelse for hverandre og kan bevege "
            "seg mot norming-fasen. Samtidig har møtene og teambuildingen brukt "
            "mye tid, så prototypefristen er i fare.")
        

    # Slutt 2: Teamet prioriterer framdrift, men presset øker.
    elif choice3 == "B" and (choice1 == "B" or choice2 == "B"):
        print("\nSLUTT 2: GOD FRAMDRIFT, MEN TEAMET BLIR MER PRESSET")
        print(
            "Erling prioriterer å få arbeidet gjort og bruker mindre tid på "
            "relasjonsbygging. Prototypen har bedre mulighet til å bli ferdig "
            "i tide, men noen konflikter kan forbli uløste. Stresset kan øke, "
            "og samarbeidet kan bli svakere på lengre sikt.")

    # Slutt 3: Relasjoner prioriteres, men det tekniske arbeidet forsinkes.
    else:
        print("\nSLUTT 3: TRYGGERE SAMARBEID, MEN PROTOTYPEN KAN BLI FORSINKET")
        print(
            "Erling bruker tid på å håndtere uenigheter og styrke samarbeidet. "
            "Teamet opplever et tryggere arbeidsmiljø, men den samlede tiden "
            "som brukes på møter og relasjonsbygging kan forsinke kodingen. "
            "Det er derfor en risiko for at prototypen ikke blir ferdig innen "
            "fristen.")

    print("\nValgene dine:")
    print(f"Situasjon 1 : Silje og Elias: {choice1}")
    print(f"Situasjon 2 : Hamdi og Hallgeir: {choice2}")
    print(f"Situasjon 3 : Motivasjon og framdrift: {choice3}")
    print("\nTakk for at du spilte! Du kan nå spille New Game+!")


if __name__ == "__main__":
    main()
