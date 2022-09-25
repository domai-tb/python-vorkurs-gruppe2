import pygame  # importiere die Biblothel PyGame
from random import randint

# Führe die Funktion init() aud er Biblothek pygame aus.
# Die Funktion richtet pygame für uns ein damit wir es nutzen können.
pygame.init()

# --- Klasse Tetromino = Spielsteine definieren -------------------------------


class Tetromino:

    x: int  # x-Koordinate des Steins
    y: int  # y-Koordinate des Steins
    typ: int  # Typ / Form des Steins
    farbe: tuple  # Farbe des Steins als (R, G, B)-Tupel
    rotation: int  # Variante / Rotation des Steins

    # Stelle unsere Blöcke als 4x4 Matrix dar. Da jeder Block gedreht werden kann
    # bekommt jeder Block verschiedene Variationen:
    #
    #          0  1  2  3
    #        _____________
    #        |--|--|--|--|
    #   4    |##|##|##|##|   -> liegendes I (türkis)
    #   8    |--|--|--|--|
    #   12   |--|--|--|--|
    #        ¯¯¯¯¯¯¯¯¯¯¯¯¯
    tetrominos = [
        # I stehnd,    I liegend
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        # J liegend, stehend,  kopf-liegend, kopf-stehend
        [[0, 4, 5, 6],   [1, 2, 5, 9], [1, 5, 9, 8], [4, 5, 6, 10]],
        # L kopf-stehend, kopf-liegend, stehend,      liegend
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        # O -> immer die gleiche Form
        [[1, 2, 5, 6]],
        # S liegend     stehend
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        # T nach oben, nach links    nach unten     nach rechts zeigend
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        # Z liegend, stehend
        [[4, 5, 9, 10], [2, 6, 5, 9]]
    ]

    # Konstruktor aka. wie wird unsere Klasse bei der Erstellung gebaut:
    def __init__(self, xKoordinate, yKoordinate):

        # Attribute x wird auf die eingegebene x-Koordinate gesetzt (x = Spalte)
        self.x = xKoordinate

        # Attribute y wird auf die eingegebene y-Koordinate gesetzt (y = Zeile)
        self.y = yKoordinate

        # Lege den Steintyp zufällig fest
        self.typ = randint(0, len(self.tetrominos)-1)

        # Lege die Farbe des Steins fest
        self.farbe = steinFarben[self.typ]

        # Da wir den Stein rotieren wollen, benötigen wir ein zusätzliches
        # Attribut für die Rotation. Diese legt die Variante des Steins fest.
        self.rotation = 0

    # Gebe und die aktuelle Variante des Steins zurück
    def steinVariante(self):
        # Von den Steinen des jeweiligen Typs, gib uns die Variante der aktuellen
        # Rotation zurück. Also liegend, stehend uws.
        return self.tetrominos[self.typ][self.rotation]

    # Rotiere den Stein -> wechsel durch seine Varianten
    def rotiere(self):
        # Variante ist die nächste in der Liste. Wenn am Ende der Liste gehe
        # wieder zum Anfang -> Modulo Länge der Liste der Varianten des Steins / Typ
        self.rotation = (self.rotation + 1) % len(self.tetrominos[self.typ])

# --- Klasse Tetris definieren -------------------------------------------------


