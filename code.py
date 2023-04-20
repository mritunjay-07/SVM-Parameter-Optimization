import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.svm import SVC
from scipy.stats import uniform
df = pd.read_csv("/content/drive/MyDrive/All csv/datatraining.csv")
df = df.drop(['s.no', 'date'], axis=1)
X = df.iloc[:,:-1].values
y = df.iloc[:,-1].values
best_kernel = []
best_Nu = []
best_epsilon = []
best_accuracy = []
for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=i)
    svc = SVC()
    param_distributions = {'kernel': ['linear', 'rbf', 'poly', 'sigmoid'],'nu': uniform(0.01, 10),'epsilon': uniform(0.01, 1.0)}
    random_search = RandomizedSearchCV(svc, param_distributions, n_iter=10, cv=5, random_state=i)
    random_search.fit(X_train, y_train)
    best_kernel.append(random_search.best_params_['kernel'])
    best_Nu.append(random_search.best_params_['nu'])
    best_epsilon.append(random_search.best_params_['epsilon'])
    best_accuracy.append(random_search.best_score_)
samples = ['Sample ' + str(i+1) for i in range(10)]
data = {'Sample Number': samples, 'Best Accuracy': best_accuracy, 'Best Kernel': best_kernel, 'Best Nu': best_Nu , 'Best Epsilon': best_epsilon}
table = pd.DataFrame(data)
print(table)