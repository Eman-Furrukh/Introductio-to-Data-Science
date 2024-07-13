
#    21I-1726    #
#  EMAN FURRUKH  #
#  ASSIGNMENT 1  #
#     BSDS-U     #

                                #   QUESTION 1   #
#function definition
def evenOrOdd(x):
    array =[0]*26
    y = len(x)
    for i in range(y):
        array[ord(x[i])-97]+= 1
    for i in range(26):
        if (array[i]% 2 == 1):
            return False
    return True
#global 
x = str(input("Enter a sentence: "))
if(evenOrOdd(x)):
    print(0)
else:
    print(1)






    
                                #   QUESTION 3   #
num = int(input("Enter a number: "))
i = 0
for i in range(0,10000):
    counter = 2
    flag = False
    while (counter < i/2):
        if(i%counter == 0):
            flag = True
            break
        counter+=1
    if(flag == False):
        primeNumber = i
        
difference = primeNumber-num
if num > 1:
    for j in range(2, int(num/2)+1):
        if (num % j) == 0:
            print(num, "Missed it by that much", difference ,"!")
            break
    else:
        print(num, "Would you believe it; it is a prime!")
else:
    print(num, "Missed it by that much", difference ,"!")






                                #   QUESTION 4    #
dictionary = ["hello","hi","apple","smile",
              "mood","while","this","that",
              "wake","try","off","take",
              "these","fun","ride","miss",
              "over","up","down","left"]
word = str(input("Enter a word: "))
for i in range(0,20):
    if(word == dictionary[i]):
        print("CORRECT!")
    else:
        break
#hello
if(word == "hell" or word == "helo" or word == "hllo" or word == "ello"):
    print("ONE LETTER OMITTED FROM hello.")
elif(word == "hel" or word == "hlo" or word == "elo" or word == "ell"):
    print("TWO LETTERS OMITTED FROM hello")
#hi        
if(word == "i" or word == "h"):
    print("ONE LETTER OMITTED hi.")
#apple
if(word == "appl" or word == "aple" or word == "appe" or word == "apel"):
    print("ONE LETTER OMITTED FROM apple.")
elif(word == "apl" or word == "ape" or word == "app"):
    print("TWO LETTERS OMITTED FROM apple")
#smile 
if(word == "smil" or word == "mile" or word == "sile"):
    print("ONE LETTER OMITTED FROM smile.")
elif(word == "smi" or word == "ile" or word == "mil"):
    print("TWO LETTERS OMITTED FROM smile")
#mood
if(word == "mod" or word == "moo" or word == "ood"):
    print("ONE LETTER OMITTED FROM mood.")
elif(word == "mo" or word == "od" or word == "md"):
    print("TWO LETTERS OMITTED FROM mood")
#while
if(word == "whil" or word == "hile" or word == "wile" or word == "whie"):
    print("ONE LETTER OMITTED FROM while.")
elif(word == "whi" or word == "hie" or word == "hil"):
    print("TWO LETTERS OMITTED FROM while")
#this
if(word == "thi" or word == "his" or word == "tis"):
    print("ONE LETTER OMITTED FROM this.")
elif(word == "th" or word == "hi" or word == "is"):
    print("TWO LETTERS OMITTED FROM this")
#that
if(word == "tha" or word == "hat" or word == "tat"):
    print("ONE LETTER OMITTED FROM that.")
elif(word == "ta" or word == "at" or word == "ha"):
    print("TWO LETTERS OMITTED FROM that")
#wake
if(word == "wak" or word == "ake" or word == "wake" or word == "wae"):
    print("ONE LETTER OMITTED FROM wake.")
elif(word == "wa" or word == "ke" or word == "we"):
    print("TWO LETTERS OMITTED FROM wake")
#try
if(word == "tr" or word == "ry" or word == "ty"):
    print("ONE LETTER OMITTED FROM try.")
#off
if(word == "of" or word == "ff"):
    print("ONE LETTER OMITTED FROM off.")
#take
if(word == "tak" or word == "tae" or word == "tke"):
    print("ONE LETTER OMITTED FROM take.")
elif(word == "tk" or word == "ak"):
    print("TWO LETTERS OMITTED FROM take")
#these
if(word == "thes" or word == "hese" or word == "tese" or word == "thee"):
    print("ONE LETTER OMITTED FROM these.")
elif(word == "the" or word == "ese" or word == "hes"):
    print("TWO LETTERS OMITTED FROM these")
#fun
if(word == "fu" or word == "un" or word == "fn"):
    print("ONE LETTER OMITTED FROM fun.")
#ride
if(word == "rid" or word == "ide" or word == "rie"):
    print("ONE LETTER OMITTED FROM ride.")
elif(word == "ri" or word == "id" or word == "re"):
    print("TWO LETTERS OMITTED FROM ride")
#miss
if(word == "mis" or word == "mss" or word == "iss"):
    print("ONE LETTER OMITTED FROM mess.")
elif(word == "mi" or word == "ms"):
    print("TWO LETTERS OMITTED FROM mess")
#over
if(word == "ove" or word == "ver" or word == "ove" or word == "ovr"):
    print("ONE LETTER OMITTED FROM mess")
elif(word == "ov" or word == "vr" or word == "or"):
    print("TWO LETTERS OMITTED FROM mess")
#up
if(word == "u" or word == "p"):
    print("ONE LETTER OMITTED.FROM up")
#down
if(word == "dow" or word == "own" or word == "dwn" or word == "don"):
    print("ONE LETTER OMITTED FROM own.")
elif(word == "do" or word == "dn" or word == "dw"):
    print("TWO LETTERS OMITTEDFROM own")
#left
if(word == "lef" or word == "eft" or word == "lft" or word == "lift"):
    print("ONE LETTER OMITTED FROM left.")
elif(word == "le" or word == "ef" or word == "lt"):
    print("TWO LETTERS OMITTED FROM left")





                                #   QUESTION 2   #
x = int(input("Enter a number: "))
y = 100000000000000000000
digit = 0
sum = 0
check = 0
difference = 0
if x < y:
    for i in range(1,20,2):
        digit = x[1::2] * 2
        if digit > 10:
            sum = (d % 10) + 1
        else:
            sum = digit

    for i in range(0,20,2):
        check = x[i] + sum

    if check % 10 == 0:
        print("VALID.")
    else:
        difference = check % 10
        print("INVALID " , difference)
