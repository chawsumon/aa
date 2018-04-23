import json

w = json.load(open('worldl.json'))
print(w)

# for c in w:
#   print(c['name'])
# count = 0
for c in w:
  c['tld'] = c['tld'][0:1]
  print(c['tld'])
