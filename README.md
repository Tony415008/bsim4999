# bsim4999
pull lihkg

It is not completed yet, just for learning purpose

The way to test the .py
1. go to https://lihkg.com/category/2
2. click the right frame to save link
3. put the .html file and .py into a same directory
4. run the .py

If you want to test other link in lihkg
1. save the link you want, i.e. you want to save 學術台 _ LIHKG, https://lihkg.com/category/18.
2. change the with open('熱　門 _ LIHKG.html', 'r', encoding = 'utf-8') as html_file: name in .py

#before
with open('熱　門 _ LIHKG.html', 'r', encoding = 'utf-8') as html_file:
#after
with open('學術台 _ LIHKG', 'r', encoding = 'utf-8') as html_file:

3. put the .html file and .py into a same directory
4. run the .py
