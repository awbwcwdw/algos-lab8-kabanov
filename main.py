# Задача 1: Средние расходы по семестрам  
# Напишите программу, которая с помощью цикла `for` вычисляет средние расходы Джона за первый семестр (январь–июнь) и второй семестр (июль–декабрь). 

monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]

for i in monthly_spending:
    first = sum(monthly_spending[:6])/len(monthly_spending[:6])
    second = sum(monthly_spending[6:])/len(monthly_spending[6:])

print("Ср. Расходы 1семестр :",first)
print("Ср. Расходы 2семестр :",second)






# Задача 2: Кто тратил больше?  
# Напишите программу, которая сравнивает расходы Джона и Сэма по месяцам и подсчитывает количество месяцев, в которых Джон тратил больше.  

john_month = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]  
sam_month = [1969.62, 3939.37, 2241.59, 3968.27, 3068.80, 1755.02, 3885.66, 2491.67, 3828.49, 3171.32, 2771.32, 3380.37]
john = 0 
sam = 0

for i in range(12):
    if john_month[i] > sam_month[i]:
        john += 1
    elif john_month[i] < sam_month[i]:
        sam += 1
       
print("Траты Джона: ", john)
print("Траты Сэма: ", sam)





# Задача 3: Список друзей   
# Объедините оба списка в один, исключив дублирующиеся имена.

pfriends = ["Mary", "Tim", "Mike", "Henry"]  
tfriends = ["Tim", "Susan", "Mary", "Josh"]

all_friends = list((set(pfriends+tfriends)))
print("Все друзья :",all_friends)





# Задача 4: Общие друзья  
# Используя те же списки друзей Пола и Тины, напишите программу, которая с помощью цикла находит их общих друзей.  

paul_friends = ["Mary", "Tim", "Mike", "Henry"]  
tina_friends = ["Tim", "Susan", "Mary", "Josh"]

all_friends = list(set(paul_friends).intersection(tina_friends))
print("Общие друзья :",all_friends)





### Задача 5: Игроки в баскетбол    
# Напишите программу, которая определяет игроков, зарегистрированных только в баскетболе (не в футболе и не в волейболе). 

football_players = {"Eve", "Tom", "Richard", "Peter"}  
volleyball_players = {"Jack", "Hugh", "Peter", "Sam"}  
basketball_players = {"Eve", "Richard", "Jessica", "Sam", "Michael"}

basketball = set(basketball_players) - (football_players | volleyball_players)
print("Выбрали баскетболл :",basketball)




# Задача 6: Подсчёт голосов  
# Используя словарь, подсчитайте количество голосов за каждый язык.

poll_results = ["Python", "Java", "Javascript", "Python", "Javascript", "Python", "C", "Python", "Python", "C", "Javascript"]
py = poll_results.count("Python")
j = poll_results.count("Java")
js = poll_results.count("Javascript")
c = poll_results.count("C")

count_votes = []
count_votes.extend([py, j, js, c])
for q, w in zip(count_votes, poll_results): print("Количество голосов :",q, w)




# Задача 7: Подсчёт очков  
# Создайте словарь, где ключами будут имена игроков, а значениями — их суммарные очки.  

score = [('Mike', 10), ('Mike', 8), ('Mike', 6), ('John', 7), ('John', 8), ('John', 5), ('Tom', 8), ('Tom', 9), ('Tom', 8)]
dict_scores = {}
for i, num in score:
    if i in dict_scores:
        dict_scores[i] += num 
    else:
        dict_scores[i] = num

print("Очки :",dict_scores)




# ### Задача 8: Статистика списка   
# Напишите функцию, которая возвращает максимальное значение, сумму и среднее арифметическое чисел в списке.  

numbers = [10, 3, 5, 9, 18, 3, 0, 7]

def new_funс():
    print("Максимум :",max(numbers))
    print("Сумма :",sum(numbers))
    print("Среднее :",sum(numbers) / len(numbers))

new_funс()




# ### Задача 9: Длинные и короткие слова  
# Напишите программу, которая определяет самое длинное и самое короткое слово в списке.  

word_list = ["apple", "airplane", "carrot", "elephant", "guitar", "moonlight"]
max = ""
min = word_list[0]
for i in word_list:
    if len(i) > len(max):
        max = i       
    elif len(i) < len(min):
        min = i
print("максимум слов: ", max)
print("минимум слов: ", min)




# ### Задача 10: Фильтрация по частоте  
# Создайте новый список, содержащий только числа, которые встречаются в оригинальном списке не менее трёх раз.  

number_list = [5, 8, 2, 7, 3, 5, 6, 9, 2, 4, 8, 7, 2, 5, 3]
count = []
for i in number_list:
    if number_list.count(i) >= 3:       
        if count.count(i) == 0:
            count.append(i)

print("3повтора :",count)





# ### Задача 11: Второй лучший результат  
# Напишите программу, которая определяет второй по величине результат в списке.  

exam_results = [23, 78, 96, 32, 53, 67, 23, 98, 33, 38, 45, 39, 86, 12, 43, 45]

exam_results.sort(reverse=True)
print("2 по величине :",exam_results[1])
