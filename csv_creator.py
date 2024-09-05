def csv_input():    
    import csv
    
    col_1=input("Enter 'Name' for cloumn_1 : ")
    col_2=input("Enter 'Name' for column_2 :  ")
    col_3=input("Enter 'Name' for column_3 :  ")
    def get_user_input():
        data = []
        

        print("Enter data for the CSV file. Type 'done' in any field to stop.")
        while True:
            name= input("Enter Value for column_1 : ")
            if name.lower() == 'done':
                break
            age = input("Enter Value for Column_2 : ")
            if age.lower() == 'done':
                break
            occupation = input("Enter Column_3 : ")
            if occupation.lower() == 'done':
                break
            data.append([name, age, occupation])

        return data

    def create_csv_file(file_name, header, data):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)

    if __name__ == "__main__":
        file_name = "user_data.csv"
        header = [col_1, col_2,col_3]

        user_data = get_user_input()
        create_csv_file(file_name, header, user_data)
        print(f"CSV file '{file_name}' created successfully with user input!")