# Fichier: tests/test_main.py
from main import greet

def test_greet(capsys):
    greet("Alice")
    # Capture la sortie standard (ce qui a été printé)
    captured = capsys.readouterr()
    # Vérifie que la sortie correspond exactement (y compris le saut de ligne \n)
    assert captured.out == "Bonjour, Alice!\n"
