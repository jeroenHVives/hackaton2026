
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define cso = Character("CSO", color="#e7eb0e")
define ceo = Character("CEO", color="#faa911")
define it = Character("IT consultant", color="#29fa11")
define wv = Character("Werknemer vertegenwoordiger", color="#118afa")
define cfo = Character("CFO", color="#03fce3")
define narator = Character(" ")

default geld = 1066000
default reputatie = 100

default WV_Happines = 7
default MFA = False
default diff_passwords = False 
default phishing_aware = False
default updates = False

#is a transform attribute to ajust the size
transform room_size:
    zoom 0.75

transform cso_size:
    zoom 0.2

transform ceo_size:
    zoom 0.13

transform it_size:
    zoom 0.13

transform wv_size:
    zoom 0.60

transform small_size: 
    zoom 0.13 #adjust as required

transform medium_size:
    zoom 0.2

transform normal_size:
    zoom 0.75


screen money():
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -20
        yoffset 20

        padding (10, 10)

        text "€[geld]":
            size 22
            color "#ffffff"


# The game starts here.
label start:
    #for the background
    scene bg room at room_size
    show ceo at ceo_size, left
    show cso at cso_size, right

    show screen money()

    ceo "Ah, kom verder. Ga zitten. Welkom bij NeXioCo."
    ceo "Je weet waarom we je hebben aangenomen. Ons bedrijf is de afgelopen jaren geëxplodeerd. We hebben inmiddels 800 werknemers op de loonlijst, we draaien miljoenenomzetten, maar als ik heel eerlijk ben... onze IT-security is een gatenkaas."
    ceo "Daarom ben jij nu onze Chief Security Officer. Jij krijgt de leiding over ons budget en jij bepaalt vanaf vandaag welke maatregelen we wel en niet doorvoeren."
    cso "Ik ben er klaar voor. Waar beginnen we mee?"
    ceo "We hebben een externe IT-consultant ingehuurd. Zij heeft ons hele bedrijf geanalyseerd en een lijst met mogelijke securitymaatregelen voorbereid."
    ceo "Het is aan jou om haar voorstellen te beoordelen. Jij hakt de knopen door over wat we wel en niet gaan invoeren. Weeg de kosten af tegen de risico's voor het bedrijf."
    ceo "Je zult harde keuzes moeten maken. Succes. Ze wachten op je in de vergaderzaal."

    # cso normal is the name for the file you want to use as character sprite this sprite stands in the images folder
    # Small_size is a self made attribute (see above)
    # left and right is a attribute in renpy that decides where the character sprite stands
    
    hide ceo
    show cso at cso_size, left
    show it at it_size, right


    jump question_1

label question_1:
    #Is to let a character say a scentence
    it "Laten we beginnen bij de basis: Multifactorauthenticatie (MFA). Dit is de belangrijkste barrière tegen ongeautoriseerde toegang."
    hide it
    show wv at wv_size, right
    wv "Wacht eens even, als we dit verplichten moeten mensen elke keer hun privételefoon pakken om in te loggen. Dat gaat veel klachten opleveren."


    #menu for mfa
    menu:

        # These display lines of dialogue.
        "Wil je Multifactorauthenticatie aanleggen voor alle medewerkers?"    

        #option 1
        "Geen MFA":
            #MFA staat al op False
            hide wv
            show it at it_size, right
            it "Dit is een groot risico. Wachtwoorden alleen zijn niet genoeg."
            hide it
            show wv at wv_size, right
            wv "Fijn om te horen dat we de mensen niet lastigvallen met extra inlogstappen."
            jump question_2            
            

        #option 2
        "Optionele MFA (de medewerkers zelf laten kiezen)":
            $ MFA = renpy.random.choice([True, False])
            hide wv
            show it at it_size, right
            it "Een halfslachtige oplossing. Slechts een deel van het bedrijf is nu beschermd."
            hide it
            show wv at wv_size, right
            wv "Een redelijk compromis, zolang het niet verplicht is."
            jump question_2
            
            
        "Verplichte MFA":
            $ MFA = True
            $ WV_Happines = WV_Happines - 1
            $ reputatie = reputatie - 5
            hide wv
            show it at it_size, right
            it "Verstandig. Dit verkleint de kans op een succesvolle hack aanzienlijk."
            hide it
            show wv at wv_size, right
            wv "De werknemers gaan hier niet blij mee zijn, dit kost ze elke dag extra tijd."
            jump question_2

