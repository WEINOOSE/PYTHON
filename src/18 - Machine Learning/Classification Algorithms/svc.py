import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC

sc = StandardScaler()
svc = SVC(kernel="linear")

# Including Data.
veri = pd.DataFrame(pd.read_csv("svc.csv"))

# Defining Dependent & Independent Variables.
x = veri[["Height","Weight","Age"]].values
y = veri[["Gender"]].values

# Splitting between train and test.
x_tr,x_ts,y_tr,y_ts = train_test_split(x, y, test_size=0.5, random_state=31)

# Educating the Model.
x_train = sc.fit_transform(x_tr)
x_test = sc.transform(x_ts)

# Fitting and Predicting.
svc.fit(x_train,y_tr)
prediction = svc.predict(x_test)

# Result
real = veri[["Gender"]].head(11)
pred = pd.DataFrame(prediction, columns=["P. Gender"])
cm = confusion_matrix(y_ts, prediction)
true = cm[1][1] + cm[0][0]
false = cm[1][0] + cm[0][1]
result = pd.concat([pred, real], axis=1)
print(result,"\n")
print(f"True: {true} | False {false} | Success Ratio %{(true/(true+false))*100}\n")
tp = (cm[0][0] / ( cm[0][0] + cm[1][0] ))*100
fp = (cm[0][1] / ( cm[0][1] + cm[1][1] ))*100
print(f"True Positive Rate : %{tp} | False Positive Rate : %{fp}\n")