class Tetris:

    höhe: int  # Höhe des Spielfeldes
    breite: int  # Breite des Spielfeldes
    spielfeld: list  # Spielfeld: Matrix breite x höhe
    punkte: int  # Aktuell erreichte Punkte im Spiel
    status: str  # Aktueller Zustand des Spiels: Start, Ende
    aktuellerStein: Tetromino  # Aktuell fallender Tetromino

    # Konstruktor aka. wie wird unsere Klasse bei der Erstellung gebaut:
    def __init__(self, _höhe, _breite):

        # Attribut "höhe" wird auf die eingegebene Höhe gesetzt
        self.höhe = _höhe

        # Attribut "breite" wird auf die eingegebene Breite gesetzt
        self.breite = _breite

        # Definiere ein leeres Spielfeld der Größe breite x höhe
        # Eine -1 steht dafür das sich da kein Stein befindet. Eine Zahl bedeutet das
        # sich an diesem Feld ein Stein befindet. Zu beginn ist unser Feld leer.
        self.spielfeld = [[-1 for i in range(self.breite)]
                          for j in range(self.höhe)]

        # Punkte die der Spieler erreicht hat. Zu Beginn sind diese 0.
        self.punkte = 0

        # Speichere den Zustand unseres Spiels. Am Anfang soll das Spiel starten,
        # aber später soll es auch pausiert und beendet werden können.
        self.status = "start"

        # Erstelle einen neuen Tetromino direkt zu beginn
        self.neuerTetromino()

    # Erstelle einen neuen Stein an der Stelle 3, 0
    def neuerTetromino(self):
        self.aktuellerStein = Tetromino(3, 0)

    # Bewege den Stein ein Feld nach links
    def bewegeSeitwärts(self, richtung):
        # Speichere Alte Position für den Fall das eine Kollision aufgetreten ist
        altePosition = self.aktuellerStein.x

        # Speichere ab ob eine Kante berührt wird
        kanteErreicht = False

        for zeile in range(4):  # Zeilen der 4x4 Matrix des Spielsteins
            for spalte in range(4):  # Spalten der 4x4 Matrix des Spielsteins

                # block = aktuelle position in 4x4 Matrix
                block = zeile * 4 + spalte

                # Wenn die Position in der 4x4 Matrix teil der Variante des
                # aktuell fallenden Steins ist ...
                if block in self.aktuellerStein.steinVariante():

                    # ... und die neue Position innerhalb der Spielfeld-Breite
                    # liegt, dann ..
                    if spalte + self.aktuellerStein.x + richtung > self.breite - 1 or \
                       spalte + self.aktuellerStein.x + richtung < 0:
                        # ... setzte die Variable kanteErreicht auf wahr.
                        kanteErreicht = True

        # Wenn die neue Position des Steines innerhalb des Spielfeldes liegt, dann ...
        if not kanteErreicht:
            # ... verschiebe die x-Kordinate ein Feld nach Links oder Rechts.
            self.aktuellerStein.x += richtung

        # Wenn eine Kollision aufgetreten ist, dann ...
        if self.kollisionsAbfrage():
            # ... setzte die aktuelle Position zurück auf die alte.
            self.aktuellerStein.x = altePosition

    # Bewege den Stein ein Feld nach Unten
    def bewegeUnten(self):

        # Bewege den Stein nach unten
        self.aktuellerStein.y += 1

        # Wenn dabei eine Kollision aufgetreten ist, dann...
        if self.kollisionsAbfrage():
            # ... setzte die y-Koordinate zurück und gehe zum nächsten Stein
            # oder falls das Spiel zu ende ist beende das Spiel.
            self.aktuellerStein.y -= 1
            self.neuerTetrominoOderSpielEnde()

    # Rotiere den Stein
    def rotiere(self):

        # Speichere die vorherige Variante für den Fall das der rotierte
        # Stein außerhalb des Spielfeldes liegt.
        alteVariante = self.aktuellerStein.rotation

        self.aktuellerStein.rotiere()  # Gehe Variante des Steins durch

        # Wenn dabei eine Kollision aufgetreten ist, dann...
        if self.kollisionsAbfrage():
            # setze den Stein auf die alte Variante zurück.
            self.aktuellerStein.rotation = alteVariante

    # Frage ab ob eine Kollision mit anderen Steinen oder dem Spielfeldrand
    # aufgetreten ist.
    def kollisionsAbfrage(self):

        # es ist keine Kollision aufgetreten
        kollision = False

        for zeile in range(4):  # Zeilen der 4x4 Matrix des Spielsteins
            for spalte in range(4):  # Spalten der 4x4 Matrix des Spielsteins

                # block = aktuelle position in 4x4 Matrix
                block = zeile * 4 + spalte

                # Wenn die Position in der 4x4 Matrix teil der Variante des
                # aktuell fallenden Steins ist ...
                if block in self.aktuellerStein.steinVariante():

                    # Beim drehen kann es vorkommen, dass ein Stein aus dem
                    # Spielfeld herraus gedreht wird. Bei der if-Abfrage von
                    # self.spielfeld[i][j] wird dabei ein Index Error auftreten.
                    # Diesen können wir ebenfalls als Kollision interpretieren.
                    try:

                        # und ( der Stein über der maximalen Höhe ODER \
                        #       der Stein unter der minimalen Höhe ODER \
                        #       der Stein über der maximalen Breite ODER \
                        #       der Stein unter der minimalen Breite ODER \
                        #       ein anderer Stein im Weg ist ) dann ...
                        if zeile + self.aktuellerStein.y > self.höhe - 1 or \
                           zeile + self.aktuellerStein.y < 0 or \
                           spalte + self.aktuellerStein.x > self.breite or \
                           spalte + self.aktuellerStein.x < 0 or \
                           self.spielfeld[zeile + self.aktuellerStein.y][spalte + self.aktuellerStein.x] >= 0:
                            # ... setzte kollission auf wahr und ...
                            kollision = True

                    except IndexError:
                        # Wenn ein Spielstein aus dem Spielfeld herrausragt, dann
                        # ist das eine Kollision.
                        kollision = True

        # ... gebe den Wert von kollision zurück.
        return kollision

    # Erstelle einen neuen Spielstein oder beende das Spiel
    def neuerTetrominoOderSpielEnde(self):

        for zeile in range(4):  # Zeilen der 4x4 Matrix des Spielsteins
            for spalte in range(4):  # Spalten der 4x4 Matrix des Spielsteins

                # block = aktuelle position in 4x4 Matrix
                block = zeile * 4 + spalte

                # Wenn die Position in der 4x4 Matrix teil der Variante des
                # aktuell fallenden Steins ist, dann ...
                if block in self.aktuellerStein.steinVariante():
                    # ... trage an die Stelle des Block den Steintypen ein.
                    self.spielfeld[zeile +
                                   self.aktuellerStein.y][spalte + self.aktuellerStein.x] = self.aktuellerStein.typ

        # Wenn der neue Stein "eingerastet" ist, wollen wir die Punkte zählen
        # und gegebenenfalls volle Zeilen löschen.
        self.zählePunkteUndLöscheVolleZeilen()

        # Erstelle einen neuen Stein, da der alte sich nicht mehr bewegt.
        self.neuerTetromino()

        # Wenn der neue Stein direkt kollidiert, dann ist das Spiel zu ende.
        if self.kollisionsAbfrage():
            self.status = 'gameover'

    # Lösche eine Zeile, falls die gesamte Zeile aus Blöcken besteht.
    def zählePunkteUndLöscheVolleZeilen(self):

        # Definiere eine Variable um die vollen Zeile zu zählen
        volleZeilen = 0

        # Für alle Zeilen im Spielfeld, mit Ausnahme der obersten
        for zeile in range(1, self.höhe):

            # Definiere eine Variable um die leeren Felder zu zählen
            leereFelder = 0

            # Für alle Spalten im Spielfeld
            for spalte in range(self.breite):

                # Wenn unser Spielfeld an der Stelle Zeile x Spalte leer ist, dann ...
                if self.spielfeld[zeile][spalte] == -1:
                    # ... zähle unsere Variable leereFelder um eins hoch
                    leereFelder += 1

            # Wenn wir keine leeren Felder in der Zeile haben, dann ...
            if leereFelder == 0:

                # ... erhöhe unsere vollenZeilen um 1 und ...
                volleZeilen += 1

                # ... schiebe alle Zeilen nach unten:
                # Für alle zeilen über der aktuellen zeile ...
                for zeile2 in range(zeile, 1, -1):
                    # gehe alle Spalten durch und...
                    for spalte in range(self.breite):

                        # setzte die aktuelle Zeile auf die Zeile davor.
                        self.spielfeld[zeile2][spalte] = self.spielfeld[zeile2 - 1][spalte]

        # Erhöhe die Punktzahl um die Anzahl der kompletten Zeilen zum Quadrat
        self.punkte += volleZeilen ** 2