label question_2:
    hide wv
    show it at it_size, right
    it "Het volgende punt: Het wachtwoordbeleid. We zien dat veel medewerkers nu simpelweg hetzelfde wachtwoord voor alle systemen gebruiken."
    hide it
    show wv at wv_size, right
    wv "Ja, natuurlijk. Je kunt toch van niemand verwachten dat ze twintig verschillende complexe codes onthouden?"
    hide wv
    show it at it_size, right
    it "Maar als dat ene wachtwoord ergens uitlekt, hebben hackers meteen toegang tot ons hele bedrijfsnetwerk. We moeten bepalen hoe we dit aanpakken, CSO."

    menu:
        "Moeten de medewerkers voor elk account een ander wachtwoord gebruiken?" 

        "De medewerkers mogen voor meerdere accounts dezelfde wachtwoorden gebruiken.":
            hide wv
            show it at it_size, right
            it "Dit is echt wachten op een ramp. Eén simpel datalek op een externe site en ons bedrijf ligt open."
            hide it
            show wv at wv_size, right
            wv "Ik ben blij dat je realistisch blijft. Zo kunnen we tenminste gewoon doorwerken zonder hoofdpijn."
            jump question_3

        
        "De medewerkers moeten voor elk account een ander wachtwoord gebruiken. Maar deze wachtwoorden mogen gelijkaardig zijn.":
            hide wv
            show it at it_size, right
            it "Hackers kennen die truc met 'Wachtwoord1' en 'Wachtwoord2' echt al lang. Dit biedt vooral schijnveiligheid."
            hide it
            show wv at wv_size, right
            wv "Het is tenminste werkbaar voor de mensen. Dan veranderen we elke maand gewoon het laatste cijfertje."
            jump question_3

        "De medewerkers moeten voor elk account een ander wachtwoord gebruiken en deze moeten telkens helemaal anders zijn.":
            hide wv
            show it at it_size, right
            it "De enige echt veilige keuze. Zo zorgen we ervoor dat elk account geïsoleerd en goed afgeschermd is."
            hide it
            show wv at wv_size, right
            wv "Dit is toch onmogelijk te onthouden?! Dan gaan mensen het gegarandeerd overal op post-its schrijven!"
            $ diff_passwords = True
            jump passwrd_safe

label passwrd_safe:
    hide it
    show wv at wv_size, right
    wv "Als we dan toch onmogelijke, complexe wachtwoorden moeten bedenken voor elk systeem, dan eisen we wel dat we een wachtwoordmanager mogen gebruiken."
    hide wv
    show it at it_size, right
    it "Een wachtwoordmanager of 'Password Safe' is inderdaad noodzakelijk nu. Maar hoe gaan we dat faciliteren? Dat is de vraag."

    menu:
        "Mogen de medewerkers een wachtwoordenmanager gebruiken?"

        "De medewerkers mogen een gratis wachtwoordenmanager gebruiken.":
            hide wv
            show it at it_size, right
            it "Het probleem is dat we als IT-afdeling geen overzicht hebben over die gratis privéklaasjes. Als iemand uit dienst gaat, raken we de toegang kwijt."
            hide it
            show wv at wv_size, right
            wv "Mij best, zolang de medewerkers hun wachtwoorden maar ergens veilig kunnen opslaan."
            jump question_3


        "De medewerkers mogen geen wachtwoordenmanager gebruiken.":
            hide it
            show wv at wv_size, right
            wv "Dit is compleet bizar! Je eist onmogelijke dingen van het personeel zonder ons de middelen te geven. Het werk wordt zo onmogelijk gemaakt!"
            hide wv
            show it at it_size, right
            it "Ik zet me alvast schrap voor een explosie aan 'wachtwoord vergeten' tickets bij de helpdesk..."
            $ WV_Happines = WV_Happines - 1
            jump question_3


        "Het bedrijf zal €8000 aan de kant zetten om te investeren in wachtwoordenmanagers zodat elke gebruiker een heeft.":
            hide wv
            show it at it_size, right
            it "Een hele sterke keuze. Met een betaalde Enterprise-versie beveiligen we de boel én kunnen we accounts centraal beheren en intrekken."
            hide it
            show wv at wv_size, right
            wv "Kijk, zo hoort het. Als de directie de juiste tools betaalt en faciliteert, werken we daar graag aan mee."
            $ geld = geld - 8000
            jump question_3

