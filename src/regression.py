import pandas as pd
from sklearn import linear_model
from src.data import get_ranking_filepath

class Regression:
    def __init__(self, coef, intercept):
        self.coefs = coef
        self.intercept = intercept

    def __call__(self, ranks):
        s = self.intercept
        for i, c in enumerate(self.coefs):
            s += c * ranks[i]
        return s

    def __str__(self):
        return "{:.2f} * bullet + {:.2f} * blitz + {:.2f} * rapid + {:.2f} * classical + {:.2f} * correspondence".format(
        *self.coefs, self.intercept)


def read_rankings_file(year, month):
    return pd.read_csv(get_ranking_filepath(year, month))


def calculate_regression(year, month):
    data = read_rankings_file(year, month)
    ranks = data.drop(['name'], axis=1)
    ranks = ranks[ranks.fide <= 2900]
    ranks = ranks[ranks.fide >= 1000]
    xs = ranks.drop(['fide'], axis=1).to_numpy()
    ys = ranks['fide'].to_numpy()
    reg = linear_model.LinearRegression().fit(xs, ys)
    return Regression(reg.coef_, reg.intercept_)