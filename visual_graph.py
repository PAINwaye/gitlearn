import matplotlib.pyplot as plt
import numpy as np

def line_graph():
    x = np.arange(1, 11)
    y = np.random.randint(10, 100, size=10)
    plt.plot(x, y, marker='o')
    plt.title("Line Graph")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

def bar_graph():
    categories = ['A', 'B', 'C', 'D', 'E']
    values = np.random.randint(10, 100, size=5)
    plt.bar(categories, values)
    plt.title("Bar Graph")
    plt.show()

def scatter_plot():
    x = np.random.randint(0, 50, 50)
    y = np.random.randint(0, 50, 50)
    plt.scatter(x, y)
    plt.title("Scatter Plot")
    plt.show()

def pie_chart():
    labels = ['Python', 'Java', 'C++', 'JS']
    sizes = np.random.randint(10, 50, size=4)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Pie Chart")
    plt.show()

def histogram():
    data = np.random.randn(100)
    plt.hist(data, bins=10)
    plt.title("Histogram")
    plt.show()

def box_plot():
    data = np.random.randn(100)
    plt.boxplot(data)
    plt.title("Box Plot")
    plt.show()

def area_plot():
    x = np.arange(1, 6)
    y = np.random.randint(10, 50, size=5)
    plt.fill_between(x, y)
    plt.title("Area Plot")
    plt.show()

def stem_plot():
    x = np.arange(10)
    y = np.random.randint(1, 20, size=10)
    plt.stem(x, y)
    plt.title("Stem Plot")
    plt.show()

def menu():
    while True:
        print("\n===== Graph Generator Menu =====")
        print("1. Line Graph")
        print("2. Bar Graph")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Box Plot")
        print("7. Area Plot")
        print("8. Stem Plot")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            line_graph()
        elif choice == '2':
            bar_graph()
        elif choice == '3':
            scatter_plot()
        elif choice == '4':
            pie_chart()
        elif choice == '5':
            histogram()
        elif choice == '6':
            box_plot()
        elif choice == '7':
            area_plot()
        elif choice == '8':
            stem_plot()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

# Run program
menu()