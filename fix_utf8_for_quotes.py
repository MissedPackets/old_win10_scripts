
txt = open("quote.txt", "r", encoding='utf-8')
prompt=txt.read()


pg='681'

author = "Foner"

verb="claims"

x = prompt.replace("”", "\'")
f = x.replace("“", "\'")
xf = f.replace("’", "'")
xfv = xf.replace("   ", " ")
xfvs = xfv.replace("  ", " ")


print(f"\n\n{verb}, " +"\""+"..." + f"{xfvs}" +"," + "\"" + f" ({author} {pg}).")
f = open("oktest.txt", "a")
f.write(f"\n\n{verb}, " +"\""+"..." + f"{xfvs}" +"," + "\"" + f" ({author} {pg}).")
f.close()