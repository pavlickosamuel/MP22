import random
fr = open("poprehadzovany_text_vstup2.txt","r")

text = []
def pomiesaj(retazec):
    pismenka = list(retazec)
    random.shuffle(pismenka)
    return ''.join(pismenka)

for line in fr:
    line = line.strip()
    text.append(line)
print("\n".join(text))
text2 = []
for i in text:
    i = i.strip().split()
    a = []
    for word in i:
        znak = []
        slovo = []
        for pismenka in word:
            if pismenka.isalpha():
                slovo.append(pismenka)
            else:
                znak.append(pismenka)
        temp = "".join(slovo[1:-1])
        index = word.index(str("".join(znak)))
        if len(znak) > 0:
            if index == 0:
                a.append("".join(znak) + "".join(slovo[0]) + pomiesaj(temp) + "".join(slovo[-1]))
            else:
                a.append("".join(slovo[0]) + pomiesaj(temp) + "".join(slovo[-1]) + "".join(znak))
        else:
            a.append("".join(slovo[0]) + pomiesaj(temp) + "".join(slovo[-1]))
    text2.append(" ".join(a))

print()
print("\n".join(text2))
fw = open("poprehadzovany_text.txt","w")
fw.write("\n".join(text2))
fw.close()
