# Fichier: main.py

def greet(name):
    # La f-string permet d'insérer la variable directement dans le texte
    print(f'Bonjour, {name}!')

if __name__ == "__main__":
    # Ce bloc ne s'exécute que si on lance le fichier directement, pas lors de l'import par le test
    print('Bonjour le monde')
    print('Bienvenue dans notre programme Python')
