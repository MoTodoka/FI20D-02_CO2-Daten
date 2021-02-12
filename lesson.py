class Lesson:
    sensor_data_list: list

    def __init__(self):
        self.sensor_data_list = []

    def __len__(self):
        return len(self.sensor_data_list)

    def append(self, sensor_value):
        self.sensor_data_list.append(sensor_value)

    def get_result(self, critical_value=1000, critical_minutes=3, values_per_minute=6):
        max_value = 0
        max_index = 0
        over_limit_counter = 0

        for idx in range(len(self.sensor_data_list)):
            if self.sensor_data_list[idx] > max_value:
                max_value = self.sensor_data_list[idx]
                max_index = idx
            if self.sensor_data_list[idx] > critical_value:
                over_limit_counter += 1
        time_of_max_value_in_minutes = max_index / values_per_minute
        percentage = over_limit_counter / len(self.sensor_data_list) * 100
        warn_teacher = over_limit_counter > critical_minutes * values_per_minute

        return critical_value, max_value, time_of_max_value_in_minutes, percentage, warn_teacher

    def get_result_string(self):
        critical_value, max_value, time_of_max_value_in_minutes, percentage, warn_teacher = self.get_result()
        result = f"Höchstwert {max_value} wurde erreicht nach {time_of_max_value_in_minutes} Minuten.\n"
        result += f"Der Richtwert {critical_value}ppm wurde bei {percentage}% der Messungen überschritten.\n"
        if warn_teacher:
            result += f"Bitte die Lehrkraft informieren\n"
        return result
