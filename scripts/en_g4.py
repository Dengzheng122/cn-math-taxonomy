# -*- coding: utf-8 -*-
"""四年级上、下。人教 PEP 三年级起点的常见单元顺序，册次待核。"""
from en_tx import V, S, P, G, F, R

# ---------- 四上 ----------

S("ph_ae", "a-e 的读音", 4, "上", 1,
  "能认出 a-e 的读音，例如 cake、name、face、make。",
  "a-e 的读音", ["cake", "name", "face", "make"], ["cat", "bag", "map", "hat"], "magic_e")

V("vo_class", "教室物品", 4, "上", 1,
  "认读 classroom、window、door 和 blackboard。",
  [("classroom", "教室"), ("window", "窗户"), ("door", "门"), ("blackboard", "黑板")])

G("gr_lets", "Let's 建议句", 4, "上", 1,
  "能读懂并用 Let's 提出一起做某事的建议。", "lets", [
    ("c", "建议一起打开书，应选哪一句？", "Let's open the book.",
     ["Let open the book.", "Let's opens the book.", "Let is open the book."], "建议一起做用 Let's 加动词原形。"),
    ("c", "Let's clean the classroom. 这句是在做什么？", "建议一起打扫教室",
     ["询问教室在哪里", "说明教室是谁的", "询问有多少教室"], "Let's 是在建议一起做。"),
    ("c", "哪一句是正确的建议句？", "Let's go.",
     ["Let's goes.", "Let we go.", "Let's going."], "Let's 后面用动词原形 go。"),
    ("c", "Let's be friends. 这句的意思是？", "我们做朋友吧",
     ["我们不是朋友", "你是我的朋友吗", "他是朋友"], "Let's be friends 是建议做朋友。"),
])

F("fu_class", "教室里的建议", 4, "上", 1,
  "在教室里用 Let's 提出开灯、关门、擦黑板等建议。", "func_place", [
    ("c", "建议一起擦黑板，应说哪一句？", "Let's clean the blackboard.",
     ["Let's open the door.", "Let's close the window.", "Let's sit down."], "黑板是 blackboard。"),
    ("c", "Let's open the door. 建议做什么？", "开门",
     ["关门", "开窗", "擦黑板"], "open the door 是开门。"),
    ("c", "Close the window, please. 这句是在说什么？", "请关上窗户",
     ["请打开窗户", "请打开门", "请坐下"], "Close the window 是关窗。"),
    ("c", "We have a new classroom. 这句的意思是？", "我们有一间新教室",
     ["我们有一块新黑板", "请打开门", "我们做朋友吧"], "classroom 是教室。"),
])

R("rw_class", "读懂教室短文", 4, "上", 1,
  "读教室里的短通知，找出要做的事。", "read_short", [
    ("c", "读一读：Let's clean the classroom. Open the door, please. 建议先提到的是什么？", "打扫教室",
     ["关门", "开窗", "坐下"], "第一句是 clean the classroom。"),
    ("c", "读一读：The window is blue. The door is yellow. 门是什么颜色？", "黄色",
     ["蓝色", "绿色", "红色"], "door is yellow。"),
    ("c", "读一读：This is our classroom. We have a big blackboard. 哪一句和短文一致？", "教室里有一块大黑板。",
     ["教室里没有黑板。", "窗户是黑色的。", "门是蓝色的。"], "短文写 We have a big blackboard。"),
    ("c", "读一读：Let's close the window. 哪一句和文字意思相同？", "我们把窗户关上吧。",
     ["我们把窗户打开吧。", "我们把门打开吧。", "我们擦黑板吧。"], "close the window 是关窗。"),
])

S("ph_ie", "i-e 的读音", 4, "上", 2,
  "能认出 i-e 的读音，例如 like、kite、five、bike。",
  "i-e 的读音", ["like", "kite", "five", "bike"], ["big", "pig", "sit", "fish"], "magic_e")

V("vo_bag", "书包里的文具", 4, "上", 2,
  "认读 schoolbag、pencil、ruler 和 eraser。",
  [("schoolbag", "书包"), ("pencil", "铅笔"), ("ruler", "尺子"), ("eraser", "橡皮")])