label question_3:
    hide wv
    show it at it_size, right
    it "We moeten het hebben over phishing. Werknemers klikken nog te vaak op onveilige links in e-mails, waardoor hackers binnenkomen."
    hide it
    show wv at wv_size, right
    wv "De meeste mensen hebben echt wel door of een mail nep is of niet. We hoeven ze daar niet voor van hun werk te houden met verplichte theorie."
    default awareness = renpy.random.randint(1,4)
    menu:
        "Moeten de werknemers een phishing awareness training doen?"

        "Ja, de medewerkerkers moeten een phishing awareness training doen.":
            hide wv
            show it at it_size, right
            it "Een verstandige keuze. Door ze te trainen, maken we van onze medewerkers een sterke verdedigingslinie."
            hide it
            show wv at wv_size, right
            wv "Daar gaan weer kostbare uren naar een verplichte cursus... De werkvloer zal hier echt niet blij mee zijn."
            if (awareness <= 3):
                $ phishing_aware = True
            jump question_4
        
        "Nee, de medewerkers zijn niet verplicht om een phishing awareness training doen.":
            hide it
            show wv at wv_size, right
            wv "Precies, we vertrouwen gewoon op het gezonde verstand van onze mensen. Dat bespaart een hoop tijd en frustratie."
            hide wv
            show it at it_size, right
            it "Ik hoop dat je gelijk hebt, maar zonder training lopen we hier echt een aanzienlijk risico."
            if (awareness <=1 ):
                $ phishing_aware = True
            jump question_4

label question_4:
    it "Het volgende punt gaat over software-updates. Verouderde software bevat vaak beveiligingslekken die hackers gemakkelijk kunnen misbruiken."
    wv "Maar die updates komen altijd op het slechtste moment! Je bent net geconcentreerd bezig en dan eist je computer ineens een herstart van een kwartier."

    menu:
        "Moeten de medewerkers auto-update aanzetten?"

        "Nee, ze moeten zelf updaten als er een update is.":
            $ WV_Happines = WV_Happines - 1
            it "Zolang de medewerkers er maar prioriteit aan geven en ze direct installeren, is het netwerk in ieder geval veilig."
            wv "Dus we moeten nu constant zélf in de gaten houden of er een update is en ons werk daarvoor stilleggen? Dat is echt enorm frustrerend!"
            $ updates = True
            jump question_5

        "Nee, ze zijn niet verplicht om updates te doen.":
            wv "Mooi, dan bepalen we zelf wel of en wanneer we er tijd voor hebben. Dat scheelt een hoop onnodige werkonderbrekingen."
            it "Dit is echt een tijdbom. Bekende kwetsbaarheden in onze systemen blijven zo simpelweg openstaan voor aanvallers."
            jump question_5

        "Ja, ze zijn verplicht om auto updates aan te zetten.":
            it "Perfect. Met automatische updates worden de lekken meteen gedicht zonder dat iemand eraan hoeft te denken."
            wv "Zolang de computers dat updaten maar 's nachts of op de achtergrond doen, scheelt het ons in ieder geval handmatig werk..."
            $ updates = True
            $ updates = True 
            jump question_5         

