import random
from decouple import config

initial_capital = config('MY_MONEY', default=1000)


def play_casino_game():
    current_balance = int(initial_capital)

    while current_balance > 0:
        try:
            selected_slot = int(input(f"У вас есть ${current_balance}. Выберите слот (1-30): "))
        except ValueError:
            print("Введите правильное число.")
            continue

        if selected_slot < 1 or selected_slot > 30:
            print("Выберите число от 1 до 30.")
            continue

        try:
            bet = int(input(f"Сколько вы хотите поставить на слот {selected_slot}? "))
        except ValueError:
            print("Введите правильную сумму.")
            continue

        if bet > current_balance:
            print("У вас недостаточно средств для этой ставки.")
            continue

        winning_slot = random.randint(1, 30)
        print(f"Вы выбрали слот {selected_slot}. Выигрышный слот: {winning_slot}")

        if selected_slot == winning_slot:
            current_balance += bet * 2
            print(f"Поздравляем! Вы выиграли ${bet}! Ваш текущий баланс: ${current_balance}")
        else:
            current_balance -= bet
            print(f"Вы проиграли ${bet}. Ваш текущий баланс: ${current_balance}")

        play_again = input("Хотите сыграть еще? (да/нет): ").lower()
        if play_again != 'да':
            break

    print(f"Игра окончена. Ваш итоговый баланс: ${current_balance}")


if __name__ == "__main__":
    play_casino_game()
