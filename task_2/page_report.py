import re

def find_url(log):
    pattern  = "GET http://(.+) HTTP"
    match = re.search(pattern,log)

    if match:
        return match.group(1)
    else:
        print("not found")


def strip_url(url):
    last_question_mark_pos = url.rfind('?')
    stripped_url = url[:last_question_mark_pos]

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
for log in logs:
    urls.append(find_url(log))


stripped_urls = []
for url in urls:
    stripped_urls.append(strip_url(url))

#test
print(urls)
print(stripped_urls)