F("fu_bag", "谈论书包里有什么", 4, "上", 2,
  "用 I have 和 What is in your schoolbag? 谈论文具。", "func_place", [
    ("c", "想问书包里有什么，应说哪一句？", "What is in your schoolbag?",
     ["Where is your schoolbag?", "What colour is your schoolbag?", "Who is your schoolbag?"], "问里面有什么用 What is in。"),
    ("c", "I have a pencil and a ruler. 书包里有什么？", "铅笔和尺子",
     ["铅笔和橡皮", "尺子和橡皮", "只铅笔"], "pencil 是铅笔，ruler 是尺子。"),
    ("c", "Put your eraser in the schoolbag. 要把什么放进书包？", "橡皮",
     ["铅笔", "尺子", "书"], "eraser 是橡皮。"),
    ("c", "哪一句表示「我有一把尺子」？", "I have a ruler.",
     ["I have an eraser.", "I have a pencil.", "I have a schoolbag."], "尺子是 ruler。"),
])

R("rw_bag", "读懂书包里的物品", 4, "上", 2,
  "读书包物品的句子，找出文具和颜色。", "read_short", [
    ("c", "读一读：I have a new schoolbag. It is black. 书包是什么颜色？", "黑色",
     ["蓝色", "黄色", "绿色"], "文字写 It is black。"),
    ("c", "读一读：What is in your schoolbag? A pencil and an eraser. 里面有什么？", "铅笔和橡皮",
     ["尺子和书", "只铅笔", "只橡皮"], "a pencil and an eraser。"),
    ("n", "读一读：I have three pencils and one ruler. 铅笔有几支？", 3, "three pencils 是 3 支。"),
    ("c", "读一读：The ruler is blue. The eraser is white. 哪一句和文字一致？", "尺子是蓝色的。",
     ["尺子是白色的。", "橡皮是蓝色的。", "书包是蓝色的。"], "ruler is blue。"),
])

S("ph_oe", "o-e 的读音", 4, "上", 3,
  "能认出 o-e 的读音，例如 nose、note、home、rose。",
  "o-e 的读音", ["nose", "note", "home", "rose"], ["dog", "box", "hot", "not"], "magic_e")

V("vo_friend", "描述朋友", 4, "上", 3,
  "认读 friend、strong、quiet 和 friendly。",
  [("friend", "朋友"), ("strong", "强壮的"), ("quiet", "安静的"), ("friendly", "友好的")])

G("gr_has", "He has 与 I have", 4, "上", 3,
  "用 I have 说自己有什么，用 He has 或 She has 说他人有什么。", "present_basic", [
    ("c", "He ____ a new pen. 横线上应填哪个词？", "has",
     ["have", "is", "are"], "He 后面用 has。"),
    ("c", "哪一句是正确的？", "She has a bag.",
     ["She have a bag.", "She has are a bag.", "She having a bag."], "She 后面用 has。"),
    ("c", "I ____ a ruler. 横线上应填哪个词？", "have",
     ["has", "am", "is"], "I 后面用 have。"),
    ("c", "He has glasses. 这句的意思是？", "他有眼镜",
     ["他没有眼镜", "他是眼镜", "眼镜有他"], "has glasses 是有眼镜。"),
])

F("fu_friend", "介绍朋友", 4, "上", 3,
  "用 He is 和 He has 介绍朋友长什么样。", "func_daily", [
    ("c", "介绍一个强壮的朋友，应说哪一句？", "He is strong.",
     ["He is quiet.", "He is friendly.", "He is tall."], "强壮是 strong。"),
    ("c", "She is friendly. 她怎么样？", "很友好",
     ["很安静", "很强壮", "很矮"], "friendly 是友好的。"),
    ("c", "What is his name? 这句是在问什么？", "他叫什么名字",
     ["他在哪里", "他有什么", "他来自哪里"], "What is his name 问名字。"),
    ("c", "My friend is quiet. 哪一句和这句话意思相同？", "我的朋友很安静。",
     ["我的朋友很强壮。", "我的朋友很友好。", "我的朋友很高。"], "quiet 是安静的。"),
])

R("rw_friend", "读懂朋友介绍", 4, "上", 3,
  "读介绍朋友的短文，找出名字和特点。", "read_short", [
    ("c", "读一读：I have a friend. He is strong. His name is John. 朋友叫什么？", "John",
     ["Mike", "Amy", "Sarah"], "His name is John。"),
    ("c", "读一读：She is quiet and friendly. 哪一句和短文一致？", "她安静而且友好。",
     ["她强壮而且高。", "她不友好。", "他很安静。"], "quiet and friendly，主语是 She。"),
    ("c", "读一读：He has a blue bag. 他有什么？", "一个蓝色的包",
     ["一个红色的包", "一副眼镜", "一把尺子"], "a blue bag。"),
    ("c", "读一读：My friend is Amy. She has long hair. 谁留着长头发？", "Amy",
     ["John", "Mike", "Chen Jie"], "Amy 是朋友，She has long hair。"),
])

