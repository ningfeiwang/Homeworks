import math
# Linear Regression Classifier
def linear_regression_classifier():
    from sklearn import linear_model
    model = linear_model.LinearRegression()
    param_grid = dict()
    return model, param_grid
 
def naive_bayes_classifier():
    from sklearn.naive_bayes import MultinomialNB
    model = MultinomialNB()
    param_grid = {'alpha': [math.pow(10,-i) for i in range(11)]}
    return model,param_grid
 
# KNN Classifier
def knn_classifier():
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier(n_neighbors=90, weights='uniform', 
        algorithm='auto', leaf_size=30, p=2, metric='minkowski', 
        metric_params=None, n_jobs=1)
    param_grid = {'n_neighbors': list(range(1,21))}
    return model,param_grid
 
# Random Forest Classifier
def random_forest_classifier():
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier()
    param_grid = {'n_estimators' : list(range(1,21)), 'max_depth' : list(range(1,6)), 'max_features' : list(range(1,6))}
    return model, param_grid
 
# Decision Tree Classifier
def decision_tree_classifier():
    from sklearn.tree import DecisionTreeClassifier
    model = DecisionTreeClassifier(max_depth=5)
    param_grid = {'max_depth' : list(range(1,11,2))}
    return model, param_grid
 
def gradient_boosting_classifier():
    from sklearn.ensemble import GradientBoostingClassifier 
    model = GradientBoostingClassifier()
    param_grid = {'n_estimators': list(range(100,200,20))}
    return model, param_grid

# SVM Classifier
def svm_classifier():
    from sklearn.svm import SVC
    model = SVC(kernel="linear", C=0.025)
    param_grid = {'C': [1e-2, 1e-1, 1, 10]}
    return model, param_grid

# AdaBoost Classifier
def ada_boost_validation():
    from sklearn.ensemble import AdaBoostClassifier
    model = AdaBoostClassifier(n_estimators=100)
    param_grid = {'n_estimators' : [50, 100, 200]}
    return model, param_grid

def neural_network_classifier():
    from sklearn.neural_network import MLPClassifier
    model = MLPClassifier(hidden_layer_sizes=(500,500,500,500,200),
        activation = 'relu', 
        solver='sgd', 
        alpha=0.0001, batch_size=100, learning_rate='adaptive', 
        learning_rate_init=0.001, power_t=0.5, max_iter=200, shuffle=True, 
        random_state=None, tol=0.0001, verbose=False, warm_start=False, 
        momentum=0.95, nesterovs_momentum=True, early_stopping=False, 
        validation_fraction=0.1, beta_1=0.9, 
        beta_2=0.999, epsilon=1e-08)
    param_grid = dict()
    return model, param_grid

def xgboost_classifier():
    from xgboost import XGBClassifier
    model = XGBClassifier()
    param_grid = dict()
    return model, param_grid