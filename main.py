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
strassenbahn_haltestelle_BS_bahnhof_text="Du befindest Dich an der Straßenbahn-Haltestelle Braunschweig Hauptbahnhof.\n" \
                                         "Die Straßenbahngleise verlaufen von Südwesten nach Nordosten, parallel zu den Bahngleisen.\n" \
                                         "Rund um die Haltestelle verläuft eine einspurige Einbahnstraße wie ein zu einem Oval langgezogener Kreisel für den Busverkehr.\n" \
                                         "Am nordöstlichen Ende der Haltestelle befindet sich ein Leitstreifen, der zum Haupteingang des Hauptbahnhofs Braunschweig führt Richtung Südosten.\n" \
                                         "Südlich befindet sich der Taxistand, der parallel zur Straßenbahnhaltestelle eine weitere langgezogene Straßenschleife für die Taxis bildet.\n"

vor_bahnhof_BS_text="Du befindest Dich vor dem Haupteingang des Braunschweiger Hauptbahnhofs.\n" \
                    "Südwestlich befindet sich ein Stand der Bäckerei Ditsch.\n" \
                    "Östlich ist der Haupteingang des Hauptbahnhofs Braunschweig.\n" \
                    "Nach Südwesten verläuft ein Fußweg zum Taxistand.\n"

taxistand_bahnhof_BS_text="Du befindest Dich am Taxistand vor dem Braunschweiger Hauptbahnhof.\n" \
                     "Ein Fußweg führt nach Nordosten am Bahnhofsgebäude entlang zum Haupteingang des Bahnhofs.\n" \
                     "Nach Südosten führt der Fußweg zur DHL Packstation.\n" \
                     "Nordwestlich von Dir befindet sich die Straßenbahn-Haltestelle Braunschweig Hauptbahnhof.\n"

vorhalle_bahnhof_BS_text="Du befindest Dich in der Vorhalle des Braunschweiger Hauptbahnhofs.\n" \
                    "Ein Leitstreifen führt nach Osten in den Gang zu den Gleisen.\n" \
                    "Hier befinden sich:\n" \
                    "-	Ein Euronet Bankautomat\n" \
                    "-	Ein Reisebank Bankautomat\n" \
                    "-	Ein Informationsstand der Deutschen Bahn\n" \
                    "-	Ein Verkaufsstand der Deutschen Bahn\n" \
                    "-	Bäckerei Steinicke\n" \
                    "-	Drogerie Rossman Express\n"

gleistunnel_bahnhof_BS_text="Du befindest Dich im Tunnel zu den Gleisen im Hauptbahnhof Braunschweig.\n" \
                       "Nach Südosten befinden sich die Treppen und Aufzüge die nach oben zu den Bahnsteigen führen.\n" \
                       "Am nächsten befindet sich der Aufgang zu Gleis 1 und 2.\n" \
                       "Weiter im Südosten befinden sich die Aufgänge zu den Gleisen mit den höheren Nummern.\n"

Strassenbahn_Leitstreifen_text="Du befindest Dich am nordöstlichen Ende der Straßenbahnhaltestelle Braunschweig Hauptbahnhof.\n" \
                               "Ein taktiler Leitstreifen verläuft nach Osten zum Haupteingang des Bahnhofs.\n"

richtungen= ("n","s","w","o","nw","no","sw","so")

kommandos=("inventar", "inventory", "inv",
           "help", "hilfe", "h",
           "save", "speichern", "speichere",
           "quit", "ende", "beenden", "q"
           "info", "untersuche", "examine", "look", "schau", "sieh",
           "objekte")

raeume= {
    1: {"id": 1, "name":"Straßenbahnhaltestelle", "n":False, "s": False, "o":False,"w":False, "so": False, "no":6, "nw":False, "sw": False, "Beschreibung":strassenbahn_haltestelle_BS_bahnhof_text},
    2: {"id": 2, "name":"Vor dem Bahnhof", "n":False, "s": False, "o":4,"w":6, "so": False, "no":False,"nw":False, "sw": 3, "Beschreibung":vor_bahnhof_BS_text},
    3: {"id": 3, "name":"Taxistand", "n":False, "s":False, "o":False,"w":False, "so": False, "no":2,"nw":False, "sw": False, "Beschreibung":taxistand_bahnhof_BS_text},
    4: {"id": 4, "name":"Bahnhofsvorhalle", "n":False, "s": False, "o":5,"w":2, "so": False, "no":False,"nw":False, "sw": False, "Beschreibung":vorhalle_bahnhof_BS_text},
    5: {"id": 5, "name":"Tunnel zu den Gleisen", "n":False, "s": False, "o":False,"w":4, "so": False, "no":False,"nw":False, "sw": False, "Beschreibung":gleistunnel_bahnhof_BS_text},
    6: {"id": 6, "name":"Straßenbahn Leitstreifen", "n":False, "s": False, "o":2, "w":False, "so": False, "no":False,"nw":False, "sw": 1, "Beschreibung":Strassenbahn_Leitstreifen_text}
    }

