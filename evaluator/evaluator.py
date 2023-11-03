import pandas as pd


class Evaluator:
    def __init__(ev, classrooms, classes, output):
        ev.classrooms = classrooms
        ev.classes = classes
        ev.output = output


    #
    def is_friday(ev):
        friday_ids = []
        for index, row in output_df.iterrows():
            if row['day'] == 'Friday':
                friday_ids.append(row['id'])
        print(friday_ids)
        return True

    #
    def class_capacity(ev):
        return True

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
        return True

    #
    def unit_validation(ev):
        return True

    #
    def class_time(ev):
        output_df['class_length'] = pd.to_datetime(output_df['end']) - pd.to_datetime(output_df['start'])
        two_hour_classes = output_df[(output_df['class_length'] != pd.Timedelta(hours=2))]['id'].tolist()
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
        return error_logs



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
