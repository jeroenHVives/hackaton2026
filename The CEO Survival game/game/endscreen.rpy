################################################################################
## SCREEN: DE VISUELE UI VAN HET EINDSCHERM (VERBETERD)
################################################################################
screen simpel_eindscherm(titel, bericht, kleur):
    modal True
    zorder 200
    
    # Donkere, semi-transparante achtergrond (dimt het spel erachter)
    add Solid("#000000cc")
    
    # De Pop-up kaart (Modern donker paneel)
    frame:
        xalign 0.5
        yalign 0.5
        padding (60, 50)
        background Solid("#1a1a1a") 
        
        vbox:
            xalign 0.5
            spacing 20
            
            # Gekleurd accentlijntje bovenaan de kaart
            add Solid(kleur) xsize 650 ysize 4 xalign 0.5
            
            null height 10
            
            # Titel en bericht
            text "[titel]" size 60 bold True color kleur xalign 0.5
            text "[bericht]" size 22 color "#cccccc" xalign 0.5 text_align 0.5 xmaximum 650
            
            null height 40
            
            # Stats horizontaal naast elkaar voor een strakker dashboard-gevoel
            hbox:
                xalign 0.5
                spacing 100
                
                # Linker kolom: Budget
                vbox:
                    xalign 0.5
                    spacing 5
                    text "RESTEREND BUDGET" size 16 color "#7f8c8d" bold True xalign 0.5
                    text "€ [geld:,d]" size 45 bold True color "#2ecc71" xalign 0.5
                
                # Rechter kolom: Reputatie
                vbox:
                    xalign 0.5
                    spacing 5
                    text "BEDRIJFSREPUTATIE" size 16 color "#7f8c8d" bold True xalign 0.5
                    text "[reputatie]%" size 45 bold True color "#f1c40f" xalign 0.5
            
            null height 50
            
            # Brede, moderne knop die meekleurt met het thema
            textbutton "OPNIEUW SPELEN" action Start():
                xalign 0.5
                text_size 24
                text_bold True
                text_color "#1a1a1a"
                xpadding 80
                ypadding 20
                background Solid(kleur) 
                hover_background Solid("#ffffff")

################################################################################
## LABELS OM DE UI OP TE ROEPEN
################################################################################

label the_end:
    hide screen money
    # Groen thema voor succes
    call screen simpel_eindscherm("MISSIE GESLAAGD", "Je hebt de aanvallen afgeslagen en het bedrijf veilig gehouden. NeXioCo kan verder groeien!", "#2ecc71")
    return

label failliet:
    hide screen money
    # Rood thema voor faillissement
    call screen simpel_eindscherm("FAILLIET", "Je hebt het volledige budget verbrand. We kunnen de salarissen niet meer betalen. Je bent ontslagen.", "#e74c3c")
    return

label gehackt:
    hide screen money
    # Rood thema voor gehackt
    call screen simpel_eindscherm("GEHACKT", "Je beveiliging was een gatenkaas. Ransomware heeft alle bestanden versleuteld en het bedrijf verwoest.", "#e74c3c")
    return