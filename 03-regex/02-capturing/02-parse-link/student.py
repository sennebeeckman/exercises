import re

#<a href="https://www.w3schools.com">Visit a website</a>
def parse_link(string):
    match = re.fullmatch(r'<a href="(.*)">(.*)</a>', string)

    if match:
        link = match.group(1)
        caption = match.group(2)
        return (caption, link)
    
    return match

print(parse_link('<a href="https://www.w3schools.com">Visit a website</a>'))