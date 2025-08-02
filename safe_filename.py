# Helper function to make a string strictly filename-safe
import re

def make_filename_safe(s):
    s = s.strip().lower()
    s = s.replace(' ', '-')
    # Remove all characters except alphanumeric, hyphens, and underscores
    s = re.sub(r'[^a-z0-9-_]', '', s)
    return s

test_string = " hello,4$23/| world         "
changed_string = make_filename_safe(test_string)
print("#" + changed_string + "#")