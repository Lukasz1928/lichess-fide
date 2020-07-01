import json

from sklearn import linear_model

from src.utils.variants import variants


class Regression:
    def __init__(self, coef, intercept, score=None):
        self.coefs = [round(x, 2) for x in coef]
        self.intercept = intercept
        self.score = score

    def __call__(self, ranks):
        s = self.intercept
        for i, c in enumerate(self.coefs):
            s += c * ranks[i]
        return s

    def __str__(self):
        s = ""
        for i in range(len(variants)):
            s += "{:.2f} * {} + ".format(self.coefs[i], variants[i])
        s += "{:.2f}".format(self.intercept)
        return s

    @staticmethod
    def calculate(rankings):
        xs = [[player[v] for v in variants] for player in rankings]
        ys = [player['fide'] for player in rankings]
        reg = linear_model.LinearRegression().fit(xs, ys)
        return Regression(reg.coef_, reg.intercept_, reg.score(xs, ys))

    def save(self, filename):
        json_reg = {'coefs': self.coefs,
                    'intercept': self.intercept,
                    'coefs_order': variants}
        str_reg = json.dumps(json_reg)
        with open(filename, 'w+') as f:
            f.write(str_reg)


def filter_rankings_by_fide(rankings):
    return [r for r in rankings if r['fide'] is not None]