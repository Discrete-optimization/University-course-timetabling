import pandas as pd
from RandomGnswerGeneration.RAG import Random_answer_generator
from Evaluator.main import Evaluator
"""
RAG1 = Random_answer_generator(500)
print(RAG1.excel_creator())
"""
# Reading dataset:
Classrooms_df = pd.read_csv('Evaluator/dataset/classrooms.csv')
Class_df = pd.read_csv('Evaluator/dataset/class.csv')
# reading output:
output_df = pd.read_csv('Evaluator/project output/output.csv')

E1 = Evaluator(Classrooms_df, Class_df, output_df)
E1.print_progress_percent()