# --- Spielfenster erstellen ---------------------------------------------------


# Von der Biblothek pygame, nutze das Modul display und rufe die Funktion auf:
# Setzte die Größe auf 400 x 650
fenster = pygame.display.set_mode(size=(400, 725))

# Setze den Namen des Fensters auf "Tetris"
pygame.display.set_caption("Tetris")

# ---- Variablen definieren ----------------------------------------------------

# Setzte die Frames per Second auf 2. Mit jedem neuen Frame wird sich der
# Tetris-Stein eine Position weiter bewegen.
fps = 2

# Von der Biblothek pygame, nutze des Modul time und erstelle eine Clock()
# -> kontrolliert wann wir unser Spiel als solches aktualisieren
uhr = pygame.time.Clock()

# Farben: Jede Farbe ist ein Tupel aus den Farben (Rot, Grün, Blau)
schwarz = (0, 0, 0)        # alle Farben aus -> schwarz
weis = (255, 255, 255)     # alle Farben an -> weis
grau = (128, 128, 128)

# Tetris Farben der verschiedenen Steine
steinFarben = [
    (0, 240, 240),      # türkis -> ####

    (0, 0, 240),        # blau   -> #
    #                               ###

    (240, 0, 160),      # orange ->   #
    #                               ###

    (240, 240, 0),      # gelb ->  ##
    #                              ##

    (0, 240, 0),        # grün ->   ##
    #                              ##

    (160, 0, 240),      # lila ->   #
    #                              ###

    (240, 0, 0),        # rot -> ##
    #                             ##
]

