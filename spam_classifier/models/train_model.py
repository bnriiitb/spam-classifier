import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

def load_dataset():
    # Dataset from - https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection
    df = pd.read_table('../../data/raw/smsspamcollection/SMSSpamCollection',
                       sep='\t',
                       header=None,
                       names=['label', 'sms_message'])

    # Output printing out first 5 columns
    return df

def train_test_split(df):
    print('\n########## Train Test Split ########## ')
    # split into training and testing sets
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(df['sms_message'],
                                                        df['label'],
                                                        random_state=1)

    print('Number of rows in the total set: {}'.format(df.shape[0]))
    print('Number of rows in the training set: {}'.format(X_train.shape[0]))
    print('Number of rows in the test set: {}'.format(X_test.shape[0]))
    return X_train, X_test, y_train, y_test

def eval_model(y_test,predictions):
    print('\n########## Model Performance ########## ')
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    print('Accuracy score: ', format(accuracy_score(y_test, predictions)))
    print('Precision score: ', format(precision_score(y_test, predictions, pos_label="spam")))
    print('Recall score: ', format(recall_score(y_test, predictions, pos_label="spam")))
    print('F1 score: ', format(f1_score(y_test, predictions, pos_label="spam")))

def persist_model(model,filename):
    from pathlib import Path
    Path("artefacts").mkdir(parents=True, exist_ok=True)
    pickle.dump(model, open("artefacts/"+filename, 'wb'))



if __name__=='__main__':
    df = load_dataset()
    print('##### Sample Data #####')
    print(df.head())
    X_train, X_test, y_train, y_test = train_test_split(df)
    count_vector = CountVectorizer()
    # Fit the training data and then return the matrix
    training_data = count_vector.fit_transform(X_train)
    # Transform testing data and return the matrix. Note we are not fitting the testing data into the CountVectorizer()
    testing_data = count_vector.transform(X_test)
    naive_bayes = MultinomialNB()
    naive_bayes.fit(training_data, y_train)
    predictions = naive_bayes.predict(testing_data)
    eval_model(y_test,predictions)
    print("\n########## Persisting model artefacts ########## ")
    # persisting models as artefacts
    persist_model(count_vector, "count_vector.pkl")
    persist_model(naive_bayes, "naive_bayes.pkl")



