# -*- coding: utf-8 -*-
"""五年级上、下。人教 PEP 三年级起点的常见单元顺序，册次待核。"""
from en_tx import V, S, P, G, F, R, X

# ---------- 五上 ----------

P("ph_blend", "开头辅音连缀 bl、cl、fl", 5, "上", 1,
  "能分辨 black、class、floor、blue 开头的辅音连缀。", "blend", [
    ("c", "哪个单词以 bl 开头？", "black",
     ["class", "floor", "green"], "black 以 bl 开头。"),
    ("c", "哪个单词以 cl 开头？", "class",
     ["black", "blue", "floor"], "class 以 cl 开头。"),
    ("c", "哪个单词以 fl 开头？", "floor",
     ["black", "class", "blue"], "floor 以 fl 开头。"),
    ("c", "blue 和哪个词的开头辅音连缀相同？", "black",
     ["class", "floor", "green"], "blue 和 black 都以 bl 开头。"),
])

V("vo_char", "性格和外貌", 5, "上", 1,
  "认读 old、young、kind 和 strict。",
  [("old", "年老的"), ("young", "年轻的"), ("kind", "和蔼的"), ("strict", "严格的")])

G("gr_like_person", "What is he like", 5, "上", 1,
  "用 What is he like? 询问人的性格，而不是询问他喜欢什么。", "present_basic", [
    ("c", "What is he like? 这句是在问什么？", "他是什么样的人",
     ["他喜欢什么", "他在哪里", "他是谁"], "What is he like 问性格或外貌，不是问喜好。"),
    ("c", "He is kind. 他怎么样？", "很和蔼",
     ["很严格", "很年轻", "很强壮"], "kind 是和蔼的。"),
    ("c", "哪一句表示「她很严格」？", "She is strict.",
     ["She is kind.", "She is funny.", "She is quiet."], "严格是 strict。"),
    ("c", "Miss White is young. 怀特老师怎么样？", "很年轻",
     ["很年老", "很和蔼", "很有趣"], "young 是年轻的。句子没有说她和蔼。"),
])

F("fu_teacher", "描述老师", 5, "上", 1,
  "用 He is 或 She is 描述老师的性格。", "func_life", [
    ("c", "想说音乐老师很和蔼，应说哪一句？", "The music teacher is kind.",
     ["The music teacher is strict.", "The music teacher is old.", "The music teacher is young."], "和蔼是 kind。"),
    ("c", "Who is your English teacher? 这句是在问什么？", "谁是你的英语老师",
     ["英语老师什么样", "你喜欢英语吗", "英语课在星期几"], "Who is 问是谁。"),
    ("c", "She is strict but kind. 这句的意思是？", "她严格但是和蔼",
     ["她只是很年轻", "她不严格", "她很有趣"], "strict but kind。"),
    ("c", "Mr Young is our art teacher. 杨老师教什么？", "美术",
     ["音乐", "英语", "数学"], "art teacher 是美术老师。"),
])

R("rw_teacher", "读懂老师介绍", 5, "上", 1,
  "读介绍老师的短文，找出性格。", "read_text", [
    ("c", "读一读：Mr Li is our maths teacher. He is tall and strict. 李老师怎么样？", "又高又严格",
     ["又矮又和蔼", "年轻而且有趣", "只说了他很老"], "tall and strict。"),
    ("c", "读一读：Miss White is young and kind. 哪一句和短文一致？", "怀特老师年轻而且和蔼。",
     ["怀特老师年老而且严格。", "怀特老师是男老师。", "怀特老师教数学。"], "young and kind，Miss 通常指女老师。"),
    ("c", "读一读：I like my Chinese teacher. She is funny. 语文老师怎么样？", "很有趣",
     ["很严格", "很年老", "很安静"], "funny 是有趣。"),
    ("c", "读一读：He is old. He is kind. 哪一句是短文里有的意思？", "他又年老又和蔼。",
     ["他很年轻。", "他很严格。", "他不和蔼。"], "old 和 kind 都写了。"),
])

V("vo_week", "星期", 5, "上", 2,
  "认读 Monday、Tuesday、Wednesday 和 Friday。",
  [("Monday", "星期一"), ("Tuesday", "星期二"), ("Wednesday", "星期三"), ("Friday", "星期五")])

