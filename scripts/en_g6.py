# -*- coding: utf-8 -*-
"""六年级上、下。人教 PEP 三年级起点的常见单元顺序，册次待核。"""
from en_tx import V, P, G, F, R, X

# ---------- 六上 ----------

V("vo_city", "城市场所", 6, "上", 1,
  "认读 hospital、cinema、bookstore 和 post office。",
  [("hospital", "医院"), ("cinema", "电影院"), ("bookstore", "书店"), ("post office", "邮局")])

G("gr_turn", "左转、右转和直行", 6, "上", 1,
  "用 Turn left、Turn right 和 Go straight 指路。", "func_out", [
    ("c", "想说「在书店左转」，应选哪一句？", "Turn left at the bookstore.",
     ["Turn right at the bookstore.", "Go straight at the bookstore.", "Turn bookstore left."], "左转是 Turn left。"),
    ("c", "Where is the hospital? 这句是在问什么？", "医院在哪里",
     ["医院是谁的", "医院里有什么", "怎么去电影院"], "Where is 问地点。"),
    ("c", "Go straight. 这句是在说什么？", "直行",
     ["左转", "右转", "停下"], "Go straight 是直行。"),
    ("c", "Turn right at the cinema. 在电影院怎么走？", "右转",
     ["左转", "直行", "往回走"], "Turn right 是右转。"),
])

F("fu_way", "问路和指路", 6, "上", 1,
  "用 How can I get to 问路，并用 next to 说明在旁边。", "func_out", [
    ("c", "想问怎么去医院，应说哪一句？", "How can I get to the hospital?",
     ["Where is a turn left?", "What is the hospital like?", "When is the hospital?"], "问路说 How can I get to。"),
    ("c", "The bookstore is next to the cinema. 书店在哪里？", "在电影院旁边",
     ["在医院里", "在邮局对面很远", "在学校里面"], "next to the cinema 是在电影院旁边。"),
    ("c", "Turn left at the post office. 在邮局怎样走？", "左转",
     ["右转", "直行", "停下"], "Turn left。"),
    ("c", "Is it far? 若很近，应回答哪一句？", "No. It is near.",
     ["Yes. It is far.", "Turn right.", "Go to the hospital."], "近是 near，所以用 No。"),
])

R("rw_way", "读懂指路", 6, "上", 1,
  "读指路短文，找出怎么走。", "read_text", [
    ("c", "读一读：Go straight. Turn left at the bookstore. The hospital is on the right. 在书店怎样走？", "左转",
     ["右转", "停下", "往回走"], "Turn left at the bookstore。"),
    ("c", "读一读：The cinema is next to the hospital. 电影院在哪里？", "在医院旁边",
     ["在书店里面", "在邮局里", "离医院很远"], "next to the hospital。"),
    ("c", "读一读：How can I get to the post office? Turn right at the cinema. 去邮局要在哪里右转？", "在电影院",
     ["在书店", "在医院", "在学校"], "Turn right at the cinema。"),
    ("c", "读一读：It is not far. Go straight and you can see it. 哪一句和短文一致？", "不远，直行就能看见。",
     ["很远，要左转。", "在书店左转。", "医院在右边。"], "not far，Go straight。"),
])

V("vo_trans", "交通工具", 6, "上", 2,
  "认读 bus、plane、ship 和 train。",
  [("bus", "公共汽车"), ("plane", "飞机"), ("ship", "轮船"), ("train", "火车")])

G("gr_must", "must 与交通规则", 6, "上", 2,
  "用 must 和 Do not 说明交通规则。", "modal_imp", [
    ("c", "哪一句表示「你必须停」？", "You must stop.",
     ["You must stops.", "You are must stop.", "You stop must."], "must 后面用动词原形 stop。"),
    ("c", "Do not go at a red light. 红灯时应该怎样？", "不要走",
     ["可以走", "必须跑", "左转"], "Do not go 是不要走。"),
    ("c", "We must look right before crossing. 过马路前必须看哪边？", "右边",
     ["左边", "上面", "后面"], "句子写的是 look right。"),
    ("c", "I must pay attention to the traffic lights. 这句是在说什么？", "必须注意交通信号灯",
     ["可以不看信号灯", "信号灯在书店", "我不会看信号灯"], "must pay attention to the traffic lights。"),
])

