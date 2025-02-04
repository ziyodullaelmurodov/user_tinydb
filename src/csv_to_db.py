import csv
from tinydb import TinyDB, Query


def read_csv(file_path):
    # Read and parse the CSV file
    with open(file_path, "r") as f:
        data = f.read().strip().split("\n")
        headers = data[0].split(",")
        records = [dict(zip(headers, row.split(","))) for row in data[1:]]
    return records

def insert_into_db(data, db_path):
    # Insert data into TinyDB
    db = TinyDB(db_path, indent=4)
    table = db.table("students")
    insertmultiple = table.insert_multiple(data)
    return insertmultiple

def query_db(db_path, query_field, query_value):
    # Query the database

    db = TinyDB(db_path)
    table =db.table('students')
    User = Query()
    searchdata = table.search(User[query_field] == query_value)
    return searchdata

if __name__ == "__main__":
    # Main execution logic
    csv_file = r"C:\Users\ziyod\OneDrive\Desktop\user_tinydb\user_data.csv"
    db_file = r"C:\Users\ziyod\OneDrive\Desktop\user_tinydb\user_data.json"
    
    db2 = TinyDB("search2.json", indent=4)

    data = read_csv(csv_file)

    insert_into_db(data,db_file)

    search_data = query_db(db_file, "gender", "Male")

    print(search_data)
    db2.insert_multiple(search_data)