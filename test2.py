import matplotlib.pyplot as plt
figure, axes = plt.subplots()
x1, y1 = [400, 400], [0, 800]
x2, y2 = [0, 800],[400, 400]
plt.plot(x1, y1, x2, y2,  marker = 'o')
circle = plt.Circle((0.6, 0.6), 0.2)
axes.set_aspect(1)
axes.add_artist(circle)
plt.show()

