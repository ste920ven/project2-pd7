#!/usr/bin/python

from factual import *

KEY = "ayza4T1yldZH6VlPIQcFPYEtRs3CfhTp43Cs9Ulb"
SECRET = "qsxNCmjAEt0PUlYO6ZYisIh6lFQbtcCuFi6Nizyt"

def main():
    factual = Factual(KEY, SECRET)
    
    table = factual.table('places')
    
    q1 = table.search("sushi Santa Monica")
    print q1.data()[1]
    print q1.get_url()
    
    q2 = table.filters({'category': "Food & Beverage", 'region': "CA"}).limit(1)
    print q2.data()
  
if __name__ == '__main__':
  main()