F("fu_come", "说明出行方式", 6, "上", 2,
  "用 I come to school by 说明怎么来学校。", "func_out", [
    ("c", "想说自己骑自行车来学校，应说哪一句？", "I come to school by bike.",
     ["I come to school by bus.", "I come to school by train.", "I come to school by plane."], "自行车是 by bike。"),
    ("c", "How do you come to school? 这句是在问什么？", "你怎么来学校",
     ["学校在哪里", "你必须停下吗", "你喜欢公共汽车吗"], "How do you come 问方式。"),
    ("c", "I usually walk. 这个人通常怎么来？", "步行",
     ["坐公共汽车", "坐火车", "坐飞机"], "walk 是步行。"),
    ("c", "Slow down and stop at a yellow light. 黄灯时应该怎样？", "减速并停下",
     ["加速通过", "不必看灯", "可以跑"], "Slow down and stop。"),
])

R("rw_traffic", "读懂交通规则", 6, "上", 2,
  "读交通短文，按文字找出规则。", "read_text", [
    ("c", "读一读：I come to school by bus. Amy says, \"I come by bike.\" Amy 怎么来学校？", "骑自行车",
     ["坐公共汽车", "步行", "坐火车"], "引号里写的是 I come by bike。"),
    ("c", "读一读：Do not go at a red light. You must stop. 红灯时必须怎样？", "停下",
     ["走", "跑", "左转"], "must stop。"),
    ("c", "读一读：In China, people drive on the right. 在中国，车靠哪边行驶？", "右边",
     ["左边", "中间", "短文没写"], "on the right。"),
    ("c", "读一读：Some children come by subway. 哪一句和短文一致？", "有些孩子坐地铁来。",
     ["所有孩子步行。", "孩子们坐飞机来。", "孩子们不来学校。"], "by subway。"),
])

V("vo_plan", "周末计划", 6, "上", 3,
  "认读 film、trip、supermarket 和 dictionary。",
  [("film", "电影"), ("trip", "旅行"), ("supermarket", "超市"), ("dictionary", "词典")])

G("gr_going", "be going to 一般将来时", 6, "上", 3,
  "用 am、is、are going to 表达打算或将要做的事。", "future", [
    ("c", "哪一句表示「我打算去旅行」？", "I am going to take a trip.",
     ["I am go to take a trip.", "I going to take a trip.", "I are going to take a trip."], "I 用 am going to。"),
    ("c", "What are you going to do? 这句是在问什么？", "你打算做什么",
     ["你正在做什么", "你昨天做了什么", "你会做什么"], "going to 问打算。"),
    ("c", "She is going to see a film. 她打算做什么？", "看电影",
     ["买词典", "去超市", "看望祖父母"], "see a film。"),
    ("c", "We are going to the supermarket. 我们打算去哪里？", "超市",
     ["电影院", "书店", "医院"], "the supermarket。"),
])

F("fu_plan", "谈论计划", 6, "上", 3,
  "用 be going to 说出周末计划。", "func_out", [
    ("c", "想说自己明天打算去旅行，应说哪一句？", "I am going to take a trip tomorrow.",
     ["I am going to see a film tomorrow.", "I am going to the supermarket tomorrow.", "I am going to buy a dictionary tomorrow."], "旅行是 take a trip。"),
    ("c", "What are you going to do this weekend? 这句是在问什么？", "这个周末你打算做什么",
     ["这个周末你正在做什么", "上个周末你做了什么", "你每天做什么"], "this weekend 加上 going to 是打算。"),
    ("c", "He is going to buy a dictionary. 他打算买什么？", "词典",
     ["电影票", "旅行票", "超市里的面包"], "a dictionary。"),
    ("c", "Have a good time! 这句是在说什么？", "祝你玩得开心",
     ["你必须停下", "请靠右走", "这太贵了"], "Have a good time 是祝对方玩得开心。"),
])

