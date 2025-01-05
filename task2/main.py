import os
#import uvicorn
#os.system('python3 -m venv virtualenv')
#os.system('source virtualenv/bin/activate')
#os.system('pip install django')
#os.system('python.exe -m pip install --upgrade pip')
#os.system('django-admin startproject UrbanDjango')
#os.chdir('UrbanDjango')
#print(os.getcwd())
#os.system('python manage.py startapp task2')
#os.system("pip freeze > requirements.txt")



if __name__=='__main__':
    os.chdir('UrbanDjango')
    os.system('python manage.py runserver')
