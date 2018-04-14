CREDIT CARD FRAUD DETECTION

         The data consists of Normal Transactions and Fraud transaction.
The data is an Imbalance data (More number of Normal class than the Fraud class).

APPROACH

         Its not possible to split the dataset into train and test dataset. Following are the fuctions carried to handle such type of dataset:
     A)	Undersampling:- Taking the less number of majority class(Less number of Normal transactions so that our new data will be balanced.
     
     B)	SMOTE:- Oversampling were we will make a synthetic example of minority class(Fraud transactions) to fet a balanced dataset
This notebook has the following phases:
 	Data Ingestion
 	Data Preparation
 	Feature Engineering 
	Feature Selection
        Modeling
 	Pickle 
 	Uploading files to Amazon S3

PERFORMANCE METRICS
       Changing the performance metric:
     * Use the confusion matrix to calculate Precision, Recall
     * F1score (weighted average of precision recall)
     * Use Kappa - which is a classification accuracy normalized by the imbalance of the classes in the data
     * ROC curves - calculates sensitivity/specificity ratio.

Application of Algorithms
       We will now compare what happens when using resampling and when not using it. We will test this approach using following models:
     * Logistic Regression
     * SVM
     * Random forest classifier
     * Naive Bayes

Dataset - https://s3.amazonaws.com/assignment3datasets/creditcard.csv.zip