R("rw_plan", "读懂周末计划", 6, "上", 3,
  "读计划短文，找出谁打算做什么。", "read_text", [
    ("c", "读一读：I am going to see a film. Amy is going to the supermarket. Amy 打算去哪里？", "超市",
     ["电影院", "书店", "医院"], "Amy is going to the supermarket。"),
    ("c", "读一读：We are going to take a trip next week. 哪一句和短文一致？", "我们下周打算去旅行。",
     ["我们正在旅行。", "我们上周旅行了。", "我们不去旅行。"], "are going to take a trip next week。"),
    ("c", "读一读：Mike is going to buy a dictionary this evening. Mike 今晚打算买什么？", "词典",
     ["电影票", "面包", "地图"], "a dictionary。"),
    ("c", "读一读：Sarah says, \"I am going to read a book.\" Sarah 打算做什么？", "看书",
     ["看电影", "去超市", "去旅行"], "引号里是 read a book。"),
])

V("vo_hobby", "爱好", 6, "上", 4,
  "认读 hobby、hiking、puzzle 和 dancing。",
  [("hobby", "爱好"), ("hiking", "远足"), ("puzzle", "谜题"), ("dancing", "跳舞")])

G("gr_does", "does 与第三人称单数", 6, "上", 4,
  "用 does 提问，并在第三人称单数陈述句里给动词加 s 或 es。", "present3", [
    ("c", "____ he live in China? 横线上应填哪个词？", "Does",
     ["Do", "Is", "Are"], "he 前面的一般现在时疑问句用 Does。"),
    ("c", "哪一句是正确的？", "He lives in China.",
     ["He live in China.", "He living in China.", "He does lives in China."], "He 后面的 live 要变成 lives。"),
    ("c", "Does she like dancing? 肯定回答应选哪一句？", "Yes, she does.",
     ["Yes, she do.", "Yes, she is.", "Yes, she likes."], "Does 的肯定回答是 Yes, she does。"),
    ("c", "What are his hobbies? 这句是在问什么？", "他有什么爱好",
     ["他住在哪里", "他是做什么工作的", "他打算做什么"], "hobbies 是爱好。"),
])

F("fu_pen", "谈论笔友和爱好", 6, "上", 4,
  "用 I have a pen pal 和 He likes 介绍笔友。", "func_out", [
    ("c", "想说自己有一个笔友，应说哪一句？", "I have a pen pal.",
     ["I have a puzzle.", "I like hiking.", "I am dancing."], "笔友是 pen pal。"),
    ("c", "He likes hiking. 他喜欢什么？", "远足",
     ["谜题", "跳舞", "唱歌"], "hiking 是远足。"),
    ("c", "Does your pen pal live in Sydney? 这句是在问什么？", "你的笔友住在悉尼吗",
     ["你的笔友喜欢跳舞吗", "你有谜题吗", "你打算去旅行吗"], "live in Sydney。"),
    ("c", "She likes doing word puzzles. 她喜欢做什么？", "字谜",
     ["远足", "跳舞", "游泳"], "word puzzles 是字谜。"),
])

R("rw_pen", "读懂笔友介绍", 6, "上", 4,
  "读笔友短文，找出住在哪里、爱好是什么。", "read_text", [
    ("c", "读一读：I have a pen pal. He lives in Canada. He likes hiking. 笔友住在哪里？", "加拿大",
     ["中国", "澳大利亚", "英国"], "lives in Canada。"),
    ("c", "读一读：Amy likes dancing and doing word puzzles. 哪一句和短文一致？", "Amy 喜欢跳舞和做字谜。",
     ["Amy 喜欢远足。", "Amy 住在加拿大。", "Amy 不喜欢跳舞。"], "dancing and doing word puzzles。"),
    ("c", "读一读：Does he like puzzles? Yes, he does. 他喜欢谜题吗？", "喜欢",
     ["不喜欢", "没说", "只喜欢远足"], "Yes, he does。"),
    ("c", "读一读：Her hobby is hiking. 她的爱好是什么？", "远足",
     ["跳舞", "字谜", "唱歌"], "hobby is hiking。"),
])

V("vo_job6", "更多职业", 6, "上", 5,
  "认读 factory、worker、postman 和 businessman。",
  [("factory", "工厂"), ("worker", "工人"), ("postman", "邮递员"), ("businessman", "商人")])