label question_5:
    it "Een andere vorm van toegangscontrole is biometrie. We kunnen investeren in vingerafdrukscanners voor alle computers."
    wv "Vingerafdrukken? Gaan we nu ook al fysieke kenmerken van ons personeel opslaan? Dat voelt toch wel als een flinke inbreuk op de privacy."
    menu:
        "Moeten de medewerkers fingerprint scanners gebruiken om in te loggen?"

        "Ja, ze moeten fingerprint scanners gebruiken en we gaan voor iedereen een scanner kopen. Dit zal €40.000 kosten":
            $ MFA = True
            $ geld = geld - 40000
            if (geld < 0):
                jump failliet
            else:
                $ WV_Happines = WV_Happines - 1

                it "Een flinke investering, maar biometrische MFA is ontzettend lastig te omzeilen voor hackers. Ons netwerk is hiermee veel veiliger."

                if( WV_Happines <= 3):
                    wv "Dit is echt de druppel! Eerst al die andere extreme regels, en nu moeten we ook nog gescand worden alsof we criminelen zijn?! Het werk is hier niet meer te doen!"
                else:
                    wv "Ik blijf het een inbreuk op de privacy vinden en het kost een fortuin... maar goed, als de directie denkt dat het echt moet."
                jump intro_deel2

        "Nee, ze moeten geen fingerprint scanners gebruiken":
            wv "Gelukkig. Laten we onze biometrische gegevens gewoon lekker privé houden. En het bespaart nog geld ook."
            it "Jammer. Ik begrijp dat de kosten hoog zijn, maar we laten hiermee wel een ijzersterke beveiligingslaag liggen."
            jump intro_deel2
        

default firewall = 0
default backups = 0
default backups_time = 0
default eigen_server = False

label intro_deel2:        
    it "Goed, we hebben de beleidsafspraken voor het personeel nu rond. De werknemervertegenwoordiger kan weer aan het werk."
    it "Nu we het gaan hebben over de harde IT-infrastructuur en de grote systemen, heb ik iemand anders aan tafel gevraagd."
    cfo "Goedemiddag. Als Chief Financial Officer houd ik de portemonnee van NeXioCo strak in de gaten. Ik hoor dat deze hardware-plannen in de tienduizenden euro's gaan lopen."
    cfo "We hebben geen bodemloze put als budget, CSO. Elke euro die we aan 'onzichtbare' security uitgeven, kunnen we niet in onze groei steken. Ik verwacht dat je alleen investeert in wat écht strikt noodzakelijk is."
    jump deel2_question_1

label deel2_question_1:
    it "Laten we beginnen met de voordeur van ons bedrijfsnetwerk: de firewall. Met 800 medewerkers stroomt er dagelijks gigantisch veel data in en uit."
    it "We hebben een krachtige Next-Generation Firewall nodig die al dat netwerkverkeer scant op virussen en indringers buiten de deur houdt."
    cfo "Ik heb de mogelijke offertes gezien en ik schrok me kapot. Die apparaten zijn peperduur. Is dat echt nodig, of kunnen we het met een budgetoplossing af?"
    
    menu:
        "Welke firewall moet het bedrijf aankopen?"

        "Het bedrijf moet geen firewall aankopen":
            $ firewall = 0
            it "Dit is absolute waanzin! Zonder firewall staan al onze bedrijfsgegevens, servers en klantinformatie gewoon open en bloot op het internet!"
            cfo "Kijk, dat is nou eens een flinke besparing. Ik hoop wel dat je weet wat je doet, CSO, de verantwoordelijkheid ligt volledig bij jou."
            jump deel2_question_2


        "Het bedrijf moet een goedkope firewall aankopen. (€ 20.000)":
            $ firewall = 1
            $ geld = geld - 20000
            it "Een instapmodel. Het houdt de meest simpele aanvallen tegen, maar we kopen er maar één. Als dit apparaat crasht, ligt de internetverbinding voor alle 800 medewerkers plat."
            cfo "Twintigduizend euro is nog net te overzien. Zolang het dat vinkje voor de security-audit maar op groen zet, vind ik het best."
            if (geld < 0):
                jump failliet
            else:
                jump deel2_question_2

        "Het bedrijf moet een iets duurdere firewall aankopen. (€ 60.000)":
            $ firewall = 2
            $ geld = geld - 60000
            it "Een uitstekende en verstandige keuze. Hiermee kopen we twee firewalls die elkaars werk naadloos overnemen als er één uitvalt, mét geavanceerde virusscans."
            cfo "Zestigduizend euro... Pfft, dat is een flinke hap uit onze winstmarge. Maar goed, als het ons een nog duurdere hack en downtime bespaart, heb je mijn zegen."
            if (geld < 0):
                jump failliet
            else:
                jump deel2_question_2

        "Het bedrijf moet een heel dure firewall aankopen. (€ 120 000)":
            $ firewall = 3
            $ geld = geld - 120000
            it "Perfect! Dit is de absolute top van de markt voor enterprise netwerken. Onverslaanbare netwerksegmentatie, topsnelheid en de allerbeste actieve virusdetectie die we kunnen krijgen."
            cfo "Honderdtwintigduizend euro?! Ben je je verstand verloren? Dit is zwaar overdreven en slaat een gigantisch gat in onze kas!"
            if (geld < 0):
                jump failliet
            else:
                jump deel2_question_2

