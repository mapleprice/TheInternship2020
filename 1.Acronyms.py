def AddingAcronyms(string, lst):
    stringList = string.split()
    acro = ""
    for s in stringList:
        if len(s) and s[0].isupper():
            acro += s[0]
    InsertionSort(acro, lst)
    return lst

def InsertionSort(string, lst):
    if len(lst) == 0:
        lst.append(string)
        return lst
    for i in range(len(lst)):
        if len(string) > len(lst[i]):
            lst.insert(i,string)
            break
        elif len(string) == len(lst[i]):
            if string < lst[i]:
                lst.insert(i, string)
                break
        elif i == len(lst) - 1:
            lst.append(string)
            break

if __name__ == "__main__":
    n = int(input())
    wordlist = []
    for i in range(n):
        string = input()
        AddingAcronyms(string, wordlist)
    print("-----------------Results------------------")
    for i in wordlist:
        print(i)