G("gr_work", "What does he do", 6, "上", 5,
  "用 What does he do? 询问职业，并用 works 描述在哪里工作。", "present3", [
    ("c", "What does he do? 这句是在问什么？", "他是做什么工作的",
     ["他正在做什么", "他喜欢做什么", "他昨天做了什么"], "What does he do 问职业。"),
    ("c", "He works in a factory. 他在哪里工作？", "工厂",
     ["邮局", "医院", "学校"], "factory 是工厂。"),
    ("c", "哪一句是正确的？", "She works at sea.",
     ["She work at sea.", "She working at sea.", "She does works at sea."], "She 后面用 works。"),
    ("c", "My uncle is a postman. 叔叔的职业是？", "邮递员",
     ["商人", "工人", "渔民"], "postman 是邮递员。"),
])

F("fu_work", "介绍职业和工作地点", 6, "上", 5,
  "用 He is a 和 He works 介绍家人的工作。", "func_out", [
    ("c", "想说妈妈是商人，应说哪一句？", "My mother is a businesswoman.",
     ["My mother is a postman.", "My mother is a worker.", "My mother is a factory."], "女商人是 businesswoman。"),
    ("c", "Where does he work? 这句是在问什么？", "他在哪里工作",
     ["他是谁", "他喜欢什么", "他打算做什么"], "Where does he work 问工作地点。"),
    ("c", "He is a fisherman. He works at sea. 他在哪里工作？", "在海上",
     ["在工厂", "在邮局", "在医院"], "at sea。"),
    ("c", "She works in a university. 她在哪里工作？", "大学",
     ["工厂", "海上", "邮局"], "university 是大学。"),
])

R("rw_work", "读懂职业短文", 6, "上", 5,
  "读职业短文，找出谁做什么、在哪里工作。", "read_text", [
    ("c", "读一读：My father is a worker. He works in a factory. 爸爸在哪里工作？", "工厂",
     ["邮局", "海上", "大学"], "in a factory。"),
    ("c", "读一读：My aunt is a businesswoman. She works in a university. 姑姑或阿姨的职业是？", "商人",
     ["工人", "邮递员", "渔民"], "businesswoman。工作地点是大学，职业仍是商人。"),
    ("c", "读一读：He is a postman. He works in a post office. 哪一句和短文一致？", "他是邮递员，在邮局工作。",
     ["他是工人。", "他在工厂工作。", "他在海上工作。"], "postman，post office。"),
    ("c", "读一读：John wants to be a coach. 约翰想成为什么？", "教练",
     ["商人", "邮递员", "渔民"], "a coach 是教练。"),
])

V("vo_feel", "感受", 6, "上", 6,
  "认读 angry、afraid、sad 和 happy。",
  [("angry", "生气的"), ("afraid", "害怕的"), ("sad", "难过的"), ("happy", "高兴的")])

G("gr_should", "should 提建议", 6, "上", 6,
  "用 should 加动词原形提出建议。", "modal_imp", [
    ("c", "哪一句表示「你应该去看医生」？", "You should see a doctor.",
     ["You should sees a doctor.", "You are should see a doctor.", "You see should a doctor."], "should 后面用动词原形 see。"),
    ("c", "I feel ill. 这句的意思是？", "我感到不舒服",
     ["我很高兴", "我很生气", "我很害怕"], "ill 是不舒服。"),
    ("c", "You should wear warm clothes. 这是在做什么？", "提出建议",
     ["描述过去", "询问价格", "问路"], "should 用来提建议。"),
    ("c", "Do not be sad. 这句的意思是？", "别难过",
     ["别生气", "别害怕", "别高兴"], "sad 是难过。"),
])

F("fu_feel", "询问感受并建议", 6, "上", 6,
  "用 How do you feel? 询问感受，并用 should 给出建议。", "func_out", [
    ("c", "想问对方感觉怎么样，应说哪一句？", "How do you feel?",
     ["What are you going to do?", "Where does he work?", "How do you come to school?"], "问感受说 How do you feel?"),
    ("c", "I am angry. 这个人感觉怎样？", "生气",
     ["害怕", "难过", "高兴"], "angry 是生气。"),
    ("c", "You should take a deep breath. 这句建议做什么？", "深呼吸",
     ["去看医生", "穿暖和的衣服", "数到十"], "take a deep breath 是深呼吸。"),
    ("c", "The mouse is afraid of the cat. 老鼠对猫感觉怎样？", "害怕",
     ["生气", "高兴", "难过"], "afraid of 是害怕。"),
])

