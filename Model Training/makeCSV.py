import os
import pandas as pd
from selenium import webdriver
import urllib.request
import time

path = 'C:/Users/vivas/OneDrive/Desktop/Myntra/Images'
colors = ['black', 'blue', 'red', 'green', 'yellow', 'orange', 'white']
subTypes = ['informal', 'formal']
types = ['shoe', 'shirt', 'pant', 'tshirt']

image_set = []
folder_set = []

def create_search_folder_name():
    for color in colors:
        for subtype in subTypes:
            for type in types:
                if type == 'shirt' and subtype == 'informal':
                    continue
                elif type == 'tshirt' and subtype == 'formal':
                    continue
                elif type == 'shoe' and subtype == 'informal':
                    image_set.append(color + '_' + type + '_casual')
                    folder_set.append(color + '_' + type + '_casual')
                elif subtype == 'informal':
                    image_set.append(color + '_' + type)
                    folder_set.append(color + '_' + type + '_' + subtype)
                else:
                    image_set.append(color + '_' + type + '_' + subtype)
                    folder_set.append(color + '_' + type + '_' + subtype)


def load_image_name_to_pd(folder):
    data = []

    for subdir in os.listdir(folder):
        subdir = folder + '/' + subdir
        
        print(subdir)
        for filename in os.listdir(subdir):
            print(filename)
            color = filename.split('.')[0].split('_')[0]
            type = filename.split('.')[0].split('_')[1]
            subtype = filename.split('.')[0].split('_')[2]
            data.append([filename, type, subtype, color])

    df = pd.DataFrame(data, columns=['filename', 'type', 'subType', 'color'])
    df.to_csv(path + '/../Dataset.csv', index=False, encoding='utf-8')


def get_images():
    driver = webdriver.Chrome('C:/Users/vivas/Downloads/chromedriver')   

    for folder in folder_set:
        try:
            os.makedirs(path + '/' + folder)
        except:
            continue
    
    for index in range(len(image_set)):
        count = 0
        for loop in range(1, 15):
            driver.get('https://www.myntra.com/'+'-'.join(image_set[index].split('_'))+'?p=' + str(loop))
            
            loop += 1
            y = 1000
            for timer in range(0, 7):
                driver.execute_script("window.scrollTo(0," + str(y) + ")")
                y += 1000
                time.sleep(0.5)
            
            img = driver.find_elements_by_tag_name('img')
            image_count = 0
            for item in img:
                src = item.get_attribute('src')
                if('assets' in src and 'constant' not in src):
                    print(path + '/' + folder_set[index] + '/' + folder_set[index] + '_' + str(count) + '.png')
                    urllib.request.urlretrieve(src, path + '/' + folder_set[index] + '/' + folder_set[index] + '_' + str(count) + '.png')
                    count += 1
                    image_count += 1

            if image_count%50 != 0:
                break
        
        print(image_set[index] + ":" + str(count))
    driver.close()


create_search_folder_name()
get_images()
load_image_name_to_pd(path)