S("ph_ue", "u-e 的读音", 4, "上", 4,
  "能认出 u-e 的读音，例如 use、cute、tube、huge。",
  "u-e 的读音", ["use", "cute", "tube", "huge"], ["fun", "run", "cup", "sun"], "magic_e")

V("vo_home", "家里的房间", 4, "上", 4,
  "认读 bedroom、kitchen、bathroom 和 study。",
  [("bedroom", "卧室"), ("kitchen", "厨房"), ("bathroom", "卫生间"), ("study", "书房")])

G("gr_isin", "is 和 are 说明人在哪里", 4, "上", 4,
  "用 is 或 are 加上 in 说明一个人或几个人在哪个房间。", "be", [
    ("c", "She ____ in the kitchen. 横线上应填哪个词？", "is",
     ["am", "are", "be"], "She 和 is 搭配。"),
    ("c", "哪一句表示「他在书房」？", "He is in the study.",
     ["He are in the study.", "He am in the study.", "He be in the study."], "He 后面用 is。"),
    ("c", "Where is she? 这句是在问什么？", "她在哪里",
     ["她是谁", "她喜欢什么", "她有什么"], "Where is she 问地点。"),
    ("c", "They ____ in the bedroom. 横线上应填哪个词？", "are",
     ["is", "am", "be"], "They 和 are 搭配。"),
])

F("fu_home", "询问家人在哪个房间", 4, "上", 4,
  "用 Where is 询问家人在家的哪个房间。", "func_place", [
    ("c", "想问妈妈在哪里，应说哪一句？", "Where is my mother?",
     ["Who is my mother?", "What is my mother?", "How is my mother?"], "问位置用 Where is。"),
    ("c", "She is in the kitchen. 她在哪里？", "厨房",
     ["卧室", "卫生间", "书房"], "kitchen 是厨房。"),
    ("c", "Go to the bathroom. 这句是让人去哪里？", "卫生间",
     ["书房", "厨房", "卧室"], "bathroom 是卫生间。"),
    ("c", "Is she in the study? 这句是在问什么？", "她在书房吗",
     ["她在厨房吗", "书房是谁的", "书房有多大"], "study 是书房。"),
])

R("rw_home", "读懂家里的位置", 4, "上", 4,
  "读短文，找出人在哪个房间。", "read_short", [
    ("c", "读一读：My father is in the study. My mother is in the kitchen. 爸爸在哪里？", "书房",
     ["厨房", "卧室", "卫生间"], "father is in the study。"),
    ("c", "读一读：The cat is in the bedroom. 哪一句和文字一致？", "猫在卧室。",
     ["猫在厨房。", "猫在书房。", "妈妈在卧室。"], "bedroom 是卧室。"),
    ("c", "读一读：Where is Amy? She is in the bathroom. Amy 在哪里？", "卫生间",
     ["书房", "厨房", "卧室"], "bathroom 是卫生间。"),
    ("c", "读一读：They are in the living room. 这句说他们在客厅。哪一个词是「他们」？", "They",
     ["She", "He", "It"], "They 表示他们。"),
])

S("ph_longe", "长元音 e", 4, "上", 5,
  "能认出 he、she、me、we 里的长元音 e。",
  "长元音 e", ["he", "she", "me", "we"], ["ten", "pen", "red", "leg"], "magic_e")

V("vo_dinner", "晚餐食物", 4, "上", 5,
  "认读 beef、chicken、noodles 和 soup。",
  [("beef", "牛肉"), ("chicken", "鸡肉"), ("noodles", "面条"), ("soup", "汤")])

F("fu_would", "Would you like 用餐", 4, "上", 5,
  "用餐时用 Would you like some 邀请，并用 Yes, please. 回答。", "func_place", [
    ("c", "想问对方要不要一些汤，应说哪一句？", "Would you like some soup?",
     ["Do you like some soup?", "Where is the soup?", "I like soup."], "邀请对方用 Would you like some。"),
    ("c", "Would you like some beef? 若想要，应回答哪一句？", "Yes, please.",
     ["No, I do not.", "Yes, I do.", "Here you are."], "接受邀请常说 Yes, please。"),
    ("c", "What would you like? 若想吃面条，应说哪一句？", "I would like some noodles.",
     ["I would like some soup.", "I would like some beef.", "I would like some chicken."], "面条是 noodles。"),
    ("c", "Help yourself. 这句是在说什么？", "请随便吃",
     ["请坐下", "请开门", "请看黑板"], "Help yourself 是请对方随便吃。"),
])

