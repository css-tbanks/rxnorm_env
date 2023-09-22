import os
import requests
import zipfile
import sys
# from log import *
# from api import warehouse_run, formatted_api_call, file_api_call

from dotenv import *
from datetime import datetime
load_dotenv()

## nest classes for main
config = os.environ

root_path = config["root_folder"]


runid = datetime.today().strftime("%Y%m%d")
fileid = '09132023' # datetime.today().strftime("%Y%m")

url_id = config["rxNorm_weekly"]
file_url = url_id # .format(fileid) -- for date formatting. not necessary during development

def log(file):
    sys.stdout = open(file, 'w')

def check_path(path,run):
    print("PROCESS: check_path():")
    mypath = path + '/' + run
    if not os.path.isdir(mypath):
        os.makedirs(mypath)
        print("INFO: Path has been created.")
    else:
        print(f"INFO: Path has been identified.\nINFO: Currently using: {mypath}")
    return mypath

folder_path = check_path(root_path,runid)


def retrieve_rx(fileid):
    print("PROCESS: retrieve_rx():\nINFO: Checking file status")
    response = requests.get(file_url)

    open(folder_path + f'/RxNorm_weekly_prescribe_{fileid}.zip', "wb").write(response.content)
    # open(folder_path + f'/RxNorm{fileid}.zip', "wb").write(response.content)
    print('INFO: File received and retrieved')

def extract_zip(fileid):
    # extract contents of zip file
    with zipfile.ZipFile(folder_path + f'/RxNorm_weekly_prescribe_{fileid}.zip', "r") as zip_ref:
        zip_ref.extractall(folder_path)

def main_extract():
    retrieve_rx(fileid)
    extract_zip(fileid)

def is_folder_empty(folder_path):
    # Get a list of files and folders in the folder
    contents = os.listdir(folder_path)

    # Check if there are any items (files or folders) in the folder
    return len(contents) == 0
