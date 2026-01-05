ИГРА

import random
import time

print("🎮 ДОБРО ПОЖАЛОВАТЬ В ИГРУ!")
print("=" * 40)

# Простая игра "Угадай число"
def guess_game():
    print("\n🎯 ИГРА: УГАДАЙ ЧИСЛО")
    secret = random.randint(1, 5)
    
    for attempt in range(3):
        try:
            guess = int(input(f"Попытка {attempt + 1}/3. Число от 1 до 5: "))
            
            if guess == secret:
                print("🎉 УГАДАЛ! +10 очков")
                return 10
            elif guess < secret:
                print("⬆️ Больше!")
            else:
                print("⬇️ Меньше!")
        except:
            print("⚠️ Введи число!")
    
    print(f"😔 Не угадал! Число было: {secret}")
    return 0

# Игра "Камень-Ножницы-Бумага"
def rps_game():
    print("\n✊✌️✋ КАМЕНЬ-НОЖНИЦЫ-БУМАГА")
    choices = ["камень", "ножницы", "бумага"]
    
    while True:
        player = input("Выбери: камень, ножницы, бумага (или 'выход'): ").lower()
        
        if player == "выход":
            break
        if player not in choices:
            print("⚠️ Такого варианта нет!")
            continue
        
        computer = random.choice(choices)
        print(f"🤖 Компьютер выбрал: {computer}")
        
        if player == computer:
            print("🤝 Ничья!")
        elif (player == "камень" and computer == "ножницы") or \
             (player == "ножницы" and computer == "бумага") or \
             (player == "бумага" and computer == "камень"):
            print("🎉 Ты выиграл!")
        else:
            print("😔 Ты проиграл!")
        
        print()

# Главное меню
score = 0

while True:
    print("\n" + "=" * 40)
    print("           ГЛАВНОЕ МЕНЮ")
    print("=" * 40)
    print(f"Твой счет: {score}")
    print("1. Угадай число")
    print("2. Камень-Ножницы-Бумага")
    print("3. Выход")
    print("=" * 40)
    
    choice = input("Выбери игру (1-3): ")
    
    if choice == "1":
        score += guess_game()
    elif choice == "2":
        rps_game()
    elif choice == "3":
        print(f"\n📊 Игра окончена! Твой финальный счет: {score}")
        print("Спасибо за игру! 👋")
        break
    else:
        print("❌ Такого варианта нет!")
    
    time.sleep(1)

input("\nНажми Enter чтобы выйти...")