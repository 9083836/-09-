# numbers = [1, 2, 3, 4, 5, 6, 7]
# result = {}
# for num in numbers:
#     if num % 2 != 0:
#         result[num] = num**3

# print(result)



# numbers = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
# result = set()
# for num in numbers:
#     if num % 2 == 0:
#         result.add(num)

# print(result)




# numbers = []
# for num in range(0,10):
#     a = num*10
#     numbers.append(a)
# print(numbers)



# def num(n):
#     for i in range(n + 1):
#         if i % 7 == 0:
#             yield i

# n = 50
# for number in num(n):
#     print("Числа делящиеся на 7 до n: ",number, sep=' ')






    
from itertools import permutations

def filter_alpha(input_str):
    return ''.join(filter(str.isalpha, input_str))

def generate_unique_words(input_str):
    filtered_input = filter_alpha(input_str)
    unique_words = set()

    for i in range(1, len(filtered_input) + 1):
        for perm in permutations(filtered_input, i):
            unique_words.add(''.join(perm))
    
    sorted_unique_words = sorted(unique_words, key=lambda x: (len(x), x))
    return sorted_unique_words


user_input = input("Введите символ: ")
unique_words = generate_unique_words(user_input)
for word in unique_words:
    print(word)