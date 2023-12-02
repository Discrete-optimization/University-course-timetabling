from operator import mod
from statistics import mode
import pandas as pd
import numpy as np
import pyomo.environ as pyo

class_df = pd.read_csv(
    "E:/projects/University-course-timetabling-main/evaluator/dataset/class.csv")
room_df = pd.read_csv(
    "E:/projects/University-course-timetabling-main/evaluator/dataset/classrooms.csv")

class_list = []
for i in range(len(class_df)):
    class_list.append(class_df["id"].loc[i])

class_room = []
for i in range(len(room_df)):
    class_room.append(room_df["id"].loc[i])

class_times = ['8:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00']
week_days = ['Saturday', 'Sunday', 'Monday',
             'Tuesday', 'Wednesday', 'Thursday']

time_penalty = {'8:00': 2, '10:00': 0, '12:00': 1,
                '14:00': 2, '16:00': 0, '18:00': 2, '20:00': 3}

model = pyo.ConcreteModel()


model.x = pyo.Var(class_list, class_room, week_days,
                  class_times, within=pyo.Binary)


# check if more than one class has been assigned to a room
model.cons1 = pyo.ConstraintList()

for i in week_days:
    for j in class_times:
        for r in class_room:
            model.cons1.add(
                sum(model.x[c, r, i, j] for c in class_list) <= 1)


# check if more than one room has been assigned to a class
model.cons2 = pyo.ConstraintList()

for i in week_days:
    for j in class_times:
        for c in class_list:
            model.cons2.add(
                sum(model.x[c, r, i, j] for r in class_room) <= 1)

# check if a teacher has been assigned to more than one class at a time
model.cons3=pyo.ConstraintList()
c = class_df["Professor_id"].values.tolist()
c=list(dict.fromkeys(c))
a={}
for i in c:
    a[i]=class_df.query("Professor_id == @i")["id"].values.tolist()

def exp3(q,i,j):
    t=0
    for c in a[q]:
        t=t+sum(model.x[c,r,i,j] for r in class_room)
    return t

for i in week_days:
    for j in class_times:
        for q in a:
            model.cons3.add(exp3(q,i,j) <= 1)

# check if the room capacity has been exceeded
model.cons4 = pyo.ConstraintList()


def exp4(c, r):
    t = 0
    for i in week_days:
        for j in class_times:
            t = t+model.x[c, r, i, j]
    return t


for c in class_list:
    for r in class_room:
        num_students = int(class_df.query("id== @c")
                           ["number_of_students"].iloc[0])
        cap = int(room_df.query("id==@r")["capacity"].iloc[0])
        if(num_students >= cap):
            model.cons4.add(exp4(c, r) == 0)


# check if the number units have been met
model.cons5 = pyo.ConstraintList()


def exp5(c):
    t = 0
    for i in week_days:
        for j in class_times:
            for r in class_room:
                t = t+model.x[c, r, i, j]
    return t


for c in class_list:
    units = class_df.query("id==@c")["units"].iloc[0]
    model.cons5.add(exp5(c) == units)


def obj_expression(model):
    t = 0
    for i in week_days:
        for j in class_times:
            for r in class_room:
                for c in class_list:
                    t = t+(model.x[c, r, i, j]*time_penalty[j])

    return t


model.obj = pyo.Objective(expr=obj_expression, sense=pyo.minimize)

opt = pyo.SolverFactory('glpk')

results = opt.solve(model)  # solves and updates model
model.solutions.store_to(results)




results.write()
