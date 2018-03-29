import sys

def lookup_list(file, cost):
    with open(file) as f:
        content = f.readlines()

    for c in content:
        print(lookup_cost(c,cost))



def lookup_cost(phone,fname):
    with open(fname) as f:
        content = f.readlines()

    # check first 2 characters
    limit = 2
    # filter by first digit
    small = filter(lambda x: x[:limit] in phone, content)

    # init answer
    answer = None

    # keep incrementing limit until you stop finding a match.
    while len(list(small)) > 1:
        # search an extra character
        limit += 1

        # reduce the search area
        smaller = filter(lambda x: x[:limit] in phone, list(small))
        if( len(list(smaller)) < 1):
            answer = list(small)[0]
            break

        # get rid of temp list
        small = smaller

        # set best answer for now
        answer = list(small)[0]

    # split at comma now
    answer = answer.split(",")

    # make sure it actually matches and isn't a dirty match
    if phone.startswith(answer[0]):
        return answer[1]
    else:
        return "not routeable"



if __name__ == "__main__":
    lookup_list("./data/phone-numbers-10.txt","./data/route-costs-100.txt")
