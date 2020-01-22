# upload and scan the files from CodeSnippets
import csv
label = open('y.csv','w')
y = csv.writer(label)
y.writerow(['Label'])
for i in range(100):
    import requests

    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': '46d8bb2a014b101be3ed2d3d0c5b970f81aba2b3d864588657a543837d82caa2'}


    files = {'file': ('CodeSnippets/file-'+str(i)+'.txt', open('CodeSnippets/file-'+str(i)+'.txt', 'rb'))}
    response = requests.post(url, files=files, params=params)
    response_dict = (response.json())
    print(response_dict)

    import time
    time.sleep(20)
# report
#46d8bb2a014b101be3ed2d3d0c5b970f81aba2b3d864588657a543837d82caa2

    while True:
        try:
            import requests
            url = 'https://www.virustotal.com/vtapi/v2/file/report'
            x = response_dict['resource']
            params = {'apikey': '46d8bb2a014b101be3ed2d3d0c5b970f81aba2b3d864588657a543837d82caa2', 'resource': str(x)}
            response = requests.get(url, params=params)
            response_dict = response.json()
            print(response_dict)
            total_engines = response_dict['total']
            malware_engines = response_dict['positives']
            print('Total Engines - '+str(response_dict['total']))
            print('Engines Detecting Malware- '+str(response_dict['positives']))
            print('Malware Detection Percentage - '+str(int(malware_engines/total_engines*100))+'%')

            if malware_engines>0:
                y.writerow([1])
            else:
                y.writerow([0])
            break
        except:
            pass

#print(count)
