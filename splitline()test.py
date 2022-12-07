# txt = '''Thank you for the music
# Welcome to the jungle
# MeYOW'''

# x = txt.splitlines()

# print(x)



import re

def search_text(text):
    return re.search(text, text).group(0)

def main():
    text = "This is a text"
    print(search_text(text))

if __name__ == "__main__":
    main()