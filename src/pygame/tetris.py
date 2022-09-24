import time
from turtle import Screen
import pygame  # importiere die Biblothel PyGame

# Führe die Funktion init() aud er Biblothek pygame aus.
# Die Funktion richtet pygame für uns ein damit wir es nutzen können.
pygame.init()


# --- Spielfenster erstellen ---------------------------------------------------

# Von der Biblothek pygame, nutze das Modul display und rufe die Funktion auf:

# Setzte die Größe auf 400 x 650
fenster = pygame.display.set_mode(size=(400, 725))

# Setze den Namen des Fensters auf "Tetris"
pygame.display.set_caption("Tetris")

# ---- Variablen definieren ----------------------------------------------------

# Setzte die Frames per Second auf 25. Mit jedem neuen Frame wird sich der
# Tetris-Stein eine Position weiter bewegen.
fps = 25

# Von der Biblothek pygame, nutze des Modul time und erstelle eine Clock()
# -> kontrolliert wann wir unser Spiel als solches aktualisieren
uhr = pygame.time.Clock()

# Erstelle eine Variable um die Punkte des Spielers zu zählen
score = 0

# Definiere Variablen für den Fall das der Spieler die Pfeiltasten nach unten,
# links oder rechts gedrückt hält.
halteUnten = False
halteLinks = False
halteRechts = False

# Farben: Jede Farbe ist ein Tupel aus den Farben (Rot, Grün, Blau)
schwarz = (0, 0, 0)        # alle Farben aus -> schwarz
weis = (255, 255, 255)     # alle Farben an -> weis
grau = (128, 128, 128)
steinFarben = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]

# Definiere ein leeres Spielfeld der Größe breite x höhe
# Eine 0 steht dafür das sich da kein Stein befindet. Eine 1 bedeutet das sich
# an diesem Feld ein Stein befindet. Zu beginn ist unser Feld leer.
breite, höhe = (10, 20)
spielfeld = [[0 for i in range(breite)] for j in range(höhe)]

# --- Game Loop ----------------------------------------------------------------

# Erstelle die Variable "spielIstZuEnde" und setzte diese auf False
# -> unser Spiel läuft noch
spielIstZuEnde = False

# Game Loop -> Herzstück unseres Spiels
while not spielIstZuEnde:

    # --- Eingaben abfragen ----------------------------------------------------

    # PyGame gibt uns die Möglichkeit z.B. Tastendrücke abzufangen. Diese Events
    # können über die get() Funktion erhalten werden. Um alle Events die vom Spieler
    # verursacht werden auslesen zu können, brauchen wir eine Schleife über alle
    # erfolgten Events.
    for event in pygame.event.get():

        # Jedes Event hat einen Typen, welchen wir abfragen können.

        # Event-Typ ist QUIT -> wir beenden das Spiel
        if event.type == pygame.QUIT:
            spielIstZuEnde = True

        # Event-Typ ist KEYDOWN -> Spieler drückt eine Taste
        if event.type == pygame.KEYDOWN:

            # Wenn der Benutzer die Pfeiltaste nach open drückt
            if event.key == pygame.K_UP:
                pass

            # Wenn der Benutzer die Pfeiltaste nach unten drückt
            if event.key == pygame.K_DOWN:
                halteUnten = True

            # Wenn der Benutzer die Pfeiltaste nach links drückt
            if event.key == pygame.K_LEFT:
                halteLinks = True

            # Wenn der Benutzer die Pfeiltaste nach rechts drückt
            if event.key == pygame.K_RIGHT:
                halteRechts = True

        # Wenn der Spieler die Pfeiltasten gedrückt hat bzw. gedrückt hält.
        if halteUnten:
            pass
        if halteLinks:
            pass
        if halteRechts:
            pass

        # Event-Typ ist KEYUP -> Spieler lässt eine Taste los
        if event.type == pygame.KEYUP:

            # Wenn der Benutzer die Pfeiltaste nach unten loslässt
            if event.key == pygame.K_DOWN:
                halteUnten = False

            # Wenn der Benutzer die Pfeiltaste nach links loslässt
            if event.key == pygame.K_LEFT:
                halteLinks = False

            # Wenn der Benutzer die Pfeiltaste nach rechts loslässt
            if event.key == pygame.K_RIGHT:
                halteRechts = False

    # --- Zeichne unser Fenster mit den Veränderungen neu ----------------------

    fenster.fill(color=weis)    # Fülle unser Fenster mit weiser Farbe

    # Für all unsere Blöcke im Spielfeld...
    for i in range(höhe):
        for j in range(breite):
            if spielfeld[i][j] == 0:    # wenn Block nicht belegt, dann ...
                farbe = grau            # wähle als Farbe grau und
                nurRand = 1             # zeichne nur den Rand ein.
            else:                       # Andernfalls ...
                # wähle die Farbe des Blocks
                farbe = steinFarben[spielfeld[i][j]]
                nurRand = 0  # und zeichne das gesamte Feld ein.

            # Zeichne ein Rechteck an der Stelle j, i der Größe 30x30 und
            # nimm zum Fensterrand einen Platz von 50.
            pygame.draw \
                  .rect(fenster, farbe, [50+j*30, 50+i*30, 30, 30], nurRand)

    pygame.display.flip()  # Aktualisiere unser Fenster
    uhr.tick(fps)    # Zähle unsere Uhr um eins hoch

# ------------------------------------------------------------------------------

# Wenn das Spiel zu ende ist, dann beende das Programm und schließe das Fenster
pygame.quit()
