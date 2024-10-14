x = [1, 2, 3]
y = {5, 3, 4, 2, 1}
import re
[y.remove(block) for block in x]
print(y)
def is_valid_name(name):
        return bool(re.fullmatch('[a-zA-Z0-9.]{1,16}', name))
print(is_valid_name("aaaaaaaaaaaa"))