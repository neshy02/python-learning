letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', 
'.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', 
'-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', 
'...--', '....-', '.....', '-....', '--...', '---..', '----.']
zipped = dict(zip(letters, morse))
word = input().upper()

for ch in word:
    if ch in zipped:
        print(zipped[ch], end = ' ')
