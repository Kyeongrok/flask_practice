file = open('./info.csv')

def list_to_dict(list):
    # print(list)
    return {'name':list[0], 'id':int(list[1]), 'subject':list[2], 'score':list[3]}

list = []
for line  in file.readlines():
    arr = line.replace('\n', '').split(',')
    dict = list_to_dict(arr)
    list.append(dict)

dict = {
}
for line in list:
    if dict.get(line['id']) == None:
        dict[line['id']] = []

    dict[line['id']].append(line)

def calculate_mean(list):
    total = 0
    for info in list:
        total += int(info['score'])
    return total / len(list)

# for each dict
for key, value in dict.items():
    print(key, calculate_mean(value))

