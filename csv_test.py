import csv

def test_reader():
    with open('test.csv') as csvfile:
        read_list = csv.reader(csvfile)
        for row in read_list:
            print(row, type(row))
            
def test_dict_reader():
    with open('test.csv') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=['name'])
        for row in reader:
            print(row.keys())
            
def test_writer():
    with open('test_writer.csv', 'w', newline='') as csvfile:
        write_list = csv.writer(csvfile)
        write_list.writerow(['abc']*5+['ddd'])
        write_list.writerow(['abc','def','gh'])
        write_list.writerows([[123,34,5],[45,67,78]])
        
def test_dict_writer():
    with open('test_writer.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, ['name', 'value', None],extrasaction='ignore', quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerow({None:'张三', 'value':'123'})
        writer.writerow({'name':'李四', 'value':{'a':'b'}, 'age':34})

if __name__ == '__main__':
    # test_reader()
    # test_dict_reader()
    test_writer()
    # test_dict_writer()