import pandas as pd


class Evaluator:
    def __init__(ev, classrooms, classes, output):
        ev.classrooms = classrooms
        ev.classes = classes
        ev.output = output



    def is_friday(ev):
        return(True)

    def class_capacity(ev):
        return (True)

    def repeated_class(ev):
        return (True)

    def repeated_profesor(ev):
        return (True)

    def start_end(ev):
        return (True)

    def unit_validation(ev):
        return (True)

    def class_time(ev):
        return (True)

    def class_period(ev):
        return (True)



    # Monitoring
    def monitor_classrooms(ev):
        return (ev.classrooms)

    def monitor_classes(ev):
        return (ev.classes)

    def monitor_output(ev):
        return (ev.output)


# Reading dataset:
Classrooms_df = pd.read_csv('dataset/classrooms.csv')
Class_df = pd.read_csv('dataset/class.csv')
# reading output:
output_df = pd.read_csv('project output/output.csv')

# Call constructor:
E1 = Evaluator(Classrooms_df, Class_df, output_df)
print(E1.monitor_output())
