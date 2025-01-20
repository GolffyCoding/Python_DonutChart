import matplotlib.pyplot as plt

# Correct the lengths of labels and sizes
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [30, 20, 35, 15]
colors = ['red', 'blue', 'green', 'yellow']

# Create the donut chart
plt.pie(sizes, labels=labels, colors=colors, wedgeprops={'width': 0.4})
centre_circle = plt.Circle((0, 0), 0.65, color='white', fc='white', linewidth=1.25)
plt.gca().add_artist(centre_circle)

# Add other elements
plt.axis('equal')
plt.title('Donut Chart in Python')

# Display the chart
plt.show()