R("rw_feel", "读懂感受和建议", 6, "上", 6,
  "读短文，找出人物的感受和建议。", "read_text", [
    ("c", "读一读：Sarah is sad. She should talk to her friends. Sarah 感觉怎样？", "难过",
     ["生气", "害怕", "高兴"], "sad。"),
    ("c", "读一读：I am ill. I should see a doctor. 哪一句和短文一致？", "我不舒服，应该去看医生。",
     ["我很高兴。", "我不应该看医生。", "我很害怕猫。"], "ill，should see a doctor。"),
    ("c", "读一读：He is angry. He should take a deep breath. 他应该做什么？", "深呼吸",
     ["去旅行", "买词典", "骑自行车"], "take a deep breath。"),
    ("c", "读一读：The cat is happy. The mouse is afraid. 谁很高兴？", "猫",
     ["老鼠", "医生", "两个都高兴"], "The cat is happy。"),
])

# ---------- 六下 ----------

P("ph_tone", "陈述句和疑问句的语调", 6, "下", 1,
  "一般疑问句通常用升调，陈述句、祈使句和特殊疑问句通常用降调。", "tone", [
    ("c", "一般疑问句通常用什么语调？", "升调",
     ["降调", "先降后升再降", "没有语调"], "Do you like apples? 这一类一般疑问句通常用升调。"),
    ("c", "陈述句 I am ten. 朗读时通常用什么语调？", "降调",
     ["升调", "一直升到最高", "不读语调"], "陈述句通常用降调。"),
    ("c", "祈使句 Open the door. 朗读时通常用什么语调？", "降调",
     ["升调", "先升后降再升", "不读语调"], "祈使句通常用降调。"),
    ("c", "Where is the cat? 这一句通常用什么语调？", "降调",
     ["升调", "只升不降", "没有语调"], "以 Where 开头的特殊疑问句通常用降调。"),
])

V("vo_measure", "身高和体重", 6, "下", 1,
  "认读 metre、kilogram、size 和 heavy。",
  [("metre", "米"), ("kilogram", "千克"), ("size", "尺码"), ("heavy", "重的")])

G("gr_comp", "形容词比较级", 6, "下", 1,
  "能写出 tall、long、heavy 的比较级 taller、longer、heavier。", "compare", [
    ("c", "tall 的比较级是哪一个？", "taller",
     ["more tall", "tallest", "tallier"], "tall 的比较级是 taller。"),
    ("c", "哪一句是正确的？", "He is taller.",
     ["He is more taller.", "He is tallier.", "He is more tall."], "taller 前面不要再加 more。"),
    ("c", "long 的比较级是哪一个？", "longer",
     ["more long", "longest", "longger"], "long 的比较级是 longer。"),
    ("c", "heavy 的比较级是哪一个？", "heavier",
     ["more heavy", "heavyler", "heavyer"], "heavy 的比较级是 heavier。"),
])

G("gr_than", "用 than 比较", 6, "下", 1,
  "用比较级加 than 对两者进行比较。", "compare", [
    ("c", "哪一句是正确的比较？", "I am taller than you.",
     ["I am more taller than you.", "I am taller then you.", "I am tall than you."], "比较两者说 taller than。"),
    ("c", "Amy is 1.5 metres tall. John is 1.6 metres tall. 谁更高？", "John",
     ["Amy", "一样高", "无法从这两句知道"], "1.6 大于 1.5，所以 John 更高。"),
    ("n", "Zhang Peng is 48 kilograms. Sarah is 42 kilograms. 更重的那个人是多少千克？", 48,
     "48 大于 42，所以更重的体重是 48 千克。"),
    ("c", "This dinosaur is bigger than that one. 这句在比较什么？", "谁更大",
     ["谁更高", "谁更重", "谁更老"], "bigger 是更大。"),
])

F("fu_tall", "询问身高", 6, "下", 1,
  "用 How tall are you? 和 How heavy are you? 询问身高、体重。", "func_out", [
    ("c", "想问对方多高，应说哪一句？", "How tall are you?",
     ["How old are you?", "How heavy are you?", "How much is it?"], "问身高说 How tall are you?"),
    ("c", "I am 1.6 metres tall. 这句话在说什么？", "身高是 1.6 米",
     ["体重是 1.6 千克", "年龄是 16 岁", "鞋子是 36 码"], "metres 说的是身高。"),
    ("c", "How heavy are you? 若是 40 千克，应回答哪一句？", "I am 40 kilograms.",
     ["I am 1.5 metres.", "I am 12 years old.", "I am size 36."], "体重用 kilograms。"),
    ("c", "Your feet are bigger than mine. 这句在比较什么？", "脚的大小",
     ["身高", "体重", "年龄"], "feet 和 bigger 是在比脚。"),
])

