import stringTester as st

# TESTS:
# print(st.Tst("({})"))          # True
# print(st.Tst("({[]})"))        # True
# print(st.Tst("({[}])"))        # False
# print(st.Tst("({<[]>})"))      # True
# print(st.Tst("<<<amogus>>>"))  # True
# print(st.Tst("a<<<<<<a"))      # False

with open('input.txt', 'r') as f, open('output.txt', 'w') as out:
    for line in f:
        print(st.Tst(line.strip()))
        out.write(str(st.Tst(line.strip())) + '\n')
