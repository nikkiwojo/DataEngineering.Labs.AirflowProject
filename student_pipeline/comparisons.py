import pandas as pd
import original_data

class Comparisons:

    def genderCompare(data):
        fmath = data.loc[data['gender'] == 'female', 'math score'].mean()
        mmath = data.loc[data['gender'] == 'male', 'math score'].mean()

        freading = data.loc[data['gender'] == 'female', 'reading score'].mean()
        mreading = data.loc[data['gender'] == 'male', 'reading score'].mean()

        fwriting = data.loc[data['gender'] == 'female', 'writing score'].mean()
        mwriting = data.loc[data['gender'] == 'female', 'writing score'].mean()

        gender_info = {'Average Math Scores':[fmath, mmath], 'Average Reading Scores':[freading, mreading], 'Average Writing Scores':[fwriting, mwriting]}
        return pd.DataFrame(gender_info, index =['Female', 'Male']).round(2)

    def groupCompare(data);

        groupA_math = data.loc[data['race/ethnicity'] == 'group A', 'math score'].mean()
        groupB_math = data.loc[data['race/ethnicity'] == 'group B', 'math score'].mean()
        groupC_math = data.loc[data['race/ethnicity'] == 'group C', 'math score'].mean()
        groupD_math = data.loc[data['race/ethnicity'] == 'group D', 'math score'].mean()
        roupE_math = data.loc[data['race/ethnicity'] == 'group E', 'math score'].mean()

        groupA_reading = data.loc[data['race/ethnicity'] == 'group A', 'reading score'].mean()
        groupB_reading = data.loc[data['race/ethnicity'] == 'group B', 'reading score'].mean()
        groupC_reading = data.loc[data['race/ethnicity'] == 'group C', 'reading score'].mean()
        groupD_reading = data.loc[data['race/ethnicity'] == 'group D', 'reading score'].mean()
        groupE_reading = data.loc[data['race/ethnicity'] == 'group E', 'reading score'].mean()

        groupA_writing = data.loc[data['race/ethnicity'] == 'group A', 'writing score'].mean()
        groupB_writing = data.loc[data['race/ethnicity'] == 'group B', 'writing score'].mean()
        groupC_writing = data.loc[data['race/ethnicity'] == 'group C', 'writing score'].mean()
        groupD_writing = data.loc[data['race/ethnicity'] == 'group D', 'writing score'].mean()
        groupE_writing = data.loc[data['race/ethnicity'] == 'group E', 'writing score'].mean()

        grouping_info = {'Average Math Scores':[groupA_math, groupB_math, groupC_math, groupD_math, groupE_math],
                'Average Reading Scores': [groupA_reading, groupB_reading, groupC_reading, groupD_reading, groupE_reading],
                'Average Writing Scores':[groupA_writing, groupB_writing, groupC_writing, groupD_writing, groupE_writing]}

        groupCompare = pd.DataFrame(grouping_info, index = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E'])
        return groupCompare.round(2)

    def parentsCompare(data):

        cM = data.loc[data['parental level of education'] == 'some college', 'math score'].mean()
        aM = data.loc[data['parental level of education'] == "associate's degree", 'math score'].mean()
        hM = data.loc[data['parental level of education'] == 'high school', 'math score'].mean()
        someM = data.loc[data['parental level of education'] == 'some high school', 'math score'].mean()
        bM = data.loc[data['parental level of education'] == "bachelor's degree", 'math score'].mean()
        mM = data.loc[data['parental level of education'] == "master's degree", 'math score'].mean()

        cR = data.loc[data['parental level of education'] == 'some college', 'reading score'].mean()
        aR = data.loc[data['parental level of education'] == "associate's degree", 'reading score'].mean()
        hR = data.loc[data['parental level of education'] == 'high school', 'reading score'].mean()
        someR = data.loc[data['parental level of education'] == 'some high school', 'reading score'].mean()
        bR = data.loc[data['parental level of education'] == "bachelor's degree", 'reading score'].mean()
        mR = data.loc[data['parental level of education'] == "master's degree", 'reading score'].mean()

        cW = data.loc[data['parental level of education'] == 'some college', 'writing score'].mean()
        aW = data.loc[data['parental level of education'] == "associate's degree", 'writing score'].mean()
        hW = data.loc[data['parental level of education'] == 'high school', 'writing score'].mean()
        someW = data.loc[data['parental level of education'] == 'some high school', 'writing score'].mean()
        bW = data.loc[data['parental level of education'] == "bachelor's degree", 'writing score'].mean()
        mW = data.loc[data['parental level of education'] == "master's degree", 'writing score'].mean()

        parents_info = {'Average Math Scores':[someM, hM, cM, aM, bM, mM], 'Average Reading Scores':[someR, hR, cR, aR, bR, mR],
               'Average Writing Scores':[someW, hW, cW, aW, bW, mW]}
        parentsCompare = pd.DataFrame(parents_info, index = ['Some High School', "High School", 'Some College',
                                                    "Associate's Degree", "Bachelor's Degree", "Master's Degree"])
        return parentsCompare.round(2)

    def lunchCompare(data): 

        freeM = data.loc[data['lunch'] == 'free/reduced', 'math score'].mean()
        standM = data.loc[data['lunch'] == 'standard', 'math score'].mean()

        freeR = data.loc[data['lunch'] == 'free/reduced', 'reading score'].mean()
        standR = data.loc[data['lunch'] == 'standard', 'reading score'].mean()

        freeW = data.loc[data['lunch'] == 'free/reduced', 'writing score'].mean()
        standW = data.loc[data['lunch'] == 'standard', 'writing score'].mean()

        lunch_info = {'Average Math Scores':[freeM, standM], 'Average Reading Scores':[freeR, standR], 
              'Writing Scores':[freeW, standW]}
        lunchCompare = pd.DataFrame(lunch_info, index = ['Free/Reduced', 'Standard'])
        
        eturn lunchCompare.round(2)

    def prepCompare(data):
        
        noM = data.loc[data['test preparation course'] == 'none', 'math score'].mean()
        yesM = data.loc[data['test preparation course'] == 'completed', 'math score'].mean()

        noR = data.loc[data['test preparation course'] == 'none', 'reading score'].mean()
        yesR = data.loc[data['test preparation course'] == 'completed', 'reading score'].mean()

        noW = data.loc[data['test preparation course'] == 'none', 'writing score'].mean()
        yesW = data.loc[data['test preparation course'] == 'completed', 'writing score'].mean()

        prep_info = {'Average Math Scores':[yesM, noM], 'Average Reading Scores':[yesR, noR], 'Average Writing Scores':[yesW, noW]}
        prepCompare = pd.DataFrame(prep_info, index = ['Test Prep Course', 'None'])
        return prepCompare.round(2)

