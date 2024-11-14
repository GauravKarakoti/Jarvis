def graph_creator():
    import pandas as pd
    import matplotlib.pyplot as plt
    import csv

    def create_comparison_graph(csv_file):
        df = pd.read_csv(csv_file)

        column_names = df.columns.tolist()

        column1 = column_names[0]
        column2 = column_names[1]
        column3 = column_names[2]

        column1_data = df[column1]
        column2_data = df[column2]
        column3_data = df[column3]

        plt.figure(figsize=(10, 6))
        plt.plot(column1_data, label=column1)
        plt.plot(column2_data, label=column2)
        plt.plot(column3_data, label=column3)

        plt.xlabel('Index')
        plt.ylabel('Values')
        plt.title(f'Comparison of {column1}, {column2}, {column3}')
        plt.legend()
        plt.grid(True)
        plt.show()

    def csv_input():    
        col_1 = input("Enter 'Name' for column_1: ")
        col_2 = input("Enter 'Name' for column_2: ")
        col_3 = input("Enter 'Name' for column_3: ")

        data = []
        print("Enter data for the CSV file. Type 'done' in any field to stop.")
        while True:
            name = input(f"Enter Value for {col_1}: ")
            if name.lower() == 'done':
                break
            age = input(f"Enter Value for {col_2}: ")
            if age.lower() == 'done':
                break
            occupation = input(f"Enter Value for {col_3}: ")
            if occupation.lower() == 'done':
                break
            data.append([name, age, occupation])

        file_name = "user_data.csv"
        header = [col_1, col_2, col_3]

        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)

        print(f"CSV file '{file_name}' created successfully with user input!")
        return file_name

    
    csv_file = csv_input()
    create_comparison_graph(csv_file)

