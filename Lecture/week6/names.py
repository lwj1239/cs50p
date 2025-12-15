import csv

name = input("What's your name? ")
university = input("What;s your university? ")

with open("students.csv", "a", newline="") as file:
    writer = csv.DictWriter(file,fieldnames=["name", "university"])
    writer.writerow({"name": name, "university": university})