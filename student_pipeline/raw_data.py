import pandas as pd 

class original_data:

    def load_raw_data():
        studentData = pd.read_csv('StudentsPerformance.csv')
        data = pd.DataFrame(studentData)
        return data

    def summary_stats(data_set):
        return data_set.describe()

    def total_gender(data_set):
        return data_set['gender'].value_counts()

    def total_groups(data_set):
        return data_set['race/ethnicity'].value_counts()

    def total_parentEd(data_set):
        return data_set['parental level of education'].value_counts()

    def total_prep(data_set):
        return data_set['test preparation course'].value_counts()