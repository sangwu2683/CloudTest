import csv
import pandas as pd
import re
html_output = ''

# open Workbook2.csv file
csv_data = pd.read_csv('Workbook2.csv', encoding='ISO-8859-1')

# output columns values
html_output += '<table style="width:100%">'
html_output += '\n<tr>'

for col in range(len(list(csv_data.columns.values))):
    html_output += f'<th>{list(csv_data.columns.values)[col]}</th>'
html_output += '\n</tr>'

# output data in the csv file
for row in range(len(csv_data)):
    html_output += '\n<tr>'

    for col in range(len(list(csv_data.columns.values))):
        html_output += f'<th>{csv_data.iloc[row,col]}</th>'

    html_output += '\n</tr>'

# open Workbook2.prn file
data_prn = open('Workbook2.prn', "r", encoding='utf-8', errors='ignore')

# split data from prn file
strings = []
arr = []

# copy the file content into strings
for line in data_prn:
    string = str(line)
    strings.append(string)

# A function use regular expression to describe data format


def data_format(str):
    row = []
    x = re.search(r"^[a-zA-Z]*[,]\s+[a-zA-Z]*", str)
    index = x.span()
    name = str[index[0]:index[1]]
    row.append(name)
    str = str.replace(name, "")

    y = re.search(r"([a-zA-Z]+\s)+[0-9a-zA-Z]*", str)
    index = y.span()
    address = str[index[0]:index[1]]
    row.append(address)
    str = str.replace(address, "")

    z = re.search(r"[0-9a-zA-Z]+\s[0-9a-zA-Z]*", str)
    index = z.span()
    poscode = str[index[0]:index[1]]
    row.append(poscode)
    str = str.replace(poscode, "")

    a = re.search(r"([+]+[0-9]+\s+)*[0-9]+([-]*\s*)+[0-9]+", str)
    index = a.span()
    telephone = str[index[0]:index[1]]
    row.append(telephone)
    str = str.replace(telephone, "")

    b = re.search(r"[0-9]+", str)
    index = b.span()
    credit = str[index[0]:index[1]]
    row.append(credit)
    str = str.replace(credit, "")

    birthday = str.replace(" ", "")
    # change birthday format from 20190101 to 01/01/2019
    birthday = f'{birthday[-3:-1]}/{birthday[-5:-3]}/{birthday[0:4]}'
    row.append(birthday)

    return row


# use data_format function to ingest data from strings
for i in range(1, len(strings)):
    str = strings[i]
    row = data_format(str)

    html_output += '\n<tr>'
    for j in range(len(row)):
        html_output += f'<th>{row[j]}</th>'
    html_output += '\n</tr>'


# close the table
html_output += '</table>'

print(html_output)

# write into html file
html_file = open('test.html', 'w', encoding='utf-8')
htmal_file = html_file.write(html_output)
html_file.close()
