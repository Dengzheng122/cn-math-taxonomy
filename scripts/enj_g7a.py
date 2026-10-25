# -*- coding: utf-8 -*-
"""七年级上册。人教版 Go for it! 通行目录，单元名与册次待核。"""
from en_tx import V, P, G, F, R


def q(prompt, answer, wrongs, expl):
    return ("c", prompt, answer, wrongs, expl)


P("ph_stress", "单词重音", 7, "上", 1,
  "能判断常见单词的重音在第几个音节。", "stress", [
    q("teacher 的重音在第几个音节？", "第一个音节",
      ["第二个音节", "两个音节同样重", "没有重音"], "tea-cher 的重音在 tea。"),
    q("about 的重音在第几个音节？", "第二个音节",
      ["第一个音节", "两个音节同样重", "没有重音"], "a-bout 的重音在 bout。"),
    q("哪个单词的重音在第二个音节？", "begin",
      ["student", "China", "apple"], "be-gin 的重音在 gin，其余三个词的重音在第一个音节。"),
    q("computer 的重音在第几个音节？", "第二个音节",
      ["第一个音节", "第三个音节", "三个音节同样重"], "com-pu-ter 的重音在 pu。"),
])

P("ph_tone7", "句末升降调", 7, "上", 1,
  "能区分陈述句、特殊疑问句的降调和一般疑问句的升调。", "tone", [
    q("一般疑问句 Are you a student? 句末通常用什么语调？", "升调",
      ["降调", "先降后升", "每个词都重读"], "一般疑问句句末通常用升调。"),
    q("陈述句 My name is Gina. 句末通常用什么语调？", "降调",
      ["升调", "先升后降再升", "没有语调"], "陈述句句末通常用降调。"),
    q("特殊疑问句 Where is she? 句末通常用什么语调？", "降调",
      ["升调", "和一般疑问句相同的升调", "只在 where 上升"], "特殊疑问句句末通常用降调。"),
    q("哪一句朗读时句末通常用升调？", "Is he your friend?",
      ["He is my friend.", "Where is your friend?", "She is Gina."],
      "Is he your friend 是一般疑问句，句末用升调。"),
])

V("vo_name", "姓名与称呼", 7, "上", 1,
  "认读 name、friend、girl 和 boy。",
  [("name", "名字"), ("friend", "朋友"), ("girl", "女孩"), ("boy", "男孩")], "vocab7")

G("gr_be7", "be 动词 am、is、are", 7, "上", 1,
  "能按主语选用 am、is 或 are。", "be_have", [
    q("I ___ Gina. 横线处填哪一个？", "am",
      ["is", "are", "be"], "I 后面用 am。"),
    q("She ___ my friend. 横线处填哪一个？", "is",
      ["am", "are", "be"], "She 后面用 is。"),
    q("They ___ students. 横线处填哪一个？", "are",
      ["am", "is", "be"], "They 后面用 are。"),
    q("哪一句是正确的？", "He is a boy.",
      ["He am a boy.", "He are a boy.", "He be a boy."], "He 和 is 搭配。"),
])

F("fu_intro", "问候与自我介绍", 7, "上", 1,
  "能问候别人，并说出自己的名字。", "func_school", [
    q("初次见面，对方说 Nice to meet you. 你应回答什么？", "Nice to meet you, too.",
      ["Good night.", "See you yesterday.", "Nice to meeting you, too."], "回答 Nice to meet you 时加上 too。"),
    q("想告诉别人自己叫 Gina，哪一句合适？", "My name is Gina.",
      ["Your name is Gina.", "She name is Gina.", "My name are Gina."], "说自己的名字用 My name is。"),
    q("早上见面，哪一句是问候？", "Good morning.",
      ["Good mornings.", "Good moning.", "Good monring."], "Good morning 用来问候早晨。"),
    q("对方问 What's your name? 你叫 Tom，应回答什么？", "My name is Tom.",
      ["His name is Tom.", "I name Tom.", "You are Tom?"], "询问你的名字时，用 My name is 回答。"),
])

