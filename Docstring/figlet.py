import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
available_fonts = figlet.getFonts()

# 1. Vérification des arguments de la ligne de commande
if len(sys.argv) == 1:
    # Aucun argument : choix d'une police au hasard
    selected_font = random.choice(available_fonts)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    # Deux arguments avec le bon drapeau
    selected_font = sys.argv[2]
    # Vérification si la police existe
    if selected_font not in available_fonts:
        sys.exit("Invalid usage")
else:
    # Mauvais arguments ou mauvais drapeau
    sys.exit("Invalid usage")

# 2. Configuration de la police
figlet.setFont(font=selected_font)

# 3. Récupération et conversion du texte
user_input = input("Input: ")
print(figlet.renderText(user_input))
