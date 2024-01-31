
import csv


def read_csv_file(file_path):
   with open(file_path, 'r') as csv_file:
       # Create a CSV reader object
       csv_reader = csv.reader(csv_file)


       # Read the header
       header = next(csv_reader)
       print(f'Header: {header}')


       # Read the remaining rows
       for row in csv_reader:
           print(row)


if __name__ == "__main__":
  
   csv_file_path = 'username.csv'
   read_csv_file(csv_file_path)




