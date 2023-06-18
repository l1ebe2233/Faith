# def counter(s): # 0(N * M) кол во уникальных * на общее кол во значений
#     for i in set(s): # set приобразовывает обьект к множеству(вытаскивает только уникальные значения)
#
#         count = 0
#         for j in s:
#             if i == j:
#                 count += 1
#         print(i, count)
#
# counter("abbd")


# s = "aa ab b cd"
# print(len(s.split()))



# def counter(s): # 0(N)
#     syms = {}
#     for i in s:
#         syms[i] = syms.get(i, 0) + 1
#     for i, count in syms.items():
#         print(i, count)
# counter("abbdgfttyuu")




def polindrom(orb):
    a = orb
    b = a[::-1]
    if a == b:
        print(True)
    else:
        print(False)

polindrom('сос')




        