R("rw_intro", "读自我介绍", 7, "上", 1,
  "读一段自我介绍，找出姓名和身份。", "read_detail", [
    q("Hello. My name is Gina. I am 12. I am a student. 她叫什么？", "Gina",
      ["Alice", "Tom", "Jack"], "短文写 My name is Gina。"),
    q("Hello. My name is Gina. I am 12. I am a student. 她是做什么的？", "学生",
      ["老师", "医生", "司机"], "I am a student 是学生。"),
    q("Hi. I am Jack. I am a boy. My friend is Gina. Jack 的朋友是谁？", "Gina",
      ["Tom", "Alice", "Mike"], "短文写 My friend is Gina。"),
    q("Hi. I am Jack. I am a boy. My friend is Gina. 哪一句和短文一致？", "Jack is a boy.",
      ["Jack is a girl.", "Gina is Jack.", "Jack is 12."], "短文只说 Jack is a boy，没有说他 12 岁。"),
])

V("vo_family7", "家庭成员", 7, "上", 2,
  "认读 family、parent、sister 和 brother。",
  [("family", "家庭"), ("parent", "父或母"), ("sister", "姐姐或妹妹"), ("brother", "哥哥或弟弟")], "vocab7")

G("gr_this7", "This is 与 These are", 7, "上", 2,
  "能用 This is 介绍单数，用 These are 介绍复数。", "noun_pron", [
    q("介绍一位姐姐，哪一句正确？", "This is my sister.",
      ["These are my sister.", "This are my sister.", "These is my sister."], "一个人用 This is。"),
    q("介绍两个弟弟，哪一句正确？", "These are my brothers.",
      ["This is my brothers.", "These is my brothers.", "This are my brothers."], "复数用 These are。"),
    q("These are my parents. 这句在说什么？", "这些是我的父母",
      ["这是我的姐姐", "这些是我的书", "这是我的朋友"], "parents 是父母，these are 表示这些是。"),
    q("That is my brother. 哪一个词表示远指单数？", "That",
      ["These", "Those", "Are"], "That 指较远的那一个。"),
])

G("gr_plural7", "名词复数", 7, "上", 2,
  "能把常见可数名词变成复数。", "noun_pron", [
    q("book 的复数是哪一个？", "books",
      ["bookes", "book", "bookies"], "一般直接加 s，books。"),
    q("box 的复数是哪一个？", "boxes",
      ["boxs", "boxies", "box"], "以 x 结尾加 es，boxes。"),
    q("family 的复数是哪一个？", "families",
      ["familys", "familyes", "familis"], "辅音字母加 y 结尾，变 y 为 i 再加 es。"),
    q("哪一句的名词复数是正确的？", "I have two sisters.",
      ["I have two sister.", "I have two sisteres.", "I have two sisteries."], "two 后面用复数 sisters。"),
])

P("ph_s", "词尾 s 的读音", 7, "上", 2,
  "能分辨词尾 -s、-es 读 /s/、/z/ 还是 /ɪz/。", "esound", [
    q("books 词尾 s 的读音和哪一个同类？", "maps",
      ["pens", "bags", "buses"], "books 和 maps 的词尾都读 /s/。"),
    q("bags 词尾 s 的读音和哪一个同类？", "pens",
      ["books", "maps", "buses"], "bags 和 pens 的词尾都读 /z/。"),
    q("哪个单词的词尾读 /ɪz/？", "buses",
      ["books", "bags", "maps"], "buses 的 -es 读 /ɪz/。"),
    q("boxes 的词尾和哪个词的读音相同？", "watches",
      ["cats", "dogs", "birds"], "boxes 和 watches 的词尾都读 /ɪz/。"),
])

F("fu_family7", "介绍家人", 7, "上", 2,
  "能向别人介绍自己的家人。", "func_school", [
    q("想把姐姐介绍给同学，哪一句合适？", "This is my sister.",
      ["These are my sister.", "She is my parent?", "I am your sister."], "介绍一个人用 This is。"),
    q("对方问 Who is he? 他是你的弟弟，应回答什么？", "He is my brother.",
      ["She is my brother.", "He are my brother.", "This are my brother."], "弟弟是 he，用 is。"),
    q("These are my parents. 说话人在介绍谁？", "父母",
      ["同学", "老师", "朋友的书"], "parents 是父母。"),
    q("哪一句能用来介绍照片里的一家人？", "This is my family.",
      ["This is my schoolbag.", "These are my pens.", "This are my family."], "family 是家庭。"),
])

