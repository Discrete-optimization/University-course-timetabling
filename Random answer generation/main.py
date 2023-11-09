# Necessary libraries for making random outputs
import numpy as np
import pandas as pd

# We use the following libraries to receive the output in Excel:
import os
import openpyxl



class Random_answer_generator:
    def __init__(self, answer_num):
        self.answer_num = answer_num

    
    """
    It chooses the days of the week for classes randomly.
    Note that the probability of placing on Thursdays and Fridays is less than on other days.
    """
    def randoom_weekday(self):
        week_days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        probabilities = [0.195, 0.19, 0.19, 0.19, 0.19, 0.04, 0.005] #The ratio of the number of classes per day of the week
        arr = np.random.choice(week_days, size=self.answer_num, p=probabilities) #We create a random element according to the number of inputs
        curr_df = pd.DataFrame(arr, columns=['Weekday']) #Convert list to dataframe
        
        return curr_df
        

    def randoom_classroom(self):
        return curr_df


    def randoom_class(self):
        return curr_df
        

    def randoom_time(self):
        return curr_df


    def aggregator(self):
        #call functions:
        week_day = self.randoom_weekday()
        class_room = self.randoom_classroom()
        classes = self.randoom_class()
        time = self.randoom_time()
        
        #combine dataframes:
        result = pd.concat([df1, df2, df3], axis=1, join='inner')

        return result
        

    def excel_creator(self):
        curr_df = self.aggregator()
        curr_df.to_excel('out.xlsx', index=False)


RAG1 = Random_answer_generator(500)
