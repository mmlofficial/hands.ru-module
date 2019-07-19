import urllib.request
#"https://www.hands.ru/company/about"
#"https://www.repetitors.info"

def check8(string):
    res = ""
    for symb in string:
        if ('(' > symb or symb > '9') and symb != ' ':
            return -1
        if  '0' <= symb <= '9':
            res += symb
    if len(res) == 11 and res[0] == "8":
        return res
    if len(res) == 7:
        vsp = "8495"
        return vsp + res
    return -1

def TelephoneSearcher(webpage):
    page = urllib.request.urlopen(webpage)
    page_content = page.read()

    file = open("webpage.txt", "w", encoding = "utf-8")
    file.write(str(page_content))
    file.close()

    file = open("webpage.txt", 'r', encoding = "utf-8")
    telephones = open("telephones.txt", 'w')

    for l in file:
        line = l
        while(1):
            flag = 0
            min_start = -1
            for i in range (10):
                start = line.find(">"+str(i))
                if start != -1 and flag == 0:
                    flag = 1
                    min_start = start
                if start != -1 and start < min_start:
                    min_start = start
            if min_start != -1:
                end = line[min_start:].find("<")
                numb = line[min_start+1:end+min_start]
                tel = check8(numb)
                if tel != -1:
                    telephones.write(tel + "\n")
                    print(tel)
                line = line[min_start+end:]
            else:
                break
    telephones.close()
    file.close()


if __name__ == "__main__":
    TelephoneSearcher("https://www.hands.ru/company/about")