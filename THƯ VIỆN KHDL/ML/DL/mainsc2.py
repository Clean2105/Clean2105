from sklearn.model_selection import train_test_split  
from sklearn.svm import SVC 
from sklearn.metrics import RocCurveDisplay 
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt 

X, y = make_classification(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

svc = SVC(random_state=42)
svc.fit(X_train, y_train)
rfc = RandomForestClassifier(random_state=42)
rfc.fit(X_train, y_train)

fig, ax = plt.subplots()

svc_disp = RocCurveDisplay.from_estimator(svc, X_test, y_test, ax=ax)
rfc_disp = RocCurveDisplay.from_estimator(rfc, X_test, y_test, ax=ax)
fig.suptitle("ROC curve comparison")
plt.show() 