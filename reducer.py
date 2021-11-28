import sys

def Nmaxelements(dic):
    final_list = {}
    for i in range(0, 10): 
        max1 = 0
        k =''
        for key,value in dic.items():     
            if value > max1:
                max1 = value;
                k = key
        del dic[k]
        final_list[k] = max1    
    print(final_list)
    
current_word = None
current_count = 0
word = None
my_dict = {}

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            my_dict [current_word] = current_count
        current_count = count
        current_word = word
if current_word == word:
    my_dict [current_word] = current_count
Nmaxelements(my_dict)
