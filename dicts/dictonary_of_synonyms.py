# https://stepik.org/lesson/488831/step/4?unit=480067

n = int(input())
synons = {}

for _ in range(n):
    words = input()
    syn1, syn2 = words.split()
    synons[syn1] = syn2
    synons[syn2] = syn1

word = input()

print(synons[word])