R("rw_dinner", "读懂晚餐对话", 4, "上", 5,
  "读晚餐对话，找出想吃的食物。", "read_short", [
    ("c", "读一读：Would you like some soup? Yes, please. 这个人想要汤吗？", "想要",
     ["不想要", "没说", "想要米饭"], "回答是 Yes, please。"),
    ("c", "读一读：I would like some noodles and beef. 想吃什么？", "面条和牛肉",
     ["汤和鸡肉", "只面条", "只牛肉"], "noodles and beef。"),
    ("c", "读一读：Dinner is ready. Have some chicken. 哪一句和文字一致？", "请吃些鸡肉。",
     ["请喝些汤。", "晚饭还没好。", "请吃些面条。"], "Have some chicken。"),
    ("c", "读一读：Sarah says, \"I would like some soup.\" Sarah 想要什么？", "汤",
     ["牛肉", "鸡肉", "面条"], "引号里是 soup。"),
])

V("vo_job", "职业", 4, "上", 6,
  "认读 doctor、nurse、driver 和 farmer。",
  [("doctor", "医生"), ("nurse", "护士"), ("driver", "司机"), ("farmer", "农民")])

G("gr_job", "询问职业与 his、her", 4, "上", 6,
  "用 What is his job? 询问职业，并用 his、her 说明是谁的家人。", "pronoun", [
    ("c", "问「他的职业是什么」，应选哪一句？", "What is his job?",
     ["What is he job?", "Where is his job?", "Who is his job?"], "询问职业说 What is his job?"),
    ("c", "He is a doctor. 他的职业是？", "医生",
     ["护士", "司机", "农民"], "doctor 是医生。"),
    ("c", "My father is a driver. 爸爸的职业是？", "司机",
     ["医生", "护士", "农民"], "driver 是司机。"),
    ("c", "哪一句表示「她的妈妈是护士」？", "Her mother is a nurse.",
     ["His mother is a nurse.", "Her mother is a doctor.", "His father is a nurse."], "她的用 Her，护士是 nurse。"),
])

F("fu_job", "介绍家人的职业", 4, "上", 6,
  "用 My father is a 介绍家人的职业。", "func_daily", [
    ("c", "想说叔叔是农民，应说哪一句？", "My uncle is a farmer.",
     ["My uncle is a doctor.", "My uncle is a nurse.", "My uncle is a driver."], "农民是 farmer。"),
    ("c", "Is this your baby brother? 这句是在问什么？", "这是你的小弟弟吗",
     ["这是你的爸爸吗", "这是你的叔叔吗", "这是你的阿姨吗"], "baby brother 是小弟弟。"),
    ("c", "She is a nurse. 哪一句和这句话意思相同？", "她是护士。",
     ["她是医生。", "他是护士。", "她是司机。"], "She 是她，nurse 是护士。"),
    ("c", "What is your aunt's job? 这句是在问什么？", "你姑姑或阿姨做什么工作",
     ["你爸爸做什么工作", "你妈妈在哪里", "你几岁了"], "aunt 是姑姑或阿姨，job 是职业。"),
])

R("rw_job", "读懂家人职业", 4, "上", 6,
  "读介绍家人职业的短文，找出谁做什么工作。", "read_short", [
    ("c", "读一读：This is my father. He is a doctor. 爸爸的职业是？", "医生",
     ["护士", "司机", "农民"], "He is a doctor。"),
    ("c", "读一读：My mother is a nurse. My uncle is a driver. 谁是司机？", "叔叔",
     ["妈妈", "爸爸", "阿姨"], "uncle is a driver。"),
    ("c", "读一读：She is a farmer. 哪一句和文字一致？", "她是农民。",
     ["他是农民。", "她是医生。", "她是护士。"], "She 是她，farmer 是农民。"),
    ("c", "读一读：His father is a doctor. Her mother is a teacher. 谁的爸爸是医生？", "他的爸爸",
     ["她的爸爸", "他的妈妈", "她的妈妈"], "His father 是他的爸爸。"),
])

# ---------- 四下 ----------

V("vo_school", "学校场所", 4, "下", 1,
  "认读 school、playground、library 和 computer。",
  [("school", "学校"), ("playground", "操场"), ("library", "图书馆"), ("computer", "计算机")])

