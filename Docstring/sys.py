import sys
if len(sys.argv) < 3:
    print("To few")
elif len(sys.argv) > 3:
    print("To many")
else:
    print("Hello , my name is :", sys.argv[1], sys.argv[2]) # où ils font  "AYENA Roussel" et pas besoin de "sys.argv[2]"
    