R("rw_family7", "读家庭介绍", 7, "上", 2,
  "读一段家庭介绍，找出人物关系。", "read_detail", [
    q("This is my family. These are my parents. This is my sister, Gina. 说话人的姐姐是谁？", "Gina",
      ["Tom", "Alice", "Jack"], "This is my sister, Gina 说明姐姐是 Gina。"),
    q("This is my family. These are my parents. This is my sister, Gina. 哪一句和短文一致？", "Gina is the speaker's sister.",
      ["Gina is the speaker's brother.", "The speaker has no parents.", "Gina is a parent."],
      "短文说 This is my sister, Gina。"),
    q("I have a brother. His name is Tom. I have no sister. 说话人有姐姐吗？", "没有",
      ["有一个", "有两个", "短文没说"], "I have no sister 是没有姐姐或妹妹。"),
    q("I have a brother. His name is Tom. I have no sister. Tom 是谁？", "说话人的弟弟或哥哥",
      ["说话人的姐姐", "说话人的父母", "说话人的老师"], "His name is Tom 指 brother。"),
])

V("vo_school7", "学习用品", 7, "上", 3,
  "认读 pencil、eraser、dictionary 和 ruler。",
  [("pencil", "铅笔"), ("eraser", "橡皮"), ("dictionary", "词典"), ("ruler", "尺子")], "vocab7")

G("gr_poss7", "形容词性物主代词", 7, "上", 3,
  "能选用 my、your、his、her 修饰名词。", "noun_pron", [
    q("这是她的橡皮。哪一句正确？", "This is her eraser.",
      ["This is she eraser.", "This is hers eraser.", "This is her an eraser."], "her 后面直接加名词。"),
    q("___ pencil is blue. 铅笔是 Tom 的，横线处填哪一个？", "His",
      ["He", "Him", "Her"], "Tom 是男性，形容词性物主代词用 His。"),
    q("I 的形容词性物主代词是哪一个？", "my",
      ["me", "mine", "myself"], "I 对应 my，不能用 myself。"),
    q("哪一句是正确的？", "Your dictionary is here.",
      ["You dictionary is here.", "Your is dictionary here.", "Yours dictionary is here."],
      "your 修饰 dictionary，名词性物主代词 yours 后面不再加名词。"),
])

G("gr_yesno", "be 动词一般疑问句", 7, "上", 3,
  "能把含 be 动词的句子改成一般疑问句并作简答。", "be_have", [
    q("This is her pencil. 改成一般疑问句，哪一句正确？", "Is this her pencil?",
      ["Does this is her pencil?", "Is this her pencil.", "Are this her pencil?"],
      "be 动词提到句首，this 仍用 is。"),
    q("Are you Gina? 肯定简答是哪一句？", "Yes, I am.",
      ["Yes, I are.", "Yes, I'm.", "Yes, I is."], "简答 Yes, I am 不能缩写 am。"),
    q("Is he your brother? 否定简答是哪一句？", "No, he isn't.",
      ["No, he aren't.", "No, he not.", "No, he doesn't."], "he 和 is 对应，否定用 isn't。"),
    q("哪一句是一般疑问句？", "Are these your rulers?",
      ["These are your rulers.", "Your rulers are these.", "What these are?"],
      "Are these 把 are 放在句首。"),
])

F("fu_lost", "认领失物", 7, "上", 3,
  "能询问物品是谁的，并回答是或不是。", "func_school", [
    q("捡到一支铅笔，想问是不是对方的，哪一句合适？", "Is this your pencil?",
      ["This is your pencil.", "Are this your pencil?", "What your pencil?"], "询问用 Is this your pencil。"),
    q("对方问 Is this your eraser? 是你的，应回答什么？", "Yes, it is.",
      ["Yes, it are.", "No, it is mine.", "Yes, I am."], "物品用 it，肯定是 Yes, it is。"),
    q("失物招领牌上写什么可以表示「请找老师」？", "Ask the teacher for it.",
      ["I am the teacher.", "This are a teacher.", "Ask you teacher."], "Ask the teacher for it 是向老师索取。"),
    q("想说这本词典是他的，哪一句合适？", "This is his dictionary.",
      ["This is he dictionary.", "This is him dictionary.", "This are his dictionary."], "his 修饰 dictionary。"),
])

