#!/usr/bin/env python


class BankAccount:
	'''a class to represent a Bank Account'''
	Account_number = 0
	def __init__(self,balance):
		self.balance = balance
		BankAccount.Account_number += 1
		self.Account_number = BankAccount.Account_number

	def __str__(self):
		return "Account number: " + str(self.Account_number) + "\n" + "Balance: " + str(self.balance)

	def lodge(self,amount):
		 self.balance += amount

	def withdraw(self,amount):
		self.balance -= amount

if __name__ == '__main__':
	account1 = BankAccount(1000)
	account2 = BankAccount(1500)
	print account1
	print account2
	account2.withdraw(500)
	account1.lodge(500)
	print account1
	print account2

