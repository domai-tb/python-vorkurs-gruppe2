import pygame  # importiere die Boblothek PyGame
from random import randint  # importiere die Funktion randint von der Biblothek random
from time import sleep  # importiere die Funktion sleep von der Biblothek Time

# Führe die Funktion init() aud er Biblothek pygame aus.
# Die Funktion richtet pygame für uns ein damit wir es nutzen können.
pygame.init()

# --- Spielfenster erstellen ---------------------------------------------------

# Von der Biblothek pygame, nutze das Modul display und rufe die Funktion auf:
# Setzte die Größe auf 1080 x 720
breite, höhe = 1080, 720
fenster = pygame.display.set_mode(size=(breite, höhe))

# Setze den Namen des Fensters auf "Snake"
pygame.display.set_caption("Snake")

# ---- Variablen definieren ----------------------------------------------------

# Setzte die Frames per Second auf 2. Mit jedem neuen Frame wird sich der
# Tetris-Stein eine Position weiter bewegen.
fps = 10

# Setzte die Skalierung auf 20 um die Schlange und Früchte in einem Raster
# mit 20x20 großen Feldern zu Platzieren
skalierung = 20

# Von der Biblothek pygame, nutze des Modul time und erstelle eine Clock()
# -> kontrolliert wann wir unser Spiel als solches aktualisieren
uhr = pygame.time.Clock()

# Definiere eine read-only Liste mit den Richtungen in den sich unsere
# Schlange später bewegen können wird.
richtungen = ('OBEN', 'UNTEN', 'LINKS', 'RECHTS')

# Am Anfang soll unsere Schlange nach rechts laufen.
richtung = richtungen[3]

# Definiere uns einen Kopf für die Schlange und einen Körper, welcher an der
# Position des Kopfes anfängt und zwei weitere Felder einnimmt.
snakeKopf = [250, 250]
snakeKörper = [
    [250, 250],     # [x-Koordinate, y-Koordinate]
    [240, 250],
    [230, 250],
]

