
with open('input.txt', 'r') as file:
    try:
        lines = file.readlines()
        chars_to_remove = input("Input symbols to delete on the right side of string: ")

        cleaned_lines = []
        for line in lines:
            line = line.rstrip('\n')
            while line and line[-1] in chars_to_remove + ';':
                line = line[:-1]
            cleaned_lines.append(line)

        reversed_lines = [line[::-1] for line in cleaned_lines]
    except Exception:
        print(f'Invalid input')

with open('output.txt', 'w') as file:
    for line in reversed_lines:
        file.write(line + '\n')
