def main():

    provinces_list = read_list("L09-checkpoint/provinces.txt")
    print(provinces_list)

    occurence_Alberta = count_Alberta(provinces_list)

    print(f"Alberta occurs {occurence_Alberta} times in the modified list.")

def read_list(filename):
    """Read the contents of a text file into a list and return the list. Each element in the list will contain one line of text from the text file.
    
    Parameter filename: the name of the text file to read
    Return: a list of strings
    """

    # Create an empty list that will store the lines of text from the text file.
    text_list = []

    with open(filename, "rt") as text_file:

        for line in text_file:

            clean_line = line.strip()

            text_list.append(clean_line)

    return text_list


def count_Alberta(list):
    # Remove the first element from the list.
    list.pop(0)
    # Remove the last element from the list.
    list.pop()

    for i in range(len(list)):

        if list[i] == "AB":
            list[i] = "Alberta"

    number_of_Alberta = list.count("Alberta")
    
    return number_of_Alberta

if __name__ == "__main__":
    main()