G("gr_haveon", "have 与 on Mondays", 5, "上", 2,
  "用 I have 加课程，并用 on Mondays 表示在星期一。", "when_ord", [
    ("c", "I ____ Chinese on Mondays. 横线上应填哪个词？", "have",
     ["has", "am", "is"], "I 后面用 have。"),
    ("c", "哪一句表示「我星期一有语文课」？", "I have Chinese on Mondays.",
     ["I has Chinese on Mondays.", "I have Chinese in Mondays.", "I am Chinese on Mondays."], "在星期几用 on，I 后面用 have。"),
    ("c", "Do you often read books? 肯定回答应选哪一句？", "Yes, I do.",
     ["Yes, I does.", "Yes, I am.", "Yes, I have."], "Do you 的肯定回答是 Yes, I do。"),
    ("c", "What do you have on Fridays? 这句是在问什么？", "星期五有什么课",
     ["星期五是几月几日", "星期五天气如何", "星期五你在哪里"], "What do you have on Fridays 问星期五的课。"),
])

V("vo_weekend_act", "周末活动", 5, "上", 2,
  "认读 wash、watch、read 和 play。",
  [("wash", "洗"), ("watch", "看"), ("read", "读"), ("play", "玩")])

F("fu_often", "用 often 谈论日常", 5, "上", 2,
  "用 often 和 on the weekend 谈论经常做的事。", "func_life", [
    ("c", "想说自己星期六经常看书，应说哪一句？", "I often read books on Saturdays.",
     ["I often watch TV on Saturdays.", "I often wash clothes on Saturdays.", "I often play football on Saturdays."], "看书是 read books。"),
    ("c", "What do you do on the weekend? 这句是在问什么？", "你周末做什么",
     ["你星期一有什么课", "你喜欢什么课", "你的老师什么样"], "on the weekend 是在周末。"),
    ("c", "I often wash my clothes on Sundays. 星期日经常做什么？", "洗衣服",
     ["看书", "看电视", "踢足球"], "wash my clothes 是洗衣服。"),
    ("c", "Do you often play sports? 若经常，应回答哪一句？", "Yes, I do.",
     ["Yes, I am.", "Yes, I often do sports am.", "No, I does not."], "Do you 的肯定回答是 Yes, I do。"),
])

R("rw_week", "读懂一周课程", 5, "上", 2,
  "读课程句子，找出哪一天有什么课。", "read_text", [
    ("c", "读一读：I have Chinese, English and maths on Mondays. 星期一有英语课吗？", "有",
     ["没有", "只有语文", "短文没写星期一"], "句子里写了 English。"),
    ("c", "读一读：I often read books on the weekend. 周末经常做什么？", "看书",
     ["洗衣服", "看电视", "踢足球"], "read books。"),
    ("c", "读一读：We have PE on Fridays. 哪一天有体育课？", "星期五",
     ["星期一", "星期二", "星期三"], "on Fridays。"),
    ("c", "读一读：On Wednesdays I have art. 哪一句和短文一致？", "星期三有美术课。",
     ["星期三有音乐课。", "星期五有美术课。", "星期一有美术课。"], "Wednesdays 是星期三，art 是美术。"),
])

V("vo_meal", "餐食", 5, "上", 3,
  "认读 tea、sandwich、salad 和 hamburger。",
  [("tea", "茶"), ("sandwich", "三明治"), ("salad", "沙拉"), ("hamburger", "汉堡包")])

F("fu_would2", "What would you like to eat", 5, "上", 3,
  "用 What would you like to eat? 点餐。", "func_life", [
    ("c", "想问对方想吃什么，应说哪一句？", "What would you like to eat?",
     ["What do you have on Mondays?", "Where is the kitchen?", "How much is the salad?"], "点餐问 What would you like to eat?"),
    ("c", "I would like a sandwich and some tea. 想要什么？", "三明治和茶",
     ["沙拉和汉堡包", "只三明治", "只茶"], "a sandwich and some tea。"),
    ("c", "What would you like to drink? 若想喝茶，应说哪一句？", "I would like some tea.",
     ["I would like a hamburger.", "I would like a sandwich.", "I would like some salad."], "喝的是 tea。"),
    ("c", "She would like a salad. 她想要什么？", "一份沙拉",
     ["一个汉堡包", "一杯茶", "一个三明治"], "a salad。"),
])

