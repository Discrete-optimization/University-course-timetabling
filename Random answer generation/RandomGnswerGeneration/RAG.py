# Necessary libraries for making random outputs
import numpy as np
import pandas as pd

# We use the following libraries to receive the output in Excel:
import os
import openpyxl

from datetime import datetime

class Random_answer_generator:
    def __init__(self, answer_num):
        self.answer_num = answer_num

    """
    It chooses the days of the week for classes randomly.
    Note that the probability of placing on Thursdays and Fridays is less than on other days.
    """

    def randoom_weekday(self):
        week_days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        probabilities = [0.195, 0.19, 0.19, 0.19, 0.19, 0.04,
                         0.005]  # The ratio of the number of classes per day of the week
        arr = np.random.choice(week_days, size=self.answer_num,
                               p=probabilities)  # We create a random element according to the number of inputs
        curr_df = pd.DataFrame(arr, columns=['Weekday'])  # Convert list to dataframe

        return curr_df

    def randoom_classroom(self):
        classroom_types = ['Course', 'Lab', 'Seminar']
        probabilities = [0.5, 0.3, 0.2]
        classroom_type_arr = np.random.choice(classroom_types, size=self.answer_num, p=probabilities)
        curr_df = pd.DataFrame({'type': classroom_type_arr})

        return curr_df

    def randoom_class(self):
        class_id = []
        for i in range(29):
            class_id.append(i + 1)

        # probability for each class is proportional to the number of its unit
        probabilities = [0.029850746268656716, 0.04477611940298507, 0.05970149253731343, 0.04477611940298507,
                         0.014925373134328358, 0.029850746268656716, 0.029850746268656716, 0.029850746268656716,
                         0.029850746268656716, 0.05970149253731343,
                         0.04477611940298507, 0.029850746268656716, 0.05970149253731343, 0.05970149253731343,
                         0.029850746268656716, 0.04477611940298507,
                         0.014925373134328358, 0.04477611940298507, 0.014925373134328358,
                         0.029850746268656716, 0.029850746268656716, 0.029850746268656716, 0.014925373134328358,
                         0.014925373134328358, 0.029850746268656716, 0.014925373134328358, 0.05970149253731343,
                         0.04477611940298507, 0.014925373134328358]

        arr = np.random.choice(class_id, size=self.answer_num, p=probabilities)
        curr_df = pd.DataFrame(arr, columns=['class_id'])  # Convert list to dataframe
        return curr_df

    def random_times(self):
        class_times = ['8:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00']
        probabilities = [0.1, 0.2, 0.2, 0.2, 0.2, 0.05, 0.05]  # Ratio of the number of classes per hour of the day
        arr = np.random.choice(class_times, size=self.answer_num, p=probabilities)
        curr_df = pd.DataFrame(arr, columns=['start'])

        return curr_df

    def aggregator(self):
        # call functions:
        week_day = self.randoom_weekday()
        time = self.random_times()
        class_room = self.randoom_classroom()
        classes = self.randoom_class()

        # combine dataframes:
        result = pd.concat([week_day, class_room, classes, time], axis=1, join='inner')

        return result

    def excel_creator(self):
        curr_df = self.aggregator()
        time_now = datetime.now()
        current_time = time_now.strftime("%Y-%m-%d_%H-%M-%S")
        path = "RandomGnswerGeneration/answers/" + current_time + ".xlsx"
        curr_df.to_excel(path, index=False)
        print("file {} created successfuly!".format(path))
