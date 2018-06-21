import requests, re, getpass
MAIN_URL = "https://www.netlab.tkk.fi/mailman/private/theone/"
username = input("Username:")
password = getpass.getpass()
payload = {'username':username, 'password':password}
session = requests.Session()
r = session.post(MAIN_URL, payload)

all = re.findall(r"\d{4}-\w+.txt.gz", r.text)
for a in all:
    content = session.get(MAIN_URL+a).content
    open(a,'wb').write(content)
