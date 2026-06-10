from datetime import date
class BirthDay(object):
	"Очень функциональный поздравлятор"
	months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
	def __init__(self, d):
		self.dates = d
		self.talk(self.dates)
		self.first_menu()

	def delete_or_rename_dates(self):
		collection = ["0"]
		for i in range(len(self.dates)):
			print(f"{i+1}) {" ".join(self.dates[i])}")
			collection += [str(i+1)]
		number_date = ""
		while not str(number_date).isdigit() or str(number_date) not in collection:
			number_date = input("\nВведите номер записи (0 - отмена): ")
			if not str(number_date).isdigit() or str(number_date) not in collection:
				print(f"Запись {number_date} не найдена, повторите попытку")
			else:
				number_date = int(number_date)
		return number_date

	def test_date(self, date):
		if len(date[0][:-1].split()) != 2 or date[2] not in BirthDay.months:
			int("error)")

	def day_today(self):
		today = str(date.today()).split("-")[1:]
		for i in range(len(today)):
			if today[i][0] == "0":
				today[i] = today[i][1:]
		return today

	def question(self):
			self.choice = input("Выбор: ")
			print()

	def first_menu(self):
		print(
			"\n[Главное]",
			"1 - Список ДР",
			"2 - Сегодняшние и ближайщие ДР",
			"3 - Добавление записей ДР",
			"4 - Удаление записей ДР",
			"5 - Редактирование записей ДР",
			"0 - Сохранить и выйти",
			sep="\n", end = "\n\n"
		)
		self.question()
		if self.choice == "1":
			self.talk(self.dates)
			self.second_menu()
		elif self.choice == "2":
			self.today_near(self.sorting(self.dates, notalk = True))
			self.second_menu(sort = False, fp = False)
		elif self.choice == "3":
			self.append_dates()
			self.first_menu()
		elif self.choice == "4":
			self.delete_dates()
			self.first_menu()
		elif self.choice == "5":
			self.rename_dates()
			self.first_menu()
		elif self.choice == "0":
			self.save_and_exit()
		else:
			print(f"error: пункт \"{self.choice}\" не найден")
			self.first_menu()

	def talk(self, dates, show_menu = False):
		if dates:
			for i in dates:
				print(" ".join(i))
		else:
			print("<список пуст>")

	def today_near(self, dates):
		if dates:
			today = self.day_today()
			today_dates = []
			near_dates = self.future_past(self.dates, notalk = True)[:3]
			print(near_dates)
			for i in dates:
				if i[2] == BirthDay.months[int(today[0])-1] and i[1] == today[1]:
					today_dates.append(i)
			
			today_dates.insert(0, ["Сегодняшние ДР:"])
			if len(today_dates) == 1:
				today_dates.insert(1, ["<список пуст>"])
			near_dates.insert(0, ["Ближайшие ДР:"])
			if len(near_dates) == 1:
				near_dates.insert(1, ["<список пуст>"])
			dates = today_dates + ["\n"] + near_dates
			self.talk(dates)

	def append_dates(self):
		name = input("Имя (например, Иван ): ")
		surname = input("Фамилия (например, Иванов): ")
		day_bitrhday = input("День рождения (например, 1 апреля): ").lower().split()
		try:
			date = [f"{name} {surname}:", day_bitrhday[0], day_bitrhday[1]]
			self.test_date(date)
		except:
			print("error: некорректный ввод")
			self.first_menu()
		confirm = None
		while confirm not in ("y", "n"):
			confirm = input(f"Добавить запись {" ".join(date)}? y/n: ").lower()
		if confirm == "y":
			self.dates.append(date)
			if date in self.dates:
				print("Запись успешно добавлена!")
		else:
			print("Отменено")

	def delete_dates(self):
		print("Какую запись желаете удалить?\n")
		delete_date = self.delete_or_rename_dates()-1
		if delete_date+1:
			confirm = None
			while confirm not in ("y", "n"):
				confirm = input(f"Удалить запись {' '.join(self.dates[delete_date])}? y/n: ").lower()
			if confirm == "y":
				del self.dates[delete_date]
				print("Запись успешно удалена!")
			else:
				print("Отменено")
		else:
			print("Отменено")

	def rename_dates(self):
		print("Какую запись желаете редактировать?\n")
		rename_date = self.delete_or_rename_dates()-1
		if rename_date+1:
			name = input("Новое Имя: ")
			surname = input("Новая Фамилия: ")
			day_bitrhday = input("Новый День рождения: ").lower().split()
			try:
				date = [f"{name} {surname}:", day_bitrhday[0], day_bitrhday[1]]
				self.test_date(date)
			except:
				print("error: некорректный ввод")
				self.first_menu()
			confirm = None
			while confirm not in ("y", "n"):
				confirm = input(f"\nРедактировать запись:\n{" ".join(self.dates[rename_date])}\nНа:\n{" ".join(date)}? y/n: ").lower()
			if confirm == "y":
				self.dates[rename_date] = date
				print("Запись успешно изменена!")
			else:
				print("Отменено")
		else:
			print("Отменено")

	def save_and_exit(self):
		self.files_dates = open("HappyDayBase.txt", "w", encoding="utf-8")
		write_st = ""
		for i in self.dates:
			write_st += " ".join(i) + "\n"
		write_st = write_st[:-1]
		self.files_dates.write(write_st)
		self.files_dates.close()

	def second_menu(self, sort = True, fp = True):
		save_sort = sort
		save_fp = fp
		choice_range = {"0"}
		print("\n[Доп возможности]")
		if sort:
			print("1 - Сортировка")
		if fp:
			print("2 - Текущие/Прошедшие")
		print("0 - Главное меню\n")
		self.question()
		if sort:
			choice_range.add("1")
			if self.choice == "1":
				self.sorting(self.dates)
				self.second_menu()
		if fp:
			choice_range.add("2")
			if self.choice == "2":
				self.future_past(self.sorting(self.dates, notalk = True))
				self.second_menu()
		if self.choice == "0":
			self.first_menu()
		if self.choice not in choice_range:
			print(f"error: пункт \"{self.choice}\" не найден")
			self.second_menu(save_sort, save_fp)

	def sorting(self, dates, notalk = False):
		if dates:
			for i in range(len(dates)-1):
				min = i
				for j in range(i+1, len(dates)):
					if dates[j][2] != dates[min][2]:
						if BirthDay.months.index(dates[j][2]) < BirthDay.months.index(dates[min][2]):
							min = j
					else:
						if int(dates[j][1]) < int(dates[min][1]):
							min = j
				dates[i], dates[min] = dates[min], dates[i]
			if notalk:
				return dates
		self.talk(dates)

	def future_past(self, dates, notalk = False):
		if dates:
			future_dates = []
			past_dates = []
			today = self.day_today()
			for i in dates:
				if (BirthDay.months.index(i[2])+1 > int(today[0])) or (BirthDay.months.index(i[2])+1 == int(today[0]) and int(i[1]) >= int(today[1])):
						future_dates.append(i)
				else:
					past_dates.append(i)
			if notalk:
				return future_dates
			future_dates.insert(0, ["Текущие:"])
			past_dates.insert(0, ["Прошедшие:"])
			dates = future_dates + ["\n"] + past_dates
			self.talk(dates)
def main():
	file_dates = open("HappyDayBase.txt", "a+", encoding="utf-8")
	file_dates.seek(0)
	dates = file_dates.read().split("\n")
	file_dates.close()
	if not dates[0]:
		dates = []
	for i in range(len(dates)):
		dates[i] = dates[i].split()
		if len(dates[i]) == 4:
			dates[i][0] = dates[i][0] + " " + dates[i].pop(1)
	print("Поздравлятор v1.0\n")
	congrat = BirthDay(dates)
main()