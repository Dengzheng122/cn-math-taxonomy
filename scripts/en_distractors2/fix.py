import json,re,sys
sys.path.insert(0,'/tmp/dis')
from scan import fl, tok
from wordfreq import zipf_frequency as zf, top_n_list
Q=json.load(open('data/questions.json')); by={q['id']:q for q in Q}
MAN={('cne_p052_q1','C'):"cat's",('cne_p181_q4','C'):'heaviest',('cne_p189_q2','C'):'sees',
('cne_j005_q3','C'):'Good night.',('cne_j005_q3','D'):'Good afternoon.',('cne_h005_q4','C'):'Good night',('cne_h005_q4','D'):'Good afternoon',
('cne_j009_q3','D'):"family's",('cne_j009_q4','C'):"I have two sister's.",('cne_j009_q4','D'):"I have two sisters'.",
('cne_j023_q4','C'):'He is have a volleyball.',('cne_j025_q3','C'):'We play the volleyball at school.',
('cne_j028_q1','A'):'I like a bananas.',('cne_j028_q1','C'):'I likes bananas.',('cne_j028_q3','A'):'I want a salads.',('cne_j028_q3','B'):'I want many salad.',
('cne_j030_q2','C'):"I like banana's.",('cne_j064_q2','D'):'The elephant is a friendly.',('cne_j068_q4','C'):'swims',
('cne_j089_q4','C'):'We visited a museum tomorrow.',('cne_j091_q4','B'):'We did milked a cow.',('cne_j095_q4','C'):'We had have a good time.',
('cne_j096_q4','C'):'The visitors were played badminton.',('cne_j115_q1','D'):'Which theater has the more comfortable seats?',
('cne_j126_q4','A'):"will don't",('cne_j221_q4','D'):'which',('cne_h101_q3','D'):'Could you tell me if may I take photos'}
from man2 import M2
MAN.update(M2)
KEEP_H={('cne_h259_q3','D'),('cne_h164_q3','A'),('cne_h101_q3','B')}
BLOCKW={'lerner','newest','reports','content','passport','misunderstand','differing','favorite','nearest'}
COLL=('band','team','family','audience','data','staff','crowd','class','government','group')
MODALS='will would can could may might shall should must'.split()
SWAP={'is':'are','are':'is','was':'were','were':'was','has':'have','have':'has','does':'do','am':'is'}
VERB3=set('help make carry show point describe follow start mean record introduce check need give come support'.split())
TOP=[w for w in top_n_list('en',40000) if w.isalpha() and w.isascii()]
def lev(a,b):
  p=list(range(len(b)+1))
  for i,ca in enumerate(a,1):
    c=[i]
    for j,cb in enumerate(b,1): c.append(min(p[j]+1,c[j-1]+1,p[j-1]+(ca!=cb)))
    p=c
  return p[-1]
def base(w):
  if w.endswith('ied'): return w[:-3]+'y'
  if w.endswith('ed'):
    a,b=w[:-2],w[:-1]
    if len(a)>2 and a[-1]==a[-2]: a=a[:-1]
    return max([a,b],key=lambda x:zf(x,'en'))
  return None
def grammar(C):
  ws=C.split(' '); out=[]
  for i,w in enumerate(ws):
    lw=w.lower()
    if lw in SWAP and i>0 and ws[i-1].lower() not in ('i',) and ws[i-1].lower() not in COLL:
      out.append(' '.join(ws[:i]+[SWAP[lw]]+ws[i+1:]))
    if lw in MODALS and i+1<len(ws) and ws[i+1].isalpha() and ws[i+1].islower() and ws[i+1] not in ('not','be','you','i','we','they','he','she'):
      v=ws[i+1]; out.append(' '.join(ws[:i+1]+['to',v]+ws[i+2:]))
      out.append(' '.join(ws[:i+1]+[v+('es' if v.endswith(('s','sh','ch','x')) else 's')]+ws[i+2:]))
    if lw in ('is','are','was','were','be','been','being') and i+1<len(ws):
      b=base(ws[i+1]) if ws[i+1].endswith('ed') else None
      if b and zf(b,'en')>2.5: out.append(' '.join(ws[:i+1]+[b]+ws[i+2:]))
      if ws[i+1].endswith('ing') and lw in ('is','are','am'):
        st=ws[i+1][:-3]; c=[st,st+'e',st[:-1] if len(st)>2 and st[-1]==st[-2] else st]
        b=max(c,key=lambda x:zf(x,'en'))
        if zf(b,'en')>2.5: out.append(' '.join(ws[:i+1]+[b]+ws[i+2:]))
    if lw=='me' and i>0 and ws[i-1].lower()=='let' and i+1<len(ws):
      out.append(' '.join(ws[:i+1]+['to']+ws[i+1:]))
    if lw.endswith('s') and (lw[:-1] in VERB3 or lw[:-2] in VERB3) and i>0 and ws[i-1].lower() not in ('the','a','my','your'):
      out.append(' '.join(ws[:i]+[w[:-2] if lw[:-2] in VERB3 and lw.endswith('es') else w[:-1]]+ws[i+1:]))
    if lw=='a' and i+1<len(ws) and ws[i+1][:1].lower() not in 'aeiou': out.append(' '.join(ws[:i]+['an' if w=='a' else 'An']+ws[i+1:]))
    if lw=='an' and i+1<len(ws): out.append(' '.join(ws[:i]+['a' if w=='an' else 'A']+ws[i+1:]))
  return out
