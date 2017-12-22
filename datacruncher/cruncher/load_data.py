
# import module/library to do operating system stuff like managing files and directories
import os

# full absolute path of load_data.py as saved on disk
path_of_this_script = os.path.abspath(__file__)

#Parent directory of load_data.py
parent_dir_of_this_script = os.path.dirname(path_of_this_script)

#assumed that csv is in the same directory as load_data.py
csv_filepathname= os.path.join(parent_dir_of_this_script, "person_registry.csv")

# Assumed load_data.py is in home (base) directory of django project i.e same level as manage.py file 
your_djangoproject_home = parent_dir_of_this_script 


'''
This next line of code is needed since this script is not part of django. 
Django needs 'DJANGO_SETTINGS_MODULE' variable set to point to the django settings file.
Normally manage.py does it for you but since this python file is not part of django it needs to explicitly set it. 
It needs to be set because this is how non-django code can access django stuff that is set in the settings file such as models, templates etc
Finally django setup needs to be called if running python code outside of django to access django stuff 
'''
os.environ['DJANGO_SETTINGS_MODULE'] = 'cruncher.settings' # Cruncher is the name of this project!
import django
django.setup()


from csvcruncher.models import Person 
import csv 
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"') 
for row in dataReader: 
    if row[0] != 'Name': # Ignore the header row, import everything else 
     person = Person() 
     person.name = row[0] 
     person.occupation = row[1] 
     person.age = row[2] 
     person.gender = row[3] 
     person.save()