R("rw_cmp", "读懂比较短文", 6, "下", 1,
  "读比较短文，按数字判断谁更高或更重。", "read_text", [
    ("c", "读一读：Amy is 1.5 metres. John is 1.6 metres. John is taller than Amy. 谁更高？", "John",
     ["Amy", "一样高", "短文没比较"], "1.6 大于 1.5，而且句子写 John is taller。"),
    ("n", "读一读：The dinosaur is 4 metres tall. The boy is 1 metre tall. 恐龙高几米？", 4, "4 metres。"),
    ("c", "读一读：Sarah is 42 kilograms. Zhang Peng is 48 kilograms. 谁更重？", "Zhang Peng",
     ["Sarah", "一样重", "无法知道"], "48 大于 42。"),
    ("c", "读一读：My shoes are size 37. Yours are size 35. 哪一句和短文一致？", "我的鞋是 37 码，你的是 35 码。",
     ["我的鞋是 35 码。", "两个人的鞋一样大。", "没有写尺码。"], "size 37 和 size 35。"),
])

G("gr_past", "规则动词过去式", 6, "下", 2,
  "能把 clean、watch、stay 变成过去式 cleaned、watched、stayed。", "past", [
    ("c", "clean 的过去式是哪一个？", "cleaned",
     ["cleans", "cleaning", "clean"], "规则动词 clean 的过去式是 cleaned。"),
    ("c", "哪一句表示「我上周末打扫了房间」？", "I cleaned my room last weekend.",
     ["I clean my room last weekend.", "I cleaning my room last weekend.", "I cleans my room last weekend."], "last weekend 要和过去式 cleaned 一起用。"),
    ("c", "watched 是哪个动词的过去式？", "watch",
     ["wash", "walk", "want"], "watched 来自 watch。"),
    ("c", "I stayed at home. 这句说的是什么时候的事？", "已经发生的事",
     ["正在发生的事", "将要做的事", "每天的习惯"], "stayed 是过去式。"),
])

G("gr_did", "Did 提问", 6, "下", 2,
  "用 Did 加动词原形询问过去的事。", "past", [
    ("c", "____ you clean your room? 问过去的事，横线上应填哪个词？", "Did",
     ["Do", "Does", "Are"], "问过去用 Did。"),
    ("c", "Did you watch TV? 肯定回答应选哪一句？", "Yes, I did.",
     ["Yes, I do.", "Yes, I was.", "Yes, I watched."], "Did 的肯定回答是 Yes, I did。"),
    ("c", "哪一句是正确的？", "Did he wash his clothes?",
     ["Did he washed his clothes?", "Does he washed his clothes?", "Did he washes his clothes?"], "Did 后面用动词原形 wash。"),
    ("c", "I did not stay at home. 这句的意思是？", "我没有待在家里",
     ["我待在家里", "我正待在家里", "我将待在家里"], "did not stay 表示过去没有待着。"),
])

F("fu_weekend", "谈论上周末", 6, "下", 2,
  "用 What did you do last weekend? 谈论已经发生的周末。", "func_out", [
    ("c", "想问上周末做了什么，应说哪一句？", "What did you do last weekend?",
     ["What do you do on the weekend?", "What are you going to do?", "What are you doing?"], "问过去用 What did you do last weekend?"),
    ("c", "I cleaned my room and watched TV. 做了哪两件事？", "打扫房间和看电视",
     ["洗衣服和睡觉", "只打扫房间", "只看电视"], "cleaned my room and watched TV。"),
    ("c", "Did you wash your clothes? 若洗了，应回答哪一句？", "Yes, I did.",
     ["Yes, I do.", "Yes, I was.", "No, I did not wash do."], "Did 的肯定回答是 Yes, I did。"),
    ("c", "I stayed at home all weekend. 这个人周末在哪里？", "待在家里",
     ["去了公园", "去了医院", "去旅行了"], "stayed at home。"),
])

