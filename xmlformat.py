import xmltodict

with open('new_posts.xml') as fd:
    doc = xmltodict.parse(fd.read())
i = 0

for item in doc['posts']['row']:
    if i==1:
        print(item['@Body'])
        break
    i += 1