# Definiere uns eine Frucht zu beginn des Spies. Diese soll zufällig auf
# dem Spielfeld verteielt werden.
frucht = [
    randint(5, ((breite - 2) // skalierung)) * skalierung,  # x-Koordinate
    randint(5, ((höhe - 2) // skalierung)) * skalierung,    # y-Koordinare
]

# Definiere eine Variable für die Punktzahl
punkte = 0


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

            # Wenn der Benutzer die Pfeiltaste nach unten drückt und die
            # Schlange nicht nach unten läuft, dann ...
            if event.key == pygame.K_UP and richtung != richtungen[1]:
                # ... setzte die Richtung auf open.
                richtung = richtungen[0]

            # Wenn der Benutzer die Pfeiltaste nach open drückt und die
            # Schlange nicht nach open läuft, dann ...
            if event.key == pygame.K_DOWN and richtung != richtungen[0]:
                # ... setzte die Richtung auf unten.
                richtung = richtungen[1]

            # Wenn der Benutzer die Pfeiltaste nach rechts drückt und die
            # Schlange nicht nach links läuft, dann ...
            if event.key == pygame.K_RIGHT and richtung != richtungen[2]:
                # ... setzte die Richtung auf rechts.
                richtung = richtungen[3]

            # Wenn der Benutzer die Pfeiltaste nach links drückt und die
            # Schlange nicht nach rechts läuft, dann ...
            if event.key == pygame.K_LEFT and richtung != richtungen[3]:
                # ... setzte die Richtung auf links.
                richtung = richtungen[2]

    # --- Schlange in die vorgegebene Richtung bewegen -------------------------

    # Wenn Rcihtung nach oben ist, dann ...
    if richtung == richtungen[0]:
        # bewege den Kopf der Schlange ein Feld nach oben.
        snakeKopf[1] -= skalierung

    # Wenn Rcihtung nach unten ist, dann ...
    if richtung == richtungen[1]:
        # bewege den Kopf der Schlange ein Feld nach unten.
        snakeKopf[1] += skalierung

    # Wenn Rcihtung nach links ist, dann ...
    if richtung == richtungen[2]:
        # bewege den Kopf der Schlange ein Feld nach links.
        snakeKopf[0] -= skalierung

    # Wenn Rcihtung nach rechts ist, dann ...
    if richtung == richtungen[3]:
        # bewege den Kopf der Schlange ein Feld nach rechts.
        snakeKopf[0] += skalierung

    # Füge dem Körper an der Position 0 den neuen Kopf hinzu
    snakeKörper.insert(0, list(snakeKopf))

    # Wenn der Kopf von Snake weniger als ein Feld (also gleich dem Feld) ist, dann ...
    if abs(snakeKopf[0] - frucht[0]) < skalierung and abs(snakeKopf[1] - frucht[1]) < skalierung:

        # ... erhöhe die Punktzahl um eins und ...
        punkte += 1

        # ... erzeuge eine neue Frucht an zufälligen Koordinaten.
        frucht = [
            randint(5, ((breite-2) // skalierung))*skalierung,  # x-Koordinate
            randint(5, ((höhe-2) // skalierung))*skalierung,  # y-Koordinare
        ]

    # Andernfalls ...
    else:
        # ... entferne das hintere Ende von Snake. Somit hängen wir ein neues
        # Körperteil hinten dran, wenn eine Frucht gefressen wurde. Da sich erstmal
        # nur der Kopf bewegt, muss also das letzte Element des Körpers entfernt
        # werden, wenn sich die Schlange bewegt.
        snakeKörper.pop()

    # --- Zeichne unser Fenster mit den Veränderungen neu ----------------------

    # Fülle unser Fenster mit schwarzer Farbe
    fenster.fill(color=(0, 0, 0))

    # Für jedes Teil des Körpers in snakeKörper (inkl. Kopf) ...
    for körperTeil in snakeKörper:

        # ... zeichne einen grünen Kreis auf dem Fenster, an den Koordinaten
        # des jeweiligen Körperteils mit halber Skalierung.
        pygame.draw.circle(fenster, (0, 255, 0),
                           (körperTeil[0], körperTeil[1]), skalierung / 2)

    # Zeichne ein rotes Rechteck auf dem Fenster, an den Koordinaten
    # des der Frucht mit der ganzen Skalierung.
    pygame.draw.rect(fenster, (255, 0, 0),
                     [frucht[0] - skalierung / 2, frucht[1] - skalierung / 2, skalierung, skalierung])

    # --- Game Over ------------------------------------------------------------

    # Wenn der Kopf von Snake über der maximalen ODER unter der minimalen Breite \
    # ODER wenn der Kopf unter der minimalen ODER über der maximalen Höhe ist, dann...
    if snakeKopf[0] < 0 or snakeKopf[0] > breite - 10 \
       or snakeKopf[1] < 0 or snakeKopf[1] > höhe - 10:
        # ... dann setzte spielIstZuEnde auf wahr.
        spielIstZuEnde = True

    # Für jedes Teil des Körpers in snakeKörper (ohne Kopf) ...
    for körperTeil in snakeKörper[1:]:

        # Wenn der Kopf von Snake gleichen einem seiner Körperteile entspricht, dann ...
        if snakeKopf[0] == körperTeil[0] and snakeKopf[1] == körperTeil[1]:

            # ... hat Snake sich selbst gebissen und das Spiel ist zu ende.
            spielIstZuEnde = True

    if spielIstZuEnde:
        gameoverSchrift = pygame.font.SysFont(
            'Arial', 65, bold=True, italic=True)
        gameoverText = gameoverSchrift.render(
            'Game Over!', True, (42, 42, 42))
        fenster.blit(gameoverText, dest=[breite // 2, höhe // 2])

    # Definiere uns eine fette Schrift um die Punkte einblenden zu können
    punkteSchrift = pygame.font.SysFont('Arial', skalierung * 2)
    punkteText = punkteSchrift.render(
        f'Punkte: {punkte}', True, pygame.Color(255, 255, 255))

    # Zeige den Text an der Stelle 0x0 an.
    fenster.blit(punkteText, dest=[0, 0])

    # Aktualisiere unser Fenster
    pygame.display.flip()

    # Zähle unsere Uhr um eins hoch
    uhr.tick(fps)

    # Warte eine Zentel-Sekunde bevor das Spiel weitergeht -> sonst zu schnell
    sleep(0.1)


# ------------------------------------------------------------------------------

# Wenn das Spiel zu ende ist, dann beende das Programm und schließe das Fenster
# nach 5 Sekunden
sleep(5)
pygame.quit()