R("rw_weekend", "读懂上周末日记", 6, "下", 2,
  "读过去时日记，找出做了什么。", "read_text", [
    ("c", "读一读：Last weekend I cleaned my room. I did not watch TV. 这个人看电视了吗？", "没有",
     ["看了", "只看了一会儿", "短文没写"], "did not watch TV。"),
    ("c", "读一读：Amy washed her clothes on Saturday. 哪一句和日记一致？", "Amy 星期六洗了衣服。",
     ["Amy 星期六看了电视。", "Amy 没有洗衣服。", "Amy 星期日洗了衣服。"], "washed her clothes on Saturday。"),
    ("c", "读一读：Did you stay at home? Yes, I did. 这个人待在家里了吗？", "待了",
     ["没有", "去了公园", "没回答"], "Yes, I did。"),
    ("c", "读一读：I watched a film on Sunday. 星期日做了什么？", "看了一部电影",
     ["打扫了房间", "洗了衣服", "去旅行了"], "watched a film。"),
])

G("gr_irr", "不规则动词过去式", 6, "下", 3,
  "能认出 go、see、eat 的过去式 went、saw、ate。", "past", [
    ("c", "go 的过去式是哪一个？", "went",
     ["goed", "goes", "going"], "go 的过去式是 went。"),
    ("c", "see 的过去式是哪一个？", "saw",
     ["seed", "seen", "seeed"], "see 的过去式是 saw。"),
    ("c", "哪一句是正确的？", "I went to the park.",
     ["I goed to the park.", "I go to the park yesterday.", "I going to the park yesterday."], "过去去了某地说 went。"),
    ("c", "eat 的过去式是哪一个？", "ate",
     ["eated", "eats", "eating"], "eat 的过去式是 ate。"),
])

F("fu_trip", "谈论去过哪里", 6, "下", 3,
  "用 Where did you go? 询问过去去了哪里。", "func_out", [
    ("c", "想问对方去了哪里，应说哪一句？", "Where did you go?",
     ["Where do you go?", "Where are you going?", "Where did you went?"], "问过去去向用 Where did you go?"),
    ("c", "I went to Xinjiang. 去了哪里？", "新疆",
     ["北京", "上海", "海南"], "Xinjiang 是新疆。"),
    ("c", "What did you do there? 这句是在问什么？", "你在那里做了什么",
     ["你要去哪里", "你正在做什么", "你喜欢那里吗"], "did you do there 问过去在那里做的事。"),
    ("c", "I saw grapes and ate good food. 做了什么？", "看见了葡萄，还吃了好吃的",
     ["只去了公园", "洗了衣服", "看了电影"], "saw grapes and ate good food。"),
])

R("rw_trip", "读懂旅行日记", 6, "下", 3,
  "读旅行日记，找出去了哪里、看见了什么。", "read_text", [
    ("c", "读一读：I went to Hainan. I saw the beach. 去了哪里？", "海南",
     ["新疆", "北京", "上海"], "went to Hainan。"),
    ("c", "读一读：We ate fresh food and took pictures. 哪一句和日记一致？", "我们吃了新鲜的食物，还拍了照片。",
     ["我们没有吃东西。", "我们去了学校。", "我们洗了衣服。"], "ate fresh food and took pictures。"),
    ("c", "读一读：Where did you go? I went to a forest. 去了什么地方？", "一片森林",
     ["一片海滩", "一家医院", "一家商店"], "a forest。"),
    ("c", "读一读：I saw a mule. It was interesting. 看见了什么？", "一头骡子",
     ["一匹马", "一只猫", "一条狗"], "a mule 是骡子。"),
])

V("vo_change", "过去和现在", 6, "下", 4,
  "认读 ago、different、active 和 Internet。",
  [("ago", "以前"), ("different", "不同的"), ("active", "活跃的"), ("Internet", "互联网")])

G("gr_was", "was 与 were", 6, "下", 4,
  "用 was 和 were 表示过去的状态，用 There was 表示过去有。", "past", [
    ("c", "There ____ no library in my school ten years ago. 横线上应填哪个词？", "was",
     ["is", "were", "are"], "单数 library 的过去式用 There was。"),
    ("c", "哪一句表示「以前我很矮」？", "I was short.",
     ["I were short.", "I was shorted.", "I am short yesterday."], "I 的过去式用 was。"),
    ("c", "They ____ young then. 横线上应填哪个词？", "were",
     ["was", "are", "is"], "They 的过去式用 were。"),
    ("c", "There were no computers in the old school. 这句的意思是？", "以前学校里没有电脑",
     ["以前学校里有电脑", "现在学校里没有电脑", "电脑在图书馆里"], "There were no 表示过去没有。"),
])

