# https://stepik.org/lesson/2284240/step/9?thread=solutions&unit=2318722

def are_anagrams(s1, s2, *, start=0, end=-1, ignore_case=True):
    if ignore_case:
        s1, s2 = s1.lower(), s2.lower()
    return sorted(s1[start: end]) == sorted(s2[start: end])
        

words = input().split()

result = are_anagrams(words[0], words[1], ignore_case=False)