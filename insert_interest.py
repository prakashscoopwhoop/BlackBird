import csv,os
from pymongo import MongoClient
import urllib
def read_file(file_to_analyze):
    lines = open(file_to_analyze,'r').readlines()
    to_write = []
    chk_to_write = True
    for l in lines:
        if l==',,\r\n':
            chk_to_write = False
            break
        elif chk_to_write:
            to_write.append(l)
        else:
            chk_to_write = False
            break   
    open('temp.csv', 'w').writelines(to_write)
    records = []
    with open('temp.csv') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            r_category = row['Category']
            if not any(record['category'] == r_category for record in records):
                records.append(
                               {'category': r_category})
    if os.path.isfile('temp.csv'):
        os.remove('temp.csv')
    return  records

def download_images_locally(url):
    cwd = os.getcwd()
    if not os.path.exists('data'): 
        os.makedirs('data')
    filename = url.split('/')[-1]+".jpg"
    os.chdir('data')
    image_path = os.getcwd()
    urllib.urlretrieve(url,filename)
    os.chdir(cwd)
    return filename

if __name__== "__main__":
    client =  client = MongoClient()
    db = client.blackbird
    col_name = db.categories
    to_insert = read_file("stumleupon.csv")
    for row in to_insert:
        col_name.save(row)
    print "insert successfully..."

    