objekte= {
    1: {"name":"fahrkartenautomat", "ort": 4, "beschreibung": "Der rote Fahrkartenautomat ist eingeschaltet. Da ist niemand."},
    2: {"name": "bäckerei", "ort": 2, "beschreibung": "Die Bäckerei heißt Steinicke. Die Öffnungszeiten sind Montags bis Sonntags von 8:00h bis 19:00h."}
    }

objektliste = []

for key in objekte:
    objektliste.append(objekte[key]["name"])

print (objektliste)

# Initialisierung
current_room = 1  # Beginne an der Straßenbahnhaltestelle

# Hauptprogramm

while True:
    print(raeume[current_room]["Beschreibung"])
    print("Du kannst in folgende Richtungen gehen:")
    for richtung in richtungen:
        if not(raeume[current_room][richtung]==False):
            print("-\"" + richtung + "\""+" führt Dich zu "+ "\""+ raeume[raeume[current_room][richtung]]["name"]+ "\"")
            #print(raeume[current_room][richtung])
            #print(raeume[raeume[current_room][richtung]]["name"])


    """ print(raeume[current_room]["n"])
    print(raeume[current_room]["s"])
    print(raeume[current_room]["w"])
    print(raeume[current_room]["o"])
    print(raeume[current_room]["nw"])
    print(raeume[current_room]["no"])
    print(raeume[current_room]["sw"])
    print(raeume[current_room]["so"])"""

    # Benutzereingabe abfragen
    next_action = input("> ")
    next_action = next_action.lower()
    # print(raeume[current_room][next_action])


    if next_action in richtungen:
        # Gehen
        if not raeume[current_room][next_action]==False :
            current_room=raeume[current_room][next_action]
            print("Du bist ein Stück gegangen. \n")
        else:
            print("In diese Richtung führt kein Weg.\n")
    else:
        # Aktionen, die nicht Gehen sind
        print ("Du bist nicht gegangen.")
        # print("Deine Eingabe war:"+ next_action)
        print(f"Deine Eingabe war: {next_action}" )

        if next_action in ("inventar", "inventory", "inv"):
            print("Du guckst in alle Deine Taschen und findest:")
            print("- Dein Handy.")

        elif next_action in ("save", "speichern", "speichere"):
            print("Du möchtest speichern:")
            print("Eine solche Funktion ist leider noch nicht implementiert.")

        elif next_action in ("hilfe", "help", "h"):
            print("\nDu möchtest Hilfe:")
            print("Versuche eine Himmelsrichtung einzugeben, um in diese Richtung zu gehen z.b. N, NO, S, SW\n")
            print("Ich verstehe folgende Kommandos:")
            print(kommandos)
            print("\nDu brauchst keine Großbuchstaben zu benutzen.\n")

        elif next_action in ("objekte"):
            print("Hier befinden sich folgende Objekte:")

            for key in objekte :
                number_of_objects=0
                if objekte[key]["ort"]==current_room :
                    print("-" + objekte[key]["name"])
                    number_of_objects= number_of_objects+1
            if number_of_objects ==0 :
                print("keine.")
            print(" ")

        elif next_action in ("info", "untersuche", "examine", "look", "schau", "sieh"):
            print("Du möchtest etwas untersuchen. Was?")
            next_object = input(": ")
            if next_object.lower() in (objektliste):
                print("Ich habe Dein Objekt \"" + next_object + "\" erkannt.")
                current_object = None

                for key in objekte:
                    if objekte[key]["name"] == next_object:
                        current_location = objekte[key]["ort"]
                        current_object=key
                        break

                #print(Das Objekt "+" next_object + " befindet sich am Ort " + current_location)
                print("Du bist gerade am Ort \""+ raeume[current_room]["name"] + "\".")
                if not current_location == current_room:
                    print("Dein Objekt ist nicht hier.")
                else:
                    print("Dein Objekt ist hier.")
                    #print(current_object)
                    #print(objekte[current_object])
                    print(objekte[current_object]["beschreibung"])

                print(" ")
            else:
                print("Ich habe Dein Objekt nicht erkannt. Ich kenne folgende Objekte:")
                print (objekte)
                print(" ")

        elif next_action in ("ende", "quit", "q", "beenden"):
            print("Du möchtest den Dialog beenden. Vielen Dank für die Benutzung der Look-and-Listen-Map. Tschüss, bis zum nächsten Mal!")
            break # while Schleife verlassen und damit das Programm beenden
        else:
            print("Ich habe Dich nicht verstanden. Versuche \"hilfe\", um eine Liste von Kommandos zu erhalten.")


# Ende While-Schleife
"""elif "quit" in next_door.split(' ') or "q" in next_door.split(' '):
print("You quit the game.")
break
elif "save" in next_door.split(' ') or "s" in next_door.split(' '):
print("You want to save the game, but this function does not exist yet.")
elif "help" in next_door.split(' ') or "h" in next_door.split(' '):
print("You might try the following:")
print("Help, inventory, save, quit, north, south, east, west, turn light on, go window")
else:
print("I've got no idea what that means. Try ""help"" for a list of commands.")
    next_door = input("> ")
    elif "inventory" in next_door.split(' ') or "inv" in next_door.split(' '):
        print("You look into your pockets and you see:...")
    
"""
