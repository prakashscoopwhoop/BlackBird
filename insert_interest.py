import csv,os
from pymongo import MongoClient
def read_file(file_to_analyze):
    lines = open(file_to_analyze,'r').readlines()
    to_write = []
    chk_to_write = True
    for l in lines:
        if l==',,\n':
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
            r_sub_category = row['Name']
            r_image = row['ImageUrl']
            records.append(
                {'category': r_category, 'sub_category': r_sub_category, 'image': r_image})
    if os.path.isfile('temp.csv'):
        os.remove('temp.csv')
    return records

if __name__== "__main__":
    client =  client = MongoClient()
    db = client.black_bird
    col_name = db.interests
    to_insert = read_file("stumleupon.csv")
    for row in to_insert:
        col_name.save(row)
    print "insert successfully..."
    