R("rw_meal", "读懂点餐", 5, "上", 3,
  "读点餐短文，找出每个人想吃什么。", "read_short", [
    ("c", "读一读：Sarah would like a sandwich. Mike would like a hamburger. Sarah 想要什么？", "三明治",
     ["汉堡包", "沙拉", "茶"], "Sarah 对应 sandwich。"),
    ("c", "读一读：I would like some salad and some tea. 哪一句和文字一致？", "我想要沙拉和茶。",
     ["我想要汉堡包。", "我想要一个三明治。", "我只想要茶。"], "salad and tea 都写了。"),
    ("c", "读一读：What would you like to eat? I would like a hamburger. 想吃什么？", "汉堡包",
     ["三明治", "沙拉", "茶"], "a hamburger。"),
    ("c", "读一读：My favourite food is salad. It is healthy. 最喜欢的食物是什么？", "沙拉",
     ["茶", "汉堡包", "三明治"], "favourite food is salad。"),
])

V("vo_can", "能力动词", 5, "上", 4,
  "认读 sing、dance、draw 和 swim。",
  [("sing", "唱歌"), ("dance", "跳舞"), ("draw", "画画"), ("swim", "游泳")])

G("gr_can", "can 表示能力", 5, "上", 4,
  "用 can 加动词原形表示会做某事。", "can_there", [
    ("c", "I ____ swim. 横线上应填哪个词？", "can",
     ["am", "is", "are"], "表示会，用 can。"),
    ("c", "哪一句表示「她会画画」？", "She can draw.",
     ["She can draws.", "She cans draw.", "She is draw."], "can 后面用动词原形 draw。"),
    ("c", "Can you sing? 肯定回答应选哪一句？", "Yes, I can.",
     ["Yes, I do.", "Yes, I am.", "Yes, I sing."], "Can 的肯定回答是 Yes, I can。"),
    ("c", "He cannot dance. 这句的意思是？", "他不会跳舞",
     ["他会跳舞", "他正在跳舞", "他喜欢跳舞"], "cannot dance 是不会跳舞。"),
])

F("fu_can", "谈论会做的事", 5, "上", 4,
  "用 What can you do? 询问对方会做什么。", "func_life", [
    ("c", "想问对方会做什么，应说哪一句？", "What can you do?",
     ["What do you look like?", "What would you like?", "What do you have?"], "问能力用 What can you do?"),
    ("c", "I can sing and dance. 会做哪两件事？", "唱歌和跳舞",
     ["画画和游泳", "只唱歌", "只跳舞"], "sing and dance。"),
    ("c", "Can you swim? 若不会，应回答哪一句？", "No, I cannot.",
     ["No, I do not.", "Yes, I can.", "No, I am not."], "Can 的否定回答是 No, I cannot。"),
    ("c", "We can draw pictures for the party. 能为聚会做什么？", "画画",
     ["游泳", "唱歌", "做饭"], "draw pictures 是画画。"),
])

R("rw_can", "读懂能力短文", 5, "上", 4,
  "读短文，找出谁会做什么。", "read_text", [
    ("c", "读一读：John can swim. Amy can draw. 谁会游泳？", "John",
     ["Amy", "Sarah", "Mike"], "John can swim。"),
    ("c", "读一读：I can sing English songs. 哪一句和短文一致？", "我会唱英文歌。",
     ["我会跳舞。", "我不会唱歌。", "我会画画。"], "sing English songs。"),
    ("c", "读一读：What can you do? I can dance. 这个人会什么？", "跳舞",
     ["游泳", "画画", "做饭"], "I can dance。"),
    ("c", "读一读：Zhang Peng cannot cook, but he can swim. Zhang Peng 会什么？", "游泳",
     ["做饭", "唱歌", "画画"], "cannot cook，但是 can swim。"),
])

V("vo_room5", "房间里的东西", 5, "上", 5,
  "认读 bed、photo、plant 和 clock。",
  [("bed", "床"), ("photo", "照片"), ("plant", "植物"), ("clock", "时钟")])

G("gr_there", "There is 与 There are", 5, "上", 5,
  "用 There is 接单数，用 There are 接复数，表示某处有什么。", "can_there", [
    ("c", "房间里有一张床，应选哪一句？", "There is a bed.",
     ["There are a bed.", "There is beds.", "There be a bed."], "一张床是单数，用 There is。"),
    ("c", "There are two photos. 有多少张照片？", "2 张",
     ["1 张", "3 张", "12 张"], "two 是 2。"),
    ("c", "哪一句是正确的？", "There are some plants.",
     ["There is some plants.", "There are a plant.", "There be plants."], "plants 是复数，用 There are。"),
    ("c", "There is a clock. 这句的意思是？", "有一个时钟",
     ["时钟在哪里", "这是谁的时钟", "时钟多少钱"], "There is 表示有。"),
])

