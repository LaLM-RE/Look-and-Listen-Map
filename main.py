intro_text = """
================= Look and Listen Map Fake Demo 1.0 =====================
Willkommen bei der Look and Listen Map.

Dies ist ein Textinterface für Blinde und sehbehinderte Personen zur OpenStreetMap.
Die Look and Listen Map soll eine Möglichkeit bieten, Straßenkarten in Textform zu erkunden.
Du probierst eine unechte Demo aus. Sie soll dazu dienen, einen Eindruck zu vermitteln, wie die echte
Look and Listen Map funktionieren soll, sobald sie fertig programmiert ist.

Es gibt in dieser Demo nur einen kleinen Ausschnitt der Welt, nämlich den Bahnhof in Braunschweig.
Die echte Look and Listen Map wird für die ganze Welt funktionieren, allerdings mit sprachlichen Einschränkungen.

Benutze Deine Tastatur für Texteingabe.
Versuche "hilfe" einzugeben, wenn Du nicht weiter weißt.

"""
print(intro_text)



# Ein "Raum" hat folgende Eigenschaften:
# - Name
# - Erlaubte Richtungen und die Namen der Richtungen (Straßennamen) und deren Zielraum
# - Dort befindliche Objekte




# Ein Objekt hat folgende Eigenschaften
# Objekttyp (Bäckerei, Schnellimbiss, Fahrkartenautomat
# Dimension (Gebäude / Fläche / Strecke / Punkt (Telefonzelle))
# Liste der bekannten Eigenschaften (Name, Öffnungszeiten, )

# Hier werden die Texte definiert
strassenbahn_haltestelle_BS_bahnhof_text="Du befindest Dich an der Straßenbahn-Haltestelle Braunschweig Hauptbahnhof." \
                                         "Die Straßenbahngleise verlaufen von Südwesten nach Nordosten, parallel zu den Bahngleisen." \
                                         "Rund um die Haltestelle verläuft eine einspurige Einbahnstraße wie ein zu einem Oval langgezogener Kreisel für den Busverkehr." \
                                         "Am nordöstlichen Ende der Haltestelle befindet sich ein Leitstreifen, der zum Haupteingang des Hauptbahnhofs Braunschweig führt Richtung Südosten." \
                                         "Südlich befindet sich der Taxistand, der parallel zur Straßenbahnhaltestelle eine weitere langgezogene Straßenschleife für die Taxis bildet."

vor_bahnhof_BS_text="Du befindest Dich vor dem Haupteingang des Braunschweiger Hauptbahnhofs." \
                    "Südwestlich befindet sich ein Stand der Bäckerei Ditsch." \
                    "Östlich ist der Haupteingang des Hauptbahnhofs Braunschweig." \
                    "Nach Südwesten verläuft ein Fußweg zum Taxistand."

taxistand_bahnhof_BS_text="Du befindest Dich am Taxistand vor dem Braunschweiger Hauptbahnhof." \
                     "Ein Fußweg führt nach Nordosten am Bahnhofsgebäude entlang zum Haupteingang des Bahnhofs." \
                     "Nach Südosten führt der Fußweg zur DHL Packstation." \
                     "Nordwestlich von Dir befindet sich die Straßenbahn-Haltestelle Braunschweig Hauptbahnhof."

vorhalle_bahnhof_BS_text="Du befindest Dich in der Vorhalle des Braunschweiger Hauptbahnhofs. " \
                    "Ein Leitstreifen führt nach Osten in den Gang zu den Gleisen." \
                    "Hier befinden sich:" \
                    "-	Ein Euronet Bankautomat" \
                    "-	Ein Reisebank Bankautomat" \
                    "-	Ein Informationsstand der DB" \
                    "-	Ein Verkaufsstand der DB" \
                    "-	Bäckerei Steinicke" \
                    "-	Drogerie Rossman Express"

gleistunnel_bahnhof_BS_text="Du befindest Dich im Tunnel zu den Gleisen im Hauptbahnhof Braunschweig. " \
                       "Nach Südosten befinden sich die Treppen und Aufzüge die nach oben zu den Bahnsteigen führen." \
                       "Am nächsten befindet sich der Aufgang zu Gleis 1 und 2." \
                       "Weiter im Südosten befinden sich die Aufgänge zu den Gleisen mit den höheren Nummern."

