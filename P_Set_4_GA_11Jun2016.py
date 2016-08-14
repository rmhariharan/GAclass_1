'''Make a list of all email addresses from a webpage.
    e.g. http://www.microstrategy.com/us/company/contact-us'''

import urllib.request
import re

my_page = urllib.request.urlopen("http://www.microstrategy.com/us/company/contact-us")

my_page_text = str(my_page.read())

email_list = re.findall(">(\w*\S*\w*@\w*\.\w+)",my_page_text)

print(email_list)

'''Now use the list redundancy removal function to come up with a unique list
    of e-mail ids'''


