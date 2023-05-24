# Part 2 and 3
import urllib.request
import json
import csv


def dic_list_gen(strings, listsoflist):
    acc = []
    for l in listsoflist:
        dict1 = {}
        for i in range(len(strings)):
            dict1[strings[i]] = l[i]
        acc.append(dict1)
    return acc


def read_values(filename):
    acc = []
    with open(filename) as f:
        read = csv.reader(f)
        next(read)
        for line in read:
            acc.append(line)
    return acc


def write_values(filename, list1):
    with open(filename, "a") as f:
        write = csv.writer(f)
        for l in list1:
          write.writerow(l)


def json_loader(url):
    response = urllib.request.urlopen(url)
    json_blob = response.read().decode()
    readable_code = json.loads(json_blob)
    return readable_code


def make_values_numeric(strings, dict1):
    for keys in strings:
     float_value = dict1[keys]
     dict1[keys] = float(float_value)
    return dict1


def save_data(strings, listofdicts, filename):
    acc = []
    acc.append(strings)
    for dict in listofdicts:
        acc2 = []
        for keys in strings:
            acc2.append(dict[keys])
        acc.append(acc2)
    write_values(filename, acc)


def load_data(filename):
    acc = []
    with open(filename) as f:
        read = csv.reader(f)
        for line in read:
          acc.append(line)
    acc1 = []
    for i in range(1, len(acc)):
        acc1.append(acc[i])
    return dic_list_gen(acc[0], acc1)


def make_lists(strings, listofdicts):
    acc = []
    for dict in listofdicts:
        acc2 = []
        for keys in strings:
            acc2.append(dict[keys])
        acc.append(acc2)
    return acc
