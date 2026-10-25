import json
H={'j005_q3 C':'Goodbye.','h005_q4 C':'Goodbye',
'h013_q3 C':'Have you join a club','h029_q3 C':'Stop train if you feel an injury','h029_q3 D':'Stop to train if you feel an injury',
'h034_q1 C':'The flood is seriously and many people need help','h034_q2 B':'Could you please donate some blanket',
'h034_q2 C':'Could you please donating some blankets','h034_q2 D':'Could you please to donate some blankets',
'h034_q3 D':'I am worry about the survivors','h041_q2 A':'Can you speaking your local dialect','h041_q2 B':'Can you speak you local dialect',
'h041_q3 C':'Could you say that again more slow','h041_q3 D':'Could you say that again more slower',
'h044_q3 B':'My plan for learn Chinese is simple','h044_q3 C':'My plan for learning Chinese is simply',
'h049_q2 C':'The damage comes from visitors cut the walls','h049_q3 C':'I see you point, but the site is worth it','h049_q3 D':'I see your point, but the site is worthy it',
'h051_q3 A':'I suggest we protecting the old city wall','h056_q2 B':'Hunter are the main danger to this species','h056_q2 D':'Hunter is the main danger to this species',
'h056_q4 B':'Please not buy products made from wild animals','h056_q4 C':'Please do not buying products made from wild animals','h056_q4 D':'Please do not buy products make from wild animals',
'h063_q2 D':'The rude comment has been delete','h070_q3 C':'I support keep this gathering','h072_q3 C':'Let me tell you about a local traditions',
'h079_q3 B':'The audience sat there, smile','h087_q3 B':'The origin of the festival connected with the moon',
'h094_q1 C':'It was honest for you to return the wallet','h094_q3 D':'Respect for other is a virtue','h096_q3 C':'Mei made a choice that shows kind',
'h103_q3 B':'Today I learning about a local ethnic group','h108_q4 B':'Shall we watching the rocket launch','h108_q4 C':'Shall we to watch the rocket launch',
'h110_q3 A':'What I learning about the mission','h115_q4 B':'Give some money to charity is of greater value','h117_q3 C':'I learning a lesson about value',
'h122_q4 A':'Next, he publish the theory','h122_q4 D':'Next, he was published the theory','h129_q1 B':'First, the sensor checking the food','h129_q1 D':'First, sensor checks the food',
'h152_q3 B':'Here is the plans for the harvest','h152_q3 C':'Here is plan for the harvest','h179_q3 A':'The plain was looked boundless',
'h186_q1 A':'First, putting pressure on the wound','h188_q3 C':'Follow these step when someone is bleeding','h193_q4 A':'First, looking at the whole canvas',
'h195_q3 D':'This note is record one visit to a gallery','h209_q3 C':'The evidences points to policy, not only to weather',
'h237_q3 D':'This walk starts in the city landmark','h244_q3 A':'Checking the tide before the voyage','h244_q3 B':'Check tide before the voyage',
'h244_q3 C':'Check the tide before the voyage starting'}
Q=json.load(open('data/questions.json')); by={q['id']:q for q in Q}; ex=[]
for k,v in H.items():
  qid,key=k.split(); q=by['cne_'+qid]
  c=[c for c in q['choices'] if c['key']==key][0]; assert key!=q['answer']
  ex.append((qid,key,c['text'],v)); c['text']=v
  t=[x['text'].strip().lower() for x in q['choices']]; assert len(set(t))==len(t),qid
json.dump(Q,open('data/questions.json','w'),ensure_ascii=False,indent=2); open('data/questions.json','a').write('\n')
json.dump(ex,open('scripts/en_distractors2/hand_fixes.json','w'),ensure_ascii=False,indent=1)
print(len(ex))
