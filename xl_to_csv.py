import xlrd
import csv

def csv_from_excel():

	wb = xlrd.open_workbook('/home/py01/Desktop/user_genre.xlsx')
	sh = wb.sheet_by_name('Sheet1')
	your_csv_file = open('/home/py01/Desktop/user_genre.csv', 'wb')
	wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

	for rownum in xrange(sh.nrows):
	    wr.writerow(sh.row_values(rownum))

	your_csv_file.close()

csv_from_excel()