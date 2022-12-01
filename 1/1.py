inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

elf_count = []
count = 0
for x in inp:
    try:
        count += int(x)
    except:
        elf_count.append(count)
        count = 0

elf_count.append(count)

print(max(elf_count))
