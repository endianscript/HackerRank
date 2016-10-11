s =list(input().strip().lower())
character_list = {ord(i) : 1 for i in s if i != " "}
try:
    for i in range(97,123):
        if character_list[i]:
            pass
    print('pangram')
except Exception:
    print('not pangram')
