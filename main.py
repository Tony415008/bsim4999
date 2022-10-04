#import
from bs4 import BeautifulSoup
import requests
import re

#open file
with open('熱　門 _ LIHKG.html', 'r', encoding = 'utf-8') as html_file:
  response = html_file.read()
  soup = BeautifulSoup(response, 'lxml')

  #find the html tags
  title_tags = soup.find_all('span', class_ = '_20jopXBFHNQ9FUbcGHLcHH')
  creator_type = ['CxY4XDSSItTeLVg0cKCN0 A0jheqYUBHNW93KykXKEH', #blue: male
                'CxY4XDSSItTeLVg0cKCN0 jj_3ZDzjtPixL1b2KTcpS', #red: female
                'CxY4XDSSItTeLVg0cKCN0 _208tAU6LsyjP5LKTdcPXD0'] #yellow: su
  creator_tags = soup.find_all('span', class_ = creator_type)
  created_time_and_like_tags = soup.find_all('span', class_ = '_37XwjAqVHtjzqzEtybpHrU')
  link_tags = soup.find_all('a', class_ = '_2A_7bGY9QAXcGu1neEYDJB', href = True)

  #print result
with open('posts.txt', 'w', encoding = 'utf-8') as f:
  for order, index in enumerate(range(len(title_tags))):
    f.write(f'---#{order}\n')
    f.write(f'Title: {title_tags[index].text}\n')
    f.write(f'Time creadted: {created_time_and_like_tags[0+2*index].text}\n')
    f.write(f'Likeness: {created_time_and_like_tags[1+2*index].text.strip()}\n')
    f.write(f"See: {link_tags[index].get('href')}\n")
    f.write('\n')
    
