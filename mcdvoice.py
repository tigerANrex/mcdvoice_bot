from splinter import Browser
from random import randint

survey_code = input('Survey Code: ')
if len(survey_code) > 26:
    char = '- '
    for i in char:
        survey_code = survey_code.replace(i,"")
    print(survey_code)
browser = Browser('chrome')

browser.visit('https://www.mcdvoice.com')
browser.fill('CN1', survey_code[:5])
browser.fill('CN2', survey_code[5:10])
browser.fill('CN3', survey_code[10:15])
browser.fill('CN4', survey_code[15:20])
browser.fill('CN5', survey_code[20:25])
browser.fill('CN6', survey_code[25])
browser.find_by_name('NextButton').click()

while True:
    spans = browser.find_by_tag("span")
    button = []
    count = 0
    for i in spans:
        # if i.has_class('radioButtonHolder'):
        #     button.append(i)
        if i.has_class('radioBranded'):
            button.append(i)
            count += 1
            if count == 5:
                button[randint(0, len(button)-1)].click()
                count = 0
                button = []
    try:
        if len(button) < 5 and len(button) > 0:
            button[randint(0, len(button)-1)].click()
        browser.find_by_id('NextButton').click()
    except:
        if browser.is_element_not_present_by_id('finishForm'):
            break
        # browser.fill('S081000','Aye that\'s pretty good. The drive thru wait wasn\'t too long, and person who took my order spoke clearly and got my order correctly. When I got my food it was warm and the order was correct.')