label deel2_question_2:
    it "Het volgende agendapunt is onze back-up strategie. Als er ooit ransomware op ons netwerk belandt, versleutelen de hackers al onze data."
    it "Zonder goede back-ups zijn we in zo'n scenario letterlijk al onze bedrijfsgegevens kwijt, of moeten we miljoenen aan losgeld betalen."
    cfo "Ik weet dat we data moeten bewaren, maar ik zie ook de facturen van die cloud-opslag. Het kost ons handenvol geld om dingen dubbel op te slaan."

    menu:
        "Wat gaan we back-uppen?"

        "Alles back-uppen. (computers, documenten, mails, shares ...) (€225.000)":
            $ backups = 2
            $ geld = geld - 225000
            it "Een fantastische keuze. Mocht er een ramp gebeuren, dan kunnen we letterlijk het hele bedrijf inclusief alle mailboxen en pc-instellingen binnen no-time herstellen."
            cfo "Tweehonderdvijfentwintigduizend euro?! Dit is te bizar voor woorden! We betalen een kwart miljoen voor het opslaan van gigabytes aan nutteloze e-mails en kattenplaatjes van het personeel!"
            if (geld < 0):
                jump failliet
            else:
                jump deel2_question_3

        "Alleen de documenten back-uppen (€66.000)":
            $ backups = 1
            $ geld = geld - 66000
            it "Een werkbaar compromis. De harde bedrijfsdata is veilig, al zijn we bij een hack wel alle e-mailhistorie en individuele computerinstellingen kwijt."
            cfo "Kijk, zesenzestigduizend euro klinkt al een stuk logischer. De essentiële contracten zijn veilig, en de rest is toch maar ballast."
            if (geld < 0):
                jump failliet
            else:
                jump deel2_question_3
        
        "Niets back-uppen":
            $ backups = 0
            it "Dit is een onverantwoord risico! Als we een ransomware-aanval binnenkrijgen of een zware servercrash hebben, riskeren we het voortbestaan van het hele bedrijf."
            cfo "Kijk, dat is weer nul euro op de begroting. Bovendien hebben we net geld uitgegeven aan de voordeur, toch? Zorg dan gewoon dat die hackers überhaupt niet binnenkomen."
            jump hack



label deel2_question_3:
    narator "placeholder om de hoeveel dagen back-uppen."
    
    menu:
        "Wanneer wordt er geback-upt?"
        
        "elk jaar back-uppen (€250.000)":
            $ backups_time = 1
            $ geld = geld - 250000
            narator "placeholder jaarlijks back-uppen"
            if (geld < 0):
                jump failliet
            else:
                jump deel2_question_4

        "elke maand back-uppen (€650.000)":
            $ backups_time = 2
            $ geld = geld - 650000
            narator "placeholder maandelijks back-uppen"
            if (geld < 0):
                jump failliet
            else:
                jump hack

        "elke week back-uppen (€800.000)":
            $ backups_time = 3
            $ geld = geld - 800000
            narator "placeholder weekelijks back-uppen"
            if (geld < 0):
                jump failliet
            else:
                jump hack
                #jump deel2_question_4
        
        "elke dag back-uppen (€1.000.000)":
            $ backups_time = 4
            $ geld = geld - 1000000
            narator "placeholder dagelijks back-uppen"
            if (geld < 0):
                jump failliet
            else:
                jump hack
                #jump deel2_question_4

"""label deel2_question_4:
    narator "placeholder eigen server of externe server"
    
    menu:
        "Wil je back-uppen op eigen servers of op externe servers?"
        
        "Eigen servers. (€110.000)":
            $ eigen_server = True
            $ geld = geld - 110000
            narator "placeholder eigen server voor backups"
            if (geld < 0):
                jump failliet
            else:
                jump hack

        "Externe servers (€90.000)":
            $ eigen_server = False
            $ geld = geld - 90000
            narator "placeholder externe server voor backups"
            if (geld < 0):
                jump failliet
            else:
                jump hack
"""
default weakness = 0

