import re

def find_url(log):
    #finds an url inside a line with a log and returns it
    pattern  = "GET http://(.+) HTTP"
    match = re.search(pattern,log)

    if match:
        return match.group(1)

def strip_url(url):
    #stripes an url by searching for the last question mark, removing it and everything after it
    #removes the last slash mark when it exists in a striped url

    if url.rfind('?') != -1:
        #means that question mark exist in a given url
        last_question_mark_pos = url.rfind('?')
        stripped_url = url[:last_question_mark_pos]
    else:
        stripped_url = url

    if(stripped_url[-1] == '/'):
        stripped_url = stripped_url[:-1]

    return stripped_url


logs = ["10.4.180.222 [28/Jan/2018:10:02:32 +0100] GET http://clearcode.cc/ HTTP/1.1 200 1080",
        "10.4.180.222 [28/Jan/2018:10:03:31 +0100] GET http://www.clearcode.cc HTTP/1.1 200 3056",
        "10.4.180.222 [28/Jan/2018:10:05:30 +0100] GET http://clearcode.cc/careers HTTP/1.1 200 3056",
        "10.4.180.222 [28/Jan/2018:10:08:29 +0100] GET http://clearcode.cc/careers/ HTTP/1.1 200 3056",
        "10.4.180.222 [28/Jan/2018:10:13:29 +0100] GET http://clearcode.cc/careers? HTTP/1.1 200 3056",
        "10.4.180.222 [28/Jan/2018:10:21:27 +0100] GET http://clearcode.cc/careers/? HTTP/1.1 200 3056",
        "10.4.180.222 [28/Jan/2018:10:34:26 +0100] GET http://clearcode.cc/careers?offer=internship&type=python HTTP/1.1 200 4545",
        "10.4.180.222 [28/Jan/2018:10:55:25 +0100] GET http://clearcode.cc/careers?type=frontend&offer=internship HTTP/1.1 200 5454"]


urls = []
invalid_log_counts = 0
for log in logs:
    if(find_url(log)):
        urls.append(find_url(log))
    else:
        invalid_log_counts += 1


stripped_urls = []
for url in urls:
    stripped_urls.append(strip_url(url))


stripped_urls_dict = {}
for stripped_url in stripped_urls:
    if stripped_url not in stripped_urls_dict.keys():
        stripped_urls_dict[stripped_url] = 1
    else:
        stripped_urls_dict[stripped_url] += 1

for k, v in sorted(stripped_urls_dict.iteritems(), key=lambda(k,v):(-v,k)):
    print('"{}",{}'.format(k,v))











