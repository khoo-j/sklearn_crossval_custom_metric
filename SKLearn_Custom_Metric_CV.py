'''
This code does not run because there is no supplementary data file

Goal is to demonstrate how to feed a custom scorer into sklearn's cross validate function

To run it, supply your own x & y data for prediction
'''

import kds
import pandas as pd

from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer

from sklearn import tree as skt

def lift_scorer(y_true, y_pred):
    '''
    Function returning lift in top 5 percentile
    
    Args:
    y_true: panda series containing truth labels
    y_pred: panda series containing predicted labels
    
    Returns: Lift score of 5th percentile calculated by kds.metrics
    '''
    lift_table = kds.metrics.decile_table(y_true, y_pred, labels=False, change_deciles = 20)
    return (lift_table.loc[0,'lift'])

custom_cv_metric = make_scorer(lift_scorer, greater_is_better= True)

tree_model = DecisionTreeClassifier(min_samples_leaf = 15)

cv_score = cross_val_score(tree_model, x_data, y_data, cv=10, scoring = custom_cv_metric)

print("%0.3f mean lift in top 5 percentile with a standard deviation of %0.3f" % (cv_score.mean(), cv_score.std()))
