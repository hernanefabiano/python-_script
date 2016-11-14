
#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import unicode_literals, print_function

import time
import threading
import queue
import re
import requests


urls = [
    ("https://www.amazon.co.jp/",),
    ("https://www.python.org/",),
    ("https://www.w3.org/",),
]

def run_in_threads(target, args_list):
    result = queue.Queue()
    
    def task_wrapper(*args):
        result.put(target(*args))
    
    threads = [threading.Thread(target=task_wrapper, args=args) for args in args_list]
    for t in threads: 
	    t.start()
    for t in threads:
	    t.join()
    
    return result


def get_title(url):
    try:
        page_title = re.search('<title>(.+?)</title>', requests.get(url).text, re.M|re.I).group(1)
        print ('{}: u{}'.format(url, page_title))
        
        with open('somefile.txt', 'a') as the_file:
            the_file.write(page_title)

    except Exception as oO:
        print ('{}: {}'.format(url, oO))


if __name__ == "__main__":
	start = time.time()
	run_in_threads(get_title, urls)
	print("--- {} seconds ---".format((time.time() - start)))