G("gr_floor", "楼层与 first、second", 4, "下", 1,
  "用 on the first floor 和 on the second floor 说明场所在第几层。", "when_ord", [
    ("n", "The library is on the second floor. 图书馆在第几层？", 2, "second 是第二，所以是第 2 层。"),
    ("c", "first floor 是第几层？", "第 1 层",
     ["第 2 层", "第 3 层", "第 4 层"], "first 是第一。"),
    ("c", "想问「教师办公室在哪里」，应选哪一句？", "Where is the teachers' office?",
     ["What is the teachers' office?", "Who is the teachers' office?", "How is the teachers' office?"], "问地点用 Where is。"),
    ("c", "It is on the first floor. 这句是在说什么？", "在第一层",
     ["在第二层", "在操场上", "在图书馆里"], "first floor 是第一层。"),
])

F("fu_school", "问路：学校里的场所", 4, "下", 1,
  "用 Where is 询问学校里的操场、图书馆在哪里。", "func_place", [
    ("c", "想问图书馆在哪里，应说哪一句？", "Where is the library?",
     ["Where is the playground?", "Where is the classroom?", "Do you have a library?"], "图书馆是 library。"),
    ("c", "The playground is on the first floor. 操场在第几层？", "第 1 层",
     ["第 2 层", "第 3 层", "第 4 层"], "first floor 是第一层。"),
    ("c", "Do you have a computer room? 这句是在问什么？", "你们有计算机教室吗",
     ["计算机教室在哪里", "你喜欢计算机吗", "计算机是谁的"], "Do you have 问有没有。"),
    ("c", "This is my school. 哪一句和这句话意思相同？", "这是我的学校。",
     ["这是我的教室。", "这是图书馆。", "这是操场。"], "school 是学校。"),
])

R("rw_school", "读懂学校平面说明", 4, "下", 1,
  "读学校场所的说明，找出地点和楼层。", "read_short", [
    ("c", "读一读：The library is on the second floor. 图书馆在第几层？", "第 2 层",
     ["第 1 层", "第 3 层", "第 4 层"], "second floor 是第二层。"),
    ("c", "读一读：We have a big playground. 哪一句和短文一致？", "我们有一个大操场。",
     ["我们没有操场。", "图书馆很大。", "操场在第二层。"], "a big playground。"),
    ("c", "读一读：The computer room is next to the library. 计算机教室在哪里？", "在图书馆旁边",
     ["在操场上", "在教室里", "在第一层的门后"], "next to the library 是在图书馆旁边。文字没有写楼层。"),
    ("c", "读一读：Classroom 2 is on the first floor. 二班教室在第几层？", "第 1 层",
     ["第 2 层", "第 3 层", "第 4 层"], "on the first floor；2 是教室编号，不是楼层。"),
])

V("vo_timew", "一天中的活动", 4, "下", 2,
  "认读 breakfast、lunch、dinner 和 music。",
  [("breakfast", "早餐"), ("lunch", "午餐"), ("dinner", "晚餐"), ("music", "音乐")])

G("gr_time", "What time is it", 4, "下", 2,
  "用 What time is it? 询问时刻，并用 It is 6 o'clock. 回答。", "number_q", [
    ("c", "想问「现在几点」，应选哪一句？", "What time is it?",
     ["What time it is?", "How many time is it?", "Where is the time?"], "问时刻说 What time is it?"),
    ("c", "It is 6 o'clock. 现在几点？", "6 点",
     ["5 点", "7 点", "9 点"], "6 o'clock 是 6 点。"),
    ("c", "It is time for lunch. 该做什么了？", "吃午饭",
     ["吃早饭", "吃晚饭", "上音乐课"], "lunch 是午饭。"),
    ("c", "It is 7 o'clock. It is time for breakfast. 该吃哪一餐？", "早饭",
     ["午饭", "晚饭", "下午茶"], "breakfast 是早饭。"),
])

F("fu_time", "说时刻和该做的事", 4, "下", 2,
  "用 It is time for 说出该吃饭或上课了。", "func_daily", [
    ("c", "现在 9 点，该上音乐课了，应说哪一句？", "It is 9 o'clock. It is time for music.",
     ["It is 9 o'clock. It is time for lunch.", "It is 6 o'clock. It is time for breakfast.", "It is 12 o'clock. It is time for dinner."],
     "音乐是 music，时刻要和 9 点一致。"),
    ("c", "What time is it? 若是 12 点，应回答哪一句？", "It is 12 o'clock.",
     ["It is 10 o'clock.", "It is 2 o'clock.", "It is 8 o'clock."], "12 点说 It is 12 o'clock。"),
    ("c", "It is time for English. 该上什么课？", "英语",
     ["音乐", "数学", "体育"], "English 是英语。"),
    ("c", "Hurry up! It is time for school. 这句是在催什么？", "该去上学了",
     ["该吃晚饭了", "该睡觉了", "该回家了"], "time for school 是该上学了。"),
])

