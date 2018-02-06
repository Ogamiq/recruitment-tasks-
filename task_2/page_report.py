#version of python: 2.7
#author: Milosz Ogaza, email: miloszogaza@gmail.com

#!/usr/bin/python
import re
import sys

def find_url(log):
    #finds an url inside a line with a log and returns it
    pattern  = "GET https?://(.+) HTTP"
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

if len(sys.argv)!= 2:
    print 'to run the program correctly type: python page_report.py and the name of the log file after it'
    sys.exit(1)

with open(sys.argv[1],'r') as f:
    logs = f.readlines()

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


if(invalid_log_counts > 1):
    sys.stderr.write('"Invalid log lines",{} \n'.format(invalid_log_counts - 1))