R("rw_notice", "读失物招领", 7, "上", 3,
  "读一则失物招领，找出物品和联系人。", "read_detail", [
    q("Found: a blue pencil. Is this your pencil? Call Mary at 622-6033. 捡到的是什么？", "一支蓝色铅笔",
      ["一块橡皮", "一本词典", "一把尺子"], "a blue pencil 是蓝色铅笔。"),
    q("Found: a blue pencil. Is this your pencil? Call Mary at 622-6033. 应该给谁打电话？", "Mary",
      ["Gina", "Tom", "Jack"], "Call Mary 是给 Mary 打电话。"),
    q("Lost: my dictionary. My name is Tom. Please call 139-0011. 谁丢了词典？", "Tom",
      ["Mary", "Gina", "Alice"], "My name is Tom，丢的是 my dictionary。"),
    q("Lost: my dictionary. My name is Tom. Please call 139-0011. 哪一句和启事一致？", "Tom lost a dictionary.",
      ["Tom found a dictionary.", "Mary lost a pencil.", "The dictionary is blue."],
      "Lost: my dictionary 表示词典丢失了。"),
])

V("vo_room7", "房间与家具", 7, "上", 4,
  "认读 room、bed、table 和 chair。",
  [("room", "房间"), ("bed", "床"), ("table", "桌子"), ("chair", "椅子")], "vocab7")

G("gr_prep7", "方位介词", 7, "上", 4,
  "能用 in、on、under 表示物品的位置。", "there_prep", [
    q("书在桌子上。哪一句正确？", "The book is on the table.",
      ["The book is under the table.", "The book is in the table.", "The book are on the table."],
      "在表面上用 on。"),
    q("包在床底下。哪一句正确？", "The bag is under the bed.",
      ["The bag is on the bed.", "The bag is under the chair only.", "The bag are under the bed."],
      "在下面用 under。"),
    q("Where is my schoolbag? 这句在问什么？", "我的书包在哪里",
      ["我的书包是什么颜色", "书包是谁的", "书包多少钱"], "Where 问地点。"),
    q("钥匙在书包里。哪一句正确？", "The keys are in the schoolbag.",
      ["The keys is in the schoolbag.", "The keys are on the in.", "The key are in the schoolbag."],
      "keys 是复数，用 are；在里面用 in。"),
])

F("fu_where7", "询问位置", 7, "上", 4,
  "能询问东西在哪里，并说明位置。", "func_life", [
    q("找不到书包，哪一句用来询问？", "Where is my schoolbag?",
      ["What is my schoolbag?", "Where are my schoolbag?", "Who is my schoolbag?"],
      "单数物品用 Where is。"),
    q("书包在椅子下面，应回答什么？", "It is under the chair.",
      ["It are under the chair.", "It is the under chair.", "They is under the chair."],
      "单数用 It is under。"),
    q("对方说 Where are my books? 书在桌子上，应回答什么？", "They are on the table.",
      ["It is on the table.", "They is on the table.", "They are in the table."],
      "books 用 they are，在桌面上用 on。"),
    q("哪一句是在请对方看床底下？", "Look under the bed.",
      ["Look the bed under.", "Look on name.", "See you under."], "Look under the bed 是看床底下。"),
])

R("rw_room7", "读房间描述", 7, "上", 4,
  "读一段房间描述，找出物品位置。", "read_detail", [
    q("This is my room. The book is on the table. The bag is under the chair. 书在哪里？", "在桌子上",
      ["在椅子下面", "在书包里", "在床上"], "The book is on the table。"),
    q("This is my room. The book is on the table. The bag is under the chair. 包在哪里？", "在椅子下面",
      ["在桌子上", "在床上", "在书里面"], "The bag is under the chair。"),
    q("The keys are in the schoolbag. The schoolbag is on the bed. 钥匙在哪里？", "在书包里",
      ["在床底下", "在桌子上", "在椅子上"], "The keys are in the schoolbag。"),
    q("The keys are in the schoolbag. The schoolbag is on the bed. 哪一句和短文一致？", "The schoolbag is on the bed.",
      ["The keys are on the bed.", "The schoolbag is under the bed.", "The keys are under the chair."],
      "书包在床上，钥匙在书包里，不是直接在床上。"),
])

V("vo_ball", "球类运动", 7, "上", 5,
  "认读 basketball、soccer、tennis 和 volleyball。",
  [("basketball", "篮球"), ("soccer", "足球"), ("tennis", "网球"), ("volleyball", "排球")], "vocab7")

