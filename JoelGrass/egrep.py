import sys,re
# sys.argv - список аргументов коммандной строки
# sys.argv[0] - имя самой программмы
# sys.argv[1] - регулярное выражение, указываемое в коммандной строке
regex = sys.argv[1]

# для каждой строки, переданной сценарию
for line in sys.stdin:
    # если она соответствует регулярному выражению regex,
    # записать её в stdout
    if re.search(regex,line): sys.stdout.write(line)