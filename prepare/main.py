import os
import ast
import pandas as pd
from dotenv import *
load_dotenv()

config = os.environ


def df_gen(path):
    # Create empty DataFrames with desired column names
    path = path + f'/rrf/'
    conso_columns = ast.literal_eval(config['conso_col'])
    conso = pd.DataFrame(columns=conso_columns)
    
    rel_columns = ast.literal_eval(config['rel_col'])
    rel = pd.DataFrame(columns=rel_columns)
    
    sat_columns = ast.literal_eval(config['sat_col'])
    sat = pd.DataFrame(columns=sat_columns)

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if filename.lower() == 'rxnconso.rrf':
            conso = pd.read_csv(file_path, sep='|', names=conso_columns)
        elif filename.lower() == 'rxnrel.rrf':
            rel = pd.read_csv(file_path, sep='|', names=rel_columns)
        elif filename.lower() == 'rxnsat.rrf':
            sat = pd.read_csv(file_path, sep='|', names=sat_columns)
        else:
            print(f'Unrecognized file: {filename}')

    return conso, rel, sat

