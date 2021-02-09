def read_sensor_data_from_file_as_list(path_to_filename):
    """
    Funktion zum Einlesen eines Sensordatensatzes aus einer *.txt Datei
    :param path_to_filename: Pfad zum Datensatz
    :return: Liste, die die Messwerte aus den Zeilen des Datensatzes als Integer-Zahlen enthaelt
    """
    # Oeffnen des Datensatzes im read-only-Modus
    file = open(path_to_filename, 'r')
    # Entfernen der Zeilenumbruchszeichen "\n" und Umwandlung der Strings in int
    file_content_list = [int(line.strip()) for line in file]
    # Rueckgabe der Messwert-Liste
    return file_content_list


########################################################################################################################
# Setzen des Pfades zum Datensatz
path_to_data = "./data_0.txt"
# Einlesen der Messdaten als int-Liste
sensor_data = read_sensor_data_from_file_as_list(path_to_data)
# Bestimmen der Messpunktanzahl
number_of_data_points = len(sensor_data)
# Setzen der Kontrollflaggen & der Zaehlvariable nicht valider Messwerte; Anfaengliche Annahme: Daten sind valide
flag_negative_values = False
flag_values_too_big = False
nr_of_invalid_values = 0
# Durchlaufen aller Messwerte zum Ueberpruefen auf Validitaet
for idx in range(number_of_data_points):
    # Falls der aktuelle Messwert < 0: Invalide! Teile pro Million koennen maximal nicht vorhanden sein, aber
    # nicht negativ!
    if sensor_data[idx] < 0:
        # Setzen der zugehoerigen Fehler-Flag
        flag_negative_values = True
        # Erhoehen der Zaehlvariable invalider Werte
        nr_of_invalid_values += 1
    # Falls der aktuelle Messwert > 1e6: Invalide! Maximal eine Million Teile CO2 pro einer Million Teile koennen
    # vorhanden sein!
    elif sensor_data[idx] > 1e6:
        # Setzen der zugehoerigen Fehler-Flag
        flag_values_too_big = True
        # Erhoehen der Zaehlvariable invalider Werte
        nr_of_invalid_values += 1
    # Der aktuelle Messwert bewegt sich im zulaessigen Intervall [0,1e6]
    else:
        # Gehe zur naechsten Iteration und tue nichts.
        continue

# Setze den Ausgabestring stueckweise zusammmen. Zunaechst wird ueber die Anzahl der im Datensatz enthaltenen
# Messwerte informiert.
message_string = "Der aus "+path_to_data+" eingelesene Datensatz enthält "\
                 +number_of_data_points.__str__()+" Messungen, "
# Falls keine invaliden Messungen im Datensatz enthalten sind, wird der Ausgabestring um diese erfreuliche
# Information erweitert.
if nr_of_invalid_values == 0:
    message_string += "die alle valide sind.\n"
# Falls invalide Messwerte im Datensatz vorliegen, sollen entsprechende Informationen ausgegeben werden.
else:
    # Zunaechst wird die Ausgabe um die Anzahl unzulaessiger Messungen erweitert.
    message_string += "von denen "+nr_of_invalid_values.__str__()+" Messung(en) invalide ist (sind).\n"
    # Falls negative Werte in den Daten vorlagen, wird diese Information angefuegt.
    if flag_negative_values:
        message_string += "Mindestens ein C02-Messwert in diesem Datensatz ist negativ.\n"
    # Falls zu hohe Werte in den Daten vorlagen, wird diese Information angefuegt.
    if flag_values_too_big:
        message_string += "Mindestens ein C02-Messwert in diesem Datensatz überschreitet die Höchstzahl.\n"
    # Eine Information ueber das Aussehen valider Messwerte wird als weitere Information angefuegt.
    message_string += "Da CO2-Werte in ppm angegeben werden, erscheint der Datensatz fehlerhaft.\n" \
                      "Valide Messwerte bewegen sich ausschliesslich im Intervall [0,1e6]."
# Ausgeben des Informationsstrings.
print(message_string)
