# twitter.py
import re

# (?:...): non-capturing version

url = input("URL:").strip()

# 對不照格式輸入無效
username = re.sub(r"^(?:https?://)?(?:www\.)?twitter\.com/", "", url)
print(f"re.sub Username: {username}")

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"re.research Username: {matches.group(1)}")

# python twitter.py
# URL:http://www.twitter.com/robert
# re.sub Username: robert
# re.research Username: robert
#
# python twitter.py
# URL:www.google.com
# re.sub Username: www.google.com
