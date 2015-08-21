import re
import urllib
import urllib2

req = urllib2.Request("http://www.buzzfeed.com/danieldalton/there-will-be-scrolling")
response = urllib2.urlopen(req)
contents_unparsed = response.read()
contents = ''
for item in contents_unparsed:
    contents += item

matchObj = re.findall(r'<p class="print"><a href="(.*\.(?:jpg|png))"', contents)
if matchObj:
    for ind, url in enumerate(matchObj):
        urllib.urlretrieve(url, str(1000 + ind + 1) + "_buzzfeed." + url[-3:])
