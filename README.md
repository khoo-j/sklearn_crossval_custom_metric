# Using a custom metric for cross validation in sklearn

Brief: Sample code file demonstrates how to use sklearn's make_scorer to create your own metric.

#### Lenghty example:

Suppose we're trying to classify online purchasers vs non-purchasers from total website visitors. There is a heavy class imbalance here: with > 90% being non-purchasing website visitors. If one were to use accuracy to score this classifier, one would get a stunning accuracy of 90% if the classifier simply predicts everyone does not purchase! However, it defeats the point of creating a classifier.

This is where lift makes more sense: We get our classifier to arrange all website visitors by most likely to purchase to least likely, then we compare that against randomly arranged visitors. Lift is thus the difference between classifier's prediction vs randomly arranged: we could then study how good is our classifier up to the n-th decile of the dataset, when compared against randomly classifying a website visitor. This arrangement is typically done by decile, but can be broken down into further granularity.

The issue here is: on its own, sklearn's cross validate is not able to provide scores by lift. 

In this sample code file, sklearn cross validate is fed with a custom lift scoring function. Additionally, decile is broken down into bins of 5 percentile: 0-5 percentile, 5-10 percentile, etc.

#### Additional reading:

1. What is cross-validation? https://scikit-learn.org/stable/modules/cross_validation.html
2. What is lift? https://www.kdnuggets.com/2016/03/lift-analysis-data-scientist-secret-weapon.html