F("fu_there", "描述自己的房间", 5, "上", 5,
  "用 There is 和 There are 描述房间里有什么。", "func_life", [
    ("c", "想说房间里有一张大床，应说哪一句？", "There is a big bed.",
     ["There are a big bed.", "There is big beds.", "There be a big bed."], "一张床用 There is a big bed。"),
    ("c", "There are so many pictures. 这句的意思是？", "有很多画",
     ["有一张床", "有一个时钟", "房间很脏"], "so many pictures 是很多画。"),
    ("c", "My grandparents live in a small house. 祖父母住在哪里？", "一所小房子里",
     ["一所大学校里", "一个公园里", "一家商店里"], "a small house。"),
    ("c", "The computer is on the desk. 计算机在哪里？", "在书桌上",
     ["在床上", "在照片里", "在植物下"], "on the desk。"),
])

R("rw_room", "读懂房间短文", 5, "上", 5,
  "读房间短文，找出有什么。", "read_text", [
    ("c", "读一读：There is a big bed and a clock. There are two plants. 床有几张？", "1 张",
     ["2 张", "3 张", "没有床"], "There is a big bed 是一张。"),
    ("n", "读一读：There are three photos on the wall. 墙上有几张照片？", 3, "three photos。"),
    ("c", "读一读：There is a plant beside the clock. 植物在哪里？", "在时钟旁边",
     ["在床下", "在门外", "在厨房里"], "beside the clock 是在时钟旁边。"),
    ("c", "读一读：There are some pictures. There is no computer. 哪一句和短文一致？", "有一些画，没有计算机。",
     ["有计算机，没有画。", "只有一张床。", "什么都没有。"], "some pictures，并且 no computer。"),
])

V("vo_nature", "自然公园", 5, "上", 6,
  "认读 river、lake、mountain 和 forest。",
  [("river", "河"), ("lake", "湖"), ("mountain", "山"), ("forest", "森林")])

G("gr_isthere", "Is there 与 Are there", 5, "上", 6,
  "把 There is 和 There are 改成疑问句，询问某处有没有。", "can_there", [
    ("c", "问「河里有鱼吗」，应选哪一句？", "Are there any fish in the river?",
     ["Is there any fish are?", "There are fish?", "Do there fish?"], "fish 在这里看复数，用 Are there any。"),
    ("c", "Is there a lake? 肯定回答应选哪一句？", "Yes, there is.",
     ["Yes, there are.", "Yes, it is.", "Yes, there be."], "Is there 的肯定回答是 Yes, there is。"),
    ("c", "Are there any mountains? 否定回答应选哪一句？", "No, there are not.",
     ["No, there is not.", "No, they are not.", "No, there not."], "Are there 的否定回答是 No, there are not。"),
    ("n", "There is one forest and there are two rivers. 河有几条？", 2, "two rivers 是 2 条河。"),
])

F("fu_park", "谈论公园里有什么", 5, "上", 6,
  "用 Is there 和 Are there 谈论自然公园。", "func_life", [
    ("c", "想问公园里有没有湖，应说哪一句？", "Is there a lake in the park?",
     ["Are there a lake in the park?", "Is there any lakes?", "There is a lake?"], "一个湖用 Is there a lake。"),
    ("c", "There is a forest in the park. 公园里有什么？", "一片森林",
     ["一条河", "一座山", "一个湖"], "a forest。"),
    ("c", "Are there any tall buildings? 这句是在问什么？", "有高楼吗",
     ["有河吗", "有湖吗", "有森林吗"], "tall buildings 是高楼。"),
    ("c", "The nature park is quiet. 自然公园怎么样？", "很安静",
     ["很吵", "很小", "很贵"], "quiet 是安静。"),
])

