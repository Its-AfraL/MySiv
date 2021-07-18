# MySiv, a OSINT python tool to find information about a car plate number
# Created by AfraL
# https://www.github.com/Its-AfraL

# pip install -r requirements.txt
# install.bat
# Or : pip install selenium / pip install terminaltables / pip install colorama

from selenium import webdriver
from terminaltables import SingleTable
import time
from colorama import init, Fore, Style
import os, sys
import random

chaine = "[*]"+' Starting MySiv and SIV folder instance...'

def loading():
	charspec = "$*.X^%_/\\#~!?;"
	chainehack = ""
	for c in chaine:
		chainehack += c
		r = random.choice(charspec)+random.choice(charspec)+random.choice(charspec)
		if len(chainehack+r) <= len(chaine):
			pass
		else:
		    r = ""
		sys.stdout.write('\r'+chainehack+r)
		time.sleep(0.06)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

init()
print("\n")                                                             
print(Fore.WHITE + Style.NORMAL + "        _____          _________.__        ")
print(Fore.WHITE + Style.NORMAL + "       /     \ ___.__./   _____/|__|__  __ ")
print(Fore.WHITE + Style.NORMAL + "      /  \ /  <   |  |\_____  \ |  \  \/ / ")
print(Fore.WHITE + Style.NORMAL + "     /    Y    \___  |/        \|  |\   /  " + Fore.WHITE + Style.NORMAL + " https://www.github.com/" + Fore.RED + Style.NORMAL + "Its-AfraL")
print(Fore.WHITE + Style.NORMAL + "     \____|__  / ____/_______  /|__| \_/   ")
print(Fore.WHITE + Style.NORMAL + "             \/\/            \/            ")
print(Fore.WHITE + Style.NORMAL + "\n")

loading()
chaine = "[+]"+' Successfully started'
print("\n")

options = webdriver.ChromeOptions()
options.add_argument("--headless") 
options.headless = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
driver.get("https://www.autorigin.com")

cookie_button = driver.find_element_by_id("rgpdCookieBtnAll")
cookie_button.click()                                                       

loading()
print("\n")

number_plate = input("Enter the plate number [?] ")

search_bar = driver.find_element_by_id("numberplate")
search_bar.send_keys(number_plate)

search_button = driver.find_element_by_xpath("//*[@id=\"main\"]/section[1]/div/div/div[1]/form/div/div[2]/button")
search_button.click()

time.sleep(10)
car_name = driver.find_element_by_class_name("car")

vin_code = driver.find_element_by_xpath("//*[@id=\"main\"]/div[1]/div[2]/div/div/div[2]/section/div[3]/div[1]/div[2]")

fuel_used = driver.find_element_by_xpath("//*[@id=\"main\"]/div[1]/div[2]/div/div/div[2]/section/div[3]/div[2]/div[2]")

cylinder = driver.find_element_by_xpath("//*[@id=\"main\"]/div[1]/div[2]/div/div/div[2]/section/div[3]/div[3]/div[2]")

car_color = driver.find_element_by_xpath("//*[@id=\"main\"]/div[1]/div[2]/div/div/div[2]/section/div[3]/div[4]/div[2]")

place_number = driver.find_element_by_xpath("//*[@id=\"main\"]/div[1]/div[2]/div/div/div[2]/section/div[3]/div[5]/div[2]")

print("\n") 

table_car_name = car_name.text
table_vin_code = vin_code.text
table_fuel = fuel_used.text
table_cylinder = cylinder.text
table_car_color = car_color.text
table_place_number = place_number.text

table_data = [
    [number_plate, table_car_name],
    ['VIN Code', table_vin_code],
    ['Carburant utilisé', table_fuel],
    ['Cylindrée', table_cylinder],
    ['Couleur de la voiture', table_car_color],
    ['Nombre de places', table_place_number]
]

table = SingleTable(table_data)
print(table.table)