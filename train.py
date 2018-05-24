import os
import json


'''
    0: ham
    1: spam
'''


def get_data():
    path = os.getcwd()
    list_filenames_spam_train = []
    list_filenames_ham_train = []

    for (dirpath, dirnames, filenames) in os.walk('{}/spam'.format(path)):
        list_filenames_spam_train.append(filenames)
    for (dirpath, dirnames, filenames) in os.walk('{}/ham'.format(path)):
        list_filenames_ham_train.append(filenames)
    data_train = []
    label_train = []
    for filename in list_filenames_spam_train[0]:
        with open('{}/spam/{}'.format(path, filename), 'rt') as f:
            temp = f.read().lower()
            temp.replace('.', '')
            temp.replace(',', '')
            temp.replace('!', '')
            temp.replace('?', '')
            temp.replace(':', '')
            temp.replace('"', '')
            data_train.append(temp)
            label_train.append(1)
    for filename in list_filenames_ham_train[0]:
        with open('{}/ham/{}'.format(path, filename), 'rt') as f:
            temp = f.read().lower()
            temp.replace('.', '')
            temp.replace(',', '')
            temp.replace('!', '')
            temp.replace('?', '')
            temp.replace(':', '')
            temp.replace('"', '')
            data_train.append(temp)
            label_train.append(0)
    return data_train, label_train, len(list_filenames_spam_train[0])


def solve():
    data_train, label_train, count = get_data()
    temp = ' '.join(data_train).split(' ')
    table = {0: {}, 1: {}}
    table['spam'] = count
    table['ham'] = len(data_train) - count
    for data in temp:
        table[0][data] = 0
        table[1][data] = 0
    for data in data_train[:count]:
        temp2 = data.split(' ')
        temp3 = set(temp2)
        for value in temp3:
            if value in table[1]:
                table[1][value] += temp2.count(value)
    for data in data_train[count:]:
        temp2 = data.split(' ')
        temp3 = set(temp2)
        for value in temp3:
            if value in table[0]:
                table[0][value] += temp2.count(value)

    with open('train.json', 'wt') as f:
        json.dump(table, f)


def main():
    solve()


if __name__ == '__main__':
    main()
