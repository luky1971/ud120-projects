#!/usr/bin/python

import operator

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    errors = map(operator.sub, predictions, net_worths)
    cleaned_data = zip(ages, net_worths, errors)

    cleaned_data.sort(key=lambda items: items[2]) # sort by error

    return cleaned_data[:int(len(cleaned_data) * 0.9)]

