import subprocess
import os


workdir = os.getcwd()
print('This is your working directory: ' + str(workdir))
print('If it is not the directory "Presentazione" \nplease specify the correct path, otherwise press Enter...')

path = input('Enter the path ')
if path == '':
    path = str(workdir)

key = input('Do you want the news of "Fanpage"?[y/n]')
if key != 'n':
    os.chdir(path + '/Fanpage')
    print('PROCESS: STARTED')
    subprocess.call('scrapy crawl FanpageNews', shell=True)
    print('PROCESS: ENDED')

key = input('Do you want the news of "La Stampa"?[y/n]')
if key != 'n':
    os.chdir(path + '/La_Stampa')
    print('PROCESS: STARTED')
    subprocess.call('scrapy crawl LaStNews', shell=True)
    print('PROCESS: ENDED')
    
key = input('Do you want the news of "Il Giornale"?[y/n]')
if key != 'n':
    os.chdir(path + '/Il_Giornale')
    print('PROCESS: STARTED')
    subprocess.call('scrapy crawl IlGiornaleNews', shell=True)
    print('PROCESS: ENDED')
    
key = input('Do you want the news of "Il Corriere della Sera"?[y/n]')
if key != 'n':
    os.chdir(path + '/Il_Corriere')
    print('PROCESS: STARTED')
    subprocess.call('scrapy crawl IlCorrNews', shell=True)
    print('PROCESS: ENDED')

key = input('Do you want the news of "La Repubblica"?[y/n]')
if key != 'n':
    os.chdir(path + '/Repubblica')
    print('PROCESS: STARTED')
    subprocess.call('scrapy crawl RepNews', shell=True)
    print('PROCESS: ENDED')
