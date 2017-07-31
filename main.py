#Seong Ma

'''
This program allows the user to enter a valid path directory
and rename any files in the path that contains a date (MM-DD-YYYY)
in its
filename to a new date
'''

import os, shutil, re, input_methods

DATE_RE = re.compile(r"""^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$"""
                     , re.VERBOSE)

def valid_directory(path: str):
    return os.path.exists(path) and os.path.isdir(path)
    
    

if __name__ == '__main__':

    while True:
        directory = input_methods.get_directory()
        
        #end program if q
        if directory.lower() == 'q': break
        
        #continue otherwise
        if valid_directory(directory):
            new_date = input_methods.get_new_date()
            for filename in os.listdir(directory):
                match = DATE_RE.search(filename)
                if match == None:
                    continue
                else:
                    pre_date_filename = match.group(1)
                    month_filename = match.group(2)
                    day_filename = match.group(4)
                    year_filename = match.group(6)
                    post_filename = match.group(8)
                    
                    new_filename = pre_date_filename + new_date[0] + '-' + new_date[1] + '-' + new_date[2] + post_filename
                    absolute_directory = os.path.abspath(directory)
                    filename = os.path.join(absolute_directory, filename)
                    new_filename = os.path.join(absolute_directory, new_filename)
                    shutil.move(filename, new_filename)

        else:
            print("INVALID DIRECTORY!\n")
            