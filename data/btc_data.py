from data.Data import DataSample
import numpy
import csv


def get_btc_train_data():
    open_train = []
    close_train = []
    avg_train = []
    mov_avg3_train = []
    mov_avg10_train = []
    mov_avg30_train = []
    volumen_train = []
    target_train = []
    with open("./data/201516may1d_train.csv") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            open_train.append(float(row['Open']))
            close_train.append(float(row['Close']))
            avg_train.append(float(row['Weighted Price']))
            mov_avg3_train.append(float(row['Simple Moving Average(3)']))
            mov_avg10_train.append(float(row['Simple Moving Average (10)']))
            mov_avg30_train.append(float(row['Simple Moving Average(30)']))
            volumen_train.append(float(row['Volumen (BTC)']))
            target_train.append(float(row['Target']))
    open_range=(min(open_train),max(open_train))
    close_range=(min(close_train),max(close_train))
    avg_range=(min(avg_train),max(avg_train))
    mov_avg3_range=(min(mov_avg3_train),max(mov_avg3_train))
    mov_avg10_range=(min(mov_avg10_train),max(mov_avg10_train))
    mov_avg30_range=(min(mov_avg30_train),max(mov_avg30_train))
    volumen_range=(min(volumen_train),max(volumen_train))
    target_range=(min(target_train),max(target_train))
    inputs = []
    outputs = []
    for i in xrange(0, len(open_train)):
        inputs.append((open_train[i], close_train[i], avg_train[i], mov_avg3_train[i], mov_avg10_train[i],
                       mov_avg30_train[i], volumen_train[i]))
        outputs.append(target_train[i])
    in_rang = [open_range, close_range, avg_range, mov_avg3_range, mov_avg10_range, mov_avg30_range, volumen_range]
    out_rang = target_range
    return DataSample(inputs, outputs, in_rang, out_rang)


def get_btc_test_data():
    open_test = []
    close_test = []
    avg_test = []
    mov_avg3_test = []
    mov_avg10_test = []
    mov_avg30_test = []
    volumen_test = []
    target_test = []
    with open("201516may1d_test.csv") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            open_test.append(float(row['Open']))
            close_test.append(float(row['Close']))
            avg_test.append(float(row['Weighted Price']))
            mov_avg3_test.append(float(row['Simple Moving Average(3)']))
            mov_avg10_test.append(float(row['Simple Moving Average (10)']))
            mov_avg30_test.append(float(row['Simple Moving Average(30)']))
            volumen_test.append(float(row['Volumen (BTC)']))
            target_test.append(float(row['Target']))
    open_range=(min(open_test),max(open_test))
    close_range=(min(close_test),max(close_test))
    avg_range=(min(avg_test),max(avg_test))
    mov_avg3_range=(min(mov_avg3_test),max(mov_avg3_test))
    mov_avg10_range=(min(mov_avg10_test),max(mov_avg10_test))
    mov_avg30_range=(min(mov_avg30_test),max(mov_avg30_test))
    volumen_range=(min(volumen_test),max(volumen_test))
    target_range=(min(target_test),max(target_test))
    inputs = []
    outputs = []
    for i in xrange(0, len(open_test)):
        inputs.append((open_test[i], close_test[i], avg_test[i], mov_avg3_test[i], mov_avg10_test[i],
                       mov_avg30_test[i], volumen_test[i]))
        outputs.append(target_test[i])
    in_rang = [open_range, close_range, avg_range, mov_avg3_range, mov_avg10_range, mov_avg30_range, volumen_range]
    out_rang = target_range
    return DataSample(inputs, outputs, in_rang, out_rang)
