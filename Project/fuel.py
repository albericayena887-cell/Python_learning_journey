def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass  # En cas d'erreur, la boucle while continue


def convert(fraction):
    # Séparation du numérateur et du dénominateur
    if "/" not in fraction:
        raise ValueError
        
    parts = fraction.split("/")
    
    # Vérification que ce sont bien des nombres entiers
    try:
        x = int(parts[0])
        y = int(parts[1])
    except ValueError:
        raise ValueError

    # Règle : Le dénominateur ne peut pas être 0
    if y == 0:
        raise ZeroDivisionError

    # Règle : Le numérateur ne peut pas être supérieur au dénominateur
    if x > y:
        raise ValueError

    # Calcul et arrondi au plus proche
    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()


"""

import pytest
from fuel import convert, gauge

def test_convert_valid():
    # Tests de conversions standards et arrondis
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("1/3") == 33
    assert convert("0/4") == 0
    assert convert("4/4") == 100

def test_convert_errors():
    # Vérification que les bonnes exceptions sont levées (exigé par check50)
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
        
    with pytest.raises(ValueError):
        convert("5/4")  # X > Y
        
    with pytest.raises(ValueError):
        convert("three/four")  # Pas des chiffres

def test_gauge():
    # Vérification de l'affichage textuel de la jauge
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"


"""