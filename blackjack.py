from random import sample, randint

class Blackjack:
	def __init__(self, balance):
		self.balance = balance
		self.bet = 0

		self.start()

	def start(self):
		enter = int(input("Введите 1, если хотите начать игру: \n"))
		
		if enter == 1:
			self.accept_bets()

	def accept_bets(self):
		self.bet = int(input(f"Сделайте ставку, чтобы начать игру! Ваш баланс: {self.balance} \n"))

		if self.bet < 25:
			print(f"Минимальная сумма ставки 25 фишек. Ваш баланс: {self.balance}")
		elif self.bet > self.balance:
			print(f"Недостаточно средств на счету. Ваш баланс: {self.balance}")
		else:
			self.balance -= self.bet
			self.card_allocation()

	def card_allocation(self):
		def card_generation():
			cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
			hands = {
				'player': sample(cards, 2),
				'dealer': sample(cards, 2),
			}

			return hands

		hands = card_generation()

		hands_player = sum(hands['player'])
		hands_dealer = sum(hands['dealer'])
		
		self.action(hands)

	def action(self, hands):
		print(f"\nВаша рука: {sum(hands['player'])}\nРука дилера: {sum(hands['dealer'])}\nВаш баланс: {self.balance}\n")

		action = int(input("Сделайте выбор:\n1) Нажмите 1, чтобы остановиться\n2) Нажмите 2, чтобы взять ещё одну карту\n"))

		if action == 1:
			self.end(hands)
		else:
			self.take_card(hands['player'], 'player')
			
			if sum(hands['player']) > 21:
				self.end(hands)
			else:
				self.action(hands)

	def take_card(self, list, who):
		if who == 'dealer':
			i = sum(list)
			while i < 17:
				new_card = randint(1, 11)
				list.append(new_card)
				i = sum(list)
			return list
		else:
			new_card = randint(1, 11)
			list.append(new_card)
			return list

	def end(self, hands):
		if sum(hands['dealer']) < 17:
			hands['dealer'] = self.take_card(hands['dealer'], 'dealer')

		if sum(hands['player']) > 21:
			print(f"\nПеребор!\nВаша рука: {sum(hands['player'])}\nРука дилера: {sum(hands['dealer'])}\nВаш баланс: {self.balance}\n")
			self.bet = 0

		elif sum(hands['dealer']) > 21:
			print(f"\nУ дилера перебор!\nВаша рука: {sum(hands['player'])}\nРука дилера: {sum(hands['dealer'])}\nВаш баланс: {self.balance}\n")
			self.balance += self.bet * 2
			self.bet = 0

		elif sum(hands['player']) > sum(hands['dealer']):
			print(f"\nВы победили!\nВаша рука: {sum(hands['player'])}\nРука дилера: {sum(hands['dealer'])}\nВаш баланс: {self.balance}\n")
			self.balance += self.bet * 2
			self.bet = 0

		elif sum(hands['player']) == sum(hands['dealer']):
			print(f"\nНичья!\nВаша рука: {sum(hands['player'])}\nРука дилера: {sum(hands['dealer'])}\nВаш баланс: {self.balance}\n")

		else:
			print(f"\nВы проиграли!\nВаша рука: {sum(hands['player'])}\nРука дилера: {sum(hands['dealer'])}\nВаш баланс: {self.balance}\n")
			self.bet = 0

		self.start()

Blackjack(1000)