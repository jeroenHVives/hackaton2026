# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ceo = Character("CEO")
define IT = Character("IT consultant")
define narator = Character(" ")

transform small_size: 
    zoom 0.10 #adjust as required


transform big_size:
    zoom 1.5


transform normal_size:
    zoom 0.4
# The game starts here.

label start:
    scene bg room at normal_size

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ceo normal at small_size, left
    show it guy at big_size, right

    IT "Kunnen we €2000 krijgen voor beveiliging van ons netwerk?"

    menu:
        # Show a background. This uses a placeholder by default, but you can
        # add a file (named either "bg room.png" or "bg room.jpg") to the
        # images directory to show it.

        

        # These display lines of dialogue.
        "Wil je €2000 uitgeven aan het beveiligen van het netwerk?"    

        "Goedgekeuren":

            narator "Er was een poging om jullie bedrijf te hacken. Maar de firewall heeft de hack tegen gehouden."

        "Afkeuren":

            narator "Er was een poging om jullie bedrijf te hacken."
            IT "Het bedrijf is gehackt en we zijn al onze data kwijt. Hadden we maar ons netwerk beveiligd."


    # This ends the game.

    


    return

