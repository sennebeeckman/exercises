import re

def scrape_email_addresses(string):
    match = re.findall(r'([^ *<>]*@[^ *<>]*)', string)
    return match