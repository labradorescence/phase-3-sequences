# # #!/usr/bin/env python3

# #  [0, 1, 1, 2, 3, 5, 8, 13, 21]
# #  n[x] + n[x+1] = n[x+2]

#Greem's solution
# def print_fibonacci(length):
   
#     x = 0

#     if length == 0:
#         fiblist = []
#         return fiblist
#     elif length == 1:
#         fiblist = [0]
#         return fiblist
#     elif length == 2:
#         fiblist = [0, 1]
#         return fiblist
#     else:
#         fiblist = [0, 1]
    
#         while(x < length-2):
#             fiblist.append(fiblist[x] + fiblist[x+1])
#             x += 1

#         print(fiblist)
#         return fiblist

# print(print_fibonacci(9))


### Eleanor's solution #####
# def print_fibonacci(n):
#     sequence = [0, 1]

#     for i in range (n - 2):
#         next = sequence[-2] + sequence[-1]
#         sequence.append(next)

#     print(sequence)
#     return sequence

# print(print_fibonacci(9))



### solution that passes all the test
# def print_fibonacci(length):
#     pass
#     fibonacci_sequence = []
#     if length > 0:
#         fibonacci_sequence.append(0)
#         if length > 1:
#             fibonacci_sequence.append(1)
#             if length > 2:
#                 for i in range(2, length):
#                     fibonacci_sequence.append(
#                         fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])

#     print(fibonacci_sequence)
