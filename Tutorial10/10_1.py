src_path = "source.txt"
des_path = "destination.txt"

content = ""

with open(src_path, 'r') as fin:
    content = fin.read()

with open(des_path, 'w') as fout:
    for i in content:
        fout.write(i)