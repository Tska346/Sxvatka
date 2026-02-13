import random
from random import randint
rand = random.SystemRandom()
price_damage = 1200
price_xp = 1000
price = 300
reward = 0
coin = 0
finalstage = 6
power = 0
p = 3
pv = 3
standartuser = 100
xp = 100
xpv = 50
stage = 1
nagrada = 0
d = randint(1,20)
b = randint(1,20)
w = 0
while True:
    try:

        A = input("Выберите уровень сложности! Простой(1) Средний(2) Тяжёлый(3): ")
        
        # Преобразуем строку в целое число
        A = int(A)
        
        if A in [1, 2, 3]:
            break  
        else:
            print("Ошибка! Нужно ввести цифру 1, 2 или 3.")
    
    except ValueError:
        print("Ошибка! Вы ввели не число. Попробуйте снова!")
if A == 1:
    sl = 1
    coin = 600
    xpv = 50
    reward = 300
    nagrada = 300
if A == 2:
    sl = 2
    coin = 1000
    xpv = 70
    reward = 600
    nagrada = 600
if A == 3:
    sl = 3
    coin = 2000
    xpv = 100
    reward = 1000
    nagrada = 1500
standart = xpv
print("Добро пожаловать в схватку сражайсесь с врагами для победы! Чтоб прочитать правила нажмите 6 ")
while True:
    vr = True
    print('Чтобы открыть магазин нажмите 5 ')
    print(f"Задача дойти до {finalstage} стадии, Жизни врага {xpv} хп ,Ваши жизни {xp} хп Ваша стадия {stage} " )
    print (f"Врагу выпало: {d}")
    print(f'Вам Выпало {b} ')
    print(f'Перебросов осталось {p} У врага осталось {pv}')
    print(f"Количество монет {coin} ")
    while True:
        try:
            v = int(input('Вы можете атаковать(1) лечиться(2) перебросить кубик(3) выйти из игры(4):'))
        
   
            if v in [1, 2, 3, 4, 5, 6]:  
                break  
            else:
                print("Ошибка! Нужно ввести цифру 1, 2, 3, 4, 5 или 6.")  
    
        except ValueError:
            print("Ошибка! Вы ввели не число. Попробуйте снова!")  
    if v == 1:
        xpv = xpv - b
        b = randint(1,20)
        while vr:
            if d < 10 and pv != 0 and xpv > 0:
                d = randint(sl,20) 
                pv = pv - 1
            if xpv > 25 and xpv > 0 or d >= xp and xpv > 0:
                xp = xp - d
                d = randint(sl,20)
                vr = False
            if xpv <= 25 and xpv > 0:
                xpv = xpv + d
                d = randint(sl,20)
                if  xpv > standart:
                    xpv = standart
                    vr = False
                else:
                    vr = False
            if xpv <= 0:
                print("Победа!")
                vr = False
            
    if v == 2:
        xp = xp + b
        b = randint(1,20)
        if xp > standartuser:
            xp = standartuser
        while vr:
            if d  < 10 and pv != 0 and xpv > 0:
                d =randint(sl,20)
                pv = pv - 1
            if xpv > 25  and xpv > 0:
                xp = xp - d
                d = randint(sl,20)
                vr = False
            if xpv <= 25 and xpv > 0:
                xpv = xpv + d
                d = randint(sl,20)
                if  xpv > standart:
                    xpv = standart
                    vr = False
                else:
                    vr = False
                Xod = 1
            
    if v == 3 and p != 0:
        b = randint(1,20)
        p = p - 1
    if v == 3 and p == 0:
        print("У тебя не осталось перебросов!")
    if v == 4:
        break
    if v == 5:
        while True:
            try:
                purchase = int(input("Что ты хочешь купить? 1(Переброс) 2(Зелье лечения!) 3(зелье урона) 4(Сведенья) 5(Выход!):"))
                if purchase in [1, 2, 3, 4, 5]:  
                    break  
                else:
                    print("Ошибка! Нужно ввести цифру 1, 2, 3, 4  или 5.")  
    
            except ValueError:
                print("Ошибка! Вы ввели не число. Попробуйте снова!")  
        if purchase == 1:
            while True:
                try:
                    purchasep =int(input(f"Купить переброс за {price} монет! 1(да) 2(нет):"))  
                    if purchasep in [1, 2]:  
                        break  
                    else:
                        print("Ошибка! Нужно ввести цифру 1, 2")  
    
                except ValueError:
                    print("Ошибка! Вы ввели не число. Попробуйте снова!") 
            if purchasep == 1 and coin >= price:
                coin = coin - price
                price = price + 300
                p = p + 1
            elif purchasep == 2:
                print("Ладно!")
            elif purchasep == 1 and coin < price:
                print("У тебя не хватает денег!")
        if purchase == 2:
            while True:
                try:
                    purchase_xp = int(input(f"Купить зелье лечение за {price_xp} 1(Да) 2(Нет):"))
                    if purchase_xp in [1, 2]:  
                        break  
                    else:
                        print("Ошибка! Нужно ввести цифру 1, 2")  
    
                except ValueError:
                    print("Ошибка! Вы ввели не число. Попробуйте снова!") 
            if purchase_xp == 1 and coin >= price_xp and xp < standartuser:
                coin = coin - price_xp
                price_xp = price_xp + 1000
                xp = xp + (standartuser / 5)
            elif purchase_xp == 1 and coin >= price_xp and xp == standartuser:
                print("У тебя и так полное здоровье! Зачем тебе зелье? Или тебе просто нравится его вкус!")
            elif purchase_xp == 2:
                print("Ну хорошо посмотрим надолго ли тебя хватит!")
            elif purchase_xp == 1 and coin < price_xp:
                print("У тебя не хватает денег!")
        if purchase == 3:
            while True:
                try:
                    purchase_damage = int(input(f"Купить зелье лечение за {price_damage} 1(Да) 2(Нет):"))
                    if purchase_damage in [1, 2]:  
                        break  
                    else:
                        print("Ошибка! Нужно ввести цифру 1, 2")  
    
                except ValueError:
                    print("Ошибка! Вы ввели не число. Попробуйте снова!") 
            if purchase_damage == 1 and coin >= price_damage:
                xpv = xpv - 25
                coin = coin - price_damage
                price_damage = price_damage + 1200
            elif purchase_damage == 2:
                print("Хорошо враг останется целее чем тебе хотелось бы!")
            elif purchase_damage == 1 and coin < price_damage:
                print("У тебя не хватает денег!")
        if purchase == 4:
            print("Переброс: позволяет Поменять своё значения на кубике!")
            print("Зелье лечения:Лечит 20 % от максимального здоровья!")
            print("Зелье урона: наносит 25 урона врагу!")
        if purchase == 5:
            print("Хорошо приходи когда тебе понадобятся мои товары!")
    if v == 6:
        print("Правила игры Нужно уничтожать врагов тем самым проходить стадии игры каждую стадию жизнь врага будет повышаться на десятку.")
        print("Вы ходите первым потом ходит враг Вы как и враг можете атаковать лечиться или перебрасывать кубик.")
        print("После каждой победы над боссом повышается сила Врагов Которые добавляют им  и тебе количество перебросов!")
        print("Ты можешь покупать предметы за деньги падающие с врагов! тем самым повышая свои шансы! Без них я скажу не обойитись.")
        print("На этом всё удачной игры!")
    if xp <= 0:
        print(f"Вы проиграли! Пройденно Стадий  {stage}")
        break
    if xpv <= 0:
        standart = standart + 10
        xpv = standart
        stage = stage + 1
        p = 3 + power
        pv = 3 + power
        xp = standartuser
        coin = coin + reward
        reward = reward + nagrada
        d = randint(sl,20)
        if stage != 22:
            print("Новый враг Приготовся")
    if stage > finalstage:
        finalstage = finalstage + 5
        standartuser = standartuser + 50
        xp = standartuser
        power = power + 1
        w = 0
        print("lvl up!")
        coin = coin + 1000
    if stage == finalstage and w == 0:
        print("Босс! Опастность у него есть пять перебросов  не забывай силу врагов!")
        pv = 5 + power
        w = w + 1
    if stage == 21:
        print("Финальный Босс! Последняя схватка Посмотрим как ты победишь!")
    if stage == 22:
        print("Ты победил! Из тебя получился отличный боец! Теперь ты Главный босс!")
        print(f"Вы заработали {coin} Монет!")
        break