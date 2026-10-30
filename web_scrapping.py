'''
real world example: multithreading for 
I/O bound tasks

scenario : web scrapping ofen involves
making numerous network requests to fetch
web pages. these tasks are I/O because they 
spend a lot of time waiting for responses from 
servers. multithreading can significantly improve
the performance by allowing multiple web pages to 
be fetched concurrently

'''