G("gr_have", "have 与 has", 7, "上", 5,
  "能按主语选用 have 或 has。", "be_have", [
    q("I ___ a soccer ball. 横线处填哪一个？", "have",
      ["has", "am", "is"], "I 后面用 have。"),
    q("She ___ a tennis ball. 横线处填哪一个？", "has",
      ["have", "are", "haves"], "She 后面用 has。"),
    q("They ___ two basketballs. 横线处填哪一个？", "have",
      ["has", "haves", "is"], "They 后面用 have。"),
    q("哪一句是正确的？", "He has a volleyball.",
      ["He have a volleyball.", "He haves a volleyball.", "He have volleyballs a."], "He 用 has。"),
])

G("gr_do", "do 与 does", 7, "上", 5,
  "能用 do 或 does 构成一般现在时的疑问句和否定句。", "present", [
    q("___ you have a soccer ball? 横线处填哪一个？", "Do",
      ["Does", "Are", "Is"], "you 用 Do。"),
    q("___ she have a tennis ball? 横线处填哪一个？", "Does",
      ["Do", "Is", "Has"], "she 用 Does，后面动词用原形 have。"),
    q("他没有篮球。哪一句正确？", "He doesn't have a basketball.",
      ["He don't have a basketball.", "He doesn't has a basketball.", "He not have a basketball."],
      "doesn't 后面用动词原形 have。"),
    q("Do they have a volleyball? 肯定简答是哪一句？", "Yes, they do.",
      ["Yes, they have.", "Yes, they does.", "Yes, they are."], "Do 提问用 do 回答。"),
])

F("fu_ball", "谈论运动", 7, "上", 5,
  "能询问别人有没有球，并谈论运动。", "func_school", [
    q("想问对方有没有足球，哪一句合适？", "Do you have a soccer ball?",
      ["Are you have a soccer ball?", "Does you have a soccer ball?", "Do you has a soccer ball?"],
      "you 用 Do you have。"),
    q("对方问 Do you have a basketball? 你有，应回答什么？", "Yes, I do.",
      ["Yes, I have.", "Yes, I does.", "Yes, I am."], "Do you 的肯定简答是 Yes, I do。"),
    q("想说我们在学校打排球，哪一句合适？", "We play volleyball at school.",
      ["We plays volleyball at school.", "We play the volleyballs at school always the.", "Us play volleyball."],
      "We 后面用动词原形 play。球类前通常不加 the。"),
    q("Let's play soccer. 这句是在做什么？", "建议去踢足球",
      ["询问足球的价格", "说自己没有足球", "介绍一个姐姐"], "Let's 用来提出建议。"),
])

R("rw_ball", "读运动短文", 7, "上", 5,
  "读一段运动短文，判断谁有什么球。", "read_detail", [
    q("Tom has a basketball. He doesn't have a soccer ball. His sister has a tennis ball. Tom 有足球吗？", "没有",
      ["有", "有两个", "短文没说"], "He doesn't have a soccer ball。"),
    q("Tom has a basketball. He doesn't have a soccer ball. His sister has a tennis ball. 谁有网球？", "Tom 的姐姐或妹妹",
      ["Tom", "Tom 的爸爸", "Tom 的老师"], "His sister has a tennis ball。"),
    q("We have a volleyball. We play it after class. 他们有什么？", "一个排球",
      ["一个篮球", "一个足球", "一个网球"], "a volleyball 是排球。"),
    q("We have a volleyball. We play it after class. 他们什么时候打？", "课后",
      ["早上起床前", "在家里睡觉时", "只在周末的夜里"], "after class 是课后。"),
])

V("vo_food7", "食物", 7, "上", 6,
  "认读 banana、hamburger、salad 和 ice-cream。",
  [("banana", "香蕉"), ("hamburger", "汉堡包"), ("salad", "沙拉"), ("ice-cream", "冰激凌")], "vocab7")

G("gr_count", "可数与不可数名词", 7, "上", 6,
  "能区分可数名词和不可数名词，并选用 a、an 或 some。", "noun_pron", [
    q("banana 是可数名词。哪一句正确？", "I like bananas.",
      ["I like a bananaes.", "I like bananaes.", "I like an bananas."], "可数名词复数是 bananas。"),
    q("milk 是不可数名词。哪一句正确？", "I like milk.",
      ["I like a milk.", "I like milks.", "I like an milk."], "不可数名词不加 a，也不加 s。"),
    q("想要一些沙拉，哪一句正确？", "I want some salad.",
      ["I want a salades.", "I want some salads the count.", "I want an salad."],
      "salad 在这里作不可数食物，用 some salad。"),
    q("哪一个是不可数名词？", "milk",
      ["banana", "hamburger", "apple"], "milk 不可数；香蕉、汉堡和苹果可数。"),
])