F("fu_now", "比较过去和现在", 6, "下", 4,
  "用 Before, I was ... Now, I am ... 比较过去和现在。", "func_out", [
    ("c", "想说以前很安静，现在很活跃，应说哪一句？", "Before, I was quiet. Now, I am active.",
     ["Before, I am quiet. Now, I was active.", "Before, I were quiet. Now, I am active.", "Now, I was quiet. Before, I am active."], "过去用 was，现在用 am。"),
    ("c", "There was no Internet ten years ago. 这句的意思是？", "十年前没有互联网",
     ["现在没有互联网", "十年前就有互联网", "互联网在图书馆里"], "was no Internet ten years ago。"),
    ("c", "How did you change? 这句是在问什么？", "你有什么变化",
     ["你现在多高", "你上周末做了什么", "你怎么去学校"], "change 是变化。"),
    ("c", "Now there is a gym. 现在有什么？", "一个体育馆",
     ["一个图书馆", "互联网", "一台电脑"], "a gym 是体育馆。"),
])

R("rw_now", "读懂今昔对比", 6, "下", 4,
  "读今昔短文，分清过去和现在。", "read_text", [
    ("c", "读一读：Before, there was no library. Now, there is a big library. 现在有图书馆吗？", "有",
     ["没有", "只有体育馆", "短文没写现在"], "Now, there is a big library。"),
    ("c", "读一读：I was short before. Now I am tall. 哪一句和短文一致？", "我以前矮，现在高。",
     ["我以前高，现在矮。", "我一直很矮。", "我以前就很高。"], "was short before，Now I am tall。"),
    ("c", "读一读：There were no computers in my old school. 以前的学校有电脑吗？", "没有",
     ["有", "只有一台", "短文说现在没有"], "were no computers。"),
    ("c", "读一读：People did not use the Internet then. Now we use it every day. 现在人们用互联网吗？", "用",
     ["不用", "只用电话", "短文没写现在"], "Now we use it every day。"),
])

X("vo_confuse", "易混词 there、its、too", "词汇", 6, "下", 4, "conceptual",
  "在句子里区分 there 与 their、its 与 it's、too 与 two。挂在本册是便于复习，册次待核。",
  "confuse", [
    ("c", "____ is a book on the desk. 横线上应填哪个词？", "There",
     ["Their", "They are", "Theirs"], "表示「有」用 There is。"),
    ("c", "The dog wagged ____ tail. 横线上应填哪个词？", "its",
     ["it's", "it is", "its is"], "「它的」用 its，没有撇号。"),
    ("c", "I have two pens. I want one, ____. 横线上应填哪个词？", "too",
     ["two", "to", "and"], "表示「也」用 too。"),
    ("c", "____ books are on the desk. 意思是「他们的书」。横线上应填哪个词？", "Their",
     ["There", "They are", "Theirs"], "「他们的」用 Their。"),
], conf="exact")

R("rw_letter", "读懂一封短信", 6, "下", 4,
  "读一封写明时间、地点和事件的短信，抓住这三项。", "read_write", [
    ("c", "读短信：Dear Amy, I went to the park last Sunday. I saw a lake. Love, Mike. Mike 上星期日去了哪里？", "公园",
     ["湖边的学校", "医院", "超市"], "went to the park。"),
    ("c", "读短信：I am going to visit you in June. 写信人打算几月去看望对方？", "六月",
     ["五月", "三月", "十月"], "in June。"),
    ("c", "哪一句适合写在信的开头？", "Dear Sarah,",
     ["Love, Sarah,", "Yours, Sarah,", "How tall are you, Sarah,"], "称呼常用 Dear 加上名字。"),
    ("c", "读短信：Before, I could not swim. Now I can. 哪一句和短信一致？", "我以前不会游泳，现在会了。",
     ["我以前会游泳。", "我现在不会游泳。", "我打算去游泳。"], "could not swim before，Now I can。"),
])
