'''
posts = open('PostData/Posts.xml', 'r')
print(posts.readlines()[-1])
'''
import xmltodict
new = open('new_posts.xml','w')
with open('PostData/Posts.xml','r') as fd:
    x = fd.readlines()
    for i in range(100):
        new.write(x[i])
    new.write('</posts>')

new.close()
import xmltodict

with open('new_posts.xml') as fd:
    doc = xmltodict.parse(fd.read())
i = 0

for item in doc['posts']['row']:
    print(item['@Body'])
    try:
        f = open('CodeSnippets/file-'+str(i)+'.txt', 'w')
    except:
        import os
        os.makedirs('CodeSnippets/')
        f = open('CodeSnippets/file-'+str(i)+'.txt', 'w')
    f.write(item['@Body'])
    i += 1
#print(doc['posts']['row'])