G("gr_like7", "like 的句型", 7, "上", 6,
  "能用 like 的肯定句、否定句和疑问句谈论喜好。", "present", [
    q("她喜欢香蕉。哪一句正确？", "She likes bananas.",
      ["She like bananas.", "She likes banana.", "She like a bananas."], "She 后面动词加 s，bananas 用复数。"),
    q("我不喜欢汉堡。哪一句正确？", "I don't like hamburgers.",
      ["I doesn't like hamburgers.", "I don't likes hamburgers.", "I not like hamburgers."],
      "I 的否定用 don't，后面动词用原形。"),
    q("___ she like salad? 横线处填哪一个？", "Does",
      ["Do", "Is", "Are"], "she 用 Does，like 用原形。"),
    q("Do you like ice-cream? 否定回答是哪一句？", "No, I don't.",
      ["No, I doesn't.", "No, I'm not.", "No, I don't like."], "Do you 的否定简答是 No, I don't。"),
])

F("fu_food7", "谈论食物", 7, "上", 6,
  "能询问和表达对食物的喜好。", "func_life", [
    q("想问对方喜不喜欢沙拉，哪一句合适？", "Do you like salad?",
      ["Are you like salad?", "Does you like salad?", "Do you likes salad?"], "you 用 Do you like。"),
    q("你喜欢香蕉，应怎么说？", "I like bananas.",
      ["I likes bananas.", "I like bananaes.", "I am like bananas."], "I like 加可数名词复数。"),
    q("对方说 I don't like hamburgers. 这句话的意思是什么？", "我不喜欢汉堡",
      ["我有汉堡", "我正在吃汉堡", "汉堡在桌子上"], "don't like 表示不喜欢。"),
    q("想建议一起吃冰激凌，哪一句合适？", "Let's have some ice-cream.",
      ["Let's has some ice-cream.", "Let have an ice-cream the.", "Let's having ice-cream."],
      "Let's 后面用动词原形 have。"),
])

R("rw_food7", "读饮食短文", 7, "上", 6,
  "读一段饮食短文，找出人物的喜好。", "read_detail", [
    q("Gina likes bananas and milk. She doesn't like hamburgers. Gina 喜欢汉堡吗？", "不喜欢",
      ["喜欢", "只在学校喜欢", "短文没说"], "She doesn't like hamburgers。"),
    q("Gina likes bananas and milk. She doesn't like hamburgers. 她喜欢喝什么？", "牛奶",
      ["沙拉", "汉堡", "茶"], "likes milk 是喜欢牛奶。"),
    q("Tom likes salad. He doesn't like ice-cream. His sister likes ice-cream. 谁喜欢冰激凌？", "Tom 的姐姐或妹妹",
      ["Tom", "Gina", "Tom 的爸爸"], "His sister likes ice-cream。"),
    q("Tom likes salad. He doesn't like ice-cream. 哪一句和短文一致？", "Tom likes salad.",
      ["Tom likes ice-cream.", "Tom doesn't like salad.", "Tom has no sister in this text and he likes hamburgers."],
      "第一句就是 Tom likes salad。干扰项里后半句短文没有说到汉堡。"),
])

V("vo_clothes7", "衣物与颜色", 7, "上", 7,
  "认读 sock、shirt、skirt 和 sweater。",
  [("sock", "短袜"), ("shirt", "衬衫"), ("skirt", "短裙"), ("sweater", "毛衣")], "vocab7")

G("gr_much", "How much 问价格", 7, "上", 7,
  "能用 How much 询问价格，并用美元表达价钱。", "question", [
    q("询问这双袜子多少钱，哪一句正确？", "How much are these socks?",
      ["How much is these socks?", "How many are these socks?", "How much these socks are?"],
      "socks 是复数，用 are；问价格用 How much。"),
    q("这件毛衣 20 美元。哪一句正确？", "The sweater is 20 dollars.",
      ["The sweater are 20 dollars.", "The sweater is 20 dollar.", "The sweater has 20 dollar."],
      "价格里美元复数用 dollars，单数毛衣用 is。"),
    q("How much is this shirt? 这句在问什么？", "这件衬衫多少钱",
      ["衬衫是什么颜色", "衬衫在哪里", "你有几件衬衫"], "How much 问价格。"),
    q("短裙 15 美元。哪一句正确？", "The skirt is fifteen dollars.",
      ["The skirt are fifteen dollars.", "The skirt is fifteen dollar.", "The skirts is fifteen dollars."],
      "一件短裙用 is，dollars 用复数。"),
])