R("rw_park", "读懂自然公园", 5, "上", 6,
  "读公园短文，按文字判断有什么。", "read_text", [
    ("c", "读一读：There is a lake in the park. There are some ducks on the lake. 湖上有什么？", "一些鸭子",
     ["一些山", "一些高楼", "一条河"], "ducks on the lake。"),
    ("c", "读一读：Is there a forest? Yes, there is. 有森林吗？", "有",
     ["没有", "只有河", "短文没回答"], "Yes, there is。"),
    ("c", "读一读：There are no tall buildings. There is a river. 哪一句和短文一致？", "没有高楼，有一条河。",
     ["有高楼，没有河。", "有一座山。", "什么都没有。"], "no tall buildings，there is a river。"),
    ("n", "读一读：There are two mountains behind the lake. 湖后面有几座山？", 2, "two mountains。"),
])

# ---------- 五下 ----------

V("vo_routine", "一天的活动", 5, "下", 1,
  "认读 get up、go to school、eat dinner 和 go to bed 这四件日常的事。",
  [("get up", "起床"), ("go to school", "上学"), ("eat dinner", "吃晚饭"), ("go to bed", "上床睡觉")])

G("gr_when", "When do you 询问时间", 5, "下", 1,
  "用 When do you 询问做某事的时间，并用 at 6 o'clock 回答。", "when_ord", [
    ("c", "想问「你什么时候起床」，应选哪一句？", "When do you get up?",
     ["When does you get up?", "When do you gets up?", "What do you get up?"], "you 前面用 When do you。"),
    ("c", "I get up at 6 o'clock. 几点起床？", "6 点",
     ["5 点", "7 点", "8 点"], "at 6 o'clock 是 6 点。"),
    ("c", "I go to bed at 9 o'clock. 几点睡觉？", "9 点",
     ["6 点", "7 点", "8 点"], "at 9 o'clock 是 9 点。"),
    ("c", "When do you eat breakfast? 这句是在问什么？", "你什么时候吃早饭",
     ["你喜欢早饭吗", "早饭在哪里", "早饭多少钱"], "When 问的是什么时候。"),
])

F("fu_day", "谈论作息", 5, "下", 1,
  "用 I ... at ... 说出自己的作息。", "func_life", [
    ("c", "想说自己 7 点去上学，应说哪一句？", "I go to school at 7 o'clock.",
     ["I get up at 7 o'clock.", "I eat dinner at 7 o'clock.", "I go to bed at 7 o'clock."], "去上学是 go to school。"),
    ("c", "When do you eat dinner? 若是 6 点，应回答哪一句？", "I eat dinner at 6 o'clock.",
     ["I eat dinner at 9 o'clock.", "I go to bed at 6 o'clock.", "I get up at 6 o'clock."], "问的是 eat dinner，时间是 6 点。"),
    ("c", "I often clean my room on the weekend. 周末经常做什么？", "打扫房间",
     ["起床", "上学", "吃晚饭"], "clean my room。"),
    ("c", "What do you do on the weekend? 这句是在问什么？", "你周末做什么",
     ["你几点起床", "你星期几有英语课", "你的老师什么样"], "on the weekend。"),
])

R("rw_day", "读懂一天的作息", 5, "下", 1,
  "读作息短文，找出几点做什么。", "read_text", [
    ("c", "读一读：I get up at 6 o'clock. I go to school at 7 o'clock. 几点去上学？", "7 点",
     ["6 点", "8 点", "9 点"], "go to school at 7。"),
    ("n", "读一读：I eat dinner at 6 o'clock and go to bed at 9 o'clock. 几点睡觉？", 9, "go to bed at 9。"),
    ("c", "读一读：On the weekend I often wash my clothes. 哪一句和短文一致？", "周末我经常洗衣服。",
     ["周末我经常上学。", "我 6 点洗衣服。", "我从不洗衣服。"], "often wash my clothes on the weekend。"),
    ("c", "读一读：Sarah says, \"I get up at 6:30.\" Sarah 几点起床？", "6:30",
     ["6:00", "7:00", "9:00"], "引号里是 6:30。"),
])

V("vo_season", "季节", 5, "下", 2,
  "认读 spring、summer、autumn 和 winter。秋天用 autumn。",
  [("spring", "春天"), ("summer", "夏天"), ("autumn", "秋天"), ("winter", "冬天")])

