import sys

def lookup(phone):
    fname = "./data/route-costs-600.txt"

    with open(fname) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    prefix = 2
    filtered = list(filter(lambda x: phone[:prefix] in x, content))

    answer = None
    while len(filtered) > 1:
        prefix = prefix + 1
        # print(phone[:prefix] + ' ' + str(len(filtered)))

        filter_after = list(filter(lambda x: phone[:prefix] in x, filtered))
        if( len(filter_after) < 1):
            # print("henlo : " + phone + " vs " + filtered[0])
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

def lookup_list(file):
    with open(file) as f:
        content = f.readlines()

    for c in content:
        print(lookup(c))



if __name__ == "__main__":
    lookup_list("./data/phone-numbers-1000.txt")
