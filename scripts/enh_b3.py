# -*- coding: utf-8 -*-
"""人教版（2019）必修第三册。单元名按通行目录，册次待核。"""
from enh_tx import V, P, G, F, R, q


def load():
    V("vo_fest", "节日", 12, 1,
      "认读 festival、lantern、firework 和 feast。",
      [("festival", "节日"), ("lantern", "灯笼"), ("firework", "烟花"), ("feast", "宴席")], "vo_soc")

    V("vo_custom", "庆祝方式", 12, 1,
      "认读 celebrate、origin、lunar 和 decorate。",
      [("celebrate", "庆祝"), ("origin", "起源"), ("lunar", "农历的"), ("decorate", "装饰")], "vo_soc")

    G("gr_prep2", "介词短语作状语", 12, 1,
      "能识别介词短语，并判断它表示时间、地点还是方式。", "sent", [
        q("They meet on Lunar New Year's Eve. on Lunar New Year's Eve 是什么？", "介词短语作时间状语",
          "主语", "谓语", "宾语补足语", "on 引出时间，整个介词短语作状语。"),
        q("哪一个是介词短语？", "in the town square", "the town square", "celebrate happily", "very bright",
          "in 是介词，后面接名词短语。"),
        q("She wrote the cards with great care. with great care 表示什么？", "方式",
          "主语", "节日的名称", "宾语从句", "with 短语说明书写的方式。"),
        q("哪一句里的介词短语作地点状语？", "The feast is held in the hall",
          "The feast is delicious", "Held the feast they", "Delicious is the feast very",
          "in the hall 说明举办地点。"),
      ], "inferred")

    G("gr_used3", "used to 和 be used to", 12, 1,
      "能区分 used to do 表示过去习惯，be used to doing 表示习惯于。", "tense", [
        q("我过去常放烟花，现在不放了。哪一句正确？", "I used to set off fireworks",
          "I am used to set off fireworks", "I use to set off fireworks", "I am used setting fireworks",
          "过去习惯用 used to 加动词原形。"),
        q("她已经习惯早起看灯会。哪一句正确？", "She is used to getting up early for the lantern show",
          "She is used to get up early for the lantern show", "She used to getting up early",
          "She uses to getting up early",
          "习惯于用 be used to 加动词 -ing。"),
        q("There used to ___ a temple here. 横线处填哪一个？", "be",
          "being", "been", "was", "used to 后面接动词原形 be。"),
        q("哪一句表示过去常常、现在不再如此？", "People used to make lanterns at home",
          "People are used to making lanterns at home", "Lanterns are used to light the street",
          "The street is used to lanterns",
          "used to make 表示过去的习惯。be used to making 是现在习惯于。"),
      ], "inferred")

    P("ph_pausehs", "按意群停顿", 12, 1,
      "能在较长的句子里按意群停顿，而不是每个词都断开。", "link", [
        q("On New Year's Eve, families share a feast. 斜线停顿放在哪里更自然？",
          "Eve 后面", "On 后面", "share 后面", "每个词后面",
          "时间状语 On New Year's Eve 是一个意群，后面可以停。"),
        q("哪一种读法是按意群停顿？", "the long festival / in our town",
          "the / long / festival / in / our / town", "festival in 中间必须爆破", "只在冠词后停",
          "名词短语 the long festival 可以连在一起，再在短语之间停。"),
        q("意群停顿的作用是哪一个？", "把意思相关的词读成一组",
          "让每个辅音都消失", "取消句末语调", "把句子读成一个单词",
          "停顿用来分开意群，而不是拆开每一个词。"),
        q("After the fireworks, we went home. 第一处停顿更适合在哪一个词后？", "fireworks",
          "After", "we", "went", "After the fireworks 是时间状语，读完可以停一下。"),
      ])

    F("fu_fest", "谈论节日", 12, 1,
      "能介绍节日的起源和庆祝方式，并说明自己的看法。", "fu_view", [
        q("想介绍元宵节看灯笼，哪一句合适？", "During the Lantern Festival people watch lanterns",
          "During the Lantern Fsetival people watch lanterns", "During the Lantern Festiavl people watch lanterns", "During the Lantern Fetival people watch lanterns",
          "During the Lantern Festival 用来介绍时间。"),
        q("想说自己过去常和祖父母过节，哪一句合适？", "I used to spend the festival with my grandparents",
          "I am used to spend the festival", "Used to spending I the festival", "Spend used I am",
          "过去常常用 used to spend。"),
        q("想说明这个节日的起源和月亮有关，哪一句合适？", "The origin of the festival is connected with the moon",
          "The origin of the festival is cnonected with the moon", "The origin of the festival is connecetd with the moon", "The origin of the festival is conected with the moon",
          "The origin is connected with 用来说明起源。"),
        q("想建议用灯笼装饰教室，哪一句合适？", "Let's decorate the classroom with lanterns",
          "Let's to decorate the classroom with lanterns", "Let's used to decorating", "Let's decorate the calssroom with lanterns",
          "提建议用 Let's decorate。"),
      ])

    _f = "The Lantern Festival comes after the Lunar New Year. Families used to make lanterns at home. Now many people watch fireworks in the square and then share a small feast."
    R("rw_fest", "读节日短文", 12, 1,
      "读一段节日短文，找出过去和现在的庆祝方式。", "rw_detail", [
        q(_f + " 元宵节在什么时候？", "农历新年之后", "农历新年之前", "中秋当天", "没有写时间",
          "短文写 after the Lunar New Year。"),
        q(_f + " 人们过去常做什么？", "在家做灯笼", "在广场放烟花", "去跑步", "写博客",
          "短文写 used to make lanterns at home。"),
        q(_f + " 现在许多人在广场做什么？", "看烟花", "做灯笼", "修复城墙", "保护羚羊",
          "短文写 watch fireworks in the square。"),
        q(_f + " 哪一句和短文一致？", "Families used to make lanterns at home",
          "Families are used to make lanterns", "The festival comes before the Lunar New Year",
          "Nobody shares a feast",
          "过去常常做灯笼，用 used to make。"),
      ])

    R("wr_fest", "写节日介绍", 12, 1,
      "能按要点选出节日介绍里的句子。", "rw_write", [
        q("要点：元宵节在新年后、过去做灯笼、现在看烟花。哪一句三个要点都有？",
          "The Lantern Festival comes after the New Year, people used to make lanterns, and now they watch fireworks",
          "The Lantern Festival is old", "People watch fireworks", "Lanterns are red",
          "三个要点都要出现。"),
        q("介绍里要写过去习惯，哪一句正确？", "Children used to guess lantern riddles",
          "Children are used to guess lantern riddles", "Children use to guess lantern riddles",
          "Children used to guessing lantern riddles",
          "过去习惯是 used to 加原形 guess。"),
        q("哪一句适合作为介绍的第一句？", "Let me introduce a festival in my hometown",
          "Let me introduce an festival in my hometown", "Let me itnroduce a festival in my hometown", "Let me introdcue a festival in my hometown",
          "介绍开头可以用 Let me introduce。"),
        q("哪一句的介词短语表示地点？", "We have the feast in the town square",
          "We have the feast happily", "The feast is delicious", "Have we the feast",
          "in the town square 是地点状语。"),
      ])

    V("vo_moral", "道德品质", 12, 2,
      "认读 virtue、honest、generous 和 responsible。",
      [("virtue", "美德"), ("honest", "诚实的"), ("generous", "慷慨的"), ("responsible", "有责任心的")], "vo_soc")

    V("vo_virtue", "善行", 12, 2,
      "认读 kindness、respect、duty 和 courage。",
      [("kindness", "善意"), ("respect", "尊重"), ("duty", "责任"), ("courage", "勇气")], "vo_soc")

    G("gr_toattr", "不定式作定语和宾语", 12, 2,
      "能用动词不定式作定语或宾语。", "toinf", [
        q("I have a duty ___ the guests. 表示有责任去帮助，横线处填哪一个？", "to help",
          "helping", "help", "helped", "duty 后面用 to help 作定语。"),
        q("She decided ___ the truth. 横线处填哪一个？", "to tell",
          "telling", "tell", "told", "decide 后面接 to tell 作宾语。"),
        q("哪一句是正确的？", "He is a person to respect",
          "He is a person respecting to", "He is a person respect", "He is a person to respected",
          "to respect 作定语修饰 person。"),
        q("We hope ___ more kindness. 横线处填哪一个？", "to see",
          "seeing", "see", "seen", "hope 后面接 to see 作宾语。"),
      ])

    G("gr_topurp", "不定式作目的状语", 12, 2,
      "能用 in order to 或 to do 表示目的。", "toinf", [
        q("She stayed ___ the old man. 表示为了帮助，横线处填哪一个？", "to help",
          "helping", "help", "helped", "to help 作目的状语。"),
        q("哪一句表示目的？", "He got up early in order to catch the first bus",
          "He got up early catching the bus yesterday", "In order to catch, the bus got up",
          "He got up early to caught the bus",
          "in order to catch 说明早起的目的。"),
        q("___ honest, she told the teacher. 横线处用哪一个开头？", "To be",
          "Being to", "Be", "Been", "To be honest 是目的状语，说明她为什么告诉老师。"),
        q("哪一句的不定式不是目的？", "I want to leave",
          "I came to leave a message", "I opened the door to let her in", "She studied hard to pass",
          "want to leave 里的不定式是宾语。其余三句的不定式表示目的。"),
      ])

    F("fu_moral", "评价行为", 12, 2,
      "能评价一个行为是否诚实、有责任心，并说明理由。", "fu_view", [
        q("想表扬同学诚实地交还钱包，哪一句合适？", "It was honest of you to return the wallet",
          "It not was honest of you to return the wallet", "It was hnoest of you to return the wallet", "It was honset of you to return the wallet",
          "It was honest of you to 用来表扬。"),
        q("想说自己留下来是为了帮忙，哪一句合适？", "I stayed in order to help",
          "I stayed in order to helping", "I stayed helping to in order", "Help stayed I",
          "in order to help 表示目的。"),
        q("想说明尊重别人是一种美德，哪一句合适？", "Respect for others is a virtue",
          "Respect for others is an virtue", "Rsepect for others is a virtue", "Respcet for others is a virtue",
          "is a virtue 用来下判断。"),
        q("同学承认错误，你认为这很有责任心，应回答什么？", "That was responsible of you",
          "That was rseponsible of you", "That was responsilbe of you", "That was reponsible of you",
          "That was responsible of you 用来肯定。"),
      ])

    _o = "After the trip, Mei found a wallet on the bus. She stayed there to wait for the owner. Her teacher said it was responsible of her to return it."
    R("rw_moral", "读善行短文", 12, 2,
      "读一段叙述，判断人物做了什么以及老师的评价。", "rw_main", [
        q(_o + " Mei 在公交车上发现了什么？", "一个钱包", "一只灯笼", "一枚奖牌", "一本诗集",
          "短文写 found a wallet。"),
        q(_o + " 她为什么留下？", "为了等失主", "为了坐到终点", "为了放烟花", "短文没有写原因",
          "短文写 to wait for the owner。"),
        q(_o + " 老师怎样评价她？", "归还钱包很有责任心", "她不该多管闲事", "她应该留下钱包", "老师没有评价",
          "短文写 responsible of her to return it。"),
        q(_o + " 作者的态度更接近哪一种？", "肯定 Mei 的做法", "批评 Mei 多管闲事", "只在介绍公交车", "为失主担心钱包被花掉但没有评价 Mei",
          "老师的评价是肯定的，叙述没有批评她。"),
      ])

    R("wr_moral", "写评论句", 12, 2,
      "能按要点选出评论里的句子。", "rw_write", [
        q("要点：捡到钱包、等失主、老师认为有责任心。哪一句三个要点都有？",
          "Mei found a wallet, waited for the owner, and her teacher said she was responsible",
          "Mei found a wallet", "The bus was crowded", "Teachers are busy",
          "三个要点都要出现。"),
        q("评论里用不定式表示目的，哪一句正确？", "She went back to return the wallet",
          "She went back to returned the wallet", "She went back returning the wallet yesterday's purpose",
          "To returned the wallet she went",
          "to return 用原形。"),
        q("哪一句适合作为评论的第一句？", "Mei made a choice that shows kindness",
          "Mei made a choice that show kindness", "Mei made an choice that shows kindness", "Mei made a choice that shows knidness",
          "评论可以先点出 Mei made a choice。"),
        q("哪一句的不定式作定语？", "She had a chance to help",
          "She had a chance helping to", "To help she chance had", "Help to chance a she",
          "to help 修饰 chance。"),
      ])

    V("vo_region", "多元文化", 12, 3,
      "认读 diversity、ethnic、region 和 minority。",
      [("diversity", "多样性"), ("ethnic", "民族的"), ("region", "地区"), ("minority", "少数民族")], "vo_soc")

    V("vo_ethnic", "文化习俗", 12, 3,
      "认读 costume、cuisine、belief 和 greeting。",
      [("costume", "服饰"), ("cuisine", "菜肴"), ("belief", "信仰"), ("greeting", "问候语")], "vo_soc")

    G("gr_report", "间接引语", 12, 3,
      "能把直接引语改为间接引语，并改变人称、时间和时态。", "reported", [
        q("He said, I am tired. 改成间接引语，哪一句正确？", "He said that he was tired",
          "He said that I am tired", "He said that he is tired now yesterday", "He said me tired",
          "said 是过去式，间接引语里 I am 改成 he was。"),
        q("She said, I will visit you tomorrow. 哪一句是合适的间接引语？",
          "She said that she would visit me the next day",
          "She said that she will visit you tomorrow", "She said that I would visit you tomorrow",
          "She said that she visits me tomorrow",
          "will 改为 would，tomorrow 改为 the next day，you 按听话人改成 me。"),
        q("Tom said, We saw a festival yesterday. 哪一句正确？",
          "Tom said that they had seen a festival the day before",
          "Tom said that we saw a festival yesterday", "Tom said that they saw a festival tomorrow",
          "Tom said that they have seen a festival yesterday",
          "saw 往前推一步用 had seen，yesterday 改为 the day before。"),
        q("把 May I use your pen? 转述给别人，哪一句合适？", "She asked if she could use my pen",
          "She asked if she can use your pen", "She asked that use your pen", "She said me to pen",
          "请求用 asked if，may 改为 could。"),
      ])

    G("gr_thatomit", "间接引语中的 that", 12, 3,
      "能在 said 后面省略 that，并仍然保持陈述语序。", "reported", [
        q("哪一句省略 that 后仍然正确？", "He said he was ready",
          "He said was he ready", "He said that was he ready", "He said he is ready yesterday",
          "said 后面可以省 that，但语序仍是 he was ready。"),
        q("She told me ___ she liked the costume. 横线可以填哪一个？", "that",
          "what", "which", "who", "told me 后面用 that 引导宾语从句，that 也可以省略。"),
        q("哪一句语序错了？", "He said that was the food delicious",
          "He said the food was delicious", "He said that the food was delicious", "He told me the food was delicious",
          "间接引语要用陈述语序 the food was delicious。"),
        q("They said they ___ the greeting the day before. 横线处填哪一个？", "had learned",
          "have learned", "learn", "are learning", "said 之后，原来说的 learned 要改成 had learned。"),
      ], "inferred")

    F("fu_culture", "比较文化差异", 12, 3,
      "能比较不同地区的服饰、饮食和问候，并保持礼貌。", "fu_view", [
        q("想说这个地区的服饰和自己家乡不同，哪一句合适？", "The costumes in this region are different from those in my hometown",
          "The costumes in this region are different of those in my hometown", "The costumes in this region are dfiferent from those in my hometown", "The costumes in this region are differnet from those in my hometown",
          "different from 用来比较。"),
        q("想转述导游的话 I like this cuisine，哪一句正确？", "The guide said that he liked that cuisine",
          "The guide said that I like this cuisine", "The guide said that he likes this cuisine tomorrow",
          "The guide told that like he cuisine",
          "转述时 I like 改成 he liked。"),
        q("想礼貌地询问一项信仰是否可以拍照，哪一句合适？", "Could you tell me if I may take photos",
          "Could you tell me if I may taked photos", "Could you tell me if I may to take photos", "Could you tell me if I may take pohtos",
          "礼貌询问用 Could you tell me if。"),
        q("想说明问候语不一样并不代表不尊重，哪一句合适？", "A different greeting does not mean less respect",
          "A different greeting doe not mean less respect", "A dfiferent greeting does not mean less respect", "A differnet greeting does not mean less respect",
          "does not mean 用来澄清看法。"),
      ])

    _c = "The guide said that the costumes were made by a local minority group. He also said they had learned the dance the year before. Visitors may watch, but they should ask before taking photos."
    R("rw_culture", "读文化短文", 12, 3,
      "读一段文化介绍，找出服饰的制作者和拍照规则。", "rw_detail", [
        q(_c + " 服饰是谁做的？", "当地的一个少数民族群体", "导游本人", "游客", "短文没有说",
          "短文写 a local minority group。"),
        q(_c + " 舞蹈是什么时候学的？", "前一年", "当天", "下一年", "十年后", "短文写 the year before。"),
        q(_c + " 游客拍照前应该做什么？", "先询问", "直接拍摄", "穿上服饰", "离开", "短文写 ask before taking photos。"),
        q(_c + " 哪一句和短文一致？", "Visitors should ask before taking photos",
          "Visitors must take photos", "The guide made the costumes", "The dance will be learned next year",
          "规则是先问再拍。"),
      ])

    R("wr_culture", "写文化笔记", 12, 3,
      "能按要点选出文化笔记里的句子，并使用间接引语。", "rw_write", [
        q("要点：服饰由当地群体制作、舞蹈前一年学会、拍照前要问。哪一句三个要点都有？",
          "The costumes were made by a local group, they had learned the dance the year before, and visitors should ask before taking photos",
          "The costumes are colourful", "The dance is long", "Visitors like photos",
          "三个要点都要出现。"),
        q("把导游的话 We made these costumes 写进笔记，哪一句正确？",
          "The guide said that they had made those costumes",
          "The guide said that we made these costumes", "The guide said that they make these costumes tomorrow",
          "The guide said that made they costumes",
          "we made 在 said 之后改成 they had made。"),
        q("哪一句适合作为笔记的第一句？", "Today I learned about a local ethnic group",
          "Today I learned about an local ethnic group", "Today I laerned about a local ethnic group", "Today I learend about a local ethnic group",
          "笔记开头可以写 Today I learned about。"),
        q("哪一句省略 that 后仍然正确？", "He said the food was special",
          "He said was the food special", "He said that was the food special", "He said the food is special yesterday",
          "省掉 that 以后仍用陈述语序 the food was special。"),
      ])

    V("vo_space", "太空探索", 12, 4,
      "认读 astronaut、orbit、rocket 和 universe。",
      [("astronaut", "宇航员"), ("orbit", "轨道"), ("rocket", "火箭"), ("universe", "宇宙")], "vo_soc")

    V("vo_planet", "航天", 12, 4,
      "认读 planet、satellite、gravity 和 mission。",
      [("planet", "行星"), ("satellite", "卫星"), ("gravity", "重力"), ("mission", "任务")], "vo_soc")

    G("gr_toform", "不定式作主语和表语", 12, 4,
      "能用不定式或 it 作形式主语，并让不定式作表语。", "toinf", [
        q("___ a rocket is difficult. 用不定式作主语，横线处填哪一个？", "To launch",
          "Launch", "Launching to", "Launched", "句首用 To launch 作主语。"),
        q("哪一句用 it 作形式主语？", "It is hard to leave the planet",
          "To leave the planet is hard it", "Hard is to leave it the planet", "It hard to leave",
          "It 是形式主语，真正的主语是 to leave the planet。"),
        q("Her dream is ___ an astronaut. 横线处填哪一个？", "to become",
          "becoming to", "become", "became", "dream 的表语可以用 to become。"),
        q("哪一句是正确的？", "It takes years to train for a mission",
          "It takes years train for a mission", "It takes years to trained for a mission",
          "Takes it years to train for a mission",
          "It takes years to train 里的 to train 是真正的主语。"),
      ])

    G("gr_bare", "省略 to 的不定式", 12, 4,
      "能在 make、let、see、hear 等后面省略 to，并知道被动时要还原。", "toinf", [
        q("The teacher made us ___ the report. 横线处填哪一个？", "rewrite",
          "to rewrite", "rewriting", "rewrote", "make 加宾语后面的不定式省略 to。"),
        q("哪一句是正确的？", "We were made to check the data",
          "We were made check the data", "We were made checking the data", "We made to were check",
          "主动 make sb do，被动要还原 to：were made to check。"),
        q("I saw the rocket ___. 表示看见火箭升空，且不带 to，横线处填哪一个？", "rise",
          "to rise", "rose", "risen", "see 后面作宾补的不定式省略 to，用 rise。"),
        q("哪一句必须保留 to？", "It is important to wear a helmet",
          "Let me wear a helmet", "I heard her sing", "They made him wait",
          "important 后面的不定式不能省略 to。let、hear、make 后面可以省略。"),
      ], "inferred")

    F("fu_space", "谈论航天计划", 12, 4,
      "能说出已经安排或打算进行的航天任务。", "fu_plan", [
        q("想说成为宇航员很难，哪一句合适？", "It is difficult to become an astronaut",
          "Difficult to become is it an astronaut", "Become an astronaut difficult", "It difficult become",
          "It is difficult to become 用 it 作形式主语。"),
        q("想说老师让我们查卫星资料，哪一句合适？", "The teacher made us check the satellite data",
          "The teacher made us to check the satellite data", "The teacher made us checking data",
          "Made the teacher us to check",
          "make us 后面用动词原形 check。"),
        q("想说明这次任务是进入轨道，哪一句合适？", "The mission is to enter orbit",
          "The mission is enter to orbit", "Orbit is to mission", "To enter orbit the mission is it",
          "表语可以用 to enter orbit。"),
        q("想邀请同学一起看火箭发射，哪一句合适？", "Shall we watch the rocket launch",
          "Shall we watch the rcoket launch", "Shall we watch the rocekt launch", "We watched tomorrow",
          "邀请用 Shall we watch。"),
      ])

    _s = "It is not easy to become an astronaut. The next mission is to test a new satellite. Our teacher made us read a short article about gravity."
    R("rw_space", "读航天短文", 12, 4,
      "读一段航天短文，概括任务和老师的要求。", "rw_main", [
        q(_s + " 成为宇航员容易吗？", "不容易", "非常容易", "短文没有说", "只有儿童容易",
          "短文写 It is not easy。"),
        q(_s + " 下一次任务是什么？", "测试一颗新卫星", "登陆太阳", "取消重力", "修理灯笼",
          "短文写 to test a new satellite。"),
        q(_s + " 老师让学生做什么？", "读一篇关于重力的短文", "发射火箭", "省略头盔", "写密码",
          "短文写 made us read a short article about gravity。"),
        q(_s + " 哪一句和短文一致？", "The teacher made the students read an article",
          "The teacher made the students to read an article", "Becoming an astronaut is easy",
          "The mission is to close the school",
          "make us read 不带 to。"),
      ])

    R("wr_space", "写航天笔记", 12, 4,
      "能按要点选出笔记里的句子。", "rw_write", [
        q("要点：成为宇航员不容易、任务是测试卫星、老师让我们阅读。哪一句三个要点都有？",
          "It is not easy to become an astronaut, the mission is to test a satellite, and the teacher made us read",
          "It is not easy", "Satellites are useful", "We like space",
          "三个要点都要出现。"),
        q("笔记里用形式主语，哪一句正确？", "It takes courage to join a mission",
          "It takes courage join a mission", "Takes it courage to join", "Courage takes to join it a mission",
          "It takes courage to join 才完整。"),
        q("哪一句适合作为笔记标题？", "What I learned about the mission",
          "What I laerned about the mission", "What I learend about the mission", "What I lerned about the mission",
          "标题可以是 What I learned about the mission。"),
        q("被动句里要还原 to，哪一句正确？", "We were made to rewrite the notes",
          "We were made rewrite the notes", "We were made rewriting the notes", "Were made we rewrite to",
          "were made 后面用 to rewrite。"),
      ])

    V("vo_money", "金钱与价值", 12, 5,
      "认读 value、wealth、loan 和 bargain。",
      [("value", "价值"), ("wealth", "财富"), ("loan", "贷款"), ("bargain", "便宜货")], "vo_soc")

    V("vo_worth", "消费选择", 12, 5,
      "认读 worth、budget、debt 和 charity。",
      [("worth", "值得的"), ("budget", "预算"), ("debt", "债务"), ("charity", "慈善机构")], "vo_soc")

    G("gr_modperf", "情态动词加 have done", 12, 5,
      "能用 must、could、should 加 have done 表示对过去的判断或后悔。", "modal", [
        q("包已经不在桌上。她当时一定是带走了。哪一句合适？", "She must have taken it",
          "She must take it", "She must has taken it", "She must had taken it",
          "对过去的肯定推测用 must have taken。"),
        q("他当时本可以求助，却没有。哪一句合适？", "He could have asked for help",
          "He could ask for help yesterday now", "He could has asked for help", "He can have asked tomorrow",
          "本来可以做却没做，用 could have asked。"),
        q("你当时不该借那么多钱。哪一句合适？", "You should not have borrowed so much",
          "You should not borrowed so much", "You should not have borrow so much",
          "You must not to have borrowed",
          "本不该做用 should not have borrowed。"),
        q("哪一句表示对过去没有把握的推测？", "The wallet could have been lost on the bus",
          "The wallet must be on the bus now", "The wallet can lost", "The wallet should loses",
          "could have been lost 是对过去可能性的推测。"),
      ])

    G("gr_wouldrather", "would rather 的虚拟", 12, 5,
      "能用 would rather 加过去式表示与现在事实相反的愿望。", "modal", [
        q("我宁愿你现在把真相告诉我。哪一句正确？", "I would rather you told me the truth now",
          "I would rather you tell me the truth now", "I would rather you to tell me",
          "I would rather you had tell me now",
          "would rather 从句表示与现在相反时用过去式 told。"),
        q("哪一句表示宁愿自己当时没买？", "I would rather I had not bought it",
          "I would rather I did not bought it", "I would rather not buying it yesterday",
          "I would rather I buy it not",
          "与过去事实相反用 had not bought。"),
        q("She would rather ___ at home than go out. 横线处填哪一个？", "stay",
          "staying", "to stay", "stayed", "would rather 后面直接接原形时用 stay than go。"),
        q("哪一句用了从句里的过去式？", "I would rather you came tomorrow",
          "I would rather to come tomorrow", "I would rather coming tomorrow", "I rather would you to come",
          "you came 是从句里的过去式，表示愿望。"),
      ], "inferred")

    F("fu_money", "谈论价值和消费", 12, 5,
      "能就花钱、预算和慈善交换看法并说明理由。", "fu_view", [
        q("想说这件便宜货不值得买，哪一句合适？", "This bargain is not worth buying",
          "This bargain is not worth to buy", "Worth buying is not this", "This bragain is not worth buying",
          "worth 后面接 buying。"),
        q("想推测钱包一定是落在公交车上了，哪一句合适？", "You must have left the wallet on the bus",
          "You must leave the wallet on the bus yesterday", "You must had left the wallet",
          "Must have you left the wallet",
          "对过去的推测用 must have left。"),
        q("想建议先做预算再借钱，哪一句合适？", "You should make a budget before you take a loan",
          "You should have make a budget tomorrow", "You should maked a budget before you take a loan", "You should to make a budget before you take a loan",
          "建议用 You should make a budget。"),
        q("想说明把一部分钱捐给慈善更有价值，哪一句合适？", "Giving some money to charity is of greater value",
          "Giving some money to cahrity is of greater value", "Giving some money to chartiy is of greater value", "Giving some money to chrity is of greater value",
          "is of greater value 用来比较价值。"),
      ])

    _y = "Tom bought a coat because it looked like a bargain. Later he found a hole in it. His sister said he should have checked the pockets and kept to his budget."
    R("rw_money", "读消费短文", 12, 5,
      "读一段消费经历，找出姐姐的建议和作者没有直接说出的教训。", "rw_detail", [
        q(_y + " Tom 为什么买那件外套？", "它看起来像便宜货", "它很贵", "姐姐要求他买", "衣服没有洞",
          "短文写 it looked like a bargain。"),
        q(_y + " 后来他发现了什么？", "一个洞", "一笔贷款", "一件奖牌", "一张车票", "短文写 a hole。"),
        q(_y + " 姐姐认为他当时应该做什么？", "检查口袋并坚持预算", "再买一件", "把衣服捐掉", "什么都不做",
          "短文写 should have checked the pockets and kept to his budget。"),
        q(_y + " 哪一句和短文一致？", "He should have checked the coat",
          "He must check the coat tomorrow in the past", "The coat had no hole", "His sister bought the coat",
          "should have checked 表示当时该做却没做。"),
      ])

    R("wr_money", "写消费反思", 12, 5,
      "能按要点选出反思里的句子。", "rw_write", [
        q("要点：看起来便宜、后来有洞、当时该检查。哪一句三个要点都有？",
          "It looked like a bargain, but there was a hole, and I should have checked it",
          "It looked cheap", "There was a hole", "Budgets are useful",
          "三个要点都要出现。"),
        q("反思里表示当时不该借款，哪一句正确？", "I should not have taken the loan",
          "I should not took the loan", "I should not have take the loan", "I must not to have take",
          "should not have taken 表示本不该借。"),
        q("哪一句适合作为反思的第一句？", "I learned a lesson about value",
          "I learned an lesson about value", "I laerned a lesson about value", "I learend a lesson about value",
          "反思开头可以写 I learned a lesson。"),
        q("宁愿当时没买，哪一句正确？", "I would rather I had not bought the coat",
          "I would rather I did not bought the coat", "I would rather not buying the coat yesterday",
          "Rather I would bought not",
          "与过去事实相反用 had not bought。"),
      ])