F("fu_shop7", "购物用语", 7, "上", 7,
  "能询问价格、颜色，并决定买或不买。", "func_life", [
    q("在商店想问毛衣的价格，哪一句合适？", "How much is the sweater?",
      ["How many is the sweater?", "What much is the sweater?", "How much the sweater is?"],
      "单数物品用 How much is。"),
    q("店员说 It is 8 dollars. 你决定买下，哪一句合适？", "I'll take it.",
      ["I take them are.", "I'll taking it.", "I am take it."], "I'll take it 表示我买下它。"),
    q("想要一件红色的衬衫，哪一句合适？", "I want a red shirt.",
      ["I want a red shirts.", "I want red a shirt.", "I wants a red shirt."], "a red shirt 是一件红色衬衫。"),
    q("Can I help you? 店员这句是在做什么？", "询问你需要什么帮助",
      ["询问你的名字", "说衬衫很贵", "介绍自己的家人"], "Can I help you 是商店里的招呼。"),
])

R("rw_shop7", "读购物对话", 7, "上", 7,
  "读一段购物对话，找出价格和决定。", "read_detail", [
    q("Woman: How much is this skirt? Clerk: It is 15 dollars. Woman: I'll take it. 短裙多少钱？", "15 美元",
      ["8 美元", "20 美元", "50 美元"], "It is 15 dollars。"),
    q("Woman: How much is this skirt? Clerk: It is 15 dollars. Woman: I'll take it. 她买了吗？", "买了",
      ["没买", "只问了颜色", "店员不卖"], "I'll take it 表示买下。"),
    q("Boy: How much are the socks? Clerk: They are 5 dollars. Boy: They are too dear. I will not take them. 袜子贵不贵？按男孩的话。", "他认为太贵",
      ["他认为很便宜", "他马上买下", "短文没谈价格"], "too dear 是太贵，他不买。"),
    q("选词填空：The sweater is 20 ___. I will take it. 哪个词使句子完整？", "dollars",
      ["dollar", "much", "color"], "20 后面用复数 dollars。"),
])

V("vo_date", "月份与序数词", 7, "上", 8,
  "认读 January、February、March 和 April。",
  [("January", "一月"), ("February", "二月"), ("March", "三月"), ("April", "四月")], "vocab7")

G("gr_when7", "When 问日期", 7, "上", 8,
  "能用 When 询问日期，并用月份加序数词回答。", "question", [
    q("询问生日是哪一天，哪一句正确？", "When is your birthday?",
      ["When your birthday is?", "What is your birthday?", "When are your birthday?"],
      "When is your birthday 问日期。"),
    q("生日是 5 月 2 日。哪一句正确？", "My birthday is on May 2nd.",
      ["My birthday is on May two.", "My birthday is in May 2nd.", "My birthday are on May 2nd."],
      "具体日期用 on，序数词用 2nd。"),
    q("第一个月是哪一个？", "January",
      ["February", "March", "April"], "January 是一月。"),
    q("third 对应的基数词是哪一个？", "three",
      ["thirdly", "thirty", "thirteen"], "third 是第三，基数词是 three。"),
])

F("fu_bday7", "谈论生日", 7, "上", 8,
  "能询问和说明生日、年龄。", "func_school", [
    q("想问对方的生日，哪一句合适？", "When is your birthday?",
      ["Where is your birthday?", "When are your birthday?", "How much is your birthday?"],
      "问日期用 When is your birthday。"),
    q("你的生日是 9 月 5 日，应回答什么？", "It is on September 5th.",
      ["It is in September 5.", "It is on September five.", "It are on September 5th."],
      "具体日子用 on 加序数词。"),
    q("How old are you? 这句在问什么？", "你多大",
      ["你的生日是哪天", "你叫什么", "你来自哪里"], "How old 问年龄。"),
    q("想说 Alice 十二岁，哪一句合适？", "Alice is twelve.",
      ["Alice are twelve.", "Alice is twelfth.", "Alice has twelve."], "年龄用基数词 twelve，不是序数词 twelfth。"),
])