R("rw_time", "读懂作息时刻", 4, "下", 2,
  "从短文里读出几点做什么。", "read_short", [
    ("c", "读一读：It is 7 o'clock. It is time for breakfast. 7 点该做什么？", "吃早饭",
     ["吃午饭", "吃晚饭", "上音乐课"], "breakfast 是早饭。"),
    ("c", "读一读：It is 12 o'clock. Have some lunch. 几点吃午饭？", "12 点",
     ["7 点", "6 点", "9 点"], "12 o'clock。"),
    ("n", "读一读：Music is at 9 o'clock. 音乐课是几点？", 9, "at 9 o'clock 是 9 点。"),
    ("c", "读一读：It is 6 o'clock. It is time for dinner. 哪一句和短文一致？", "6 点该吃晚饭了。",
     ["6 点该吃早饭了。", "7 点该吃晚饭了。", "6 点该上音乐课了。"], "6 o'clock 和 dinner。"),
])

V("vo_weather", "天气", 4, "下", 3,
  "认读 warm、cold、cool 和 hot。",
  [("warm", "温暖的"), ("cold", "寒冷的"), ("cool", "凉爽的"), ("hot", "炎热的")])

G("gr_weather", "It is 描述天气", 4, "下", 3,
  "用 What is the weather like? 询问天气，并用 It is 加上天气词回答。", "be", [
    ("c", "想问天气，应选哪一句？", "What is the weather like?",
     ["What is the weather is?", "How the weather like?", "Where is the weather?"], "问天气说 What is the weather like?"),
    ("c", "It is cold. 天气怎么样？", "很冷",
     ["很热", "很暖和", "很凉爽"], "cold 是冷。"),
    ("c", "It is sunny in Beijing. 北京的天气怎么样？", "晴朗",
     ["下雨", "下雪", "有风"], "sunny 是晴朗。"),
    ("c", "哪一句表示「今天很热」？", "It is hot today.",
     ["It is cold today.", "It is cool today.", "It is warm today."], "热是 hot。"),
])

F("fu_weather", "谈论天气并给建议", 4, "下", 3,
  "根据天气说出可以做的事，例如 It is warm. We can fly a kite.", "func_daily", [
    ("c", "外面很冷，应说哪一句？", "It is cold outside.",
     ["It is hot outside.", "It is warm outside.", "It is cool outside."], "冷是 cold。"),
    ("c", "It is warm. We can fly a kite. 为什么可以放风筝？", "因为天气暖和",
     ["因为很冷", "因为在下雨", "因为是夜晚"], "It is warm 是天气暖和。"),
    ("c", "Can I go outside? 这句是在问什么？", "我可以出去吗",
     ["天气怎么样", "现在几点", "你喜欢冷天吗"], "go outside 是出去。"),
    ("c", "It is hot. Have some water. 这句建议做什么？", "喝些水",
     ["穿上外套", "放风筝", "关窗"], "Have some water 是喝些水。"),
])

R("rw_weather", "读懂天气预报", 4, "下", 3,
  "读一则写明城市和天气的短文，按文字判断。", "read_short", [
    ("c", "读一读：It is cold and snowy in Harbin. 哈尔滨的天气怎么样？", "又冷又下雪",
     ["很热", "很暖和", "只是有风"], "cold and snowy。"),
    ("c", "读一读：It is sunny in Beijing. It is rainy in Shanghai. 哪里下雨？", "上海",
     ["北京", "哈尔滨", "两个城市都下雨"], "rainy 写在 Shanghai。"),
    ("c", "读一读：It is warm today. Let's fly a kite. 哪一句和短文一致？", "今天暖和，建议放风筝。",
     ["今天很冷。", "今天在下雨。", "不建议出去。"], "warm，并且 Let's fly a kite。"),
    ("c", "读一读：Here is the world weather. It is cool in London. 伦敦怎么样？", "凉爽",
     ["炎热", "寒冷", "下雪"], "cool 是凉爽。"),
])

V("vo_farm", "农场", 4, "下", 4,
  "认读 tomato、potato、horse 和 cow。",
  [("tomato", "西红柿"), ("potato", "土豆"), ("horse", "马"), ("cow", "奶牛")])

