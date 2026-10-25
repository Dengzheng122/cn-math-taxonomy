# -*- coding: utf-8 -*-
"""人教版（2019）必修第一册。单元名按通行目录，册次待核。"""
from enh_tx import V, P, G, F, R, q


def load():
    G("gr_sentmem", "句子成分", 10, 0,
      "能指出简单句的主语、谓语和宾语。", "sent", [
        q("The boy likes music. 这句的主语是哪一个？", "The boy", "likes", "music", "the full stop",
          "The boy 是动作的发出者，作主语。"),
        q("The boy likes music. 这句的谓语是哪一个？", "likes", "The boy", "music", "a comma",
          "likes 表示动作，作谓语。"),
        q("She reads English every day. 这句的宾语是哪一个？", "English", "She", "reads", "every day",
          "reads 是及物动词，English 是宾语。every day 是状语。"),
        q("哪一句里的 music 作宾语？", "We love music", "Music sounds good", "The music is loud", "They are students",
          "love 后面的 music 是宾语。其余三句是主系表。"),
      ])

    G("gr_svo", "五种基本句型", 10, 0,
      "能分辨主谓、主谓宾、主系表、双宾语和宾语补足语。", "sent", [
        q("Birds fly. 这句属于哪一种基本句型？", "主谓", "主谓宾", "主系表", "双宾语",
          "fly 是不及物动词，后面没有宾语。"),
        q("She gave me a book. 这句属于哪一种基本句型？", "双宾语", "主谓", "主系表", "只有一个宾语",
          "gave 后面有 me 和 a book 两个宾语。"),
        q("The soup tastes good. 这句属于哪一种基本句型？", "主系表", "主谓宾", "双宾语", "宾语补足语",
          "tastes 是系动词，good 是表语。"),
        q("哪一句是主谓宾？", "They play basketball", "The baby cried", "He is a doctor", "She looks happy",
          "play 是及物动词，basketball 是宾语。"),
      ])

    G("gr_svoc", "宾语补足语", 10, 0,
      "能找出宾语补足语，并分辨它和双宾语。", "sent", [
        q("We call him Tom. 句中 Tom 是什么成分？", "宾语补足语", "主语", "定语", "状语",
          "Tom 补充说明宾语 him，是宾补。"),
        q("I found the film interesting. interesting 是什么成分？", "宾语补足语", "主语", "谓语", "间接宾语",
          "interesting 补充说明宾语 the film。"),
        q("哪一句含有宾语补足语？", "The news made her happy", "She gave me a pen", "They are friends", "Birds can fly",
          "happy 补充说明宾语 her。gave me a pen 是双宾语。"),
        q("Please keep the room clean. clean 修饰说明的是哪一个？", "the room", "Please", "keep", "句末的句号",
          "clean 是宾补，说明宾语 the room 的状态。"),
      ])

    V("vo_campus", "校园设施", 10, 0,
      "认读 campus、lecture、locker 和 freshman。",
      [("campus", "校园"), ("lecture", "讲座"), ("locker", "储物柜"), ("freshman", "新生")], "vo_school")

    F("fu_greet", "问候并介绍自己", 10, 0,
      "能向新同学问候，并说出自己的班级。", "fu_daily", [
        q("开学第一天，想问好并说出自己的名字，哪一句合适？", "Hi, my name is Lin",
          "Hi, my name are Lin", "Hi, your name is Lin", "Hi, my name Lin is",
          "问候并自报姓名用 Hi, my name is。"),
        q("对方说 Nice to meet you. 你应回答什么？", "Nice to meet you too",
          "See you yesterday", "Nice to meeting you too", "Nice to meets you too",
          "回应 Nice to meet you 时加上 too。"),
        q("想告诉同学自己在三班，哪一句合适？", "I am in Class 3",
          "I am at Class 3", "I is in Class 3", "He is in Class 3",
          "说明自己的班级用 I am in Class 3。"),
        q("早上在教学楼遇见老师，哪一句是问候？", "Good morning",
          "Good mornings", "Good moning", "Good monring",
          "Good morning 用来问候早晨。"),
      ])

    _w = "Lin is a new student. She is in Class 3. Her first lecture is on Monday."
    R("rw_welcome", "读新生简介", 10, 0,
      "读一段新生简介，找出班级和第一堂课的时间。", "rw_detail", [
        q(_w + " Lin 是什么身份？", "新生", "老师", "医生", "司机", "短文写 She is a new student。"),
        q(_w + " 她在哪个班？", "三班", "一班", "五班", "九班", "短文写 She is in Class 3。"),
        q(_w + " 她的第一堂讲座在哪一天？", "星期一", "星期二", "星期五", "星期日", "短文写 on Monday。"),
        q(_w + " 哪一句和短文一致？", "Lin has a lecture on Monday",
          "Lin is a teacher", "Lin is in Class 9", "The lecture is on Friday",
          "短文只说她是新生，周一有讲座。"),
      ])

    R("wr_welcome", "写自我介绍", 10, 0,
      "能按要点选出自我介绍里该写的句子。", "rw_write", [
        q("要点：姓名林晓、三班、喜欢音乐。哪一句三个要点都有？",
          "I am Lin Xiao in Class 3, and I like music",
          "I am Lin Xiao in Class 3", "I like music and football", "I am Lin Xiao in Class 3, and I like football",
          "姓名、班级和音乐三个要点都要出现。"),
        q("想用邮件向笔友介绍自己是新生，哪一句合适？",
          "I am a new student at this school",
          "I is a new student at this school", "I am an new student at this school", "I not am a new student at this school",
          "介绍自己的身份用 I am a new student。"),
        q("自我介绍要写爱好，哪一句在写爱好？", "I enjoy playing basketball",
          "The campus is large", "Monday is a day", "Class 3 is a room",
          "enjoy playing basketball 是在说爱好。"),
        q("哪一句适合放在自我介绍的开头？", "Hello, let me introduce myself",
          "Hello, let me itnroduce myself", "Hello, let me introdcue myself", "Hello, let me inroduce myself",
          "自我介绍开头常用 Hello, let me introduce myself。"),
      ])

    P("ph_toneb", "句末升调和降调", 10, 0,
      "能区分陈述句、特殊疑问句的降调和一般疑问句的升调。", "tone_b", [
        q("一般疑问句 Are you in Class 3? 句末通常用什么语调？", "升调",
          "降调", "每个词都重读", "没有语调", "一般疑问句句末通常用升调。"),
        q("陈述句 I am a new student. 句末通常用什么语调？", "降调",
          "升调", "先升后降再升", "只在 student 上不停", "陈述句句末通常用降调。"),
        q("特殊疑问句 Where is the lecture? 句末通常用什么语调？", "降调",
          "升调", "和一般疑问句相同的升调", "只在 where 上上升", "特殊疑问句句末通常用降调。"),
        q("哪一句朗读时句末通常用升调？", "Is the locker yours",
          "The locker is mine", "Where is the locker", "She is a freshman",
          "Is the locker yours 是一般疑问句，句末用升调。"),
      ])

    V("vo_course", "课程与作业", 10, 1,
      "认读 course、homework、quiz 和 grade。",
      [("course", "课程"), ("homework", "家庭作业"), ("quiz", "小测验"), ("grade", "成绩")], "vo_school")

    V("vo_challenge", "挑战与社团", 10, 1,
      "认读 challenge、debate、volunteer 和 confident。",
      [("challenge", "挑战"), ("debate", "辩论"), ("volunteer", "志愿者"), ("confident", "自信的")], "vo_school")

    G("gr_np", "名词短语", 10, 1,
      "能识别名词短语，并判断它在句中作什么成分。", "phrase", [
        q("The tall boy in blue 是什么短语？", "名词短语", "动词短语", "介词单独成句", "副词短语",
          "中心词 boy 是名词，前面有限定和形容词。"),
        q("My new schoolbag 在句中常作什么？", "主语或宾语", "谓语", "系动词", "助动词",
          "名词短语可以作主语或宾语，不能单独作谓语。"),
        q("哪一个是名词短语？", "a difficult maths course", "runs quickly", "very carefully", "looks happy",
          "course 是名词中心词，前面有冠词和形容词。"),
        q("She joined the school debate team. 宾语是哪一个？", "the school debate team",
          "She", "joined", "school 这个单词单独", "the school debate team 是名词短语，作 joined 的宾语。"),
      ])

    G("gr_adjp", "形容词短语和副词短语", 10, 1,
      "能识别形容词短语和副词短语，并判断它们作表语还是状语。", "phrase", [
        q("The question is very difficult. very difficult 是什么？", "形容词短语作表语",
          "名词短语作主语", "动词短语作谓语", "介词短语作宾语",
          "difficult 是形容词，very 修饰它，放在系动词后面作表语。"),
        q("He spoke quite clearly. quite clearly 是什么？", "副词短语作状语",
          "名词短语作宾语", "形容词短语作表语", "双宾语",
          "clearly 是副词，修饰 spoke，作状语。"),
        q("哪一个是形容词短语？", "good at maths", "the maths course", "speak English", "in the morning",
          "good 是形容词，at maths 补充说明它。"),
        q("She is afraid of the quiz. afraid of the quiz 说明的是哪一个？", "She",
          "is", "the 这个词", "句号", "表语说明主语 She 的状态。"),
      ])

    F("fu_club", "谈论课程和社团", 10, 1,
      "能说出自己喜欢的课程，并回应加入社团的建议。", "fu_daily", [
        q("想说自己最喜欢英语课，哪一句合适？", "My favourite course is English",
          "Your favourite course is English", "My fvaourite course is English", "My favourtie course is English",
          "说最喜欢的课程用 My favourite course is。"),
        q("同学建议你参加辩论社，你愿意，应回答什么？", "That sounds good. I will join",
          "That sounds good. I will joined", "That sounds good. I will to join", "That suonds good. I will join",
          "接受建议可以说 That sounds good。"),
        q("想问对方有没有加入社团，哪一句合适？", "Have you joined a club",
          "Have you joined an club", "Have you jioned a club", "Have you joiend a club",
          "询问对方用 Have you joined a club。"),
        q("想说明参加志愿者活动让自己更自信，哪一句合适？",
          "Volunteering makes me more confident",
          "Volunteering make me more confident", "Vlounteering makes me more confident", "Volunteernig makes me more confident",
          "makes me more confident 说明活动带来的变化。"),
      ])

    _t = "Chen likes his English course, but the maths quiz is a challenge. He also joins the debate club."
    R("rw_teen", "读校园生活短文", 10, 1,
      "读一段校园生活短文，找出课程和社团。", "rw_detail", [
        q(_t + " Chen 喜欢哪一门课？", "英语", "数学", "历史", "音乐", "短文写 likes his English course。"),
        q(_t + " 什么对他来说是挑战？", "数学小测验", "英语课", "辩论社", "校园", "短文写 the maths quiz is a challenge。"),
        q(_t + " 他参加了什么社团？", "辩论社", "音乐社", "篮球队", "科学社", "短文写 the debate club。"),
        q(_t + " 哪一句和短文一致？", "Chen joins the debate club",
          "Chen hates English", "The English quiz is a challenge", "Chen joins the music club",
          "挑战的是数学小测验，不是英语课。"),
      ])

    R("wr_teen", "写社团申请句", 10, 1,
      "能按要点选出申请加入社团的句子。", "rw_write", [
        q("要点：想加入辩论社、喜欢讨论、每周五有空。哪一句三个要点都有？",
          "I want to join the debate club because I like discussion and I am free on Friday",
          "I want to join the debate club", "I am free on Friday", "I like music on Monday",
          "三个要点要同时出现。"),
        q("申请句要说明理由，哪一句有理由？", "I want to join because I like debate",
          "The club is a room", "Friday is a day", "Please open the door",
          "because 后面是加入的理由。"),
        q("哪一句适合作为申请的开头？", "I would like to join the debate club",
          "I would liked to join the debate club", "I would like to joining the debate club", "I would like to joins the debate club",
          "申请开头可以直接说 I would like to join。"),
        q("老师要求用现在时介绍自己的空闲时间，哪一句符合？", "I am free on Friday afternoon",
          "I was free in 1990 only", "I will was free", "I am free in Friday afternoon",
          "现在的空闲时间用 I am free。"),
      ])

    V("vo_travel", "旅行安排", 10, 2,
      "认读 destination、brochure、accommodation 和 itinerary。",
      [("destination", "目的地"), ("brochure", "小册子"), ("accommodation", "住宿"), ("itinerary", "行程")],
      "vo_world")

    V("vo_place", "景点", 10, 2,
      "认读 castle、waterfall、temple 和 scenery。",
      [("castle", "城堡"), ("waterfall", "瀑布"), ("temple", "寺庙"), ("scenery", "风景")], "vo_world")

    G("gr_futcont", "现在进行时表将来", 10, 2,
      "能用现在进行时表示已经安排好的将来。", "tense", [
        q("I ___ Tom at the station tomorrow. 表示已经安排好的见面，横线处填哪一个？", "am meeting",
          "meet", "was meeting", "met", "已经安排的将来用现在进行时 am meeting。"),
        q("哪一句表示已经安排好的将来？", "We are flying to Xi'an next Friday",
          "We fly every Friday", "We flew last Friday", "Birds are animals",
          "next Friday 加上现在进行时，表示已安排的行程。"),
        q("She is leaving for Beijing tonight. 这句主要在说什么？", "今晚已经安排离开",
          "今晚正在睡觉", "昨晚已经离开", "她讨厌北京", "is leaving 加将来时间，表示安排。"),
        q("计划明天参观城堡，哪一句合适？", "We are visiting the castle tomorrow",
          "We visit the castle yesterday", "We visited the castle tomorrow", "We are visit tomorrow",
          "tomorrow 不能和过去式 visited 搭配，安排用 are visiting。"),
      ])

    G("gr_themoment", "时间从句用现在时表将来", 10, 2,
      "能在时间和条件状语从句中用一般现在时表示将来。", "tense", [
        q("I will call you when I ___ there. 横线处填哪一个？", "arrive",
          "will arrive", "arrived", "am arrived", "when 从句里用一般现在时表示将来。"),
        q("If it ___ tomorrow, we will stay in. 横线处填哪一个？", "rains",
          "will rain", "rained", "is rain", "if 条件从句不用 will，用 rains。"),
        q("哪一句是正确的？", "I will tell her as soon as she comes",
          "I will tell her as soon as she will come", "I tell her as soon as she will come",
          "I told her as soon as she will come tomorrow",
          "as soon as 从句用现在时，主句用 will。"),
        q("We will start after the guide ___. 横线处填哪一个？", "arrives",
          "will arrive", "arrive", "is arrive", "after 引导的时间从句用 arrives。"),
      ])

    F("fu_plantrip", "谈论旅行计划", 10, 2,
      "能说出已经安排的行程，并回应邀请。", "fu_plan", [
        q("想告诉同学周五已经订好去西安的机票，哪一句合适？", "We are flying to Xi'an on Friday",
          "We flew to Xi'an tomorrow", "We is flying to Xi'an on Friday", "We are fly to Xi'an on Friday",
          "已经安排的行程用现在进行时。"),
        q("朋友邀请你一起去看瀑布，你愿意，应回答什么？", "Yes, I would love to",
          "Yes, I would loved to", "Yes, I would to love to", "Yes, I wuold love to",
          "接受邀请可以说 Yes, I would love to。"),
        q("想问对方的住宿订在哪里，哪一句合适？", "Where is your accommodation",
          "Where is your accommodatoin", "Where is your acommodation", "Where is accommodation your",
          "询问住宿地点用 Where is your accommodation。"),
        q("想建议先看行程再出发，哪一句合适？", "Let's check the itinerary before we leave",
          "Let's to check the itinerary before we leave", "Let's check the iitnerary before we leave", "We left tomorrow",
          "提建议可以用 Let's check the itinerary。"),
      ])

    _p = "Anna is travelling to Xi'an next Friday. She is staying in a small hotel. Her itinerary includes a temple and a museum."
    R("rw_itin", "读行程短文", 10, 2,
      "读一段行程，找出时间、住宿和景点，并判断作者是否只在列计划。", "rw_main", [
        q(_p + " Anna 什么时候去西安？", "下周五", "上周五", "明年", "昨天", "短文写 next Friday。"),
        q(_p + " 她住在哪里？", "一家小旅馆", "城堡里", "学校宿舍", "瀑布旁边", "短文写 a small hotel。"),
        q(_p + " 行程里包含什么？", "寺庙和博物馆", "海滩和冰川", "农场和工厂", "车站和机场",
          "短文写 a temple and a museum。"),
        q(_p + " 作者的态度更接近哪一种？", "只是在说明已经安排的计划",
          "强烈反对这次旅行", "在批评旅馆", "在请求救援",
          "短文只列时间和安排，没有表示反对。"),
      ])

    R("wr_itin", "写行程邮件", 10, 2,
      "能按要点选出行程邮件里的句子。", "rw_write", [
        q("要点：周五出发、住小旅馆、去看兵马俑。哪一句三个要点都有？",
          "We are leaving on Friday, staying in a small hotel and visiting the Terracotta Army",
          "We are leaving on Friday", "The hotel is small", "I like museums",
          "出发、住宿和景点都要写到。"),
        q("邮件里表示已经订好车票，哪一句合适？", "I have already booked the train ticket",
          "I have already book the train ticket", "I not have already booked the train ticket", "I have arleady booked the train ticket",
          "已经订好用 have booked。"),
        q("哪一句适合作为行程邮件的开头？", "I am writing to tell you about my trip",
          "I am write to tell you about my trip", "I am writing to telling you about my trip", "I am writing to tells you about my trip",
          "说明写信目的可以用 I am writing to tell you。"),
        q("想写如果下雨就改去博物馆，哪一句正确？", "If it rains, we will go to the museum",
          "If it will rain, we go to the museum", "If it rains, we went tomorrow", "If rains it, we will go",
          "if 从句用 rains，主句用 will go。"),
      ])

    V("vo_sport", "运动项目", 10, 3,
      "认读 marathon、stadium、coach 和 medal。",
      [("marathon", "马拉松"), ("stadium", "体育场"), ("coach", "教练"), ("medal", "奖牌")], "vo_world")

    V("vo_health", "健身与健康", 10, 3,
      "认读 fitness、muscle、diet 和 injury。",
      [("fitness", "体能"), ("muscle", "肌肉"), ("diet", "日常饮食"), ("injury", "损伤")], "vo_world")

    G("gr_taghs", "附加疑问句", 10, 3,
      "能让附加问句的人称、助动词和肯定否定与陈述部分一致。", "tag", [
        q("She can swim, ___? 横线处填哪一个？", "can't she", "can she", "can't he", "doesn't she",
          "前面是肯定的 can，附加问句用否定 can't she。"),
        q("They didn't win, ___? 横线处填哪一个？", "did they", "didn't they", "do they", "won they",
          "前面是否定的 didn't，附加问句用肯定 did they。"),
        q("哪一句的附加问句是正确的？", "He is a coach, isn't he",
          "He is a coach, is he", "He is a coach, isn't she", "He is a coach, doesn't he",
          "is 的否定附加问句是 isn't he。"),
        q("You have finished the race, ___? 横线处填哪一个？", "haven't you",
          "have you", "didn't you", "don't you", "have 是助动词，肯定句后面用 haven't you。"),
      ])

    G("gr_advp", "副词短语作状语", 10, 3,
      "能识别副词短语，并判断它修饰哪一个动词。", "phrase", [
        q("She runs very quickly. very quickly 修饰哪一个？", "runs", "She", "very 单独", "句号",
          "副词短语修饰动词 runs。"),
        q("哪一个是副词短语？", "much more carefully", "a careful coach", "the big stadium", "looks strong",
          "carefully 是副词，much more 修饰它。"),
        q("He trains quite hard before the marathon. quite hard 是什么成分？", "状语",
          "主语", "宾语", "定语", "quite hard 修饰 trains，作状语。"),
        q("哪一句里的短语作状语？", "They played fairly well", "They are fairly good players",
          "A fairly good player arrived", "The fairly big stadium is new",
          "well 修饰 played。其余 fairly 修饰的是形容词。"),
      ])

    F("fu_sport", "提出运动建议", 10, 3,
      "能就运动和健康提出建议，并回应别人的建议。", "fu_plan", [
        q("朋友很少运动，你建议他每天步行，哪一句合适？", "You could walk for thirty minutes a day",
          "You could walked for thirty minutes a day", "You could walk for thirty minutes an day", "You could to walk for thirty minutes a day",
          "提建议可以用 You could。"),
        q("教练说 Don't train when you are injured. 你明白了，应回答什么？", "All right, I will rest",
          "I will train harder tonight", "The muscle is a coach", "Yesterday rest tomorrow",
          "受伤时接受建议应该休息。"),
        q("想邀请同学周六一起去体育场跑步，哪一句合适？", "Shall we run at the stadium on Saturday",
          "Shall we run at the stadium in Saturday", "Shall we run at the stadium on Staurday", "We ran tomorrow",
          "发出邀请可以用 Shall we。"),
        q("想说明均衡饮食对体能有帮助，哪一句合适？", "A balanced diet helps your fitness",
          "A balanced diet help your fitness", "A blaanced diet helps your fitness", "A balanecd diet helps your fitness",
          "helps your fitness 说明饮食的作用。"),
      ])

    _m = "Li ran a marathon last Sunday and won a medal. His coach says he should rest because of a small injury."
    R("rw_match", "读比赛短文", 10, 3,
      "读一段比赛短文，找出结果和教练的建议。", "rw_detail", [
        q(_m + " Li 参加了什么？", "马拉松", "游泳", "辩论", "讲座", "短文写 ran a marathon。"),
        q(_m + " 他得到了什么？", "一块奖牌", "一座城堡", "一本小册子", "一个储物柜", "短文写 won a medal。"),
        q(_m + " 教练为什么建议他休息？", "因为有一点损伤", "因为他输了", "因为下周还有课", "因为没有教练",
          "短文写 because of a small injury。"),
        q(_m + " 哪一句和短文一致？", "Li won a medal", "Li lost the marathon",
          "The coach wants him to train all night", "Li has no injury",
          "他赢了奖牌，但有一点损伤。"),
      ])

    R("wr_match", "写运动简讯", 10, 3,
      "能按要点选出简讯里的句子。", "rw_write", [
        q("要点：上周日马拉松、获得奖牌、教练建议休息。哪一句三个要点都有？",
          "Li ran a marathon last Sunday, won a medal, and his coach told him to rest",
          "Li ran a marathon", "He won a medal", "The coach likes music",
          "时间、结果和建议都要出现。"),
        q("简讯要用过去时写已经结束的比赛，哪一句符合？", "Our team won the game yesterday",
          "Our team wins the game yesterday", "Our team will won yesterday", "Won our team yesterday the game",
          "yesterday 搭配过去式 won。"),
        q("哪一句适合提醒读者注意伤病？", "Stop training if you feel an injury",
          "Stop tarining if you feel an injury", "Stop trainnig if you feel an injury", "Stop trining if you feel an injury",
          "if you feel an injury 是在提醒。"),
        q("附加问句想确认读者已经看过通知，哪一句正确？", "You have read the notice, haven't you",
          "You have read the notice, have you", "You have read the notice, didn't he",
          "You read the notice, aren't you",
          "have 的否定附加问句是 haven't you。"),
      ])

    V("vo_disaster", "自然灾害", 10, 4,
      "认读 earthquake、flood、hurricane 和 drought。",
      [("earthquake", "地震"), ("flood", "洪水"), ("hurricane", "飓风"), ("drought", "干旱")], "vo_soc")

    V("vo_rescue", "救援", 10, 4,
      "认读 rescue、shelter、survivor 和 warning。",
      [("rescue", "救援"), ("shelter", "庇护所"), ("survivor", "幸存者"), ("warning", "警报")], "vo_soc")

    G("gr_relpro", "关系代词定语从句", 10, 4,
      "能用 who、which 和 that 引导限制性定语从句。", "rel", [
        q("The girl ___ is singing is my classmate. 横线处填哪一个？", "who",
          "which", "where", "whom", "先行词是人，在从句中作主语，用 who。"),
        q("The book ___ I bought is about disasters. 横线处填哪一个？", "that",
          "who", "where", "whom", "先行词是物，作宾语可以用 that。"),
        q("哪一句是正确的？", "I know the doctor who saved the child",
          "I know the doctor which saved the child", "I know the doctor where saved the child",
          "I know the doctor he saved the child",
          "doctor 是人，作主语用 who，不能用 which。"),
        q("This is the warning ___ saved many lives. 横线处填哪一个？", "which",
          "who", "whom", "where", "warning 是物，作主语用 which。"),
      ])

    G("gr_relwhose", "whose 和 whom", 10, 4,
      "能用 whose 表示所属，用 whom 作介词或动词的宾语。", "rel", [
        q("The student ___ mother is a doctor sits here. 横线处填哪一个？", "whose",
          "who", "which", "whom", "mother 属于 the student，用 whose。"),
        q("The man ___ we met is a survivor. 空格作 met 的宾语，且先行词是人，填哪一个？", "whom",
          "whose", "which", "where", "先行词是人，在从句中作宾语，用 whom。"),
        q("哪一句用 whose 是正确的？", "I helped a boy whose house was flooded",
          "I helped a boy who house was flooded", "I helped a boy which house was flooded",
          "I helped a boy whom house was flooded",
          "house 属于 a boy，用 whose house。"),
        q("The woman to ___ I spoke is a volunteer. 横线处填哪一个？", "whom",
          "whose", "which", "where", "介词 to 后面指人用 whom。"),
      ])

    F("fu_rescue", "说明灾情并请求帮助", 10, 4,
      "能说明灾情、表达担心，并请求帮助。", "fu_view", [
        q("想告诉同学洪水很严重，哪一句合适？", "The flood is serious and many people need help",
          "The flood are serious and many people need help", "The flood is serious and many peoples need help", "The flood is sreious and many people need help",
          "说明灾情可以说 The flood is serious。"),
        q("想请求对方捐出毯子，哪一句合适？", "Could you please donate some blankets",
          "Could you please donate some balnkets", "Could you please donate some blanktes", "Could you please donate some blnkets",
          "礼貌请求用 Could you please。"),
        q("想表达对幸存者的担心，哪一句合适？", "I am worried about the survivors",
          "I is worried about the survivors", "He is worried about the survivors", "I am worried about the sruvivors",
          "I am worried about 用来表达担心。"),
        q("同学说救援队已经出发，你表示庆幸，应回答什么？", "I am glad the rescue team has left",
          "I am glad the team never left", "I is glad the rescue team has left", "He is glad the rescue team has left",
          "表示庆幸可以说 I am glad。"),
      ])

    _n = "A strong earthquake hit the town on Friday. Rescue teams found twenty survivors. The warning had been sent ten minutes earlier."
    R("rw_news", "读灾害新闻", 10, 4,
      "读一则已经发生的灾害新闻，找出时间、人数和警报。", "rw_detail", [
        q(_n + " 地震发生在哪一天？", "星期五", "星期一", "星期日", "没有写日期", "短文写 on Friday。"),
        q(_n + " 救援队找到了多少幸存者？", "二十人", "十人", "两人", "一百人", "短文写 twenty survivors。"),
        q(_n + " 警报是什么时候发出的？", "地震前十分钟", "地震后一天", "没有发出", "地震前一小时",
          "短文写 ten minutes earlier。"),
        q(_n + " 哪一句和短文一致？", "Rescue teams found twenty survivors",
          "The earthquake hit on Monday", "No warning was sent", "The town had no earthquake",
          "人数和时间都要和短文一致。"),
      ])

    R("wr_news", "写灾害报道句", 10, 4,
      "能按要点选出报道中的句子，并保持过去时。", "rw_write", [
        q("要点：周五地震、找到二十名幸存者、警报提前十分钟。哪一句三个要点都有？",
          "An earthquake hit on Friday, rescue teams found twenty survivors, and the warning had been sent ten minutes earlier",
          "An earthquake hit on Friday", "Twenty people arrived", "The warning was loud",
          "三个要点都要写进同一句。"),
        q("报道已经结束的救援，哪一句时态合适？", "The team rescued five people yesterday",
          "The team rescues five people yesterday", "The team will rescued yesterday", "Rescued the team yesterday five",
          "yesterday 用过去式 rescued。"),
        q("哪一句适合提醒读者去庇护所？", "Please go to the nearest shelter",
          "Please go to the naerest shelter", "Please go to the nearset shelter", "Please go to the nerest shelter",
          "祈使句 Please go to 用来提醒。"),
        q("想用定语从句说明发出警报的电台，哪一句正确？", "The station that sent the warning is local",
          "The sattion that sent the warning is local", "The station where sent the warning",
          "The station he sent the warning is local",
          "station 是物，用 that，从句里不再重复主语。"),
      ])

    V("vo_lang", "语言与文字", 10, 5,
      "认读 dialect、character、accent 和 vocabulary。",
      [("dialect", "方言"), ("character", "文字"), ("accent", "口音"), ("vocabulary", "词汇量")], "vo_world")

    V("vo_affix", "前缀和后缀", 10, 5,
      "能根据常见前后缀判断派生词的意思。",
      [("unhappy", "不快乐的"), ("careful", "仔细的"), ("writer", "作者"), ("rewrite", "重写")], "vo_form")

    G("gr_reladv", "关系副词定语从句", 10, 5,
      "能用 when、where 和 why 引导限制性定语从句。", "rel", [
        q("I remember the day ___ we met. 横线处填哪一个？", "when",
          "which", "who", "whose", "先行词 the day 表示时间，用 when。"),
        q("The village ___ I grew up is quiet. 横线处填哪一个？", "where",
          "when", "who", "whose", "先行词 the village 表示地点，用 where。"),
        q("I know the reason ___ she left. 横线处填哪一个？", "why",
          "where", "who", "whom", "先行词 the reason 表示原因，用 why。"),
        q("哪一句是正确的？", "This is the museum where we learned about characters",
          "This is the museum when we learned about characters",
          "This is the museum who we learned about characters",
          "This is the museum why we learned about characters",
          "museum 是地点，用 where。"),
      ])

    G("gr_relprep", "介词加关系代词", 10, 5,
      "能把介词放在关系代词前面，并选择 whom 或 which。", "rel", [
        q("This is the man to ___ I spoke. 横线处填哪一个？", "whom",
          "who", "whose", "where", "介词 to 提前时，指人用 whom。"),
        q("The article in ___ I found the word is short. 横线处填哪一个？", "which",
          "whom", "who", "where", "介词 in 后面指物用 which。"),
        q("哪一句是正确的？", "The student with whom I practised is kind",
          "The student with who I practised is kind", "The student with whose I practised is kind",
          "The student with where I practised is kind",
          "with 提前，指人用 whom。"),
        q("The topic about ___ we argued is dialects. 横线处填哪一个？", "which",
          "whom", "who", "when", "about 后面指事物 topic，用 which。"),
      ], "inferred")

    F("fu_lang", "谈论语言", 10, 5,
      "能交换对语言、方言和汉字的看法，并说明理由。", "fu_view", [
        q("想说汉字很有趣但难写，哪一句合适？", "Chinese characters are interesting but hard to write",
          "Chinese characters are interest but hard to write", "Chinese characters are interesting but hard to writing", "Chinese characters are interesting but hard to writes",
          "interesting but hard 用来说明看法和理由。"),
        q("想问对方会不会说家乡话，哪一句合适？", "Can you speak your local dialect",
          "Can you speak your local dailect", "Can you speak your local dialcet", "Can you speak your local dilect",
          "询问能力用 Can you speak。"),
        q("对方口音很重，你没听清，哪一句礼貌？", "Could you say that again more slowly",
          "Your accent is terrible, stop", "Could you say that again more solwly", "Could you say that again more slolwy",
          "请求对方再说一遍用 Could you say that again。"),
        q("想说明扩大词汇量需要阅读，哪一句合适？", "Reading helps you build your vocabulary",
          "Reading help you build your vocabulary", "Reading helps you build your vcoabulary", "Reading helps you build your vocabulray",
          "helps you build your vocabulary 说明阅读的作用。"),
      ])

    _l = "Mei is learning Chinese characters. She thinks the writing is difficult, but she likes reading short stories. Her vocabulary grows every week."
    R("rw_lang", "读语言学习短文", 10, 5,
      "读一段语言学习短文，概括她的困难和态度。", "rw_main", [
        q(_l + " Mei 在学什么？", "汉字", "法语语法", "马拉松", "救援", "短文写 Chinese characters。"),
        q(_l + " 她觉得什么难？", "书写", "听力教室", "跑步", "住宿", "短文写 the writing is difficult。"),
        q(_l + " 她的词汇量怎么样？", "每周都在增加", "已经停止", "完全没有", "只在周五增加",
          "短文写 grows every week。"),
        q(_l + " 她对阅读的态度是哪一种？", "喜欢读短篇故事", "讨厌所有阅读", "只担心洪水", "没有态度",
          "短文写 she likes reading short stories。"),
      ])

    P("ph_stresshs", "多音节词重音", 10, 5,
      "能判断多音节词的重音在哪一个音节。", "stress", [
        q("vocabulary 的重音在第几个音节？", "第二个音节", "第一个音节", "第四个音节", "四个音节同样重",
          "vo-CAB-u-la-ry 的重音在 cab。"),
        q("character 的重音在第几个音节？", "第一个音节", "第二个音节", "第三个音节", "没有重音",
          "CHAR-ac-ter 的重音在第一个音节。"),
        q("哪个单词的重音在第二个音节？", "disaster", "dialect", "character", "shelter",
          "dis-AS-ter 的重音在第二个音节。dialect、character、shelter 的重音在第一个音节。"),
        q("accommodation 的重音在第几个音节？", "第三个音节", "第一个音节", "第二个音节", "第五个音节",
          "a-ccom-mo-DA-tion 的重音在 da，也就是第三个音节。"),
      ])

    R("wr_lang", "写语言学习计划", 10, 5,
      "能按要点选出学习计划里的句子。", "rw_write", [
        q("要点：每天认十个汉字、读短文、周末复习词汇。哪一句三个要点都有？",
          "I will learn ten characters a day, read a short text and review vocabulary at the weekend",
          "I will learn ten characters", "I like stories", "The weekend is long",
          "三个要点都要出现。"),
        q("计划用时间从句说明做完作业再读课文，哪一句正确？", "I will read after I finish my homework",
          "I will read after I will finish my homework", "I read after I will finish tomorrow",
          "After I will finish, I read yesterday",
          "after 从句用 finish，主句用 will read。"),
        q("哪一句适合作为计划的第一句？", "My plan for learning Chinese is simple",
          "My plan for learning Chinese are simple", "My plan for laerning Chinese is simple", "My plan for learnnig Chinese is simple",
          "计划开头可以先概括 My plan is simple。"),
        q("想用定语从句介绍帮助自己的老师，哪一句正确？", "I thank the teacher who helps me every week",
          "I thank the teacher which helps me every week", "I thank the teacher where helps me",
          "I thank the teacher he helps me every week",
          "teacher 是人，用 who。"),
      ])
