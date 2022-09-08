try:
    import pyautogui as auto
    from time import sleep
    import sys
    sleep(10) # wait 10 sec to start msg sending
    list=sys.argv[1]
    file=open(list,'r') # read file 
    for word in file:
        auto.write(word)
        auto.press('enter')
        sleep(1)
    file.close()
# exceptons
except FileNotFoundError:
    print(f'{list} file not Found:')
except ModuleNotFoundError:
    print("Modules Not Installed")
except:
    print("Something Wrong Try Again")
