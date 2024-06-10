
with open('input1.txt', 'r') as file1, open('input2.txt', 'r') as file2, open('output.txt', 'w') as file:
    try:
        lines1 = file1.readlines()
        lines2 = file2.readlines()
        for l1, l2 in zip(lines1, lines2):
            file.write(''.join(sorted(l1.strip() + l2.strip())) + '\n')
    except Exception:
        print(f'Invalid input')