label hack:
    if (phishing_aware):
        $ reputatie = reputatie + 10
        wv "Wacht, een van de werknemers meldt net een extreem overtuigende e-mail over een onbetaalde factuur. Hij herkende het als phishing dankzij de training en klikte niet!"
        it "Fantastisch! Onze menselijke firewall werkt. De eerste aanvalsgolf is afgeslagen."
        jump hack_2
    else:
        it "Slecht nieuws. Een werknemer trapte in een phishing mail over een onbetaalde factuur en heeft zijn inloggegevens ingevuld."
        menu:
            "Moet de medewerker zijn wachtwoorden veranderen?"

            "Hij moet zijn wachtwoorden niet aanpassen.":
                it "We doen niets? Laten we hopen dat de hackers niet sneller zijn dan wij... Dit is gewoon gokken."
                if (diff_passwords):
                    $ weakness = weakness + 1
                if (diff_passwords):
                    $ weakness = weakness + 1
                else:
                    $ weakness = weakness + 2
                jump hack_2

            "Hij moet alleen dat wachtwoord aanpassen.":
                if not diff_passwords:
                    $ weakness = weakness + 2
                $ reputatie = reputatie - 5   
                it "We hebben het wachtwoord gereset. Maar aangezien we hetzelfde wachtwoord voor alles toestaan, proberen ze het nu vast op een ander systeem."           
                jump hack_2

            "Hij moet al zijn wachtwoorden aanpassen.":
                $ reputatie = reputatie - 15
                it "Het is streng, maar wel de enige manier om de boel nu af te dichten."
                jump hack_2
  
label hack_2:
    it "Het stopt niet. Er is zojuist een wereldwijde 'Zero-Day' kwetsbaarheid ontdekt in de software die wij gebruiken."
    if (updates):
        it "Gelukkig hebben we automatische updates aan staan! Al onze systemen zijn vannacht gepatcht, dus de hackers lopen hier tegen een muur."
        $ reputatie = reputatie + 5
        jump hack_3
    else:
        $ weakness = weakness + 1
        $ reputatie = reputatie - 5
        menu:
            "Wil je de medewerkers verplichten om te updaten?"

            "Ja, de medewerkers verplichten om te updaten.":
                wv "Je gooit nu letterlijk iedereen uit het systeem! Heel NeXioCo zit nu naar een update-scherm te staren. De productie ligt volledig plat!"
                $ reputatie = reputatie - 10
                jump hack_3
            
            "Nee, de medewerkers niet verplichten om te updaten.":
                it "We laten de lekken openstaan? De hackers hoeven nu niet eens meer moeite te doen om binnen te komen..."
                $ reputatie = reputatie - 5
                $ weakness = weakness + 1
                jump hack_3

label hack_3:
    it "Kijk naar deze logs! Ze proberen nu in te loggen met gestolen werknemersgegevens..."
    if not MFA:
        it "We hebben geen Multi-Factor Authenticatie! De hacker is succesvol ingelogd met alleen het wachtwoord. Ze zitten op ons netwerk!"
        $ weakness = weakness + 1
    else:
        it "De hacker probeerde in te loggen, maar werd geblokkeerd! Hij had de MFA-code op de telefoon van de medewerker niet. Deze aanval is afgeslagen!"
    jump hack_4

label hack_4:
    it "Ze proberen het nu met brute kracht. Er stroomt een gigantische hoeveelheid geautomatiseerde malware op onze voordeur af!"
    if (firewall == 0):
        it "We hebben geen firewall! Het schadelijke verkeer stroomt ongehinderd ons netwerk binnen. Dit is een slachtpartij!"
    elif (firewall == 1):
        it "Onze instap-firewall houdt de simpelste pings tegen, maar dit is geavanceerde malware. Het apparaat is overbelast en ze glippen erdoorheen!"
    else:
        it "Onze enterprise firewall herkent de malware direct. Het schadelijke verkeer wordt vakkundig geblokkeerd en geïsoleerd. We houden stand!"
    $ weakness = weakness + (3-firewall)
    jump the_aftermatch