# Definiere wie breit und wie hoch unser Spielfeld später sein soll
# breite = 10, höhe = 20
breite, höhe = 10, 20

# Definiere unser Spiel als Objekt der Klasse Tetris
game = Tetris(höhe, breite)

# --- Game Loop ----------------------------------------------------------------

# Erstelle die Variable "spielIstZuEnde" und setzte diese auf False
# -> unser Spiel läuft noch
spielIstZuEnde = False

# Game Loop -> Herzstück unseres Spiels
while not spielIstZuEnde:

    # Wenn das Spiel läuft, dann den aktuellen Stein um eins weiter nach unten fallen
    if game.status == 'start':
        game.bewegeUnten()

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
                game.rotiere()

            # Wenn der Benutzer die Pfeiltaste nach unten drückt
            if event.key == pygame.K_DOWN:
                game.bewegeUnten()

            # Wenn der Benutzer die Pfeiltaste nach links drückt
            if event.key == pygame.K_LEFT:
                game.bewegeSeitwärts(-1)  # Links -> x-Achse ins negative

            # Wenn der Benutzer die Pfeiltaste nach rechts drückt
            if event.key == pygame.K_RIGHT:
                game.bewegeSeitwärts(1)  # Rechts -> x-Achse ins positive

    # --- Zeichne unser Fenster mit den Veränderungen neu ----------------------

    fenster.fill(color=weis)    # Fülle unser Fenster mit weiser Farbe

    # Für all unsere Blöcke im Spielfeld...
    for zeile in range(game.höhe):
        for spalte in range(game.breite):
            # wenn Block nicht belegt, dann ...
            if game.spielfeld[zeile][spalte] == -1:
                farbe = grau            # wähle als Farbe grau aus und
                nurRand = 1             # zeichne nur den Rand ein.
            else:                       # Andernfalls ...
                # wähle die Farbe des Blocks
                farbe = steinFarben[game.spielfeld[zeile][spalte]]
                nurRand = 0  # und zeichne das gesamte Feld ein.

            # Zeichne ein Rechteck an der Stelle zeile,  der Größe 30x30 und
            # nimm zum Fensterrand einen Platz von 50.
            pygame.draw \
                  .rect(fenster, farbe, [50+spalte*30, 50+zeile*30, 30, 30], nurRand)

    # Wenn unser Spiel einen aktuellen Stein hat -> dann zeichne diesen ein
    if game.aktuellerStein is not None:
        # Jeder Stein ist 4x4 Felder groß
        for zeile in range(4):                  # Zeile
            for spalte in range(4):             # Spalte

                # block = aktuelle position in 4x4 Matrix
                block = zeile * 4 + spalte

                # Wenn die Position in der 4x4 Matrix teil der Variante des
                # aktuell fallenden Steins ist, dann ...
                if block in game.aktuellerStein.steinVariante():

                    # ... zeichne das Rechteck an der Stelle mit der Farbe
                    # des aktuell an der Position stehenden Steins ein. Die
                    # Koordinaten des Steins ergeben sich dabei aus seiner
                    # (x,y)-Koordinate in bezug zur aktuellen Zeile bzw. Spalte.
                    pygame.draw.rect(fenster, game.aktuellerStein.farbe, [
                                     50+(spalte + game.aktuellerStein.x)*30, 50+(zeile + game.aktuellerStein.y)*30, 30, 30])

    # Definiere uns eine fette Schrift um "Game Over!" einblenden zu können
    gameoverSchrift = pygame.font.SysFont('Arial', 65, bold=True, italic=True)
    gameoverText = gameoverSchrift.render(
        'Game Over!', True, (42, 42, 42))

    if game.status == 'gameover':
        fenster.blit(gameoverText, dest=[10, 250])

    # Definiere uns eine fette Schrift um die Punkte einblenden zu können
    punkteSchrift = pygame.font.SysFont('Arial', 25, bold=True, italic=False)
    punkteText = punkteSchrift.render(
        f'Punkte: {game.punkte}', True, (0, 42, 142))
    fenster.blit(punkteText, dest=[0, 0])

    pygame.display.flip()  # Aktualisiere unser Fenster
    uhr.tick(fps)  # Zähle unsere Uhr um eins hoch

# ------------------------------------------------------------------------------

# Wenn das Spiel zu ende ist, dann beende das Programm und schließe das Fenster
pygame.quit()
