
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define cso = Character("CSO")
define ceo = Character("CEO")
define IT = Character("IT consultant")
define narator = Character(" ")
define WV = Character("Werknemer vertegenwoordiger")

default geld = 4000
default WV_Happines = 7
default MFA = False
default diff_passwords = False 
default phishing_aware = False

#is a transform attribute to ajust the size
transform small_size: 
    zoom 0.10 #adjust as required

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
    show cso normal at small_size, left

    show screen money()

    ceo "Ah, kom verder. Ga zitten. Welkom bij NeXioCo."
    ceo "Je weet waarom we je hebben aangenomen. Ons bedrijf is de afgelopen jaren geëxplodeerd. We hebben inmiddels 800 werknemers op de loonlijst, we draaien miljoenenomzetten, maar als ik heel eerlijk ben... onze IT-security is een gatenkaas."
    # cso normal is the name for the file you want to use as character sprite this sprite stands in the images folder
    # Small_size is a self made attribute (see above)
    # left and right is a attribute in renpy that decides where the character sprite stands
    
    show it guy at small_size, right

    jump question_1

label question_1:
    #Is to let a character say a scentence
    narator "Placeholder gesprek MFA"


    #menu for 2fa
    menu:

        # These display lines of dialogue.
        "Wil je Multifactorauthenticatie aanleggen voor alle medewerkers?"    

        #option 1
        "Geen MFA":
            #MFA staat al op False
            IT "placeholder geen MFA"
            jump question_2            
            

        #option 2
        "Optionele MFA (de medewerkers zelf laten kiezen)":
            $ MFA = renpy.random.choice([True, False])
            IT "[MFA]"
            IT "Placeholder optionele MFA"
            jump question_2
            
            
    
        "Verplichte MFA":
            $ MFA = True
            $WV_Happines = WV_Happines - 1
            IT "Placeholder verplichte MFA"
            jump question_2

label question_2:
    narator "Placeholder verschillende wachtwoorden"

    menu:
        "Moeten de medewerkers voor elk account een ander wachtwoord gebruiken?" 

        "De medewerkers mogen voor meerdere accounts dezelfde wachtwoorden gebruiken.":
            narator "Placeholder zelfde wachtwoorden"
            jump question_3

        
        "De medewerkers moeten voor elk account een ander wachtwoord gebruiken. Maar deze wachtwoorden mogen gelijkaardig zijn.":
            narator "Placeholder gelijkaardige wachtwoorden"
            jump question_3


        "De medewerjers moeten voor elk account een ander wachtwoord gebruiken en deze moeten telkens helemaal anders zijn.":
            narator "Placeholder verschillende wachtwoorden"
            $diff_passwords = True
            jump passwrd_safe

label passwrd_safe:
    narator "placeholder paswoord safe"

    menu:
        "Mogen de medewerkers een wachtwoordenmanager gebruiken?"

        "De medewerkers mogen een gratis wachtwoordenmanager gebruiken.":
            narator "placeholder gratis wachtwoordenmanager"
            jump question_3


        "De medewerkers mogen geen wachtwoordenmanager gebruiken.":
            narator "placeholder geen wachtwoordenmanager"
            $WV_Happines = WV_Happines - 1
            jump question_3

        "Het bedrijf zal €8000 aan de kant zetten om te investeren in wachtwoordenmanagers zodat elke gebruiker een heeft.":
            narator "placeholder betalende wachtwoordenmanager"
            $ geld = geld - 8000
            if (geld < 0):
                jump failliet
            else:
                jump question_3

label question_3:
    narator "placeholder phishing awareness training"
    default awareness = renpy.random.randint(1,4)
    menu:
        "Moeten de werknemers een phishing awareness training doen?"

        "Ja, de medewerkerkers moeten een phishing awareness training doen.":
            narator "placeholder wel phishing awareness training"
            
            if (awareness <= 3):
                $ phishing_aware = True
            jump question_4
        
        "Nee, de medewerkers zijn niet verplicht om een phishing awareness training doen.":
            narator "placeholder geen phishing awareness training"
            if (awareness <=1 ):
                $ phishing_aware = True
            jump question_4

label question_4:
    narator "placeholder auto update"

label failliet: 
    narator "Je bedrijf is failliet gegaan"

    return

label the_end:
    narator "placeholder for end result"
    # This ends the game.
    return