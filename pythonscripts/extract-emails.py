import re
with open('todos.txt.gz') as  f:
    content = f.read()
    lista = re.findall(r"From: \S+ at \S+\.\S+[.\S]*", content)
    myset = set([item.split("From: ")[1].replace(" at ", "@") for item in lista])
    joined = "; ".join(myset)

    with open('emails.txt', 'w') as emails:
        emails.write(joined)

print("#complete#")
