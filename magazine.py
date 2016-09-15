# -*- coding: utf-8 -*-

while answer == "yes"
print ("ELECTRO PAY")
print (u"1)Playstaytion 4")
print (u"2)Xbox one")
print (u"3)Playstaytion 3")
numbertovara = int(input(u" Vedite nomer tovara kotoryi vam nujen:" ))
tovar1 = 350
tovar2 = 300
tovar3 = 170
if numbertovara == 1:
	kolvo1 = int(input(u"Vvedite kolichestvo tovara: "))
	summ1 = kolvo1*tovar1
	if summ1 != 0:
		print (u"itogo k oplate: ")
		print (summ1)
		money1 = int(input(u"vnesti oplatu: "))
		if money1 == summ1:
			print (u"Spasibo za pokupku Playstaytion 4")
			print (u"Приходите к нам еще")
		elif money1 > summ1:
			print (u"Спасибо за покупку Playstaytion 4")
			vernem1 = money1 - summ1
			print (u"Ваша сдача")
			print (vernem1)
			print (u"Приходите к нам еще")
		elif money1 < summ1:
			print (u"Недостаточно суммы для оплаты")
			print(u"Терминал вывел ваши деньги назад")
			print (money1)
if numbertovara == 2:
	kolvo1 = int(input(u"Введите количество товара: "))
	summ1 = kolvo1*tovar2
	if summ1 != 0:
		print (u"Итого к оплате: ")
		print (summ1)
		money1 = int(input(u"Внесите оплату: "))
		if money1 == summ1:
			print (u"Спасибо за покупку Xbox one")
			print (u"Приходите к нам еще")
		elif money1 > summ1:
			print (u"Спасибо за покупку Xbox one")
			vernem1 = money1 - summ1
			print (u"Ваша сдача")
			print (vernem1)
			print (u"Приходите к нам еще")
		elif money1 < summ1:
			print (u"Недостаточно суммы для оплаты")
			print(u"Терминал вывел ваши деньги назад")
			print (money1)
if numbertovara == 3:
	kolvo1 = int(input(u"Введите количество товара: "))
	summ1 = kolvo1*tovar3
	if summ1 != 0:
		print (u"Итого к оплате: ")
		print (summ1)
		money1 = int(input(u"Внесите оплату: "))
		if money1 == summ1:
			print (u"Спасибо за покупку Playstaytion 3")
			print (u"Приходите к нам еще")
		elif money1 > summ1:
			print (u"Спасибо за покупку Playstaytion 3")
			vernem1 = money1 - summ1
			print (u"Ваша сдача")
			print (vernem1)
			print (u"Приходите к нам еще")
		elif money1 < summ1:
			print (u"Недостаточно суммы для оплаты")
			print(u"Терминал вывел ваши деньги назад")
			print (money1)




