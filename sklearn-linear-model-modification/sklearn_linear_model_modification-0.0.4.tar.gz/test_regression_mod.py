import os
import sys
fp = os.path.dirname(os.path.abspath( __file__ ))
fpp = os.path.join(fp, 'src')
sys.path.insert(0 , fpp)

from linear_model import *
from sklearn.datasets import load_boston

def load_Xy():
    data = load_boston()
    X = pd.DataFrame( data['data'], columns=data['feature_names'] )
    y = data['target']
    return X, y


def test_mod():
    X, y = load_Xy()

    try:
        lmod = Ridge()
        lmod.fit(X, y)

        lmod = Lasso()
        lmod.fit(X, y)

        lmod = ElasticNet()
        lmod.fit(X, y)

        lmod = LinearRegression()
        lmod.fit(X, y)
        assert True
    except:
        assert False

def test_add1():
    X, y = load_Xy()

    try:
        lmod = Add1Ridge()
        lmod.fit(X, y)

        lmod = Add1Lasso()
        lmod.fit(X, y)

        lmod = Add1ElasticNet()
        lmod.fit(X, y)

        lmod = Add1LinearRegression()
        lmod.fit(X, y)
        assert True
    except:
        assert False

def test_drop1():
    X, y = load_Xy()

    try:
        lmod = Drop1Ridge()
        lmod.fit(X, y)

        lmod = Drop1Lasso()
        lmod.fit(X, y)

        lmod = Drop1ElasticNet()
        lmod.fit(X, y)

        lmod = Drop1LinearRegression()
        lmod.fit(X, y)
        assert True
    except:
        assert False
