import matplotlib.pyplot as plt

vel = [1,2,3,1,1,3,4,5,2,2,4,7,5,6]
plt.boxplot(vel,vert=True)
plt.title("Box Plot básico con Matplotlib")
plt.ylabel("Valor")
plt.show()
