import csv

def txtt(text):
    with open('File.txt', 'a', encoding='utf-8') as fi_txt:
        fi_txt.write(text + "\n")

def csvv(text):
    with open('File.csv', 'a', encoding='utf-8') as fi_csv:
        file_writer = csv.writer(fi_csv, delimiter=",", lineterminator="\r")
        file_writer.writerow(text.split())

def con_txt_csv():
    with open('File.csv', 'w', encoding='utf-8') as fi_csv, open('File.txt', "r", encoding='utf-8') as fi_txt:
        file_reader = fi_txt.readlines()
        file_writer = csv.writer(fi_csv, delimiter=",", lineterminator="\r")
        for line in file_reader:
            file_writer.writerow(line.split())

def con_csv_txt():
    with open('File.csv', encoding='utf-8') as fi_csv, open('File.txt',"w",encoding='utf-8') as fi_txt:
        file_reader = csv.reader(fi_csv, delimiter=",")
        for row in file_reader:
            fi_txt.write(f'{row[0]} {row[1]}')