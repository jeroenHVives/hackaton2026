# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define ceo = Character("CEO")
define IT = Character("IT consultant")
define narator = Character(" ")

#is a transform attribute to ajust the size
transform small_size: 
    zoom 0.10 #adjust as required

transform normal_size:
    zoom 0.75


# The game starts here.
label start:
    #for the background
    scene bg room at normal_size

    # ceo normal is the name for the file you want to use as character sprite this sprite stands in the images folder
    # Small_size is a self made attribute (see above)
    # left and right is a attribute in renpy that decides where the character sprite stands
    show ceo normal at small_size, left
    show it guy at small_size, right

    #Is to let a character say a scentence
    IT "Kunnen we €2000 krijgen voor beveiliging van ons netwerk?"

    #This is to add user options 
    menu:

        # These display lines of dialogue.
        "Wil je €2000 uitgeven aan het beveiligen van het netwerk?"    

        #option 1
        "Goedgekeuren":
            #what happens when option 1 is clicked 
            narator "Er was een poging om jullie bedrijf te hacken. Maar de firewall heeft de hack tegen gehouden."

        #option 2
        "Afkeuren":

            #What happens when option 2 is clicked
            narator "Er was een poging om jullie bedrijf te hacken."
            IT "Het bedrijf is gehackt en we zijn al onze data kwijt. Hadden we maar ons netwerk beveiligd."


    # This ends the game.
    return

