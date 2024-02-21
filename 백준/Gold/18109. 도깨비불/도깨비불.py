s = input()

first = {'q', 'w', 'e', 'r', 'R', 't', 'T',
         'a', 's', 'd', 'f', 'g',
         'z', 'x', 'c', 'v'}
second = {'y', 'u', 'i', 'o', 'O', 'p', 'P',
         'h', 'j', 'k', 'l',
         'b', 'n', 'm'}
double_fs = {'rt', 'sw', 'sg', 'fr', 'fa',
           'fq', 'ft', 'fx', 'fv', 'fg', 'qt'}

s_len = len(s)
answer = 0
for i in range(1, s_len - 2):
    if s[i - 1] in second and s[i] in first and s[i + 1] in second:
        answer += 1
    elif s[i - 1] in second and s[i:i+2] in double_fs and s[i + 2] in second:
        answer += 1

if s[-3] in second and s[-2] in first and s[-1] in second:
    answer += 1
print(answer)