import numpy as np
import matplotlib.pyplot as plt


class LinearRegression:

    'linear regression for ml'

    def __init__(self, inputArr, outputArr):
        self.inputArr = inputArr
        self.outputArr = outputArr

        self.heightName = "height"
        self.widthName = "width"
        pass

    def setHeightName(self, heightName):
        "set value height axit"
        self.heightName = heightName

    def setWidthName(self, widthName):
        self.widthName = widthName

    def train(self, isDebug=False):
        "y = landa * x + b"
        X = np.array(self.inputArr)
        y = np.array(self.outputArr)

        one = np.ones((X.shape[0], 1))
        Xbar = np.concatenate((one, X), axis=1)

        if isDebug:
            print Xbar

        A = np.dot(Xbar.T, Xbar)
        B = np.dot(Xbar.T, y)

        self.landa = np.dot(np.linalg.pinv(A), B)

    def predict(self, x):
        x = x.T
        one = np.ones((x.shape[0], 1))
        Xbar = np.concatenate((one, x), axis=1)

        self.result = np.dot(Xbar, self.landa)
        print self.result
        pass

    def display(self):

        w_0 = self.landa[0][0]
        w_1 = self.landa[1][0]
        x0 = np.linspace(145, 185, 2)
        y0 = w_0 + w_1 * x0

        plt.plot(self.inputArr, self.outputArr, 'ro')
        plt.plot(x0, y0)

        plt.axis([np.amin(self.inputArr), np.amax(self.inputArr),
                 np.amin(self.outputArr), np.amax(self.outputArr)])
        plt.xlabel(self.widthName)
        plt.ylabel(self.heightName)
        plt.show()
