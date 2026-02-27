# Bestandsnaam: eindschermen.rpy

################################################################################
## SCREEN: DE VISUELE UI VAN HET EINDSCHERM
################################################################################
screen simpel_eindscherm(titel, bericht, kleur):
    modal True
    zorder 200
    
    # Donkere, strakke achtergrond
    add Solid("#1e1e1e")
    
    # Alles netjes in het midden gecentreerd
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        
        # Titel en bericht
        text "[titel]" size 60 bold True color kleur xalign 0.5
        text "[bericht]" size 24 color "#ffffff" xalign 0.5 text_align 0.5
        
        null height 40
        
        # Stats (Geld, Score en Reputatie)
        text "GELD OVER: € [geld:,d]" size 40 bold True color "#29fa11" xalign 0.5
        
        # Berekening van de score op basis van weakness (hoe lager weakness, hoe hoger de score)
        $ security_score = 100 - (weakness * 10)
        text "SECURITY SCORE: [security_score] / 100" size 30 bold True color "#118afa" xalign 0.5
        text "REPUTATIE: [reputatie] %" size 30 bold True color "#faa911" xalign 0.5
        
        null height 50
        
        # Play Again Knop
        textbutton "PLAY AGAIN" action Start():
            xalign 0.5
            text_size 30
            text_bold True
            text_color "#1e1e1e"
            xpadding 50
            ypadding 20
            background Solid("#e7eb0e") 
            hover_background Solid("#ffffff")

################################################################################
## LABELS OM DE UI OP TE ROEPEN
################################################################################

label the_end:
    hide screen money
    # Groene titel voor succes
    call screen simpel_eindscherm("MISSIE GESLAAGD", "Je hebt het bedrijf succesvol beschermd en draaiende gehouden!", "#29fa11")
    return

label failliet:
    hide screen money
    # Rode titel voor faillissement
    call screen simpel_eindscherm("FAILLIET", "Het budget is compleet overschreden. NeXioCo is failliet.", "#ff4c4c")
    return

label gehackt:
    hide screen money
    # Rode titel voor gehackt
    call screen simpel_eindscherm("GEHACKT", "De beveiliging faalde. Ransomware heeft het bedrijf verwoest.", "#ff4c4c")
    return