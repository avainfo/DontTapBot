# Bot for DontTap

Sommaire / Table of Contents

* Bot for DontTap <img src="https://cdn-icons-png.flaticon.com/512/555/555526.png" width="15"/>
  * [Description](#description)
  * [How It Works](#how-it-works)
  * [Configuration](#configuration)
  * [How to Use](#how-to-use)
  * [Disclaimer](#disclaimer)
  * [Author](#author)
  * [License](#license)

* Bot pour DontTap <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Flag_of_France.svg/1280px-Flag_of_France.svg.png" width="15"/>
  * [Description](#description-1)
  * [Comment ça fonctionne](#comment-ça-fonctionne)
  * [Configuration](#configuration-1)
  * [Comment l'utiliser](#comment-lutiliser)
  * [Avertissement](#avertissement)
  * [Auteur](#auteur)
  * [Licence](#licence)

## Description

This project is a bot that automates the game WhiteTile2 (available on [donttap.com](https://donttap.com)) by automatically clicking on the black squares on the screen.

## How It Works

The bot utilizes the following Python libraries:
- [`win32api`](https://pypi.org/project/pywin32/) to move and click the mouse.
- [`PIL`](https://pypi.org/project/Pillow/) to capture screenshots.
- [`pynput`](https://pypi.org/project/pynput/) to detect mouse clicks by the user.

The bot operates as follows:
1. Waits for the user to click the button to start the game.
2. Detects the location of the black squares on the screen.
3. Automatically clicks on the black squares.

## Configuration

- `SCREEN_X` and `SCREEN_Y` are the coordinates of the screen where the grid is located.
- `CELL_SIZE` is the size of each square.
- `DELAY_BETWEEN_READS` is the delay between screen readings to detect the start of the game.

## How to Use

1. Ensure that Python is installed on your system.
2. Install the dependencies by running:
   - `pip install pywin32`
   - `pip install Pillow`
   - `pip install pynput`
3. Clone this repository.
4. Run `dot_tap_bot.py` to start the bot.
5. Begin a game by clicking a start button to initiate the game.

## Disclaimer

This bot was created for educational and demonstration purposes. The use of automated bots in games may violate the game's terms of use. Use this bot at your own risk.

## Author

[Ava Info Conseils](https://github.com/avainfo) - [LinkedIn](https://www.linkedin.com/in/antonin-do-souto-418623207/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.

---

## Description

Ce projet est un bot qui automatise le jeu WhiteTile2 (disponible sur [donttap.com](https://donttap.com)) en cliquant automatiquement sur les carrés noirs à l'écran.

## Comment ça fonctionne

Le bot utilise les bibliothèques Python suivantes :
- [`win32api`](https://pypi.org/project/pywin32/) pour déplacer et cliquer la souris.
- [`PIL`](https://pypi.org/project/Pillow/) pour capturer des captures d'écran.
- [`pynput`](https://pypi.org/project/pynput/) pour détecter les clics de souris de l'utilisateur.

Le bot fonctionne de la manière suivante :
1. Attend que l'utilisateur clique sur le bouton pour lancer la partie.
2. Détecte l'emplacement des carrés noirs sur l'écran.
3. Clique automatiquement sur les carrés noirs.

## Configuration

- `SCREEN_X` et `SCREEN_Y` sont les coordonnées de l'écran où se trouve la grille sur l'écran.
- `CELL_SIZE` est la taille de chaque carré.
- `DELAY_BETWEEN_READS` est le délai entre les lectures de l'écran pour détecter le début du jeu.

## Comment l'utiliser

1. Assurez-vous que Python est installé sur votre système.
2. Installez les dépendances en exécutant :
   - `pip install pywin32`
   - `pip install Pillow`
   - `pip install pynput`
3. Clonez ce répertoire.
4. Exécutez `dot_tap_bot.py` pour lancer le bot.
5. Commencez une partie en cliquant sur un bouton pour démarrer la partie.

## Avertissement

Ce bot a été créé à des fins éducatives et de démonstration. L'utilisation de bots automatisés dans des jeux peut violer les conditions d'utilisation du jeu. Utilisez ce bot à vos propres risques.

## Auteur

[Ava Info Conseils](https://github.com/avainfo) - [LinkedIn](https://www.linkedin.com/in/antonin-do-souto-418623207/)

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.