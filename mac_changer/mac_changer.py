#!/usr/bin/env python

import subprocess   # модуль запуска процессов системы
import argparse     # parser получение аргументов
import re           # регулярные выражения

# функция получение аргументов
def get_arguments():
    # получение что вводит пользователь 
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--intarface", dest="interface", help="Interface to change its MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address")
    options = parser.parse_args()
    # arguments = parser.parse_args()
    # проверка что пользовавтель ввел Interface and MAC
    if not options.interface:   #если пользователь не ввел interface
        #code to handle error
        parser.error("[-] Please specify an interface, use --help for more info")   #ошибка/пожалуйста введите interface, для справки воспользуйтесь командой --help
    elif not options.new_mac:   #если пользователь не ввел mac
        #code to handle error
        parser.error("[-] Please specify an mac-address, use --help for more info") #ошибка/пожалуйста введите mac-address, для справки воспользуйтесь командой --help
    return options

# функция смены mac
def change_mac(interface, new_mac):
    # смена mac-address
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    # команды linux'a
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# функция получения текущего mac
def get_current_mac(interface):
    # проверка mac address и вывод на экран
    ifconfig_result = subprocess.check_output(["ifconfig", interface], encoding="utf8")
    # находим и достаем по выборке определенный текст из ifconfig_result
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    # проверка существования mac address в interface
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Cloud not read MAC address") # не могу прочитать mac address


options = get_arguments() # вызов функции получения аргументов

current_mac = get_current_mac(options.interface) # вызов функции проверки текущего mac
# print("Current MAC = " + str(current_mac))

change_mac(options.interface, options.new_mac) # вызов функции смены mac

current_mac = get_current_mac(options.interface) # проверка существующего mac

# сравниваем текущий и новый mac и выводим соответствующее сообщение
if current_mac == options.new_mac:
    print("[+] MAC address was successfuly change to ", current_mac) # mac address был успешно изменен
else:
    print("[-] MAC address did not get changer.") # mac address не был изменен