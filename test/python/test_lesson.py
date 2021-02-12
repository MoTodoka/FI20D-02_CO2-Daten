from unittest import TestCase

from main.python.lesson import *


class TestLesson(TestCase):
    def test_append(self):
        sensor_data_list = [375.000000, 382.944894, 380.331071]
        lesson = Lesson()
        for value in sensor_data_list:
            lesson.append(value)
        self.assertEqual(lesson.sensor_data_list[0], sensor_data_list[0])
        self.assertEqual(lesson.sensor_data_list[1], sensor_data_list[1])
        self.assertEqual(lesson.sensor_data_list[2], sensor_data_list[2])
        self.assertNotEqual(lesson.sensor_data_list[1], sensor_data_list[2])

    def test___len__(self):
        sensor_data_list = [375.000000, 382.944894, 380.331071]
        lesson = Lesson()
        for value in sensor_data_list:
            lesson.append(value)
        expected_result = 3
        actual_result = len(lesson)
        self.assertEqual(expected_result, actual_result)

    def test_get_result(self):
        sensor_data_list = [375.000000, 382.944894, 380.331071]
        lesson = Lesson()
        for value in sensor_data_list:
            lesson.append(value)
        expected_result = (1000, 382.944894, 0.16666666666666666, 0.0, False)
        actual_result = lesson.get_result()
        self.assertEqual(expected_result, actual_result)

    def test_no_warning_get_result_string(self):
        result = (1000, 382.944894, 0.16666666666666666, 0.0, False)
        expected_result = 'Höchstwert 382.944894 wurde erreicht nach 0.16666666666666666 Minuten.\nDer Richtwert ' \
                          '1000ppm wurde bei 0.0% der Messungen überschritten.\n'
        actual_result = get_result_string(result)
        self.assertEqual(expected_result, actual_result)

    def test_warning_get_result_string(self):
        result = (1000, 1375.123456, 1.8, 0.0, True)
        expected_result = 'Höchstwert 1375.123456 wurde erreicht nach 1.8 Minuten.\nDer Richtwert 1000ppm wurde bei ' \
                          '0.0% der Messungen überschritten.\nBitte die Lehrkraft informieren\n'
        actual_result = get_result_string(result)
        self.assertEqual(expected_result, actual_result)

    def test_get_lesson_list(self):
        sensor_data_list = []
        for idx in range(1500):
            sensor_data_list.append(idx)
        lessons = get_lesson_list(sensor_data_list)
        self.assertEqual(lessons[1].sensor_data_list[0], 90 * 6 + 20 * 6)
        self.assertEqual(len(lessons[0]), 90 * 6)


