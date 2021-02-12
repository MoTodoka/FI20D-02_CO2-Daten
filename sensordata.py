import locale


def is_negative(sensor_value):
    return sensor_value < 0


def exceeds_max_value(sensor_value, max_value=1e6):
    return sensor_value > max_value


def read_sensor_data_from_file_as_list(path_to_filename):
    """
    Funktion zum Einlesen eines Sensordatensatzes aus einer *.txt Datei
    :param path_to_filename: Pfad zum Datensatz
    :return: Liste, die die Messwerte aus den Zeilen des Datensatzes als Integer-Zahlen enthält
    """
    file = open(path_to_filename, 'r')
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    file_content_list = [locale.atof(line.strip()) for line in file]
    return file_content_list


class SensorData:
    path_to_filename: str
    sensor_data_list: []

    def __init__(self, path_to_filename):
        self.path_to_filename = path_to_filename
        self.sensor_data_list = read_sensor_data_from_file_as_list(self.path_to_filename)

    def is_valid(self):
        sensor_data_list = self.sensor_data_list
        flag_negative_values = False
        flag_values_too_big = False
        nr_of_invalid_values = 0

        for sensor_value in sensor_data_list:
            if is_negative(sensor_value):
                flag_negative_values = True
                nr_of_invalid_values += 1
            elif exceeds_max_value(sensor_value):
                flag_values_too_big = True
                nr_of_invalid_values += 1
            else:
                continue
        return flag_negative_values, flag_values_too_big, nr_of_invalid_values

    def get_result_string(self):
        flag_negative_values, flag_values_too_big, nr_of_invalid_values = self.is_valid()

        message_string = "Der aus " + self.path_to_filename + " eingelesene Datensatz enthält " \
                         + len(self.sensor_data_list).__str__() + " Messungen, "

        if nr_of_invalid_values == 0:
            message_string += "die alle valide sind.\n"
        else:
            message_string += "von denen " + nr_of_invalid_values.__str__() + " Messung(en) invalide ist (sind).\n"
            if flag_negative_values:
                message_string += "Mindestens ein C02-Messwert in diesem Datensatz ist negativ.\n"
            if flag_values_too_big:
                message_string += "Mindestens ein C02-Messwert in diesem Datensatz überschreitet die Höchstzahl.\n"
            message_string += "Da CO2-Werte in ppm angegeben werden, erscheint der Datensatz fehlerhaft.\n" \
                              "Valide Messwerte bewegen sich ausschließlich im Intervall [0,1e6]."
        return not (flag_negative_values or flag_values_too_big), message_string
