import sys

from lesson import get_result_string, get_lesson_list
from sensordata import SensorData, read_sensor_data_from_file_as_list


def main(path_to_file, path_to_result):
    sensor_data = SensorData(read_sensor_data_from_file_as_list(path_to_file))
    if sensor_data.is_valid():
        lessons = get_lesson_list(sensor_data.sensor_data_list)
        file = open(path_to_result, mode="w", encoding="UTF-8")
        file.write(f"Auswertung:")
        lesson_counter = 0
        for lesson in lessons:
            lesson_counter += 1
            file.write(f"\nStunde {lesson_counter}:")
            file.write(get_result_string(lesson.get_result()))
        file.close()


# Args zum Testen "../resources/co2_daten.txt" "../../result.txt"
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
