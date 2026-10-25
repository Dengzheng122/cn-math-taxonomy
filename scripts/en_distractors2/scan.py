import json,re
from wordfreq import zipf_frequency as z
Q=json.load(open('data/questions.json'))
E=[q for q in Q if q['topicId'].startswith('cne') and q['type']=='choice']
tok=lambda s:re.findall(r"[A-Za-z]+(?:'[a-z]+)?",s)
corp=set()
for q in E:
  for s in [q['prompt'],q.get('explanation','')]+[c['text'] for c in q['choices'] if c['key']==q['answer']]:
    corp|={w.lower() for w in tok(s)}
fl=[]
for q in E:
  for c in q['choices']:
    if c['key']==q['answer']: continue
    bad=[w for w in tok(c['text']) if w.lower() not in corp and z(w.lower(),'en')<1.5 and len(w)>1]
    if bad: fl.append((q['id'],c['key'],c['text'],bad))
if __name__=='__main__':
  print(len(E),len(fl),len({f[0] for f in fl}))
  for f in fl: print(f)
