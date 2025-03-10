import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics

df = pd.read_csv("output (1).csv")
X = df[['BASELINE', 'THICKNESS', 'SPACING']] # replace 'feature1', 'feature2', 'feature3' with your feature column names
y = df['TARGET COLUMN'] # replace 'target' with your target column name

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) # 70% training and 30% testing
clf = svm.SVC(kernel='rbf', probability = True) # Linear Kernel
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred)*100)

