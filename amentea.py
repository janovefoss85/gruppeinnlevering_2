# ==============================================================================
# Interaktivt spill, rip erling (IS-118)
# ==============================================================================

def start_spill():
    print("GTA 6 loading .........")
    print("neida Erling's medborgerportal\n")

    
    # BESLUTNINGSPUNKT 1
    -
    print("\nSilje vs Elias")
    print("\nUenighet om teknologivalg har glidd fra sakskonflikt til personkonflikt")
    print("\nSilje mener at Elias låser brukeropplevelsen og hinder til innovasjon")
    print("\nElias mener Silje's forslag er urealistisk, usikkert og for dyrt")
    print("A: Skal Erling arrangere møte sammen med begge to? Altså kun de 3")
    print("B: Eller skal Erling gjennføre individuelle møter hver for seg?")
    
    valg1 = input("\nHva tenker du? (A/B): ").strip().upper()
    
    if valg1 == "A":
        print("\nLøser konflikten direkte, men fare for hete diskusjoner. Gjennomtenkt valg!")
    else:
        print("\nGir en falsk trygghet og kan virke som baksnakking. Den tapende parten kan bli mistenksom på hva som ble sagt for å påvirke utfallet. Nå mister du hode litt")

    
    # BESLUTNINGSPUNKT 2
    
    print("\n Hamdi mot Hallgeir")
    print("De er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter: Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform.Hallgeir ønsker et mer åpent, dialogbasert system med rom for spontane innspill")
    print("A: Avklaringsmøte?")
    print("B:Århhh... Vi ser det an?")
    
    valg2 = input("\nHva velger du? (A/B): ").strip().upper()
    
    if valg2 == "A":
        print("\nForebygger ny konflikt men tar verdifull arbeidstid .Meget bra valg selv om det koster litt tid")
    else:
        print("\nSparer tid nå, men kan lage ett rent he****** senere. Wow ok? mistenkelig valg........")

   
    # BESLUTNINGSPUNKT 3
   
    print("\nSørge for god stemning eller tenke framdrift?")
    print("Erling merker at det er litt amper stemning blant gruppa, de har brukt en del tid men har fortsatt litt tid til fristen. Det kan være lurt og ha litt teambuilding i gruppa slik at de leverer ett ordentlig produkt. Eller kan det være framdrift og bare gønne på slik at man 100 prosent rekker fristen")
    print("A:Sette av tid til teambuilding?")
    print("B:Eller bare gønne på å sørge for framdrift?")
    
    valg3 = input("\nDitt valg (A/B): ").strip().upper()
    
    if valg3 == "A":
        print("\nBygger tillit og trygghet, men stjeler fokustid fra koding. Bra!")
    else:
        print("\nSikrer leveranse i tide, men øker risikoen for utrenthet og missnøye. Du må begynne og tenke over valgene dine!")

    
    # SLUTTUTFALL (3 ULIKE ENDEPUNKTER)
    
    
    print("SLUTTRESULTAT")
    print("")

    # Betingelse for Utfall 1
    if valg1 == "A" and valg2 == "A" and valg3 == "A":
        print("\nErling fikk løst konflikten til Silje og Elias, de ble enige på møtet de 3 hadde sammen. Hamdi og Hallgeir fikk pratet sammen og fikk løst det på en god måte selv om det kostet verdifull arbeidstid. At Erling satset teambuilding og brukte mer tid med laget førte faktisk til at laget sammarbeidet bedre og fikk levert ett godt produkt innen tidsfristen.")

    # Betingelse for Utfall 3
    elif valg1 == "B" and valg2 == "B" and valg3 == "B":
        print("\nUTFALL 3: Her gikk det gale, konflikten mellom Silje og Elias, har gått over til personkoflikt. Hamdi og Hallgeir konflikten gikk helt utav kontroll og nå ser det ut som prosjektet er å gi slutt på. Erling kunne kanskje ha reddet teamet men han valgte å satse mer på å nå fristen i god til enn teambuilding. Dette endte opp som en katastrofe både for kommunen og teamet til Erling. Prosjektet ble gjennomført etter tidsfristen men også ett mye dårligere produkt en det som var avtalt")

    # Alle andre kombinasjoner gir Utfall 2
    else:
        print("\nUTFALL 2: Erling sitt prosjekt ble gjennomført men kunne ha gjort dette på betydelig bedre måte. Medborgerportalen ble ferdig innen tidsfristen men er ikke av ypperste kvalitet som kommunen gjerne ønsket men det er innafor. ")


# Kjører spillet når filen åpnes
if __name__ == "__main__":
    start_spill()