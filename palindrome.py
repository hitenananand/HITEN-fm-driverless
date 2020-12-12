# Program to check if the character list is palindrome or not
def pal(string):
    if(len(string)<=1):
        return True
    if string[0]==string[len(string)-1]:
        return pal(string[1:len(string)-1])
    else:
        return False
character=input("ENTER STRING: ")
if pal(character):
    print(character," is a palindrome string ")
    for c in character:
        print("ascii_value", "is",  ord(c), end=':')
        print("hex_value", "is", hex(ord(c)))
else:
    print("Not palindrome ")
