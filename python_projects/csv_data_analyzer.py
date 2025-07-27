"""Simple CSV data analyzer that computes column averages."""
import csv
from pathlib import Path


def read_csv(path):
    data = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def column_average(data, column):
    values = []
    for row in data:
        try:
            values.append(float(row[column]))
        except (KeyError, ValueError):
            continue
    return sum(values) / len(values) if values else None


def main():
    file_path = input("CSV file path: ")
    column = input("Column to average: ")
    data = read_csv(file_path)
    avg = column_average(data, column)
    if avg is None:
        print("No valid data found for that column")
    else:
        print(f"Average of {column}: {avg}")

if __name__ == "__main__":
    main()
