import sys
import re
import io
#Taking input of the files from user
a=io.open(sys.argv[1],mode='r',encoding='utf-8')
b=a.read()

#printing all the currencies in text , $,₹, £
print(re.findall('([\$|₹|£][\s]*[0-9]*.[0-9]*)',b))

#printing all dates which are of following format  dd/mm/yyyy, dd/mm/yy, mm/dd/yyyy, mm/dd/yy

print(re.findall('(\d{2,4}[/]\d{2}[/]\d{2,4})',b))

#printing all the cardilities and orders
c = re.findall('(\d+(?:st|[nr]d|th))', b)
d = re.findall('/first|second|tw(?:elfth|entieth)|th(?:irt(?:eenth|ieth)|ird)|fi(?:ft(?:eenth|ieth)|h)|(?:four|six|seven)(?:teenth|th|tieth)|eight(?:eenth|h|ieth)|nin(?:e(?:teenth|tieth)|th)|tenth|eleventh|fortieth|hundreth|thousandth/i',b)
print(c+d)

#printing all the vowels words with 4 letters
print(re.findall('([\s]+[aeiouAEIOU][a-z]{3}[\s]+)',b))
