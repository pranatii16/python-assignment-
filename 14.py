import csv

def read_and_filter_csv(filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            print("\nStudents scoring above 75%:")
            for row in reader:
                name = row['Name']
                marks = float(row['Marks'])
                if marks > 75:
                    print(f"- {name}")
    except FileNotFoundError:
        print("Error: File not found.")
    except KeyError:
        print("Error: CSV file must have 'Name' and 'Marks' columns.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get CSV file from user
filename = input("Enter the path to the CSV file : ")
read_and_filter_csv(filename)
