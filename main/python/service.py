import sys

from lesson import Lesson
from sensordata import SensorData, read_sensor_data_from_file_as_list


def get_sensor_data_per_lesson(sensor_data, values_per_lesson=90 * 6, values_per_pause=20 * 6):
    lessons = [Lesson()]
    pause_timer = 0

    for sensor_value in sensor_data.sensor_data_list:
        lesson = lessons[len(lessons) - 1]
        if len(lesson) < values_per_lesson:
            lesson.append(sensor_value)
        else:
            if pause_timer < values_per_pause - 1:
                pause_timer += 1
            else:
                lessons.append(Lesson())
                pause_timer = 0

    return lessons


def main(path_to_file, path_to_result):
    sensor_data = SensorData(read_sensor_data_from_file_as_list(path_to_file))
    if sensor_data.is_valid():
        lessons = get_sensor_data_per_lesson(sensor_data)
        file = open(path_to_result, mode="w", encoding="UTF-8")
        file.write(f"Auswertung:")
        lesson_counter = 0
        for lesson in lessons:
            lesson_counter += 1
            file.write(f"\nStunde {lesson_counter}:")
            file.write(lesson.get_result_string())
        file.close()


# Args zum Testen "../resources/co2_daten.txt" "../../result.txt"
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
