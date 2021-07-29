import pandas as pd
import matplotlib.pyplot as plt 
import original_data
import Comparisons

data = original_data()
compare = Comparisons()

class visuals:

    def bar_graph(compare):
       return compare.T.plot.bar(rot = 0, figsize = (10,5))