import re

def collect_links(string):

    all = re.findall(r'<a href="(.*)">', string)
    return all