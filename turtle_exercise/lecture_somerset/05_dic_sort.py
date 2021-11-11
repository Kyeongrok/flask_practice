file = open("./info.csv")

def convert_list_to_dict(list):
    return {'name':list[0], 'id':list[1], 'subject':list[2], 'score':int(list[3])}
list = []
for line in file.readlines():
    infos = line.replace('\n', '').split(',')
    list.append(convert_list_to_dict(infos))

list = sorted(list, key= lambda x: x['name'])

for user in list:
    print(user)
