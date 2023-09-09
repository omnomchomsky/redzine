import urllib.request
for i in range(1, 13):
    filename = str(i).zfill(4) + ".jpg"
    url ='https://red19zine.files.wordpress.com/2022/05/' + filename
    urllib.request.urlretrieve(url, filename)
