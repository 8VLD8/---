import random
import time

print("🎮 Привет, давай поиграем!")
print("=" * 40)


def guess_game():
    print("\n🔫 ИГРА: Недо-Русская рулетка")
    secret = random.randint(1, 6)
    
    for attempt in range(1):
        try:
            guess = int(input(f"У тебя {attempt + 1} попытка, угадай в какой ячейке находится пуля в шестизарядном револьвере : "))
            
            if guess == secret:
                print("🎉 Поздравляю ты выжил!")
                return 10
        except:
            print("⚠️ Давай выбирай!")
    
    print(f"💀 Не угадал(а) и получаешь пулю! Пуля была в {secret} ячейке барабана")
    return 0


def rps_game():
    print("\n  Камень-Ножницы-Бумага Super Edition")
    choices = ["1", "2", "3", "4", "5"]
    
    while True:
        player = input("Выбери: камень(1), ножницы(2), бумага(3), ящерица(4), спок(5) (или 'выход(6)'): ").lower()
        
        if player == "6":
            break
        if player not in choices:
            print("⚠️ Такого варика нету, давай по-внимательнее!!!")
            continue
        
        computer = random.choice(choices)
        print(f"🤖 Ботяра Пупень выбрал: {computer}")
        
        if player == computer:
            print("🤝 Ничья, продолжаем!")
        elif (player == "1" and computer == "2") or \
             (player == "1" and computer == "4") or \
             (player == "2" and computer == "3") or \
             (player == "2" and computer == "4") or \
             (player == "3" and computer == "1") or \
             (player == "3" and computer == "5") or \
             (player == "4" and computer == "5") or \
             (player == "4" and computer == "3") or \
             (player == "5" and computer == "2") or \
             (player == "5" and computer == "1"): 


            print("🎉 Ты выиграл поздравляю!")
        else:
            print("😔 Ты проиграл к сожалению, может по новой?")
        
        print()


score = 0

while True:
    print("\n" + "=" * 40)
    print("           ГЛАВНОЕ МЕНЮ")
    print("=" * 40)
    print(f"Твой счет: {score}")
    print("1. Недо-Русская рулетка")
    print("2. Камень-Ножницы-Бумага Super edition")
    print("3. Выход")
    print("=" * 40)
    
    choice = input("Выберай игру и давай посмотрим на сколько больша твоя удача (1-3): ")
    
    if choice == "1":
        score += guess_game()
    elif choice == "2":
        rps_game()
    elif choice == "3":
        print(f"\n📊 Игра окончена! Твой финальный счет: {score}")
        print(" Спасибо за игру, бывай! 👋")
        break
    else:
        print("❌ Такого варианта нема!")
    
    time.sleep(1)

input("\nНажми Enter чтобы выйти...")