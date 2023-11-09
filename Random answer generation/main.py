import numpy as np

week_days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
probabilities = [0.195, 0.19, 0.19, 0.19, 0.19, 0.04, 0.005]

arr = np.random.choice(week_days, size=500, p=probabilities)
for wd in week_days:
    rep = len(arr[arr == wd])
    print("number of {} is : {}".format(wd, rep))
