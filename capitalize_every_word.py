import re
import string

def lowercase_match_group(matchobj):
    return matchobj.group().lower()

# Make titles human friendly
# http://daviseford.com/python-string-to-title-including-punctuation
def title_extended(title):
    if title is not None:
        # Take advantage of title(), we'll fix the apostrophe issue afterwards
        title = title.title()

        # Special handling for contractions
        poss_regex = r"(?<=[a-z])[\']([A-Z])"
        title = re.sub(poss_regex, lowercase_match_group, title)

    return title

def title_one_liner(title):
    return re.sub(r"(?<=[a-z])[\']([A-Z])", lambda x: x.group().lower(), title.title())