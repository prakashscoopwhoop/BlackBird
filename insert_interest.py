import csv,os
from pymongo import MongoClient
import urllib
from app.service import CategoryService, InterestService


def read_file(file_to_analyze):
    lines = open(file_to_analyze, 'r').readlines()
    to_write = []
    chk_to_write = True
    for l in lines:
        if l == ',,\r\n':
            chk_to_write = False
            break
        elif chk_to_write:
            to_write.append(l)
        else:
            chk_to_write = False
            break   
    open('temp.csv', 'w').writelines(to_write)
    records = []
    interests = []
    with open('temp.csv') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            r_category = row['Category'].lower()
            r_interest = row['Name'].lower()
            if not any(record['category'] == r_category for record in records):
                records.append({'category': r_category})
            if not any(interest['interest'] == r_interest and interest['category'] == r_category for interest in interests):
                interests.append({'interest': r_interest, 'category': r_category, 'image': row['ImageUrl'], 'keywords': []})

    if os.path.isfile('temp.csv'):
        os.remove('temp.csv')
    return records, interests


def download_images_locally(url):
    cwd = os.getcwd()
    if not os.path.exists('templates/images'):
        os.makedirs('templates/images')
    filename = url.split('/')[-1]+".jpg"
    os.chdir('templates/images')
    image_path = os.getcwd()
    urllib.urlretrieve(url, filename)
    os.chdir(cwd)
    return filename

if __name__ == "__main__":
    client = client = MongoClient()
    db = client.blackbird
    col_name = db.categories
    interest_col = db.interests
    __category_service = CategoryService()
    __interest_service = InterestService()
    (to_insert, to_interest) = read_file("stumleupon.csv")
    for row in to_insert:
        __category_service.save_category(row)
    for row in to_interest:
        row['image'] = download_images_locally(row['image'])
        category_info = __category_service.find_category_by_name(row['category'])
        row['category_id'] = str(category_info['_id'])
        del row['category']
        __interest_service.save_interest(row)
        # print row
    print "insert successfully..."