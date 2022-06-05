I work with the standard MNIST data set and determine which one of the standard algorithms is better to deploy with "reasonable"
time used in training and idenfitication of integers in the MNIST dataset. 

1. The data is split into training and test subsets (in a 6:1) split. 
2. The training set X_test is transformed by using PCA into X_pca and into X_ipca. 

Algorithms used in this work:

1. SVM (support vector machines)
2. RandomForestClassifier
3. Stochastic Gradient Descent
4. OneVsRestClassifier

Conclusions:

We decide to go with the Support Vector Machine (SVM) trained on X_pca which was simply dimension-reduced by principal component
analysis, based on cross-validation score of roughly 98%, precision and recall of about 0.98 each, based on the training time
of 111s. Other classifiers with similar cross-validation scores, precision and recall had greater training time.

Further, SVM demonstrates the lowest failure rates of all the three models. It also seems to predict random samples in the test set slightly
faster in roughly 6-7 ms (with OneVsRestClassifier a close second in time required to predict samples in the test set). 
