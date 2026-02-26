# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define ceo = Character("CEO")
define IT = Character("IT consultant")
define narator = Character(" ")

default geld = 4000

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

    show screen money()

    # ceo normal is the name for the file you want to use as character sprite this sprite stands in the images folder
    # Small_size is a self made attribute (see above)
    # left and right is a attribute in renpy that decides where the character sprite stands
    show ceo normal at small_size, left
    show it guy at small_size, right

    default kost = 5000
    #Is to let a character say a scentence
    IT "Kunnen we €[kost] krijgen voor beveiliging van ons netwerk?"

    #This is to add user options 
    menu:

        # These display lines of dialogue.
        "Wil je €[kost] uitgeven aan het beveiligen van het netwerk?"    

        #option 1
        "Goedgekeuren":
            $ geld = geld - kost
            show screen money()
            if (geld <= 0):
                jump failliet
            else:
                jump goedgekeurd

        #option 2
        "Afkeuren":
            #What happens when option 2 is clicked
            jump afgekeurd
    


    

label goedgekeurd:
    narator "Er was een poging om jullie bedrijf te hacken. Maar de firewall heeft de hack tegen gehouden."

    jump the_end

label afgekeurd:
    narator "Er was een poging om jullie bedrijf te hacken."
    IT "Het bedrijf is gehackt en we zijn al onze data kwijt. Hadden we maar ons netwerk beveiligd."
    IT "Dit zal ons €5.000.000 kosten"

    $ geld = geld - 5000000
    show screen money()

    if (geld < 0):
        jump failliet
    else:
        jump the_end

label failliet: 
    narator "Je bedrijf is failliet gegaan"

    return

label the_end:
    # This ends the game.
    return