F("fu_season", "谈论最喜欢的季节", 5, "下", 2,
  "用 Which season do you like best? 谈论季节。", "func_life", [
    ("c", "想问最喜欢哪个季节，应说哪一句？", "Which season do you like best?",
     ["What time is it?", "What is the weather like?", "When do you get up?"], "问最喜欢的季节用 Which season do you like best?"),
    ("c", "I like summer best. I can swim. 最喜欢哪个季节？", "夏天",
     ["春天", "秋天", "冬天"], "summer。"),
    ("c", "It is golden in autumn. 这句在说哪个季节？", "秋天",
     ["春天", "夏天", "冬天"], "autumn 是秋天。"),
    ("c", "Winter is white. I can make a snowman. 冬天可以做什么？", "堆雪人",
     ["游泳", "放风筝", "吃冰淇淋"], "make a snowman。"),
])

R("rw_season", "读懂季节短文", 5, "下", 2,
  "读季节短文，找出喜欢的季节和原因。", "read_text", [
    ("c", "读一读：I like spring best. There are many flowers. 最喜欢哪个季节？", "春天",
     ["夏天", "秋天", "冬天"], "spring。"),
    ("c", "读一读：Summer is hot. I eat ice cream. 夏天怎么样？", "很热",
     ["很冷", "有雪", "有很多花"], "hot。"),
    ("c", "读一读：My favourite season is autumn. The colours are beautiful. 哪一句和短文一致？", "我最喜欢秋天。",
     ["我最喜欢冬天。", "秋天很冷。", "没有写颜色。"], "favourite season is autumn。"),
    ("c", "读一读：In winter I can play in the snow. 冬天可以在哪里玩？", "在雪地里",
     ["在海里", "在花丛里", "在教室里"], "in the snow。"),
])

X("vo_month", "月份", "词汇", 5, "下", 3, "conceptual",
  "认读 March、May、October 和 December，并知道一年有 12 个月。", "vocab56", [
    ("c", "哪个单词的意思是「三月」？", "March",
     ["May", "October", "December"], "三月是 March。"),
    ("c", "May 的中文意思是哪一个？", "五月",
     ["三月", "十月", "十二月"], "May 是五月。"),
    ("c", "选择表示「十月」的单词。", "October",
     ["March", "May", "December"], "十月是 October。"),
    ("n", "一年有几个月？", 12, "一年有 12 个月，从 January 到 December。"),
], conf="inferred")

G("gr_month", "in 加月份", 5, "下", 3,
  "用 in March 表示在某个月，而不是 on March。", "when_ord", [
    ("c", "in March 表示什么？", "在三月",
     ["在三月一日", "在星期一", "在三点"], "in 加月份表示在整个月。"),
    ("c", "哪一句表示「儿童节在六月」？", "Children's Day is in June.",
     ["Children's Day is on June.", "Children's Day is at June.", "Children's Day is June in."], "月份前面用 in。"),
    ("n", "一年有几个月？", 12, "一年有 12 个月。"),
    ("c", "May 是几月？", "5 月",
     ["3 月", "4 月", "6 月"], "May 是五月。"),
])

F("fu_holiday", "谈论节日在几月", 5, "下", 3,
  "用 is in 说出节日所在的月份。", "func_life", [
    ("c", "想说教师节在九月，应说哪一句？", "Teachers' Day is in September.",
     ["Teachers' Day is in October.", "Teachers' Day is in June.", "Teachers' Day is in May."], "九月是 September。"),
    ("c", "When is Tree Planting Day? 若在三月，应回答哪一句？", "It is in March.",
     ["It is in May.", "It is in October.", "It is in December."], "三月是 March。"),
    ("c", "We have a school trip in May. 学校旅行在几月？", "五月",
     ["三月", "十月", "十二月"], "in May。"),
    ("c", "The party is in December. 聚会在几月？", "十二月",
     ["三月", "五月", "十月"], "December 是十二月。"),
])

R("rw_cal", "读懂校历", 5, "下", 3,
  "读校历短文，找出活动在哪个月。", "read_text", [
    ("c", "读一读：The school trip is in May. The party is in December. 旅行在几月？", "五月",
     ["十二月", "三月", "十月"], "trip is in May。"),
    ("c", "读一读：Tree Planting Day is in March. 哪一句和短文一致？", "植树节在三月。",
     ["植树节在五月。", "聚会在三月。", "旅行在三月。"], "in March。"),
    ("c", "读一读：We have a sports meet in October. 运动会在几月？", "十月",
     ["五月", "三月", "十二月"], "October。"),
    ("n", "读一读：There are twelve months in a year. 一年有几个月？", 12, "twelve months。"),
])

