import xlrd
import csv
import pandas

def csv_from_excel():

    wb = xlrd.open_workbook('/home/py01/Desktop/ratings2.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open('/home/py01/Desktop/ratings4.csv', 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()




def exl2csv():
    df = pandas.read_excel('/home/py01/Desktop/ratings2.xlsx')
    #csvfileloc = os.path.join('uploads', 'frmxl2csv-' + get_random_id()+'.csv')
    csvfileloc = '/home/py01/Desktop/ratings5.csv'
    df.to_csv(csvfileloc, sep='\t', encoding='utf-8')
    return csvfileloc

exl2csv()