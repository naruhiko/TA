import csv


def flatten(A):
    rt = []
    for i in A:
        if isinstance(i,list): rt.extend(flatten(i))
        else: rt.append(i)
    return rt
#thanks https://stackoverflow.com/questions/17864466/flatten-a-list-of-strings-and-lists-of-strings-and-lists-in-python


people = {}
while True:
    date = input("日付を4桁で入力:")
    participants = "../../Desktop/aten/" + "onkyouron" + str(date) + ".csv" #必要に応じて変更してください
    atendantee = "../../Desktop/aten/atendantee_ta.csv"
    with open(participants) as f:
        readfile = f.readlines()
        for readtext in readfile:
            readtext = readtext.rstrip('\n').split(',')
            key = readtext[0]
            if key not in people:
                people[key] = []
            people[key].append(readtext[2])

    ans = input("finish process?[y/[n]]:") or "n"
    if not ans == "n":
        break

with open(atendantee, "w") as wf:
    vals = list(people.items())
    writer = csv.writer(wf, delimiter=',')
    for val in vals:
        val = list(val)
        val = list(flatten(val))
        writer.writerow(val)