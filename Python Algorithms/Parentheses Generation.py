def generate_parenthesis(p, left, right, parens):
    if left > 0:
        generate_parenthesis(p + '(', left - 1, right, parens)
    if right > left:
        generate_parenthesis(p + ')', left, right - 1, parens)
    if right == 0:
        parens.append(p)

def main():
    result = []
    n = 4
    generate_parenthesis("", n, n, result)

    for s in result:
        print(s)

if __name__ == "__main__":
    main()