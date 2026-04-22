import random
import os
import time
import threading
import json
import platform


def proverka_OS():
    if platform.system() == "Windows":
        print("Windows... Okey")
        time.sleep(0.5)
    else:
        print("Извините, на данной операционной системе игра не поддерживается (причина: я не знаю команды linux, тобиш остальных ОС)")
        time.sleep(3)
        return
        

def save_game():
    data = {
        "current_news_text": current_news_text,
        "gpu_level": gpu_level,
        "upgrade_cost_gpu": upgrade_cost_gpu,
        "bal": bal,
        "btc": btc,
        "price_btc": price_btc
    }

    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

current_news_text = "" 
gpu_level = 1 
upgrade_cost_gpu = 10 
bal = 10 
btc = 0 
price_btc = 20

def load_game():
    global current_news_text, gpu_level, upgrade_cost_gpu, bal, btc, price_btc

    try:
        with open("save.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        current_news_text = data["current_news_text"]
        gpu_level = data["gpu_level"]
        upgrade_cost_gpu = data["upgrade_cost_gpu"]
        bal = data["bal"]
        btc = data["btc"]
        price_btc = data["price_btc"]
        print("save load")
        time.sleep(0.5)

    except FileNotFoundError:
        print("save not found, using defaults")
        time.sleep(0.5)


def kurs_btc():
    global price_btc
    while True:
        step_price_btc = random.randint(-1, 1)
        price_btc += step_price_btc
        if price_btc < 1:
            price_btc = 1
        time.sleep(4)

def classik_kazino():
    global bal
    if bal < 1:
        print("Вам к сожелению нельзя.")
        time.sleep(1)
        return
    while True:
        os.system("cls")
        os.system("title Winddos казино-классика")
        print()
        try:
            print("Текущее кол-во очков:", bal)
            zezim_classiko = input("Выберите действие: \n[1] - начать игру \n[2] - выход \n:")
            if zezim_classiko == "1":
                print("Текущее кол-во очков:", bal)
                stavka = int(input("Какое кол-во ставки будет?:"))
                st = int(input("Выберите 1 или 2 \n:"))
                rst = random.randint(1, 2)
                if rst == st:
                    print("Вы выиграли! Ставка умножена на бал к балансу.")                    
                    bal += stavka * 2
                    print(f"Ваш баланс = {bal}")
                    time.sleep(2)
                else:
                    print("Проигрыш, ставка отнимается от баланса.")                    
                    bal -= stavka
                    time.sleep(2)
                    if bal >= 0:
                        bal = 0
                        break
            elif zezim_classiko == "2":
                return
        except ValueError:
            print("Ой... Произошла ошибочка... \nПожалуйста, перезапустите режим 1. \nP.S\nРУКИ НОГИ ПООТРЫВАЮ ЕСЛИ БУДЕТЕ ВВОДИТЬ НЕ ЧИСЛА ИЗ ДОСТУПНЫХ")
            time.sleep(1)

def slots_kazino():
    global bal
    os.system("title Winddos слоты")
    if bal <= 4.9:
        print("Вам к сожелению нельзя, у вас менее 5 баллов")
        time.sleep(2)
    elif bal >= 5:

        os.system("cls")
        print("Добро пожаловать Сэр. У вас как раз есть 5 баллов для игры.")
        print()
        time.sleep(2)
        while True:
            os.system("cls")
            din2 = input("Будете играть? [1] or [] - начать играть, [q] - выйти. \n")
            if din2 == "q":
                break
            else:
                print("Начинаю крутить барабаны \nЖдите...")
                time.sleep(0.5)
                symf2 = ["₸", "$", "₽"]
                s1 = random.choice(symf2)
                s2 = random.choice(symf2)
                s3 = random.choice(symf2)
                print(f"| {s1} | {s2} | {s3} |")
                if s1 == s2 == s3:
                    print("Джекпот! Вы получили +7 баллов к балансу (старые 5 баллов не отнимались)")
                    bal += 7
                    time.sleep(2)
                elif s1 == s2 or s2 == s3 or s1 == s3:
                    print("Не джекпот, но и не выигрыш, деньги не отнимаются")
                    time.sleep(2)
                else:
                    print("Не повезло. Отнимаю 5 баллов.")
                    bal -= 5
                    if bal < 5:
                        print("У вас закончились баллы, уходите.")
                        time.sleep(2)
                        break
                    else:
                        continue
        
def btc_sel_buy():
    global bal
    global btc
    while True:
        os.system("cls") 
            
        print("--=== БАНК КРИПТОВАЛЮТ ===--")
        print(f"Ваш баланс: {bal}")
        print(f"На вашем крипто-кошельке: {btc}")
        print(f"Стоимость ДДос-коина (ОБНОВЛЯЕТСЯ РАЗ В 4 секунды): {price_btc}")
        print("-------------------------")
        print("Управление: \n[1] - Купить \n[2] - Продать \n[q] - Выйти \n[Enter] - обновить цены")
        kbank = input("user>>")
            
            
        if kbank == "1":
            fix_price = price_btc
            while True:
                try:
                    print(f"\nЦена зафиксирована: {fix_price}")
                    yk = input("Вы уверены? [1]-Да, [2]-Нет: ")
                    if yk == "1":
                        kbtc = int(input("Сколько купить?: "))
                        if kbtc <= 0:
                            print("Число должно быть больше 0")
                            continue
                            
                        ok_price = fix_price * kbtc
                        if bal < ok_price:
                            print(f"Недостаточно средств! Нужно {ok_price}")
                            time.sleep(2)
                            break
                        else:
                            btc += kbtc
                            bal -= ok_price
                            print("Оплата прошла успешно!")
                            time.sleep(2)
                            break
                    else:
                        break 
                except ValueError:
                    print("Ошибка! Вводи только цифры.")
                    time.sleep(1)

            
        elif kbank == "q":
            break
                

        elif kbank == "2":
            try:
                fix_price = price_btc
                pfix_price = fix_price * 0.70
                sbtc = float(input("Сколько ДДос-коинов вы хотите продать?:"))
                if btc >= sbtc:
                    potyes= input("Вы уверены? [1] - да, [2] - нет \n:")
                    if potyes== "1":
                        pbtc = int(sbtc * pfix_price)
                        btc -= sbtc
                        bal += pbtc
                        print("Продано. С комиссией 30%")
                        time.sleep(2)
                    else:
                        print()
                else:
                    print("Недостаточно ДДос-коинов на балансе")
                    time.sleep(2)
                if sbtc <= 0:
                    print("Вводите положительные числа.")
                    time.sleep(2)

            except ValueError:
                print("Вводите именно число.")
                time.sleep(2)
        

def mining_wdd():
    global bal
    global btc
    global gpu_level
    os.system("cls")
    os.system("title Майнинг.wdd")
 
    print("Подождите...")
    time.sleep(0.5)
    print("Компиляция...")
    time.sleep(1.5)
    print("Компиляция завершена, запуск...")
    
    for col in ["32", "52", "03", "23", "42", "32", "52", "03", "23", "42", "32", "52", "03", "23", "42", "25"]:
        os.system(f"color {col}")
        time.sleep(0.1)
    
    os.system("cls")
    time.sleep(0.7)
    os.system("color 2")
    print("Выберите действие: \n[1] - Майнинг ДДос-коинов \n[q] - выйти")
    while True:
        mrez = input("user/майнинг.wdd>>").lower()
        if mrez == "1":
            cikl = input("Сколько циклов выполнить? \nuser/майнинг.wdd>>")
            try:
                chanse_stope_police = random.randint(1, 1000)
                cikl_int = int(cikl)

                if chanse_stope_police <= 5:
                    print("🚨🚨🚨🚨🚨")
                    print("ПОЛИЦИЯ НАСТИГЛА ВАС")
                    print("штраф -35 баллов, -все ддос-коины")
                    bal -= 35
                    btc = 0

                    if bal <= 0:
                        bal = 0
                    else:
                        pass
                    break

                for i in range(cikl_int):
                    print("Начало майнинга...")
                    time.sleep(3)
                    base_income = random.uniform(0.01, 0.02)
                    rewmin = base_income * gpu_level
                    rewmin_k = round(rewmin, 2) #округление для облегчения продажи
                    btc = round(btc + rewmin_k, 2)
                    print(f"Цикл {i+1}/{cikl_int} завершено. \nДобыто: {rewmin_k}")
                print(f"Циклы были выполнены. Сумма ДДос-коинов на кошельке: {btc} \n")
            except ValueError:
                print("Введите число!!! \n")


        elif mrez == "q":
            break

def service_mining():
    while True:
        os.system("cls")
        os.system("title Service WinDDos")
        os.system("color 80")
        global bal
        global gpu_level
        global upgrade_cost_gpu
        print("Сервисный Центр WinDDos")
        print("-" * 50)
        print(f"Баланс: {bal}, Стоимость улучшения: {upgrade_cost_gpu}, Уровень видеокарты {gpu_level}")
        print("[1] - Улучшение видеокарты \n[2] - выход")
        dei_service = input(":")
        if dei_service == "1":
            print("Уверены покупать улучшение? \n[1] - Да \n[2] - Нет (выходит из сервиса)")
            dei_ser_2 = input(":")
            if dei_ser_2 == "1":
                if bal >= upgrade_cost_gpu:
                    print("Покупка...")
                    bal -= upgrade_cost_gpu
                    upgrade_cost_gpu = int(upgrade_cost_gpu * 1.5)
                    gpu_level += 1
                    print(f"Оплачено, Уровень GPU: {gpu_level}, Баланс: {bal} \nP.S. \nЯ добавлю в будущем улучшения времени майнинга.")
                    time.sleep(3)
                else:
                    print("Недостаточно баллов на балансе. \n(иди работай)")
                    time.sleep(2)
            elif dei_ser_2 == "2":
                break
        elif dei_service == "2":
            break

def novosti():
    global price_btc, current_news_text
    ddos_novost_plus = "[DDos-K] - Стоимость ДДос-коина выросла на 5 баллов!"
    ddos_novost_minus = "[DDos-K] - Произошла массовая атака майнерами, ДДос-коин упал в цене на 5 баллов"
    
    standart_news = [
        "Сегодня РКН заблокировал российский мессенджер MAX",
        "О великий def, без тебя нам будет плохо...",
        "Система WinDDoS работает стабильно."
    ]
    while True:
        choice = random.randint(1, 20)
    
        if choice == 1: 
            current_news_text = ddos_novost_plus
            price_btc += 5
        elif choice == 2:
            current_news_text = ddos_novost_minus
            price_btc -= 5
        else:
            current_news_text = random.choice(standart_news)
        time.sleep(2)

def delete():
    os.remove("save.json")

def auto_save():
    while True:
        time.sleep(7)
        save_game()

def main_wdd():
    global current_news_text
    global btc
    global bal
    while True:
        os.system("title Winddos main")
        os.system("cls")
        os.system("color 07")
        print("Mikrosoft Winddos [Version уйуйуйуйуй] \n(c) Корпорация Майкрософт (Mikrosoft Korporation). Все права не защищены.")
        print("-------------------------------------")
        print("Ваш баланс равен =", bal)
        print("Количество ДДос-коинов у вас =", btc)
        print("-------------------------------------")
        print("Новости:")
        print(current_news_text)
        print("Обновление новостей происходит раз в 2 секунды (нажмите Enter чтобы обновить).")
        print("-------------------------------------")
        print("Выберите режим из 3-х")
        rez = input("[1] - классический казик \n[2] - слоты \n[3] - покупка криптовалют \n[4] - Майнинг \n[5] - Сервис улучшения майнинга \n[del_s] - удалить сохранение \n[0] - Выйти из программы (ОБЯЗАТЕЛЬНО ДЛЯ СОХРАНЕНИЯ). \n\n:")
        if rez == "1":
            classik_kazino()
        elif rez == "2":
            slots_kazino()
        elif rez == "3":
            btc_sel_buy()
        elif rez == "4":
            mining_wdd()                     
        elif rez == "0":
            save_game()
            break
        elif rez == "5":
            service_mining()

proverka_OS()
potok_kurs = threading.Thread(target=kurs_btc, daemon=True)
novosti_potok = threading.Thread(target=novosti, daemon=True)
auto_save_potok = threading.Thread(target=auto_save, daemon=True)
potok_kurs.start()
novosti_potok.start()
auto_save_potok.start()
load_game()
main_wdd()
