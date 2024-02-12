import datetime
import time
from BrowserOpener import BrowserOpener
from Interface import Interface

app = Interface()
browser = BrowserOpener()

def start_action_algorythm(email, password, link):
    global browser

    browser.start_browser()

    browser.open_url()

    # go to enter account
    browser.click_button_by_class('breakpoints--desktop')

    # enter email
    browser.enter_data_by_id('identifierId', email)
    browser.click_button_by_id('identifierNext')

    # enter password
    time.sleep(2)
    browser.enter_data_by_class('whsOnd.zHQkBf', password)
    browser.click_button_by_id('passwordNext')

    # enter to session
    time.sleep(3)
    browser.url = link
    browser.open_url()

    # turn off mic and cam
    time.sleep(5)
    browser.click_button_by_class('U26fgb.JRY2Pb.mUbCce.kpROve.yBiuPb.y1zVCf.HNeRed.M9Bg4d')
    browser.click_button_by_class('U26fgb.JRY2Pb.mUbCce.kpROve.yBiuPb.y1zVCf.HNeRed.M9Bg4d')

    # go to para
    time.sleep(1)
    browser.click_button_by_class('VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.jEvJdc.QJgqC')

def end_action_algorythm():
    browser.close_browser()
    app.close_app()

def submit_form(inputs):
    email = inputs['Email'].get()
    password = inputs['Password'].get()
    link = inputs['Link(Google Meet)'].get()
    start_time = inputs['Start Time(HH:MM:SS)'].get()
    end_time = inputs['End Time(HH:MM:SS)'].get()

    if email != '' and password != '' and link != '':
        print("Електронна пошта:", email)
        print("Пароль:", password)
        print("Посилання():", link)

        if start_time != '' and datetime.datetime.strptime(start_time, "%H:%M:%S"):
            while True:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                if current_time == start_time:
                    print("Go To Para!!!!!!!!!")
                    start_action_algorythm(email, password, link)
                    break
                time.sleep(1)
        else:
            print("Go To Para!!!!!!!!!")
            start_action_algorythm(email, password, link)
            time.sleep(1)

        if end_time != '' and datetime.datetime.strptime(end_time, "%H:%M:%S"):
            while True:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                if current_time == end_time:
                    print("Exit From Para!!!!!!!!!")
                    end_action_algorythm()
                    break
                time.sleep(1)

    else:
        print('Error input')

def main():
    global app

    app.add_input('Email')
    app.add_input('Password')
    app.add_input('Link(Google Meet)')
    app.add_input('Start Time(HH:MM:SS)', 'Optional')
    app.add_input('End Time(HH:MM:SS)', 'Optional')
    app.add_button('Submit', submit_form)

    app.run()

if __name__ == '__main__':
    main()
