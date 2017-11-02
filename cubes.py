import matplotlib.pyplot as plt

x_values = list(range(1,5001))
print x_values
y_values = [x**3 for x in x_values]
print y_values


plt.scatter(x_values,y_values,linewidth=5,c=y_values, cmap=plt.cm.Blues)
plt.title("Cubed Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
plt.show()