G("gr_these", "These are 与 Those are", 4, "下", 4,
  "用 These are 指近处的多个事物，用 Those are 指远处的多个事物。", "pointer", [
    ("c", "指着近处的几只鸭子，应选哪一句？", "These are ducks.",
     ["This is ducks.", "These is ducks.", "That are ducks."], "近处的复数用 These are。"),
    ("c", "Those are horses. 这句在说什么？", "远处的那些是马",
     ["近处的这一个是马", "近处的这些是马", "远处的那一个是马"], "Those are 是远处的复数。"),
    ("c", "These are potatoes. 这句里的 potatoes 是？", "复数",
     ["单数", "一个人名", "一种颜色"], "potatoes 是 potato 的复数。"),
    ("c", "哪一句说的是不止一头牛？", "These are cows.",
     ["That is a cow.", "This is a cow.", "It is a cow."], "These are cows 是复数。"),
])

F("fu_farm", "在农场谈论动物和蔬菜", 4, "下", 4,
  "用 Are these 询问近处的这些是不是某种蔬菜或动物。", "func_place", [
    ("c", "指着近处的西红柿问，应说哪一句？", "Are these tomatoes?",
     ["Are these potatoes?", "Is this a horse?", "Are these cows?"], "西红柿是 tomatoes。"),
    ("c", "Are these horses? 若是，应回答哪一句？", "Yes, they are.",
     ["Yes, it is.", "No, it is not.", "Yes, these is."], "these 的肯定回答是 Yes, they are。"),
    ("c", "Those are cows. 远处的是什么？", "奶牛",
     ["马", "土豆", "西红柿"], "cows 是奶牛。"),
    ("c", "The potatoes are big. 什么很大？", "土豆",
     ["西红柿", "马", "奶牛"], "potatoes 是土豆。"),
])

R("rw_farm", "读懂农场短文", 4, "下", 4,
  "读农场短文，按文字找出动物或蔬菜的数量。", "read_short", [
    ("c", "读一读：These are tomatoes. They are red. 近处这些是什么？", "西红柿",
     ["土豆", "马", "奶牛"], "tomatoes 是西红柿。"),
    ("c", "读一读：Those are horses. They are brown. 马是什么颜色？", "棕色",
     ["红色", "绿色", "黄色"], "brown 是棕色。文字没有说它们是黑色。"),
    ("n", "读一读：I see seventeen cows and eleven horses. 奶牛有几头？", 17, "seventeen cows 是 17 头。"),
    ("c", "读一读：The potatoes are big. The tomatoes are small. 哪一句和短文一致？", "土豆大，西红柿小。",
     ["土豆小，西红柿大。", "土豆和西红柿一样大。", "没有写大小。"], "potatoes are big，tomatoes are small。"),
])

V("vo_clothes", "衣服", 4, "下", 5,
  "认读 shirt、dress、skirt 和 pants。pants 表示裤子，用复数。",
  [("shirt", "衬衫"), ("dress", "连衣裙"), ("skirt", "裙子"), ("pants", "裤子")])

G("gr_whose", "Whose 与名词所有格", 4, "下", 5,
  "用 Whose 和名词所有格 's 询问、说明衣服是谁的。", "lets", [
    ("c", "问「这是谁的帽子」，应选哪一句？", "Whose hat is this?",
     ["Who hat is this?", "Where hat is this?", "What hat is this?"], "问属于谁用 Whose。"),
    ("c", "It is Amy's dress. 裙子是谁的？", "Amy 的",
     ["Mike 的", "老师的", "我的"], "Amy's 表示 Amy 的。"),
    ("c", "Whose pants are these? 这句是在问什么？", "这条裤子是谁的",
     ["裤子是什么颜色", "裤子多少钱", "裤子在哪里"], "Whose pants 问裤子是谁的。"),
    ("c", "This is Chen Jie's skirt. 裙子是谁的？", "Chen Jie 的",
     ["Amy 的", "John 的", "Sarah 的"], "Chen Jie's 表示 Chen Jie 的。"),
])

F("fu_clothes", "谈论穿着", 4, "下", 5,
  "用 Whose 和 I like 谈论衣服。", "func_daily", [
    ("c", "想说自己喜欢这条裙子，应说哪一句？", "I like this skirt.",
     ["I like this shirt.", "I like this dress.", "I like these pants."], "裙子是 skirt。"),
    ("c", "Whose shirt is this? 若是 Mike 的，应回答哪一句？", "It is Mike's.",
     ["It is Amy's.", "It is Sarah's.", "It is Chen Jie's."], "Mike 的要说 Mike's。"),
    ("c", "These pants are Zhang Peng's. 裤子是谁的？", "Zhang Peng 的",
     ["Amy 的", "Sarah 的", "John 的"], "Zhang Peng's 是 Zhang Peng 的。"),
    ("c", "Put on your shirt. 这句是在说什么？", "穿上你的衬衫",
     ["脱下你的裙子", "这是谁的裤子", "我喜欢这条连衣裙"], "Put on your shirt 是穿上衬衫。"),
])

