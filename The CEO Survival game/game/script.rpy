
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define cso = Character("CSO", color="#e7eb0e")
define ceo = Character("CEO", color="#faa911")
define it = Character("IT consultant", color="#29fa11")
define narator = Character(" ")
define wv = Character("Werknemer vertegenwoordiger", color="#118afa")

default geld = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
default WV_Happines = 7
default MFA = False
default diff_passwords = False 
default phishing_aware = False
default updates = False

#is a transform attribute to ajust the size
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
    scene bg room at normal_size
    show ceo normal at small_size, left
    show cso guy at medium_size, right

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
    
    hide ceo normal
    show it guy at small_size, left


    jump question_1

label question_1:
    #Is to let a character say a scentence
    it "Laten we beginnen bij de basis: Multifactorauthenticatie (MFA). Dit is de belangrijkste barrière tegen ongeautoriseerde toegang."
    wv "Wacht eens even, als we dit verplichten moeten mensen elke keer hun privételefoon pakken om in te loggen. Dat gaat veel klachten opleveren."


    #menu for 2fa
    menu:

        # These display lines of dialogue.
        "Wil je Multifactorauthenticatie aanleggen voor alle medewerkers?"    

        #option 1
        "Geen MFA":
            #MFA staat al op False
            it "Dit is een groot risico. Wachtwoorden alleen zijn niet genoeg."
            wv "Fijn om te horen dat we de mensen niet lastigvallen met extra inlogstappen."
            jump question_2            
            

        #option 2
        "Optionele MFA (de medewerkers zelf laten kiezen)":
            $ MFA = renpy.random.choice([True, False])
            it "Een halfslachtige oplossing. Slechts een deel van het bedrijf is nu beschermd."
            wv "Een redelijk compromis, zolang het niet verplicht is."

            jump question_2
            
            
        "Verplichte MFA":
            $ MFA = True
            $WV_Happines = WV_Happines - 1
            it "Verstandig. Dit verkleint de kans op een succesvolle hack aanzienlijk."
            wv "De werknemers gaan hier niet blij mee zijn, dit kost ze elke dag extra tijd."
            jump question_2

label question_2:
    it "Het volgende punt: Het wachtwoordbeleid. We zien dat veel medewerkers nu simpelweg hetzelfde wachtwoord voor alle systemen gebruiken."
    wv "Ja, natuurlijk. Je kunt toch van niemand verwachten dat ze twintig verschillende complexe codes onthouden?"
    it "Maar als dat ene wachtwoord ergens uitlekt, hebben hackers meteen toegang tot ons hele bedrijfsnetwerk. We moeten bepalen hoe we dit aanpakken, CSO."

    menu:
        "Moeten de medewerkers voor elk account een ander wachtwoord gebruiken?" 

        "De medewerkers mogen voor meerdere accounts dezelfde wachtwoorden gebruiken.":
            it "Dit is echt wachten op een ramp. Eén simpel datalek op een externe site en ons bedrijf ligt open."
            wv "Ik ben blij dat je realistisch blijft. Zo kunnen we tenminste gewoon doorwerken zonder hoofdpijn."
            jump question_3

        
        "De medewerkers moeten voor elk account een ander wachtwoord gebruiken. Maar deze wachtwoorden mogen gelijkaardig zijn.":
            it "Hackers kennen die truc met 'Wachtwoord1' en 'Wachtwoord2' echt al lang. Dit biedt vooral schijnveiligheid."
            wv "Het is tenminste werkbaar voor de mensen. Dan veranderen we elke maand gewoon het laatste cijfertje."
            jump question_3

        "De medewerjers moeten voor elk account een ander wachtwoord gebruiken en deze moeten telkens helemaal anders zijn.":
            it "De enige echt veilige keuze. Zo zorgen we ervoor dat elk account geïsoleerd en goed afgeschermd is."
            wv "Dit is toch onmogelijk te onthouden?! Dan gaan mensen het gegarandeerd overal op post-its schrijven!"
            $diff_passwords = True
            jump passwrd_safe

label passwrd_safe:
    wv "Als we dan toch onmogelijke, complexe wachtwoorden moeten bedenken voor elk systeem, dan eisen we wel dat we een wachtwoordmanager mogen gebruiken."
    it "Een wachtwoordmanager of 'Password Safe' is inderdaad noodzakelijk nu. Maar hoe gaan we dat faciliteren? Dat is de vraag."

    menu:
        "Mogen de medewerkers een wachtwoordenmanager gebruiken?"

        "De medewerkers mogen een gratis wachtwoordenmanager gebruiken.":
            it "Het probleem is dat we als IT-afdeling geen overzicht hebben over die gratis privéklaasjes. Als iemand uit dienst gaat, raken we de toegang kwijt."
            wv "Mij best, zolang de medewerkers hun wachtwoorden maar ergens veilig kunnen opslaan."
            jump question_3


        "De medewerkers mogen geen wachtwoordenmanager gebruiken.":
            wv "Dit is compleet bizar! Je eist onmogelijke dingen van het personeel zonder ons de middelen te geven. Het werk wordt zo onmogelijk gemaakt!"
            it "Ik zet me alvast schrap voor een explosie aan 'wachtwoord vergeten' tickets bij de helpdesk..."
            $WV_Happines = WV_Happines - 1
            jump question_3


        "Het bedrijf zal €8000 aan de kant zetten om te investeren in wachtwoordenmanagers zodat elke gebruiker een heeft.":
            it "Een hele sterke keuze. Met een betaalde Enterprise-versie beveiligen we de boel én kunnen we accounts centraal beheren en intrekken."
            wv "Kijk, zo hoort het. Als de directie de juiste tools betaalt en faciliteert, werken we daar graag aan mee."
            $ geld = geld - 8000
            if (geld < 0):
                jump failliet
            else:
                jump question_3

label question_3:
    it "We moeten het hebben over phishing. Werknemers klikken nog te vaak op onveilige links in e-mails, waardoor hackers binnenkomen."
    wv "De meeste mensen hebben echt wel door of een mail nep is of niet. We hoeven ze daar niet voor van hun werk te houden met verplichte theorie."
    default awareness = renpy.random.randint(1,4)
    menu:
        "Moeten de werknemers een phishing awareness training doen?"

        "Ja, de medewerkerkers moeten een phishing awareness training doen.":
            it "Een verstandige keuze. Door ze te trainen, maken we van onze medewerkers een sterke verdedigingslinie."
            wv "Daar gaan weer kostbare uren naar een verplichte cursus... De werkvloer zal hier echt niet blij mee zijn."
            
            if (awareness <= 3):
                $ phishing_aware = True
            jump question_4
        
        "Nee, de medewerkers zijn niet verplicht om een phishing awareness training doen.":
            wv "Precies, we vertrouwen gewoon op het gezonde verstand van onze mensen. Dat bespaart een hoop tijd en frustratie."
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
default eigen_laptop = False
default Security_cameras = 1

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
        "Welke firewall moet het bedrijf aankopen"

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
            it "Dit is een onverantwoord risico! Als we één keer een cryptolocker binnenkrijgen of een zware servercrash hebben, riskeren we in één klap het voortbestaan van het hele bedrijf."
            cfo "Dat is weer nul euro op de begroting. Bovendien hebben we toch net geld uitgegeven aan beveiliging? Dan zorgen jullie maar dat die hackers überhaupt niet binnenkomen."
            jump deel2_question_3


label deel2_question_3:
    pass

label failliet: 
    narator "Je bedrijf is failliet gegaan"

    return

label the_end:
    narator "placeholder for end result"
    # This ends the game.
    return