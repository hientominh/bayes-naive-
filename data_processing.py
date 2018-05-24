import csv
import os

'''
    Data downloaded from website:
        https://www.kaggle.com/uciml/sms-spam-collection-dataset/data
    0 : ham
    1 : spam
'''


def read_file(filename):
    list_ham = []
    list_spam = []
    with open(filename, newline='', encoding='latin-1') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['v1'] == 'spam':
                list_spam.append(row['v2'])
            if row['v1'] == 'ham':
                list_ham.append(row['v2'])
    return list_spam, list_ham


def file_creation(data):
    list_spam = data[0]
    list_ham = data[1]
    path = os.getcwd()
    spam_dir = '{}/spam'.format(path)
    ham_dir = '{}/ham'.format(path)
    data_test_dir = '{}/test'.format(path)
    try:
        os.mkdir(spam_dir)
        os.mkdir(ham_dir)
        os.mkdir(data_test_dir)
    except FileExistsError:
        print('Directory was exist!')
    count1 = int(len(list_spam) * 8 / 10)
    count = 1
    for spam in list_spam:
        if count == count1:
            break
        with open('{}/{}.txt'.format(spam_dir, count), 'wt') as f:
            f.write(spam)
        count += 1
    count2 = int(len(list_ham) * 8 / 10)
    count = 1
    for ham in list_ham:
        if count == count2:
            break
        with open('{}/{}.txt'.format(ham_dir, count), 'wt') as f:
            f.write(ham)
        count += 1
    list_label_test = []
    count = 1
    while count1 < len(list_spam) - 1:
        count1 += 1
        with open('{}/{}.txt'.format(data_test_dir, count), 'wt') as f:
            f.write(list_spam[count1])
            list_label_test.append(1)
        count += 1
    while count2 < len(list_ham) - 1:
        count2 += 1
        with open('{}/{}.txt'.format(data_test_dir, count), 'wt') as f:
            f.write(list_ham[count2])
            list_label_test.append(0)
        count += 1
    with open('label_test.txt', 'wt') as f:
        for label in enumerate(list_label_test):
            f.write(str(label[0]) + ' ' + str(label[1]) + '\n')


def main():
    filename = 'spam.csv'
    file_creation(read_file(filename))


if __name__ == '__main__':
    main()
