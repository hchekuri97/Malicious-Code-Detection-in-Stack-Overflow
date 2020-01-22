# Score, ViewCount, AnswerCount, CommentCount, FavoriteCount

import csv
import xmltodict

with open('new_posts.xml') as fd:
    doc = xmltodict.parse(fd.read())
i = 0
file = open('features.csv','w')
writer = csv.writer(file)
writer.writerow(['Score', 'ViewCount', 'AnswerCount', 'CommentCount', 'FavoriteCount', 'Malicious'])

y = open('y.csv','r')
label = y.readlines()
i = 0
for item in doc['posts']['row']:
    try:
        s = item['@Score']

    except:
        s = 0
        pass
    try:
        v = item['@ViewCount']
    except:
        v = 0
        pass
    try:
        a = (item['@AnswerCount'])
    except:
        a = 0
        pass
    try:
        c = (item['@CommentCount'])
    except:
        c = 0
        pass
    try:
        f = (item['@FavoriteCount'])
    except:
        f = 0
        pass

    writer.writerow([s,v,a,c,f])
    i += 1
#file.close()
