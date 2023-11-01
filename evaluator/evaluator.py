import numpy as np
import pandas as pd

class Evaluator:
    def __init__(ev, classrooms, classes, output):
        ev.classrooms = classrooms
        ev.classes = classes
        ev.output = output
        
    
    #Monitoring
    def monitor_classrooms(ev):
        return(ev.classrooms)
    def monitor_classes(ev):
        return(ev.classes)
    def monitor_output(ev):
        return(ev.output)


#Reading dataset:
Classrooms_df = pd.read_csv('classrooms.csv')
Class_df = pd.read_csv('class.csv')
#reading output:
output_df = pd.read_csv('output.csv')


#Call constructor:
E1 = Evaluator(Classrooms_df, Class_df, output_df)
