
#THIS WORKS FOR NEO_X, Neo is good for subjects; but there will be more strange syntax errors/grammar in English writing


from selenium import webdriver
from selenium.webdriver.support.ui import Select


f = open("hist_essay_prompt.txt", "r")
prompt=f.read()

#wanted_text= '''"The effeminate teenage boy exclaimed, "Men are such jerks!" Before realizing he spoke without thinking'''
wanted_text=prompt
#this works btw.
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.common.keys import Keys


def funco():
    from random import randint
    f=(randint(1,95))
    
    

    port = (f":412{f}") #randomize proxy's last 2 digits.
    myProxy="68.183.129.76" + port

    print(myProxy)

    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': myProxy,
        'ftpProxy': myProxy,
        'sslProxy': myProxy,
        'noProxy': '' # set this value as desired
        })


    input_text = (f'{wanted_text}')
    options = FirefoxOptions()
    options.add_argument("--headless")
    fp = webdriver.Firefox(options=options)


    #fp = webdriver.Firefox()
    
    fp.get("https://textsynth.com/playground.html")
    selectx = Select(fp.find_element_by_id('model'))

# select by visible text
# select.select_by_visible_text('gptneox_20B')

# select by value 
    selectx.select_by_value('gptneox_20B')
    element = fp.find_element_by_id("input_text")
    element.send_keys(input_text)

    element = fp.find_element_by_id("submit_button").click()
    savedtext=''
    outputtxt=(fp.find_element_by_id("gtext1").text)
    for i in range(0,1790):
        # print(i)
        if i == 2099:
            savedtext=(fp.find_element_by_id("gtext1").text)
            if savedtext==outputtxt:
                # print('THIS GUY FARTED')
                break
            else:
                pass
            
            

        print(fp.find_element_by_id("gtext1").text) #this checks it every loop, wasn't intentional but it works.
        pass


    # print(fp.find_element_by_id("gtext1").text)

    f = open("answer_hist_essay.txt", "a")
    f.write('\n\n=---------X-----------=\n\n' + fp.find_element_by_id("gtext1").text)
    f.close()


    fp.quit()

# func()
#element.send_keys(password)
#element.send_keys(Keys.TAB)

# element.send_keys(Keys.RETURN)
# element.close()
