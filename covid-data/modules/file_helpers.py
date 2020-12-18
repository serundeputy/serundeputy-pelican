import os as os
import requests as req
import zipfile

# Download the data
def get_file(date):
    r = req.get(base_url + date + '/download')
    with open(date + '.zip', 'wb') as outfile:
        outfile.write(r.content)

def file_unzip(path_of_zip, directory_to_extract_to):
    os.system('mkdir -p ' + directory_to_extract_to)
    with zipfile.ZipFile(path_of_zip, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)

def copy_file(date, file_name):
    os.system('mkdir -p content/images/' + date)
    os.system('cp covid-data/data/' + date + '/' + file_name + ' content/images/' + date + file_name)


