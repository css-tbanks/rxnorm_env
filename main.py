from retrieve.main import *
from prepare.main import *

fileid = datetime.today().strftime("%Y%m")

path = check_path(root_path,runid)

# retrieve
if is_folder_empty(folder_path):
    main_extract()
else:
    print("The folder is not empty. Skipping extraction.")


conso, rel, sat = df_gen(path)

# prepare
# for file in path:
#     df = df_gen(path)

# df.to_csv(folder_path + f'/RxTerms{fileid}.csv')