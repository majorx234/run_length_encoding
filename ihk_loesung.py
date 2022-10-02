def proper_encoding(input):
    compressed = ""
    last_character = input[0]
    count = 1
    for i in range(1, len(input)):
        new_character = input[i]
        if new_character == last_character:
            count += 1
        else:
            if count <= 4:
                for j in range(0, count):
                    compressed += last_character
            else:
                compressed += "%"
                compressed += "{}".format(count)
                compressed += "{}".format(last_character)
            count = 1
            last_character = new_character
    if count <= 4:
        for j in range(0, count):
            compressed += last_character
    else:
        compressed += "%"
        compressed += "{}".format(count)
        compressed += "{}".format(last_character)
    return compressed


def ihk_encoding(input):
    compressed = ""
    i = 0
    while i < len(input):
        count = 1
        print("i: {}".format(i))
        if(i < len(input)-2):
            while (input[i] == input[i+1]) and (i < len(input)-2):
                print("i: {} count: {}".format(i, count))
                count += 1
                i += 1
                if count >= 5:
                    compressed += "%"
                    compressed += "{}".format(count)
                    compressed += input[i]
                else:
                    for j in range(0, count):
                        compressed += input[i]
        i += 1
    return compressed


def main():
    input = "aaaaabbbccccccddd"
    result_ok = proper_encoding(input)
    result_bad = ihk_encoding(input)
    print(result_ok)
    print(result_bad)


if __name__ == "__main__":
    main()
