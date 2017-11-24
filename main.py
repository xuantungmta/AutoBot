from Core.LinearRegression import LinearRegression
import numpy as np

# height (cm)
X = np.array(
    [[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
y = np.array([[49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T
linear = LinearRegression(X, y)
linear.train()
linear.predict(np.array([[155, 160]]))

linear.setHeightName("Height")
linear.setWidthName("Weight")
linear.display()