G("gr_ord", "序数词", 5, "下", 4,
  "能认出 first、second、third 等序数词，并知道它们和基数词不同。", "when_ord", [
    ("c", "1st 怎么读？", "first",
     ["one", "second", "third"], "1st 读作 first。"),
    ("c", "哪一个是序数词？", "third",
     ["three", "thirteen", "thirty"], "third 是序数词，three 是基数词。"),
    ("n", "April is the fourth month. April 是第几个月？", 4, "fourth 表示第 4。"),
    ("c", "2nd 的英文是哪一个？", "second",
     ["two", "twelve", "twenty"], "2nd 是 second。"),
])

F("fu_date", "说出日期", 5, "下", 4,
  "用 on April 1st 这样的说法说出日期。", "func_life", [
    ("c", "想说艺术节在 4 月 1 日，应说哪一句？", "The art show is on April 1st.",
     ["The art show is in April 1st.", "The art show is at April 1st.", "The art show is April on 1st."], "具体日期用 on。"),
    ("c", "When is the reading festival? 这句是在问什么？", "读书节在什么时候",
     ["读书节在哪里", "你喜欢读书吗", "读书节多少钱"], "When is 问时间。"),
    ("c", "It is on May 4th. 这是几月几日？", "5 月 4 日",
     ["4 月 5 日", "5 月 1 日", "4 月 4 日"], "May 是五月，4th 是 4 日。"),
    ("c", "My birthday is on March 21st. 生日是哪一天？", "3 月 21 日",
     ["3 月 12 日", "5 月 21 日", "4 月 1 日"], "March 21st。"),
])

R("rw_date", "读懂日期通知", 5, "下", 4,
  "读通知，找出活动的日期。", "read_text", [
    ("c", "读一读：The art show is on April 1st. 艺术节是哪一天？", "4 月 1 日",
     ["4 月 5 日", "5 月 1 日", "3 月 21 日"], "April 1st。"),
    ("c", "读一读：The reading festival is on May 5th. 哪一句和通知一致？", "读书节在 5 月 5 日。",
     ["读书节在 4 月 1 日。", "艺术节在 5 月 5 日。", "读书节在 5 月。"], "May 5th，而且是 reading festival。"),
    ("n", "读一读：School starts on September 1st. 开学是几月的第几天？只填日。", 1, "September 1st 的日是 1。"),
    ("c", "读一读：The sports meet is on October 12th. 运动会在几月？", "十月",
     ["四月", "五月", "九月"], "October 是十月。"),
])

G("gr_poss", "名词性物主代词", 5, "下", 5,
  "用 mine、yours、his、hers 说明物品是谁的，不再重复名词。", "poss_pron", [
    ("c", "这支钢笔是我的，应选哪一句？", "The pen is mine.",
     ["The pen is my.", "The pen is me.", "The pen is I."], "名词性物主代词用 mine，不说 is my。"),
    ("c", "Whose book is this? It is hers. 书是谁的？", "她的",
     ["他的", "我的", "你的"], "hers 是她的。"),
    ("c", "The bag is yours. 包是谁的？", "你的",
     ["我的", "他的", "他们的"], "yours 是你的。"),
    ("c", "哪一句是正确的？", "The dog is ours.",
     ["The dog is our.", "The dog is we.", "The dog is us."], "我们的用 ours。"),
])

G("gr_ing", "现在进行时", 5, "下", 5,
  "用 am、is、are 加动词的 -ing 形式说明正在做的事。", "continuous", [
    ("c", "He ____ reading. 横线上应填哪个词？", "is",
     ["am", "are", "be"], "He 和 is 搭配，后面接 reading。"),
    ("c", "哪一句表示「他们正在吃晚饭」？", "They are eating dinner.",
     ["They are eat dinner.", "They eating dinner.", "They is eating dinner."], "They 用 are，动词用 eating。"),
    ("c", "I am singing. 这句的意思是？", "我正在唱歌",
     ["我喜欢唱歌", "我会唱歌", "我昨天唱歌"], "am singing 是正在唱歌。"),
    ("c", "What is she doing? 这句是在问什么？", "她正在做什么",
     ["她是谁", "她会做什么", "她喜欢做什么"], "What is she doing 问正在做的事。"),
])

