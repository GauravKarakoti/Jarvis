import os
def compareo():
    current_dir = os.getcwd()
    csv_name="user_data.csv"
    csv_path = os.path.join(current_dir,csv_name)
    import pandas as pd
    import matplotlib.pyplot as plt
    csv_file =csv_path
    
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
        plt.title(f'Comparison of {column1},{column2},{column3}')
        plt.legend()
        plt.grid(True)
        plt.show()

    if __name__ == "__main__":
        csv_file
        file_name = r"task_files\userdata.csv"

    create_comparison_graph(file_name)
compareo()