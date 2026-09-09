import random
from pyfiglet import Figlet

figlet = Figlet()

fig = figlet.getFonts()

fonts = random.choice(fig)
figlet.setFont(font=fonts)

user = input("Input: ")
print(figlet.renderText(user))

