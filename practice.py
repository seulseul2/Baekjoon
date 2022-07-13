import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alphabet = list(input().rstrip().split())
alphabet.sort()
word = []
vowels = ['a', 'e', 'i', 'o', 'u']

def btrk(D):
    if len(word) == L:
        vowel = 0
        consonant = 0
        for char in word:
            if char in vowels:
                vowel += 1
            else:
                consonant += 1
            if vowel>0 and consonant>1:
                print(''.join(word))
                return
    for i in range(D, C):
        word.append(alphabet[i])
        btrk(i+1)
        word.pop()
btrk(0)