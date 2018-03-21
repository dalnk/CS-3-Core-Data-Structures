import sys

def lookup_list(file):
    with open(file) as f:
        content = f.readlines()

    for c in content:
        print(lookup_cost(c))



def lookup_cost(phone):
    fname = "./data/route-costs-10.txt"

    with open(fname) as f:
        content = f.readlines()

    # create filter
    reduce = lambda x: phone.startswith(x[:limit]), content

    # check first 2 characters
    limit = 2
    # filter by first digit
    filtered = list(filter(reduce(content)))

    # init answer
    answer = None

    # keep incrementing limit until you stop finding a match.
    while len(filtered) > 1:
        prefix = prefix + 1

        # reduce the search area
        filter_after = list(filter(reduce(filtered)))
        if( len(filter_after) < 1):
            answer = filtered[0]
            break
        filtered = filter_after

    if answer == None:
        answer = filtered[0]

    answer = answer.split(",")
    if phone.startswith(answer[0]):
        return answer[1]
    else:
        return "no route cost"



if __name__ == "__main__":
    lookup_list("./data/phone-numbers-10.txt")
