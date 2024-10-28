import csv

headers = [
    'index', 'org_id', 'name', 'century'
]

new_list = []

with open("organizations-100.csv", 'r') as csvfile:
    csv_dict_reader = csv.DictReader(csvfile, delimiter=',')
    for row in csv_dict_reader:
        info = {'index': row['Index'], 'org_id': row['Organization Id'], 'name': row['Name']}
        if int(row['Founded']) < 2000:
            century = '20-th Century'
        else:
            century = '21-th Century'
        info.setdefault('century', century)
        new_list.append(info)

with open('newOrganizations-100.csv', 'w', newline='') as newFile:
    writer = csv.DictWriter(newFile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(new_list)