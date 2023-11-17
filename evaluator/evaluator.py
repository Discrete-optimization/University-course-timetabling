import pandas as pd
from itertools import chain




class Evaluator:
    def __init__(ev, classrooms, classes, output):
        ev.classrooms = classrooms
        ev.classes = classes
        ev.output = output


    #
    def is_friday(ev):
        friday_ids = []
        for index, row in ev.output.iterrows():
            if row['day'] == 'Friday':
                friday_ids.append(row['id'])

        return friday_ids

    def class_capacity(ev):
        highest_capacity = ev.classrooms['capacity'].max()
        exceeded_capacity_classes = ev.classes[ev.classes['number_of_students'] > highest_capacity]['id']

        return exceeded_capacity_classes.tolist()  # Return the list of class IDs

    #Create a dictionary to store class occurrences by day, time, and classroom
    def repeated_class(ev):

        class_occurrences = {}

        for index, row in ev.output.iterrows():
            day = row['day']
            start_time = row['start']
            end_time = row['end']
            classroom_id = row['classroom_id']
            class_id = row['id']

            # Generate a unique key for each class occurrence based on day, time, and classroom
            occurrence_key = (day, start_time, end_time, classroom_id)

            if occurrence_key in class_occurrences:
                # If it exists, add the class to the list of repeated classes
                class_occurrences[occurrence_key].append(class_id)
            else:
                # If it doesn't exist, create a new list for the key
                class_occurrences[occurrence_key] = [class_id]

        repeated_classes = []

        # Check for occurrences where more than one class has the same day, time, and classroom
        for class_ids in class_occurrences.values():
            if len(class_ids) > 1:
                repeated_classes.extend(class_ids)

        return repeated_classes

    #
    def repeated_profesor(ev):
        return True

    #
    def start_end(ev):
        n = len(ev.output)
        l = []
        for i in range(n-1):
            s = int(ev.output["start"].loc[i].replace(':', ""))
            e = int(ev.output["end"].loc[i].replace(':', ""))
            if(e <= s):
                l.append(ev.output["id"].loc[i])

        return l

    #
    def unit_validation(ev):
        n = len(ev.classes)
        l = []
        for i in range(n-1):
            x = ev.classes["id"].loc[i]
            if(len(ev.output.query("class_id == @x")) < ev.classes["units"].loc[i]):
                l.append(x)
        return l

    #Hanooz kar dare...
    def class_time(ev):
        ev.output['class_length'] = pd.to_datetime(ev.output['end']) - pd.to_datetime(ev.output['start'])
        two_hour_classes = ev.output[(ev.output['class_length'] != pd.Timedelta(hours=2))]['id'].tolist()
        print(two_hour_classes)
        return True

    #
    def class_period(ev):
        return True

    #
    def objective_functio(ev):
        error_logs = []
        """
        Other functions are called in this function
        """
        friday_log = ev.is_friday()
        error_logs.append(friday_log)
        capacity_log = ev.class_capacity()
        error_logs.append(capacity_log)
        repeated_log = ev.repeated_class()
        error_logs.append(repeated_log)
        sn_log = ev.start_end()
        error_logs.append(sn_log)
        unit_log = ev.unit_validation()
        error_logs.append(unit_log)

        error_logs = list(chain.from_iterable(error_logs))
        error_logs = list(dict.fromkeys(error_logs))

        return error_logs

    def progress_percent(ev):
        total = ev.output.shape[0]
        errors = len(ev.objective_functio())

        return 100 * (errors/total)

    def print_progress_percent(ev):

        print("The degree of proximity to the desired answer:")


        pro = ev.progress_percent()
        visual = int(pro/2)
        for i in range(1, 51):
            if(i <= visual):
                print("*", end="")
            else:
                print("-", end="")


        print(" {}%".format(round(pro, 2)))



    # Monitoring
    def monitor_classrooms(ev):
        return (ev.classrooms)

    def monitor_classes(ev):
        return (ev.classes)

    def monitor_output(ev):
        return (ev.output)


"""
data = E1.objective_functio();
df = pd.DataFrame(data)
df.to_excel('out.xlsx', index=False)
"""
