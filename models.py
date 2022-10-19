import csv

def read_csv():
    with open('File.csv', encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=",")
        a = list(file_csv)
    return a
def add_csv(list):
    with open('File.csv', 'a', encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=",", lineterminator="\r")
        file_writer.writerow(list.split())


def del_csv(list):
    temp = read_csv()
    del temp [int(list)]
    with open('File.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=",", lineterminator="\r")
        for row in temp:
            writer.writerow(row)

def update_csv(list, tel):
    temp = read_csv()
    print(temp)
    temp[list][1]= tel
    with open ('File.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=",", lineterminator="\r")
        for row in temp:
            writer.writerow(row)

def export_csv():
    with open('File.csv', 'a', encoding='utf-8') as file, open('File0.csv', encoding='utf-8') as file0:
        writer = csv.writer(file, delimiter=",", lineterminator="\r")
        file_read = csv.reader(file0, delimiter=",")
        for row in file_read:
            writer.writerow(row)

def iport_csv():
    with open('File.csv', 'w', encoding='utf-8') as file, open('File0.csv', encoding='utf-8') as file0:
        writer = csv.writer(file, delimiter=",", lineterminator="\r")
        file_read = csv.reader(file0, delimiter=",")
        for row in file_read:
            writer.writerow(row)