Strassenbahn_Leitstreifen_text="Du befindest Dich am nordöstlichen Ende der Straßenbahnhaltestelle Braunschweig Hauptbahnhof." \
                               "Ein taktiler Leitstreifen verläuft nach Osten zum Haupteingang des Bahnhofs."

#---------------------------------------------------------------------------

raum[1]={"id":1, "name":"Straßenbahnhaltestelle", "N":False, "S": False, "O":False,"W":False, "SE": False, "NE":6, "NW":False, "SW": False, "Beschreibung":strassenbahn_haltestelle_BS_bahnhof_text}

raum[2]={"id":2, "name":"Vor dem Bahnhof", "N":False, "S": False, "O":4,"W":False, "SE": False, "NE":False,"NW":False, "SW": 3, "Beschreibung":vor_bahnhof_BS_text}

raum[3]={"id":3, "name":"Taxistand", "N":False, "S": 2, "O":False,"W":False, "SE": False, "NE":2,"NW":False, "SW": False, "Beschreibung":taxistand_bahnhof_BS_text}

raum[4]={"id":4, "name":"Bahnhofsvorhalle", "N":False, "S": False, "O":5,"W":2, "SE": False, "NE":False,"NW":False, "SW": False, "Beschreibung":vorhalle_bahnhof_BS_text}

raum[5]={"id":5, "name":"Tunnel zu den Gleisen", "N":False, "S": False, "O":False,"W":4, "SE": False, "NE":False,"NW":False, "SW": False, "Beschreibung":gleistunnel_bahnhof_BS_text}

raum[6]={"id":6, "name":"Straßenbahn Leitstreifen", "N":False, "S": False, "O":False,"W":False, "SE": False, "NE":False,"NW":False, "SW": 1, "Beschreibung":Strassenbahn_Leitstreifen_text}


#---------------------------------------------------------------------------
beginning_text = strassenbahn_haltestelle_BS_bahnhof_text

print(beginning_text)

next_action = input("> ")

if "walk" in next_action and "walls" in next_action:
    print("You stumble through a door.")
    print("You look around.")
    print("There are some chracked walnut shells lying around in the far corner")

elif "light" in next_action and "turn" in next_action and "on" in next_action:
    text = """
    You now see you are in round room 5x5.
    There are two doors in the room: a north door and a west door.
    There is also a window.
    What do you do?
    """
    print(text)

    while True:
        next_door = input("> ")

        if next_door == "north" or next_door == "n":
            print("You are now in the north room. There are some cracked walnut shells lying around in the far corner.")
        elif "west" in next_door or "w" in next_door:
            print("You've entered the west room.")
            print("In front of you is a tea party.")
            print("Alice, the March Hare and the Mad Hatter are passing cups and pastries around.")
        elif "window" in next_door.split(' '):
            print("You approach the window and look out.")
            print("You are looking upon a small, dimly-lit inner courtyard, 1x1.")
            print("You see clotheslines with the neighbour's laundry hanging on them.")
            print("Apparently, they haven't gotten a single matching pair of socks.")
        elif "south" in next_door.split(' '):
            print("You try to go south.")
        elif "east" in next_door.split(' ') or "e" in next_door.split(' '):
            print("You try to go east.")
        elif "inventory" in next_door.split(' ') or "inv" in next_door.split(' '):
            print("You look into your pockets and you see:...")
        elif "quit" in next_door.split(' ') or "q" in next_door.split(' '):
            print("You quit the game.")
            break
        elif "save" in next_door.split(' ') or "s" in next_door.split(' '):
            print("You want to save the game, but this function does not exist yet.")
        elif "help" in next_door.split(' ') or "h" in next_door.split(' '):
            print("You might try the following:")
            print("Help, inventory, save, quit, north, south, east, west, turn light on, go window")
        else:
            print("I've got no idea what that means. Try ""help"" for a list of commands.")

else:
    print("You stumble around the room in the dark until you starve.")
    print("Game over.")