def lookalike(C,target):
  ws=C.split(' ');out=[]
  idx=[i for i,w in enumerate(ws) if re.sub(r'\W','',w).lower()==target.lower()]
  for i in idx:
    w=re.sub(r'\W','',ws[i]); lw=w.lower(); best=[]
    for c in TOP:
      if c==lw or c[0]!=lw[0] or abs(len(c)-len(lw))>1: continue
      if c in BLOCKW: continue
      cp=0
      while cp<min(len(c),len(lw)) and c[cp]==lw[cp]: cp+=1
      if cp>=5 or cp>=min(len(c),len(lw))-3: continue
      if c.replace('u','')==lw.replace('u','') or c.replace('z','s')==lw.replace('z','s'): continue
      d=lev(c,lw)
      if d<=2 and len(lw)>=5: best.append((d,-zf(c,'en'),c))
    best.sort()
    for _,_,c in best[:3]:
      cc=c.capitalize() if w[0].isupper() else c
      out.append(' '.join(ws[:i]+[ws[i].replace(w,cc)]+ws[i+1:]))
  return out
MIS=[('ss','s'),('mm','m'),('cc','c'),('ll','l'),('rr','r'),('nn','n'),('tt','t'),('ie','ei'),('ei','ie'),('ence','ance'),('ance','ence'),('ent','ant'),('able','ible'),('ary','ery'),('ous','us'),('tion','sion'),('ure','er'),('ck','k'),('ph','f'),('ea','ee'),('ou','o'),('au','o')]
def misspell(C,target):
  ws=C.split(' ');out=[]
  for i,w0 in enumerate(ws):
    w=re.sub(r'\W','',w0)
    if w.lower()!=target.lower() or len(w)<5: continue
    for a,b in MIS:
      j=w.find(a,1)
      if j>0:
        m=w[:j]+b+w[j+len(a):]
        if zf(m.lower(),'en')<1.0: out.append(' '.join(ws[:i]+[w0.replace(w,m)]+ws[i+1:]))
    # single->double consonant
    for j in range(1,len(w)-1):
      if w[j] in 'lmnprst' and w[j-1] in 'aeiou' and w[j+1] in 'aeiou':
        m=w[:j]+w[j]+w[j:]
        if zf(m.lower(),'en')<1.0: out.append(' '.join(ws[:i]+[w0.replace(w,m)]+ws[i+1:])); break
  return out
def nearest(t,C):
  return min([re.sub(r'\W','',w) for w in C.split(' ')],key=lambda w:lev(w.lower(),t.lower()))
changes=[];kept=[]
grp={}
for qid,k,txt,bad in fl: grp.setdefault(qid,[]).append((k,txt,bad))
for qid,items in grp.items():
  q=by[qid]; C=[c['text'] for c in q['choices'] if c['key']==q['answer']][0]
  used={c['text'] for c in q['choices']}
  gi=0
  for k,txt,bad in items:
    if (qid,k) in MAN: new=MAN[(qid,k)]
    elif qid.startswith('cne_h') and (qid,k) not in KEEP_H:
      tgt=nearest(bad[0],C)
      G=[x for x in grammar(C) if x not in used and x!=C]; L=[x for x in lookalike(C,tgt) if x not in used and x!=C]; M=[x for x in misspell(C,tgt) if x not in used and x!=C]
      order=[G,L,M][gi%3:]+[G,L,M][:gi%3]
      new=next((p[0] for p in order if p),None); gi+=1
      if not new: kept.append((qid,k,txt,'无可用的合规替换')); continue
    else: kept.append((qid,k,txt,'常见学习者错误形式（过度规则化等），保留')); continue
    assert new not in used and new!=C,(qid,new)
    for c in q['choices']:
      if c['key']==k: c['text']=new
    used.discard(txt); used.add(new); changes.append((qid,k,txt,new,C,q['prompt']))
json.dump(Q,open('data/questions.json','w'),ensure_ascii=False,indent=2); open('data/questions.json','a').write('\n')
json.dump({'changes':changes,'kept':kept},open('/tmp/dis/result.json','w'),ensure_ascii=False,indent=1)
print(len(changes),len(kept))
