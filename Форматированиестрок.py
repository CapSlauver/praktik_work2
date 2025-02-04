# Входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 350.4  # Задано согласно условию задачи
# Расчет challenge_result
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

# Использование %
string_percent_1 = "В команде Мастера кода участников: %d ! " % team1_num
string_percent_2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

# Использование format()
string_format_1 = "Команда Волшебники данных решила задач: {} !".format(score_2)
string_format_2 = " Волшебники данных решили задачи за {} с !".format(team1_time)

# Использование f-строк
string_f_1 = f"Команды решили {score_1} и {score_2} задач."
string_f_2 = f"Результат битвы: {challenge_result}"
string_f_3 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."


# Вывод
print(string_percent_1)
print(string_percent_2)
print(string_format_1)
print(string_format_2)
print(string_f_1)
print(string_f_2)
print(string_f_3)