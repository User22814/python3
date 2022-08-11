text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eu magna sit amet neque lobortis dignissim. " \
       "Mauris vehicula lacinia bibendum. Phasellus elementum ipsum et mi mollis, sed eleifend elit pharetra. Donec " \
       "interdum tempus ligula non vulputate. Cras mollis rhoncus facilisis. Fusce at viverra magna, id tempor nulla. " \
       "Quisque at felis eget arcu gravida efficitur eget ac enim. Etiam quisque efficitur lorem at lorem dictum, " \
       "a sagittis ipsum pulvinar. Maecenas elit nisi, iaculis a dolor id, tempor molestie dolor. Pellentesque " \
       "aliquet non orci at convallis. Donec laoreet nisl quam. Ut accumsan, dui ut mattis ultricies, " \
       "est nulla semper est, eget pulvinar magna lacus ut risus." \
       "Duis sed hendrerit odio. Etiam scelerisque nunc quis placerat interdum. Nam condimentum enim ac justo " \
       "fermentum, et imperdiet purus finibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Mauris " \
       "bibendum urna vitae ullamcorper pellentesque. Aenean in est vitae felis semper vulputate convallis eu quam. " \
       "Nullam feugiat elementum libero. Donec scelerisque finibus laoreet. Nam eu risus facilisis, iaculis urna " \
       "vitae, aliquam neque. Donec elementum ipsum in pretium maximus." \
       "Integer id nulla commodo elit ultricies sollicitudin vel vitae augue. Proin commodo, magna at bibendum rutrum, " \
       "odio risus dictum nisi, ac commodo ipsum dolor vitae purus. Maecenas posuere, est id vulputate porta, " \
       "erat lacus efficitur purus, a mattis justo ligula eu felis. Suspendisse potenti. Mauris commodo libero ut dui " \
       "efficitur malesuada. Donec ultricies vel purus vel pellentesque. Etiam fusce a ex in libero rutrum placerat " \
       "suscipit ac tellus. Etiam dignissim ullamcorper tincidunt. Proin tempor lorem eu nulla euismod, " \
       "id sollicitudin massa ultricies. "

word = 'etiam'
flag = False
index = 0
place = []
find_word = 0
while find_word != -1:
    find_word = text.lower().find(word, index)
    place.append(find_word)
    # print(find_word)
    index = find_word + len(word)
place.pop(-1)
print(f"1. Количество вхождение подстроки {word} = {len(place)} \n")

list_unicode = []

for i in range(len(text)):
    list_unicode.append(ord(text[i]))

all_string = ", ".join(str(x) for x in list_unicode)
print("2. Перевести каждый элемент предыдущего текста в числовые значения по юникоду:")
print(all_string + "\n")

list_unicode.sort(reverse=True)

all_string_reverse = ", ".join(str(x) for x in list_unicode)
print("3. Отсортировать в обратном порядке полученную итоговую строку:")
print(all_string_reverse)