R("rw_cal7", "读活动安排", 7, "上", 8,
  "读一则活动安排，找出日期和活动。", "read_detail", [
    q("School Day is on September 21st. The basketball game is on October 2nd. 校庆是哪一天？", "9 月 21 日",
      ["10 月 2 日", "9 月 2 日", "10 月 21 日"], "School Day is on September 21st。"),
    q("School Day is on September 21st. The basketball game is on October 2nd. 篮球赛在哪一天？", "10 月 2 日",
      ["9 月 21 日", "10 月 21 日", "11 月 2 日"], "October 2nd 是 10 月 2 日。"),
    q("Alice's birthday party is on May 5th. She is twelve. 聚会在几月？", "五月",
      ["四月", "六月", "三月"], "May 是五月。"),
    q("Alice's birthday party is on May 5th. She is twelve. 哪一句和短文一致？", "Alice is twelve.",
      ["Alice is five.", "The party is in May 5th without on.", "Alice is twenty."],
      "She is twelve。年龄是十二，不是五岁或二十岁。"),
])

V("vo_subj", "学科词汇", 7, "上", 9,
  "认读 subject、science、history 和 geography。",
  [("subject", "学科"), ("science", "科学"), ("history", "历史"), ("geography", "地理")], "vocab7")

G("gr_because", "because 说明原因", 7, "上", 9,
  "能用 because 回答 why，说明原因。", "clause_adv", [
    q("Why do you like science? 哪一句适合作为回答？", "Because it is interesting.",
      ["Because it are interesting.", "So it is interesting.", "Why it is interesting."],
      "回答 why 用 because，it 用 is。"),
    q("哪一句正确？", "I like history because it is fun.",
      ["I like history because it are fun.", "I like history so it is fun.", "Because I like history it is fun."],
      "because 连接原因，it is fun。"),
    q("Because he likes P.E. 这半句是在做什么？", "说明原因",
      ["询问时间", "询问价格", "发出命令"], "because 用来说明原因。"),
    q("她喜欢地理，因为它有用。哪一句正确？", "She likes geography because it is useful.",
      ["She like geography because it is useful.", "She likes geography because it are useful.", "She likes geography so it is useful."],
      "She likes，because 从句里 it is。"),
])

F("fu_subj", "谈论最喜欢的学科", 7, "上", 9,
  "能说出最喜欢的学科并说明原因。", "func_school", [
    q("想问对方最喜欢的学科，哪一句合适？", "What's your favorite subject?",
      ["What's your favorite subjects?", "What your favorite subject is?", "How much is your favorite subject?"],
      "What's your favorite subject 问最喜欢的一门学科。"),
    q("你最喜欢科学，应回答什么？", "My favorite subject is science.",
      ["My favorite subject are science.", "I favorite science.", "Science is my favorite subject are."],
      "subject 是单数，用 is。"),
    q("想问为什么喜欢历史，哪一句合适？", "Why do you like history?",
      ["Why does you like history?", "Why do you likes history?", "Because do you like history?"],
      "you 用 Why do you like。"),
    q("Friday 下午有地理课。想告诉同学，哪一句合适？", "We have geography on Friday afternoon.",
      ["We has geography on Friday afternoon.", "We have geography in Friday afternoon.", "We have geography on Friday the afternoon is."],
      "在星期几的下午用 on Friday afternoon，we have。"),
])

R("rw_subj", "读课程介绍", 7, "上", 9,
  "读一段课程介绍，找出喜欢的学科和原因。", "read_detail", [
    q("My favorite subject is science. I have it on Monday. I like it because it is interesting. 最喜欢的学科是什么？", "科学",
      ["历史", "地理", "体育"], "favorite subject is science。"),
    q("My favorite subject is science. I have it on Monday. I like it because it is interesting. 为什么喜欢？", "因为它有趣",
      ["因为它很难", "因为在星期五", "因为老师很严格，短文没有写别的原因"], "because it is interesting。"),
    q("Jack's favorite subject is history. He thinks it is useful. He doesn't like geography. Jack 喜欢地理吗？", "不喜欢",
      ["喜欢", "只在星期一喜欢", "短文没说"], "He doesn't like geography。"),
    q("Jack's favorite subject is history. He thinks it is useful. 哪一句和短文一致？", "Jack likes history.",
      ["Jack likes geography.", "Jack's favorite subject is science.", "History is not useful for Jack."],
      "favorite subject is history，而且他认为有用。"),
])