label the_aftermatch:
    ceo "CSO! Kom onmiddellijk naar mijn kantoor!"
    if (weakness < 3):
        ceo "Ik hoorde van IT dat we zwaar onder vuur lagen, maar dat we nagenoeg alles hebben afgeslagen."
        ceo "Uitstekend werk. Je hebt ons bedrijf gered van een miljoenenstrop. Je bent je salaris dubbel en dwars waard!"
        $ reputatie = reputatie + 50
    elif (weakness < 6):
        ceo "De hackers zijn binnengedrongen! Ze hebben onze allerbelangrijkste contracten en klantdossiers achter ransomware gezet!"
        if (backups == 1 or backups == 2):
            it "Geen paniek, we hebben gelukkig back-ups van deze bestanden veiliggesteld."
            
            if (backups_time == 4):
                it "Omdat we dagelijks back-uppen, verliezen we hooguit het werk van gistermiddag. We zijn snel weer online."
                $ reputatie = reputatie - 5
            elif (backups_time == 3):
                it "We verliezen wel een hele week aan data. Dat gaat een flinke chaos opleveren op de administratie."
                $ reputatie = reputatie - 15
            elif (backups_time == 2):
                it "We zijn een maand aan documenten kwijt. Het gaat heel veel tijd en geld kosten om dat handmatig te herstellen."
                $ reputatie = reputatie - 25
                $ geld = geld - 6000000
            else:
                narator "placeholder jaarlijkse backuppen"
                $ reputatie = reputatie - 25
                narator "placeholder grote som (€55.000.000)"
                $ geld = geld - 55000000
        else:
            ceo "En je vertelt me nu dat we GEEN back-ups hebben?! We moeten het losgeld betalen of we kunnen de deuren sluiten!"
            $ reputatie = reputatie - 50
            ceo "Dit gaat ons 70 miljoen euro kosten! Hoe heb je dit kunnen laten gebeuren?!"
            $ geld = geld - 70000000
    else:
        ceo "HET HELE BEDRIJF LIGT PLAT! De hackers hebben volledige toegang gekregen en letterlijk elke server en computer versleuteld!"
        if (backups == 2):
            it "Dit is een catastrofe, maar we hebben gelukkig wel een back-up van al onze systemen en servers."
            if (backups_time == 4):
                it "Dankzij de dagelijkse back-ups kunnen we de schade beperken tot gisteren. Het kost moeite, maar we komen hier doorheen."
                $ reputatie = reputatie - 5
            elif (backups_time == 3):
                it "We verliezen een hele week aan bedrijfsactiviteit en configuraties. De impact op de operatie is enorm."
                $ reputatie = reputatie - 15
            elif (backups_time == 2):
                it "Een maand aan dataverlies op het héle netwerk. We moeten systemen dagenlang handmatig nabouwen."
                $ reputatie = reputatie - 25
                ceo "Dat gaat ons zo'n 14 miljoen euro kosten aan herstel en misgelopen omzet. Wat een puinhoop!"
                $ geld = geld - 14000000
            else:
                it "Onze laatste volledige back-up is bijna een jaar oud... We moeten alles van de afgelopen maanden opnieuw opbouwen."
                $ reputatie = reputatie - 25
                ceo "Een jaar aan data weg?! De herstelkosten en reputatieschade gaan ons 95 miljoen euro kosten! Je speelt met de toekomst van dit bedrijf!"
                $ geld = geld - 95000000
        elif (backups == 1):
            ceo "We hebben wel onze documenten, maar de héle IT-infrastructuur is vernietigd! We moeten het netwerk van de grond af opnieuw opbouwen!"
            $ reputatie = reputatie - 50
            ceo "De schade loopt op tot wel 150 miljoen euro! Aandeelhouders gaan onze koppen eisen!"
            $ geld = geld - 150000000
        else:
            ceo "We hebben helemaal niets meer! Geen servers, geen data, en geen back-ups. Het bedrijf is volledig verwoest door jouw laksheid."
            $ reputatie = reputatie - 100
            ceo "Dat is 200 miljoen euro aan schade! Je bent op staande voet ONTSLAGEN!"
            $ geld = geld - 200000000
    
    if geld < 0:
        jump failliet
    else:
        jump the_end