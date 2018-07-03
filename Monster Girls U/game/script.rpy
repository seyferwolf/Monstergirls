# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define centaur = Character("Cindy")
init:
    image special_background:
        "space_bg.jpg"
        zoom 2.5

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene special_background

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show cindy_test

    # These display lines of dialogue.

    centaur "Howdy newcomer, welcome to the campus."

    centaur "I'm the first character ever made for this project, forget about that there hussy wolf bitch."

    # This ends the game.

    return
