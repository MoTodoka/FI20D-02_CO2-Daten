from unittest import TestCase

from main.python.sensordata import *


class TestSensordata(TestCase):
    def test_read_sensor_data_from_file_as_list(self):
        expected_result = 436.084900
        sensor_data_list = read_sensor_data_from_file_as_list("../resources/co2_daten.txt")
        actual_result = sensor_data_list[9]

        self.assertEqual(actual_result, expected_result)

    def test_is_negative(self):
        self.assertTrue(is_negative(-3), "Eingabe: Negativer Wert")
        self.assertFalse(is_negative(0), "Eingabe: Zero")
        self.assertFalse(is_negative(-0), "Eingabe: Negativ-Zero")
        self.assertFalse(is_negative(3), "Eingabe: Positiver Wert")

    def test_exceeds_max_value(self):
        limit = 1e6
        self.assertTrue(exceeds_max_value(limit + 1), "Eingabe: Über dem Limit")
        self.assertFalse(exceeds_max_value(limit), "Eingabe: Das Limit")
        self.assertFalse(exceeds_max_value(limit - 1), "Eingabe: Unter dem Limit")
        self.assertFalse(exceeds_max_value(0), "Eingabe: Zero")
        self.assertFalse(exceeds_max_value(-0), "Eingabe: Negativ-Zero")
        self.assertFalse(exceeds_max_value(-limit), "Eingabe: Limit als negativer Wert")
        self.assertFalse(exceeds_max_value(-(limit + 1)), "Eingabe: Über dem Limit als negativer Wert")

    def test___init__(self):
        sensor_data_list = [375.000000, 382.944894, 380.331071]
        sensor_data = SensorData(sensor_data_list)
        self.assertEqual(sensor_data.sensor_data_list[0], sensor_data_list[0])
        self.assertEqual(sensor_data.sensor_data_list[1], sensor_data_list[1])
        self.assertEqual(sensor_data.sensor_data_list[2], sensor_data_list[2])
        self.assertNotEqual(sensor_data.sensor_data_list[1], sensor_data_list[2])

    def test_positive_is_valid(self):
        sensor_data_list = [375.000000, 382.944894, 380.331071]
        sensor_data = SensorData(sensor_data_list)
        expected_result = (False, False, 0)
        actual_result = sensor_data.is_valid()
        self.assertTupleEqual(actual_result, expected_result)

    def test_negative_is_valid(self):
        sensor_data_list = [375.000000, 382.944894, 380.331071]
        sensor_data = SensorData(sensor_data_list)
        sensor_data.path_to_filename = "Test-Path"
        expected_result = (True, 'Der aus Test-Path eingelesene Datensatz enthält 3 Messungen, die alle valide sind.\n')
        actual_result = sensor_data.get_result_string()
        self.assertTupleEqual(actual_result, expected_result)

    def test_positive_get_result_string(self):
        sensor_data_list = [-375.000000, 382944894, 380.331071]
        sensor_data = SensorData(sensor_data_list)
        sensor_data.path_to_filename = "Test-Path"
        expected_result = (False, 'Der aus Test-Path eingelesene Datensatz enthält 3 Messungen, von denen 2 Messung('
                                  'en) invalide ist (sind).\nMindestens ein C02-Messwert in diesem Datensatz ist '
                                  'negativ.\nMindestens ein C02-Messwert in diesem Datensatz überschreitet die '
                                  'Höchstzahl.\nDa CO2-Werte in ppm angegeben werden, erscheint der Datensatz '
                                  'fehlerhaft.\nValide Messwerte bewegen sich ausschließlich im Intervall [0,1e6].')
        actual_result = sensor_data.get_result_string()
        self.assertTupleEqual(actual_result, expected_result)