R("rw_clothes", "读懂衣服是谁的", 4, "下", 5,
  "读衣服的句子，找出主人。", "read_short", [
    ("c", "读一读：This is Amy's dress. It is red. 连衣裙是谁的？", "Amy 的",
     ["Mike 的", "John 的", "Sarah 的"], "Amy's dress。"),
    ("c", "读一读：Whose pants are these? They are Zhang Peng's. 裤子是谁的？", "Zhang Peng 的",
     ["Amy 的", "Chen Jie 的", "老师的"], "回答是 Zhang Peng's。"),
    ("c", "读一读：I like that green skirt. 喜欢的裙子是什么颜色？", "绿色",
     ["红色", "蓝色", "黄色"], "green skirt。"),
    ("c", "读一读：My shirt is white. Sarah's shirt is blue. 谁的衬衫是蓝色的？", "Sarah 的",
     ["我的", "Amy 的", "Mike 的"], "Sarah's shirt is blue。"),
])

V("vo_shop", "商店物品", 4, "下", 6,
  "认读 glove、scarf、umbrella 和 sunglasses。",
  [("glove", "手套"), ("scarf", "围巾"), ("umbrella", "雨伞"), ("sunglasses", "太阳镜")])

G("gr_price", "How much 询问价格", 4, "下", 6,
  "用 How much is 或 How much are 询问价格。", "number_q", [
    ("c", "想问「这件衬衫多少钱」，应选哪一句？", "How much is this shirt?",
     ["How many is this shirt?", "How old is this shirt?", "How tall is this shirt?"], "问价格用 How much。"),
    ("n", "The sunglasses are 50 yuan. 太阳镜多少元？", 50, "句子里写的是 50 yuan。"),
    ("c", "The gloves are 8 yuan. 手套多少钱？", "8 元",
     ["7 元", "18 元", "80 元"], "8 yuan 是 8 元。"),
    ("c", "How much is it? 这句是在问什么？", "它多少钱",
     ["它有多重", "它有多高", "它有多少个"], "How much 问价钱。"),
])

F("fu_shop", "在商店购物", 4, "下", 6,
  "用 Can I help you? 和 How much 完成简单购物对话。", "func_place", [
    ("c", "售货员招呼顾客，常说哪一句？", "Can I help you?",
     ["How old are you?", "Where are you from?", "Let's clean the room."], "商店里常说 Can I help you?"),
    ("c", "想说「这条围巾很漂亮」，应说哪一句？", "This scarf is pretty.",
     ["This umbrella is pretty.", "These gloves are pretty.", "These sunglasses are pretty."], "围巾是 scarf。"),
    ("c", "How much is this umbrella? 若是 15 元，应回答哪一句？", "It is 15 yuan.",
     ["It is 50 yuan.", "They are 8 yuan.", "It is 5 yuan."], "一把伞用 It is，价格是 15 元。"),
    ("c", "They are too expensive. 这句的意思是？", "它们太贵了",
     ["它们很便宜", "我要买它们", "它们是 10 元"], "too expensive 是太贵。"),
])

R("rw_price", "读懂价签", 4, "下", 6,
  "读商店里的价格句子，找出物品和价钱。", "read_short", [
    ("c", "读一读：The scarf is 20 yuan. The umbrella is 15 yuan. 围巾多少钱？", "20 元",
     ["15 元", "50 元", "8 元"], "scarf is 20 yuan。"),
    ("n", "读一读：The sunglasses are 50 yuan. 太阳镜多少元？", 50, "50 yuan。"),
    ("c", "读一读：Can I help you? The gloves are 8 yuan. 哪一句和文字一致？", "手套是 8 元。",
     ["手套是 15 元。", "雨伞是 8 元。", "围巾是 8 元。"], "gloves are 8 yuan。"),
    ("c", "读一读：The umbrella is cheap. It is 10 yuan. 雨伞怎么样？", "便宜，10 元",
     ["很贵，50 元", "便宜，20 元", "没写价格"], "cheap 是便宜，价格是 10 yuan。"),
])
