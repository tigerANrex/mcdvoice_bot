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

spans = browser.find_by_tag("span")
button = []
count = 0
for i in spans:
    if i.has_class('radioButtonHolder'):
        button.append(i)
        # if i == button[len(button)-1]:                        Get this tow rok please
        #     print("yes")
        #     button[randint(0, len(button)-1)].click()
    elif i.has_class('radioBranded'):
        button.append(i)
        count += 1
        if count == 5:
            button[randint(0, 4)].click()
            count = 0

browser.find_by_id('NextButton').click()
