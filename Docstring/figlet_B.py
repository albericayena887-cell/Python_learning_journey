import sys
from pyfiglet import Figlet

figlet = Figlet()
available_fonts = figlet.getFonts()

if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    fonts = sys.argv[2]
else:
    sys.exit("Erreur! ")
    
figlet.setFont(font=fonts)    
user = input("Input: ")
print(figlet.renderText(user))  
    
