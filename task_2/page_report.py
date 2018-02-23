#!/usr/bin/env python
# version of python: 2.7
# author: Milosz Ogaza, email: miloszogaza@gmail.com

import re
import sys


def find_url(log):
    # given a line with a log, extracts and returns the url.
    pattern = "(GET|POST) https?://(.+) HTTP"
    match = re.search(pattern, log)
    if match:
        return match.group(2)


def strip_url(url):
    # given a line with an url, stripes it's part after a question mark and the last slash sign
    # returns it's core part
    if url.rfind('?') != -1:
        last_question_mark_pos = url.rfind('?')
        stripped_url = url[:last_question_mark_pos]
    else:
        stripped_url = url

    if stripped_url[-1] == '/':
        stripped_url = stripped_url[:-1]
    return stripped_url


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'to run the program type: python page_report.py example_log_filename.log'
        sys.exit(1)

    stripped_urls_dict = {}
    invalid_log_counter = 0

    with open(sys.argv[1], 'r') as f:
        for line in f:
            url_candidate = find_url(line)
            if url_candidate:
                stripped_url = strip_url(url_candidate)
                if stripped_url not in stripped_urls_dict.keys():
                    stripped_urls_dict[stripped_url] = 1
                else:
                    stripped_urls_dict[stripped_url] += 1
            else:
                invalid_log_counter += 1


    for k, v in sorted(stripped_urls_dict.iteritems(), key=lambda(k, v): (-v, k)):
        print('"{}",{}'.format(k, v))

    if invalid_log_counter > 1:
        sys.stderr.write('"Invalid log lines",{} \n'.format(invalid_log_counter - 1))
