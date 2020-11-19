import urllib.parse
import os
import sys
import re

try:
    path_to_file = sys.argv[1]
    delete_extensions_regex = r'.*(\.(js|png|css|eot|ttf|woff|woff2|jpg|svg|gif).*)' # change it if we you like

    # open the file
    filename = os.path.basename(path_to_file).replace('.txt','')
    way_back_file = open(path_to_file, 'r')
    content = way_back_file.read().split('\n')

    # create a new file
    result_file = open(f'./{filename}_path_only.txt', 'w')
    result_filename = f'{filename}_path_only.txt'

    for line in content:
        # print(line)
        path = urllib.parse.urlparse(line).path
        if not re.search(delete_extensions_regex, path):
            result_file.write(path + '\n')

    # sort command
    if(os.name == 'posix'):
        os.system(f'sort -u ./{result_filename} > {filename}_path_only_uniq.txt')
    else:
        print('The OS is not Linux, \'only_uniq.txt\' is not created')

    print(f'[V] File(s) successfully created!')
    result_file.close()
    way_back_file.close()

except:
    print('[X] Error with the file or no file specified')
    sys.exit()
