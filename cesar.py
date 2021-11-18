key = -1
text = ""
with open('testcase.txt') as file:
    i = 1
    for line in file:
        if i == 1: key = int(line)
        if i == 2: text = str(line)
        i += 1
def MahoaCesar(text, key):
    lst_text = list(text)
    for i in range(0, len(lst_text)):
        if int(ord(lst_text[i])) not in range(65, 91) and int(ord(lst_text[i])) not in range(97, 123):  continue
        else:
            if int(ord(lst_text[i])) + key > 90: lst_text[i] = chr(int(ord(lst_text[i])) + key - 26)
            else: lst_text[i] = chr(int(ord(lst_text[i]) + key))
    return "".join(lst_text)

def TanCongCesar(text, key):
    lst_text = list(text)
    for i in range(0, len(lst_text)):
        if int(ord(lst_text[i])) not in range(65, 91) and int(ord(lst_text[i])) not in range(97, 123):  continue
        else:
            if int(ord(lst_text[i])) - key < 65: lst_text[i] = chr(int(ord(lst_text[i])) - key + 26)
            else: lst_text[i] = chr(int(ord(lst_text[i]) - key))
    return "".join(lst_text)
print("Ma hoa: ", MahoaCesar(text,key))
print("Tan cong:")
for i in range(1, 25):
    print("key = ", i)
    print(TanCongCesar(MahoaCesar(text, key), i))
