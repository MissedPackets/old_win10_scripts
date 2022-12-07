import concurrent.futures
import time
import gptNEOX_copyuntitled2
#if youre churning out large quotes from the prompt
#use escape characters like / \ so that it can use the prompt deletion properly


from selenium.webdriver.common.proxy import Proxy, ProxyType

from selenium import webdriver
from selenium.webdriver.support.ui import Select
fileA="C:\Users\jellycat\.spyder-py3\selenium_INPUT_FILES\ao no"

f = open("{fileA}", "r", encoding='utf-8')
prompt=f.read()

# wanted_text= '''
# '''
# prompt=wanted_text
wanted_text=prompt
#this works btw.
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.common.keys import Keys



# def sleep_for_a_bit(seconds):
    # print(f"Sleeping {seconds} second(s)")
    # time.sleep(seconds)
    # return "Done sleeping"

def funco():
    from random import randint
    d=str("5.172.24.68,14.177.236.212,105.27.245.253,68.183.129.76,91.202.240.208")

    v=d.split(',')
# vd = v[1]

    import random
# print(random.randint(5, 10))
    dx=v[random.randint(0,4)]
    print(dx)
    
    f=(randint(1,95))
    
    
#91.202.240.208
#68.183.129.76
    port = (f":41{f}") #randomize proxy's last 2 digits.
    myProxy=f"{dx}" + port

    print(myProxy)
    
    
    input_text = (f'{wanted_text}')
    options = FirefoxOptions()
    options.add_argument("--headless")
    
    



    proxy = Proxy=({'proxyType':ProxyType.MANUAL,
        'httpProxy': myProxy,
        # 'ftpProxy': myProxy,
        # 'sslProxy': myProxy,
        # "noProxy":None,
        "proxyType":"MANUAL",
        # "autodetect":False
        # set this value as desired
    })


    fp = webdriver.Firefox(options=options, proxy=proxy)
    


    # fp = webdriver.Firefox()
    
    fp.get("https://textsynth.com/playground.html")
    selectx = Select(fp.find_element_by_id('model'))

# select by visible text
# select.select_by_visible_text('gptneox_20B')

# select by value 
    selectx.select_by_value('fairseq_gpt_13B')
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
        
    x = (fp.find_element_by_id("gtext1").text).replace("”", "\"")
    f = x.replace("“", '\"')
    xf = f.replace("’", "'")
    xfv = xf.replace("   ", " ")
    xfvs = xfv.replace("  ", " ")
    print(xfvs)
    xfvsa = xfvs.replace(f'{wanted_text}', "")
    

    # print(fp.find_element_by_id("gtext1").text)

    f = open("selenium_OUTPUT.txt", "a", encoding='utf-8')
    f.write('\n\n=---------X-----------=\n\n' + xfvsa)
    f.close()


    fp.quit()
with concurrent.futures.ProcessPoolExecutor() as executor:
    if __name__ == '__main__':
        f1 = executor.submit(funco)
        f2 = executor.submit(funco)
        f3 = executor.submit(funco)
        f4 = executor.submit(funco)
        print(f1.result())
        print(f2.result())
        print(f3.result())
        print(f4.result())

finish = time.perf_counter()
print("Finished in time : ", finish)