F("fu_whose", "Whose 与正在做的事", 5, "下", 5,
  "用 Whose dog is it? 和 It is mine. 说明正在提到的东西是谁的。", "func_life", [
    ("c", "问「这是谁的狗」，应说哪一句？", "Whose dog is it?",
     ["Who dog is it?", "Where dog is it?", "What dog is it?"], "问属于谁用 Whose。"),
    ("c", "Whose book is this? 若是我的，应回答哪一句？", "It is mine.",
     ["It is my.", "It is me.", "It is I."], "我的用 mine。"),
    ("c", "The dog is his. 狗是谁的？", "他的",
     ["她的", "我的", "你的"], "his 是他的。"),
    ("c", "They are playing in the park. The picture is ours. 照片是谁的？", "我们的",
     ["他们的", "你的", "她的"], "ours 是我们的。"),
])

R("rw_doing", "读懂正在做的事", 5, "下", 5,
  "读现在进行时的短文，找出谁正在做什么。", "read_text", [
    ("c", "读一读：John is eating lunch. Amy is reading a book. John 正在做什么？", "吃午饭",
     ["看书", "睡觉", "画画"], "John is eating lunch。"),
    ("c", "读一读：Look! The dog is sleeping. 狗正在做什么？", "睡觉",
     ["吃东西", "跑", "玩"], "is sleeping。"),
    ("c", "读一读：Whose picture is it? It is mine. I am drawing. 谁在画画？", "我",
     ["John", "Amy", "狗"], "I am drawing，而且 picture is mine。"),
    ("c", "读一读：They are playing football. 哪一句和短文一致？", "他们正在踢足球。",
     ["他们会踢足球。", "他们昨天踢了足球。", "他们不喜欢足球。"], "are playing 是正在踢。"),
])

V("vo_rule", "规则用词", 5, "下", 6,
  "认读 quietly、talk、keep 和 desk。",
  [("quietly", "安静地"), ("talk", "说话"), ("keep", "保持"), ("desk", "书桌")])

G("gr_imp", "祈使句", 5, "下", 6,
  "用动词原形开头的祈使句提出要求，并用 Do not 表示禁止。", "modal_imp", [
    ("c", "哪一句是祈使句？", "Talk quietly.",
     ["You talk quietly?", "She talks quietly.", "Talking quietly is."], "祈使句用动词原形开头。"),
    ("c", "Keep to the right. 这句是在说什么？", "靠右走",
     ["靠左走", "保持安静", "把桌子擦干净"], "Keep to the right 是靠右。"),
    ("c", "Do not talk. 这句的意思是？", "不要说话",
     ["请说话", "正在说话", "喜欢说话"], "Do not talk 是不要说话。"),
    ("c", "哪一句表示「请安静」？", "Be quiet.",
     ["Is quiet.", "Are quiet.", "Quiet is be."], "祈使句说 Be quiet。"),
])

F("fu_rule", "说规则", 5, "下", 6,
  "用祈使句说出图书馆或教室里的规则。", "func_life", [
    ("c", "图书馆里要小声说话，应说哪一句？", "Talk quietly.",
     ["Talk loudly.", "Keep to the left.", "Do not read."], "小声是 quietly。"),
    ("c", "Keep your desk clean. 这句是在说什么？", "保持书桌干净",
     ["靠右走", "不要说话", "可以跑"], "desk clean。"),
    ("c", "Do not eat in the library. 图书馆里不可以做什么？", "吃东西",
     ["看书", "安静地说话", "靠右走"], "Do not eat。"),
    ("c", "Work quietly. 这句是在要求什么？", "安静地做事",
     ["大声说话", "出去玩", "吃午饭"], "quietly 是安静地。"),
])

R("rw_rule", "读懂规则", 5, "下", 6,
  "读规则短文，找出可以做和不可以做的事。", "read_text", [
    ("c", "读一读：Talk quietly. Do not eat. Keep your desk clean. 不可以做什么？", "吃东西",
     ["安静说话", "保持书桌干净", "看书"], "Do not eat。"),
    ("c", "读一读：Keep to the right. 哪一句和文字一致？", "请靠右。",
     ["请靠左。", "请吃东西。", "请大声说话。"], "Keep to the right。"),
    ("c", "读一读：We are reading in the library. Please work quietly. 人们正在哪里？", "图书馆",
     ["操场", "食堂", "公园"], "in the library。"),
    ("c", "读一读：Do not run in the classroom. Walk quietly. 教室里应该怎样走？", "安静地走",
     ["跑", "吃东西", "大声说话"], "Walk quietly，并且 Do not run。"),
])
