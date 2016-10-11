s = (input().strip())
same_character = False
prev_character = ""
index = 0

while (len(s) > 0 and index < len(s)):
    if s[index] == prev_character:
        same_character = True
    if same_character:
        s = s[:index - 1] + s[index + 1:]
        same_character = False
        index = 0
        prev_character = ""
    else:
        prev_character = s[index]
        index = index + 1

if (len(s) > 0):
    print(s)
else:
    print('Empty String')


