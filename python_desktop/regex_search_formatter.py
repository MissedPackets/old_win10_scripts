# Python3 program to Split string into characters
import pyperclip

while 1!=0:
    def split(a):
        return list(a)
     #z e b  r a
# Driver code

    text=input('text to regex for x spaces: ')
   # print(text)
  #  print(split(text))
    st=split(text)
    f=(text.split())
  #  print((f))
    g=str("\s*").join(st)#this part is now working for regex
   # print(b)
    print(g)
    pyperclip.copy(g)
    spam = pyperclip.paste()

word = 'geeks'


# def store_value(a):
    # b=[]
    # c=b.append(a)
    # print(b)
# store_value('r')
# print(r'\*s')
# print(len(f))

# #for i in range(0,4-1):
   # # print(str(f[1])+r"\*s")
# b=['r','r',' ','f']
   # # print(b)
   # # c=b.append((store_value(f[i])))


# txt = input("Type something to test this out: ")

# # Note that in version 3, the print() function
# # requires the use of parenthesis.
# print("Is this what you just said? ", txt)
