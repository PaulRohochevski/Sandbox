import urllib2, threading, time

sites = ("https://www.tut.by", "http://banana.by")
sites_data = []


def reader(url, *args):
    global sites_data
    req = urllib2.urlopen(url)
    data = req.read()
    sites_data.append(data)


for site in sites:
    t = threading.Thread(target=reader, args=(site, ))
    t.start()
    t.join(100)

print(sites_data)
print(len(sites_data))
