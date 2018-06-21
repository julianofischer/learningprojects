import re
resultado = re.search(r'\d\d\w','11a22b33c')

resultado = re.search(r'(\d\d)\w','11a22b33c')
resultado.group()
resultado.group(1)
resultado.start()
resultado.end()
resultados = re.finditer(r'(\d\d)\w','11a22b33c')
for resultado in resultados:
    print "%s com grupo %s [%s,%s]" % (resultado.group(), resultado.group(1),resultado.start(), resultado.end())

#perfomance improvement
regex = re.compile(r'(\d\d)\w')
resultados = regex.finditer('11a22b33c')
