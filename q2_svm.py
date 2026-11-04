import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

# ---------- load data (snippet from the assignment) ----------
train = pd.read_csv('training.csv', encoding='utf-8-sig')
test  = pd.read_csv('test.csv',  encoding='utf-8-sig', sep=r'[,\t]+', engine='python')
X_train, y_train = train.iloc[:, :-1].to_numpy().astype(float), train.iloc[:, -1].to_numpy().astype(float)
X_test,  y_test  = test.iloc[:, :-1].to_numpy().astype(float),  test.iloc[:, -1].to_numpy().astype(float)

# ---------- Model 1: linear kernel, soft margin ----------
clf_lin = SVC(kernel='linear', C=1.0)
clf_lin.fit(X_train, y_train)
acc_lin = clf_lin.score(X_test, y_test)
print(f'linear kernel, C=1.0:        test accuracy = {acc_lin:.4f}')

# ---------- Model 2: RBF kernel, soft margin ----------
clf_rbf = SVC(kernel='rbf', C=1.0, gamma=2)
clf_rbf.fit(X_train, y_train)
acc_rbf = clf_rbf.score(X_test, y_test)
print(f'RBF kernel, C=1.0, gamma=2:  test accuracy = {acc_rbf:.4f}')
print(f'number of support vectors = {len(clf_rbf.support_)}')

# ---------- 2D plot: decision boundary (solid) + margins (dashed) ----------
def plot_svm(ax, X, y, clf, title):
    x_min, x_max = -1.6, 1.3
    y_min, y_max = -1.5, 1.6
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 400),
                         np.linspace(y_min, y_max, 400))
    Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    ax.contourf(xx, yy, Z, levels=[-10, 0, 10], colors=['#ffd0d0', '#cfe8cf'], alpha=0.6)
    ax.contour(xx, yy, Z, levels=[0],  colors='k', linewidths=1.6, linestyles='solid')   # decision boundary
    ax.contour(xx, yy, Z, levels=[-1, 1], colors='k', linewidths=1.1, linestyles='dashed') # margins
    ax.scatter(X[y == 0, 0], X[y == 0, 1], c='#1f77b4', s=50, label='class 0', edgecolors='k')
    ax.scatter(X[y == 1, 0], X[y == 1, 1], c='#d62728', s=50, label='class 1', edgecolors='k')
    ax.set_xlabel('x1'); ax.set_ylabel('x2'); ax.set_title(title)
    ax.legend(loc='lower left', fontsize=9)

fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.2))
plot_svm(axes[0], X_train, y_train, clf_rbf, 'RBF kernel (C=1.0, gamma=2) - Training set')
plot_svm(axes[1], X_test,  y_test,  clf_rbf, 'RBF kernel (C=1.0, gamma=2) - Test set')
plt.tight_layout()
plt.savefig('q2_rbf.png', dpi=200)
plt.show()
