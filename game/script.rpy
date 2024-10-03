# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Masha")
define i = Character ("eu")

image piquenique = "piquenique.png"
image bolo = "bolo.jpg"
image farofa = "farofa.png"
image lisasimm = "lisasimm.png"
image forro = "forro.jpg"



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene casinha:
        size (1920, 1080)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show masha
        
    
    # These display lines of dialogue.

    e "oi eu sou a masha, vamos brincar comigo?"

    e "o que voce quer fazer fazer?"
    menu: 
        "brincar no parque":
         jump brincarParque        
        "piquenique na floresta":
         jump piqueniquefloresta

label piqueniquefloresta:
    scene piquenique:
        size (1920, 1080)

    show masha

    e "que legal, por onde comecamos?"
    menu:
        "bolo":
            jump bolo
        "farofa":
            jump farofa
    
    return

label bolo:
    scene bolo:
        size (1920, 1080)

    show lisasimm:
        zoom 1.8

    i "que bolo delicioso"
    e "vamos para outro lugar?"
    menu:
        "sim":
            jump sim
        "nao":
            jump nao

    return

label farofa: 
    scene farofa:
        size (1920, 1080)

    show lisasimm:
        zoom 1.8

    i "que saudades eu estava de comer farofa"
    e "vamos para outro lugar?"
    menu:
        "sim":
            jump sim
        "nao":
            jump nao

    return

label brincarParque:
    e "ops, esta chovendo"
    e "#sad"

    # This ends the game.

    return

label sim:
    scene house:
        size (1920, 1080)
    show masha

    e "para onde iremos?"
    menu:
        "sala de jogos":
                jump saladejogos
        "forro do interior":
            jump forrodointerior

    return
label forrodointerior:
    scene forro:
        size (1920, 1080)
    show masha 
    show lisasimm:
        zoom 1.5

    e "agora chama na bota menino"
    i "isso aqui e bom demais"
    menu: 
        "hora de ir para casa":
            jump casa
    

    return

label saladejogos:
    scene saladejogos:
        size (1920, 1080)
    show masha 

    e "voce quer comecar por qual jogo?"
    menu:
        "sinuca":
            jump sinuca
        "raquetebol":
            jump raquetebol
        "domino":
            jump domino
     
        

    return

label sinuca:
    scene sinuca:
        size (1920, 1080)
    show masha
    show lisasimm

    i "let's go"

    menu:
        "fim":
            jump fim


    return

label raquetebol:
    scene raquetebol:
        size (1920, 1080)
    show lisasimm
    show masha 

    e "let's go"

    menu:
        "fim":
            jump fim


    return

label domino:
    scene domino:
        size (1920, 1080)
    show masha 

    i "let's go"
    menu: 
        "fim":
            jump fim


    return 

label fim:
    scene confete:
        size (1920, 1080)
    show masha 

    e "voce venceu"
    e "obrigada por jogar"

    return 

label casa:
    scene house:
        size (1920,1080)
    show masha

    e " obrigada por jogar"

    return