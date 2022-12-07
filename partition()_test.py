# import textwrap
# print(textwrap.shorten("Hello world let me sit you down chris hansen", width=35, placeholder="..."))

#this shortens quotes

#use text_inside_test.py as reference for the pythonic way of doing this

af = 'hi there, my name is stanley'

print(f"string before: {af}")



split_txt=af.split(' ')[0:4]
joint = ' '.join(split_txt)

#this creates it in a list format for easier access of chars/items for a later array format
print(split_txt)
print(len(split_txt))

#this will loop until it matches text; it'll break the for loop & get its array/list #ID
matchtext='there,'
x = "there," in str(split_txt[1])#if this position matches the wanted text "there," then it prints true & gives you the position ranging from itself to the range of a selectable maximum item limit
print(x)
if x == True:
    print(split_txt[1:4]) # this works
#----------------------------------------------------#
#although it is flawed, i need to develop a way to create a cycle that searches through the text being searched using X variable & have it break the loop,
#then it iterates through loop #2[a different loop/gen 2]
#which grabs the split text[code already made above] and finally joins the text; I could possibly make this an app.
#----------------------------------------------------#


# for split_txt in range(len(split_txt)):
    # print(af.split(' ')[0:split_txt])
    
    # if matchtext in str(split_txt):
        # print("hi")
        # print(joint)
        # print(matchtext)
        # #print(af)
        # print(f'yaee{split_txt}')
        # #break
# print('done')