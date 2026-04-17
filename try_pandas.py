import pandas as pd

def create_dataframe():
    data = {
        'Name': ['A', 'B', 'C'],
        'Age': [20, 21, 19]
    }
    df = pd.DataFrame(data)
    print("\nDataFrame Created:\n", df)

def read_csv_file():
    try:
        df = pd.read_csv('data.csv')
        print("\nCSV Data:\n", df.head())
    except FileNotFoundError:
        print("\nError: data.csv file not found!")

def select_column():
    data = {
        'Name': ['A', 'B', 'C'],
        'Marks': [85, 90, 78]
    }
    df = pd.DataFrame(data)
    print("\nMarks Column:\n", df['Marks'])

def filter_data():
    data = {
        'Name': ['A', 'B', 'C'],
        'Marks': [85, 90, 78]
    }
    df = pd.DataFrame(data)
    filtered = df[df['Marks'] > 80]
    print("\nFiltered Data (Marks > 80):\n", filtered)

def add_column():
    data = {
        'Name': ['A', 'B', 'C'],
        'Marks': [85, 90, 78]
    }
    df = pd.DataFrame(data)
    df['Grade'] = ['A', 'A+', 'B']
    print("\nData with New Column:\n", df)

def calculate_mean():
    data = {
        'Marks': [85, 90, 78]
    }
    df = pd.DataFrame(data)
    mean_value = df['Marks'].mean()
    print("\nAverage Marks:", mean_value)

def describe_data():
    data = {
        'Marks': [85, 90, 78]
    }
    df = pd.DataFrame(data)
    print("\nData Description:\n", df.describe())

while True:
    print("\n===== Pandas Menu =====")
    print("1. Create DataFrame")
    print("2. Read CSV File")
    print("3. Select Column")
    print("4. Filter Data")
    print("5. Add New Column")
    print("6. Calculate Mean")
    print("7. Describe Data")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        create_dataframe()
    elif choice == '2':
        read_csv_file()
    elif choice == '3':
        select_column()
    elif choice == '4':
        filter_data()
    elif choice == '5':
        add_column()
    elif choice == '6':
        calculate_mean()
    elif choice == '7':
        describe_data()
    elif choice == '8':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")