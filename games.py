import random

money = 100

#Write your game of chance functions here

#COIN FLIP

def coin_flip(guess,bet):
  print("Game: Coin Flip")
  flip = random.choice([1,2])
  guess.lower()
  guess.strip(" ")
  guess.strip("!")

  if bet <= money and bet > 0:
    if guess == "heads" and flip == 1:
      print("You won " + str(bet) + " euros.")
      return bet
    elif guess == "tails" and flip == 2:
      print("You won " + str(bet) + " euros.")
      return bet
    else:
      print("You lost " + str(bet)  + " euros.")
      return 0
  elif bet <= 0:
    print("That bet is not valid!")
    return 0
  else:
    print("Can't play, not enough money!")
    return 0



#CHO-HAN

def cho_han(prediction,bet):
    print("\nGame: Cho Han")

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result = dice1 + dice2

    if bet <= money and bet > 0:
      if result % 2 == 0 and prediction == "Even":
        print("You won " + str(bet) + " euros.")
        return bet

      if result % 2 != 0 and prediction == "Odd":
        print("You won " + str(bet) + " euros.")
        return bet

      else:
        print("You lost " + str(bet)  + " euros.")
        return (-bet)
    elif bet <= 0:
      print("That bet is not valid!")
      return 0
    else:
      print("Can't play, not enough money!")
      return 0

#Random Card

def random_card(bet):
    print("\nGame: Random Card")

    deck = list(range(1,14)) + list(range(1,14)) + list(range(1,14)) + list(range(1,14))
    player1 = random.choice(deck)
    deck.remove(player1)
    player2 = random.choice(deck)

    if bet <= money and bet > 0:

      if player1 > player2:
        print("You won " + str(bet) + " euros.")
        return bet

      if player1 == player2:
        print("It's a draw!\nYou don't lose or win anything.")
        return 0

      else:
        print("You lost " + str(bet)  + " euros.")
        return (-bet)

    elif bet <= 0:
      print("That bet is not valid!")
      return 0

    else:
      print("Can't play, not enough money!")
      return 0

#Roulette

def roulette(even,digits,bet):
  print("\nGame: Roulette")

  roulette_number = random.randint(1,36)
  print("It's a " + str(roulette_number))

  if bet <= money and bet > 0:

    if roulette_number % 2 == 0 and even == "Even":
      if roulette_number > 9 and digits == "00":
        print("You won " + str(bet) + " euros.")
        return bet
      if roulette_number < 9 and digits == "0":
        print("You won " + str(bet) + " euros.")
        return bet

    if roulette_number % 2 != 0 and even == "Odd":
      if roulette_number > 9 and digits == "00":
        print("You won " + str(bet) + " euros.")
        return bet
      if roulette_number < 9 and digits == "0":
        print("You won " + str(bet) + " euros.")
        return bet

    else:
      print("You lost " + str(bet)  + " euros.")
      return (-bet)

  elif bet <= 0:
    print("That bet is not valid!")
    return 0
  else:
    print("Can't play, not enough money!")
    return 0


#Call your game of chance functions here

money += coin_flip("Heads", 10)

print("You now have " + str(money) + " euros!")

money += cho_han("Odd", 20)

print("You now have " + str(money) + " euros!")

money += random_card(20)

print("You now have " + str(money) + " euros!")

money += roulette("Odd","00",30)

print("You now have " + str(money) + " euros!")
