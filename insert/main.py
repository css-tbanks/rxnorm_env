import os
from datetime import datetime
from dotenv import *
load_dotenv()

config = os.environ

def archive_folder(path):
    if not os.path.isdir(path):
        os.makedirs(path)
        print("INFO: Path has been created.")
    else:
        print(f"INFO: Path already exists.")

def df_save(path,c,r,s):
    runid = datetime.today().strftime("%Y%m%d")
    archive = config['archive_folder']
    archive = archive.format(runid)
    archive_folder(archive)
    print('PROCESS: Saving dataframes now...')
    for filename in os.listdir(path + '/rrf/'):
        if filename.lower() == 'rxnconso.rrf':
            c.to_csv(archive + f'/rxnconso_{runid}.csv')
        elif filename.lower() == 'rxnrel.rrf':
            r.to_csv(archive + f'/rxnrel_{runid}.csv')
        elif filename.lower() == 'rxnsat.rrf':
            s.to_csv(archive + f'/rxnsat_{runid}.csv')
        else:
            print(f'WARNING: Unrecognized file: {filename}')
        print(f'INFO: {filename} saved.')
    print(f'INFO: Archive file available here: {archive}')