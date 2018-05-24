import os
import json


def solve():
    path = os.getcwd()
    label_data_test = []
    list_filenames_test = []
    for (dirpath, dirnames, filenames) in os.walk('{}/test'.format(path)):
        list_filenames_test.append(filenames)
    data_test = []
    for filename in list_filenames_test[0]:
        with open('{}/test/{}'.format(path, filename), 'rt') as f:
            temp = f.read().lower()
            temp.replace('.', '')
            temp.replace(',', '')
            temp.replace('!', '')
            temp.replace('?', '')
            temp.replace(':', '')
            temp.replace('"', '')
            data_test.append(temp)
    with open('train.json', 'rt') as f:
        data_trained = json.loads(f.read())
    temp = data_trained['0'].copy()
    for key in temp:
        temp[key] = 0
    tranform_data_test = []
    for data in data_test:
        temp1 = set(data)
        temp2 = temp.copy()
        for word in temp1:
            if word in temp2:
                temp2[word] = data.count(word)
        tranform_data_test.append(temp2)
    num_ham = int(data_trained['ham'])
    num_spam = int(data_trained['spam'])
    p_ham = num_ham / (num_ham + num_spam)
    p_spam = 1 - p_ham
    for data in tranform_data_test:
        p0 = p_ham
        p1 = p_spam
        for key in data:
            if data[key] > 0:
                p0 *= (data_trained['0'][key] + 1) / (num_ham + 1)
                p1 *= (data_trained['1'][key] + 1) / (num_spam + 1)
        if p0 >= p1:
            label_data_test.append(0)
        else:
            label_data_test.append(1)
    with open('label_after_test.txt', 'wt') as f:
        for label in enumerate(label_data_test):
            f.write(str(label[0]) + ' ' + str(label[1]) + '\n')


def main():
    solve()


if __name__ == '__main__':
    main()
