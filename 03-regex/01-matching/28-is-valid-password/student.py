import re

def is_valid_password(string):
    if len(string) < 12:
        return False

    must_have = [
        r'[0-9]', 
        r'[a-z]',
        r'[A-Z]',
        r'[+\-*\/.@]'
    ]

    mustnt_have = [
        r'(.)\1\1',
        r'(.*(.).*)(\2.*){3}'
    ]

    for regex in mustnt_have:
        if re.search(regex, string):
            return False
    
    for regex in must_have:
        if not re.search(regex, string):
            return False

    return True