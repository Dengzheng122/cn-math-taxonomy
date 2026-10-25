# -*- coding: utf-8 -*-
"""人教版（2019）必修第二册。单元名按通行目录，册次待核。"""
from enh_tx import V, P, G, F, R, q


def load():
    V("vo_heritage", "文化遗产", 11, 1,
      "认读 heritage、temple、preserve 和 relic。",
      [("heritage", "遗产"), ("preserve", "保护"), ("relic", "遗物"), ("dynasty", "朝代")], "vo_soc")

    V("vo_protect", "保护文物", 11, 1,
      "认读 restore、damage、ancient 和 site。",
      [("restore", "修复"), ("damage", "损坏"), ("ancient", "古代的"), ("site", "遗址")], "vo_soc")

    G("gr_nonrest", "非限制性定语从句", 11, 1,
      "能用逗号加上 who 或 which 补充说明，而不用 that。", "rel", [
        q("My brother, ___ lives in Luoyang, is a guide. 横线处填哪一个？", "who",
          "that", "which", "whom", "非限制性定语从句里，指人作主语用 who，不用 that。"),
        q("The temple, ___ was built in the Tang Dynasty, is famous. 横线处填哪一个？", "which",
          "that", "who", "where", "非限制性定语从句指物用 which，不用 that。"),
        q("哪一句是正确的？", "The site, which we visited, is ancient",
          "The site, that we visited, is ancient", "The site which, we visited is ancient",
          "The site, who we visited, is ancient",
          "逗号后面的非限制性从句用 which。"),
        q("非限制性定语从句去掉以后，主句还成立吗？", "主句仍然成立，从句只是补充",
          "主句不能成立", "从句变成主语", "逗号必须删掉才正确",
          "非限制性从句是附加说明，去掉后主句意思仍然完整。"),
      ])

    G("gr_whichsent", "which 指代整句", 11, 1,
      "能用 which 指代前面整个句子，并和限制性定语从句区分。", "rel", [
        q("He missed the train, ___ made him late. 横线处填哪一个？", "which",
          "that", "who", "what", "which 指代 missed the train 整件事。"),
        q("哪一句里的 which 指代前面整句？", "She forgot the ticket, which was a pity",
          "The ticket which she forgot was blue", "The boy who forgot it is Tom",
          "This is the train which was late",
          "逗号后的 which 指忘记车票这件事。"),
        q("They restored the site, ___ took three years. 横线处填哪一个？", "which",
          "who", "that", "where", "which 指代修复遗址这件事。"),
        q("哪一句不能把 that 换成指代整句的 which？", "The relic that we saw is small",
          "Rain came, which stopped the work", "He was late, which annoyed the guide",
          "The bridge fell, which shocked everyone",
          "The relic that we saw 里的 that 指 relic，不是整句。"),
      ], "inferred")

    F("fu_heritage", "讨论保护遗产", 11, 1,
      "能就保护文化遗产交换看法并说明理由。", "fu_view", [
        q("想说古庙应该被保护，哪一句合适？", "I think the ancient temple should be preserved",
          "I thinks the ancient temple should be preserved", "I not think the ancient temple should be preserved", "I think the ancient temple should be perserved",
          "should be preserved 用来表达应该保护。"),
        q("想说明损坏来自游客乱刻，哪一句合适？", "The damage comes from visitors cutting the walls",
          "Damage is a coach", "The damage come from visitors cutting the walls", "The damage comes from vsiitors cutting the walls",
          "comes from 用来说明原因。"),
        q("对方认为修复太贵，你部分同意，应回答什么？", "I see your point, but the site is worth it",
          "I see your piont, but the site is worth it", "I see your poit, but the site is worth it", "I see your point, but the site is worh it",
          "部分同意可以说 I see your point, but。"),
        q("想建议设立参观规则，哪一句合适？", "We could make rules for visitors",
          "We could maked rules for visitors", "We could to make rules for visitors", "We could make rules for vsiitors",
          "提建议用 We could make rules。"),
      ])

    _h = "The old city wall is part of the local heritage. Workers are restoring a gate that was damaged by rain. Visitors may take photos but must not touch the relics."
    R("rw_heritage", "读遗产说明", 11, 1,
      "读一段遗产说明，概括作者是在介绍规则还是在反对保护。", "rw_main", [
        q(_h + " 城墙属于什么？", "当地的遗产", "一座体育场", "一封邮件", "一场马拉松", "短文写 local heritage。"),
        q(_h + " 大门为什么在修复？", "被雨水损坏了", "游客买下了它", "它是新建的", "没有大门",
          "短文写 damaged by rain。"),
        q(_h + " 游客不能做什么？", "触摸遗物", "拍照", "阅读说明", "站在门外", "短文写 must not touch the relics。"),
        q(_h + " 这段文字主要在做什么？", "说明遗产现状和参观规则", "反对保护城墙", "招聘教练", "报道一场洪水",
          "短文在介绍修复和规则，没有反对保护。"),
      ])

    R("wr_heritage", "写保护建议", 11, 1,
      "能按要点选出建议短文中的句子。", "rw_write", [
        q("要点：城墙是遗产、雨水造成损坏、游客不要触摸。哪一句三个要点都有？",
          "The wall is heritage, rain damaged it, and visitors must not touch the relics",
          "The wall is heritage", "Rain is wet", "Visitors like photos",
          "三个要点都要出现。"),
        q("想用非限制性定语从句补充城墙的年代，哪一句正确？",
          "The wall, which dates from the Ming Dynasty, needs care",
          "The wall, that dates from the Ming Dynasty, needs care",
          "The wall which, dates from the Ming Dynasty needs care",
          "The wall, who dates from the Ming Dynasty, needs care",
          "非限制性从句用 which，不用 that。"),
        q("哪一句适合作为建议的第一句？", "I suggest we protect the old city wall",
          "I sgugest we protect the old city wall", "I suggset we protect the old city wall", "I sugest we protect the old city wall",
          "建议开头可以用 I suggest。"),
        q("哪一句正确使用了 which 指代整句？", "Some people carve names, which damages the stone",
          "The stone which people carve is soft", "People who carve names are few",
          "This is the wall which is old",
          "逗号后的 which 指刻字这件事。"),
      ])

    V("vo_wild", "野生动物", 11, 2,
      "认读 wildlife、species、habitat 和 extinct。",
      [("wildlife", "野生动物"), ("species", "物种"), ("habitat", "栖息地"), ("extinct", "灭绝的")], "vo_soc")

    V("vo_habitat", "保护栖息地", 11, 2,
      "认读 reserve、hunter、endangered 和 plain。",
      [("reserve", "保护区"), ("hunter", "捕猎者"), ("endangered", "濒危的"), ("plain", "平原")], "vo_soc")

    G("gr_passcont", "现在进行时的被动语态", 11, 2,
      "能用 am、is、are 加 being 加过去分词表示进行时被动。", "passive", [
        q("The reserve ___ now. 表示正在被清理，横线处填哪一个？", "is being cleaned",
          "is cleaning", "is cleaned", "was being cleaned", "现在进行时被动是 is being 加过去分词。"),
        q("哪一句是现在进行时的被动？", "The antelopes are being protected",
          "The antelopes are protecting", "The antelopes were protected", "The antelopes have protected",
          "are being protected 是正在被保护。"),
        q("A new plain ___ for the birds this week. 横线处填哪一个？", "is being prepared",
          "is preparing", "prepares", "is been prepared", "主语是物，正在被准备，用 is being prepared。"),
        q("哪一句的语态用错了？", "The habitat is being destroy",
          "The habitat is being destroyed", "Workers are destroying the old fence", "The fence is being repaired",
          "being 后面要用过去分词 destroyed，不能用原形 destroy。"),
      ])

    G("gr_ppvsing", "过去分词和动词 -ing", 11, 2,
      "能根据主动还是被动选择动词 -ing 或过去分词。", "pp", [
        q("The story is ___ (interest). 表示故事令人感兴趣，填哪一个？", "interesting",
          "interested", "interest", "interests", "物作主语、说明性质用 interesting。"),
        q("The children are ___ in whales. 横线处填哪一个？", "interested",
          "interesting", "interest", "interests", "人感到有兴趣用 interested。"),
        q("哪一句是正确的？", "We are worried about the endangered species",
          "We are worrying species about the endangered", "The species is worried to us",
          "The news is worried",
          "人作主语用 worried。消息令人担心要用 worrying。"),
        q("a ___ species 表示令人担心的物种，横线处填哪一个？", "worrying",
          "worried", "worry", "worries", "修饰物种、说明它让人担心，用 worrying。"),
      ], "inferred")

    F("fu_protect", "讨论动物保护", 11, 2,
      "能说明保护野生动物的理由，并回应不同看法。", "fu_view", [
        q("想说藏羚羊正在被保护，哪一句合适？", "The antelopes are being protected in the reserve",
          "The antelopes are protecting the reserve", "The atnelopes are being protected in the reserve", "The anteloeps are being protected in the reserve",
          "正在被保护用 are being protected。"),
        q("想说明猎人才是危险的来源，哪一句合适？", "Hunters are the main danger to this species",
          "Hunters is the main danger to this species", "Hnuters are the main danger to this species", "Huntres are the main danger to this species",
          "are the main danger 用来说明原因。"),
        q("对方说保护区没有用，你不同意，应回答什么？", "I don't agree, because the numbers are rising",
          "I don't agree, because the numbers are rise", "I don't agree, because the nmubers are rising", "I don't agree, because the numbres are rising",
          "不同意要加上 because 说明理由。"),
        q("想建议人们不要购买野生动物制品，哪一句合适？", "Please do not buy products made from wild animals",
          "Please do not buy porducts made from wild animals", "Please do not buy produtcs made from wild animals", "Please do not buy prducts made from wild animals",
          "祈使句 Please do not buy 用来建议。"),
      ])

    _a = "The Tibetan antelope was once endangered. Now the animals are being protected on the plain. Visitors are interested in the reserve but must not feed the wildlife."
    R("rw_wild", "读动物保护短文", 11, 2,
      "读一段动物保护短文，找出过去的状况和现在的措施。", "rw_detail", [
        q(_a + " 藏羚羊曾经处于什么状态？", "濒危", "已经灭绝", "数量过多", "生活在城市",
          "短文写 was once endangered。"),
        q(_a + " 它们现在怎么样？", "正在平原上被保护", "正在被猎杀", "已经离开保护区", "在喂食游客",
          "短文写 are being protected on the plain。"),
        q(_a + " 游客不能做什么？", "给野生动物喂食", "对保护区感兴趣", "阅读说明", "站在外面",
          "短文写 must not feed the wildlife。"),
        q(_a + " 哪一句和短文一致？", "Visitors must not feed the wildlife",
          "The antelope is extinct", "The animals are protecting the visitors", "The plain has no reserve",
          "短文说的是游客不能喂食。"),
      ])

    R("wr_wild", "写保护海报句", 11, 2,
      "能按要点选出保护海报上的句子。", "rw_write", [
        q("要点：物种曾经濒危、现在正在被保护、不要喂食。哪一句三个要点都有？",
          "This species was endangered, it is being protected now, and please do not feed it",
          "This species was endangered", "Please do not feed it", "The plain is wide",
          "三个要点都要出现。"),
        q("海报要用进行时被动说明正在进行的工作，哪一句符合？", "A new fence is being built",
          "A new fence is building", "A new fence built being", "A new fence is been built",
          "is being built 才是进行时被动。"),
        q("哪一句适合作为海报标题？", "Protect the endangered antelope",
          "Protect the ednangered antelope", "Protect the endangeerd antelope", "Protect the enangered antelope",
          "标题可以用祈使句 Protect。"),
        q("哪一句正确区分了 interested 和 interesting？", "Children are interested in the interesting film",
          "Children are interesting in the interested film", "The film is interested in children",
          "Children are interest in the film",
          "人用 interested，影片用 interesting。"),
      ])

    V("vo_net", "互联网", 11, 3,
      "认读 Internet、blog、comment 和 identity。",
      [("Internet", "互联网"), ("blog", "博客"), ("comment", "评论"), ("identity", "身份")], "vo_world")

    V("vo_online", "在线行为", 11, 3,
      "认读 online、privacy、password 和 post。",
      [("online", "在线的"), ("privacy", "隐私"), ("password", "密码"), ("post", "发布")], "vo_world")

    G("gr_passperf", "现在完成时的被动语态", 11, 3,
      "能用 have 或 has 加 been 加过去分词。", "passive", [
        q("The password ___ . 表示已经被更改，横线处填哪一个？", "has been changed",
          "has changed", "has being changed", "was being changed", "现在完成时被动是 has been 加过去分词。"),
        q("哪一句是现在完成时的被动？", "Two comments have been deleted",
          "Two comments have deleted", "Two comments are deleting", "Two comments deleted been",
          "have been deleted 表示已经被删除。"),
        q("My blog ___ by many students since Monday. 横线处填哪一个？", "has been read",
          "has read", "is being read", "have been read", "blog 是单数，完成时被动用 has been read。"),
        q("哪一句是正确的？", "The post has been shared online",
          "The post has been share online", "The post has being shared online", "The post have been shared online",
          "been 后面用过去分词 shared，单数主语用 has。"),
      ])

    G("gr_since", "since 与现在完成时", 11, 3,
      "能在 since 引出的时间后使用现在完成时。", "tense", [
        q("I ___ this blog since 2020. 横线处填哪一个？", "have kept",
          "kept", "keep", "am keeping", "since 2020 要和现在完成时 have kept 搭配。"),
        q("哪一句是正确的？", "She has used the same password since May",
          "She used the same password since May", "She uses the same password since May",
          "She has used the same password since three days",
          "since 加时间点用现在完成时。since three days 缺少 ago，不作为正确项。"),
        q("The app ___ many times since it was posted. 横线处填哪一个？", "has been updated",
          "was updated", "is updated", "updated", "since 从句说明起点，主句用完成时被动。"),
        q("since Monday 更适合和哪一种时态一起用？", "现在完成时", "一般过去时单独使用", "现在进行时表安排", "一般现在时表习惯",
          "since 表示从过去持续到现在，用现在完成时。"),
      ], "inferred")

    F("fu_net", "谈论网络安全", 11, 3,
      "能就上网习惯提出建议，并说明隐私的理由。", "fu_plan", [
        q("想提醒同学不要公开密码，哪一句合适？", "Never post your password online",
          "Post your password to everyone", "Never post your psasword online", "Never post your passwrod online",
          "提醒用 Never post your password。"),
        q("想说评论已经被删除，哪一句合适？", "The rude comment has been deleted",
          "The rude comment has deleted the blog", "The rude cmoment has been deleted", "The rude commnet has been deleted",
          "已经被删除用 has been deleted。"),
        q("对方问为什么要用昵称，你说明理由，哪一句合适？", "I use a nickname to protect my privacy",
          "I use a nickname to protecting my privacy", "I use a nickname to protects my privacy", "I use an nickname to protect my privacy",
          "to protect my privacy 说明目的。"),
        q("想建议对方先核对身份再加好友，哪一句合适？", "Check the person's identity before you add them",
          "Check the person's iedntity before you add them", "Check the person's identtiy before you add them", "Check the person's idntity before you add them",
          "提建议用祈使句 Check。"),
      ])

    _i = "Since March, Lin's class blog has been read by students in three schools. One unkind comment has been deleted. Lin never posts his real name or password."
    R("rw_net", "读网络短文", 11, 3,
      "读一段网络使用短文，判断作者是在说明事实还是在赞美粗鲁评论。", "rw_main", [
        q(_i + " 博客从什么时候开始被阅读？", "三月以来", "昨天", "三年前的一天", "没有时间",
          "短文写 Since March。"),
        q(_i + " 不友善的评论怎么样了？", "已经被删除", "被置顶", "还在增加", "变成了密码",
          "短文写 has been deleted。"),
        q(_i + " Lin 不发布什么？", "真名和密码", "班级博客", "学校名称", "所有图片",
          "短文写 never posts his real name or password。"),
        q(_i + " 作者对那条不友善评论的态度是哪一种？", "把它删掉，而不是赞成它",
          "认为它很有趣所以保留", "没有提到评论", "鼓励更多这样的评论",
          "评论被删除，说明作者不赞成它。"),
      ])

    R("wr_net", "写网络提醒", 11, 3,
      "能按要点选出网络提醒里的句子。", "rw_write", [
        q("要点：不发密码、保护隐私、粗鲁评论已删除。哪一句三个要点都有？",
          "Do not post your password, protect your privacy, and the rude comment has been deleted",
          "Do not post your password", "Privacy matters", "The blog is new",
          "三个要点都要出现。"),
        q("提醒要从三月写到现在，哪一句时态合适？", "The rule has been used since March",
          "The rule was used since March", "The rule is used since March", "The rule has used since March",
          "since March 用现在完成时，规则是被使用，用 has been used。"),
        q("哪一句适合作为提醒的标题？", "Keep your identity safe online",
          "Keep your iedntity safe online", "Keep your identtiy safe online", "Keep your idntity safe online",
          "标题可以是 Keep your identity safe online。"),
        q("哪一句是正确的完成时被动？", "The photo has been removed",
          "The photo has been remove", "The photo has being removed", "The photo have been removed",
          "has been 加过去分词 removed。"),
      ])

    V("vo_hist", "历史传统", 11, 4,
      "认读 tradition、castle、battle 和 kingdom。",
      [("tradition", "传统"), ("battle", "战役"), ("kingdom", "王国"), ("custom", "习俗")], "vo_soc")

    V("vo_trad", "节日习俗", 11, 4,
      "认读 ancestor、honour、gathering 和 poem。",
      [("ancestor", "祖先"), ("honour", "纪念"), ("gathering", "聚会"), ("poem", "诗")], "vo_soc")

    G("gr_ppattr", "过去分词作定语和表语", 11, 4,
      "能用过去分词作定语或表语，表示被动或完成。", "pp", [
        q("a ___ castle 表示被毁坏的城堡，横线处填哪一个？", "ruined",
          "ruining", "ruin", "ruins", "被毁坏的城堡用过去分词 ruined 作定语。"),
        q("The gate is ___. 表示大门关着，横线处填哪一个？", "closed",
          "closing", "close", "closes", "状态用过去分词 closed 作表语。"),
        q("哪一句是正确的？", "The poem written by Li Bai is famous",
          "The poem writing by Li Bai is famous", "The poem wrote by Li Bai is famous",
          "The poem write by Li Bai is famous",
          "written by Li Bai 作定语，修饰 poem。"),
        q("The visitors were ___ by the old custom. 横线处填哪一个？", "surprised",
          "surprising", "surprise", "surprises", "人感到惊讶用 surprised 作表语。"),
      ])

    G("gr_ppcomp", "过去分词作宾补", 11, 4,
      "能用过去分词作宾语补足语，表示宾语被怎样。", "pp", [
        q("I heard my name ___. 表示名字被叫到，横线处填哪一个？", "called",
          "calling", "call", "to calling", "name 是被叫的，宾补用 called。"),
        q("She found the window ___. 表示窗户被打破了，横线处填哪一个？", "broken",
          "breaking", "broke", "break", "window 是被打破的，用 broken。"),
        q("哪一句是正确的？", "We saw the hall decorated with poems",
          "We saw the hall decorating with poems", "We saw the hall decorate with poems",
          "We saw the hall to decorated with poems",
          "hall 是被装饰的，宾补用 decorated。"),
        q("They kept the tradition ___. 表示传统被保存，横线处填哪一个？", "preserved",
          "preserving", "preserve", "to preserving", "tradition 是被保存的对象，用 preserved。"),
      ])

    F("fu_hist", "谈论传统", 11, 4,
      "能描述一项传统，并说明自己是否赞成保留它。", "fu_view", [
        q("想介绍清明纪念祖先的习俗，哪一句合适？", "On Qingming people honour their ancestors",
          "On Qingming people honour their acnestors", "On Qingming people honour their ancestros", "On Qingming people honour their anestors",
          "honour their ancestors 用来介绍习俗。"),
        q("想说这首诗是李白写的，哪一句合适？", "This is a poem written by Li Bai",
          "This is a poem writing by Li Bai", "This is a poem wrote by Li Bai", "Poem is written Li Bai by",
          "written by 作定语。"),
        q("想表示自己支持保留这项聚会，哪一句合适？", "I support keeping this gathering",
          "I support eating the tradition", "I support keeping this gtahering", "I support keeping this gathernig",
          "I support keeping 用来表态。"),
        q("对方问你有没有看见被装饰的大厅，哪一句回答正确？", "Yes, I saw the hall decorated with flowers",
          "Yes, I saw the hall decorating with flowers", "Yes, I saw the hall decorate flowers",
          "Yes, decorated saw I the hall",
          "宾补用 decorated，表示大厅被装饰。"),
      ])

    _d = "During the festival, families hold a gathering to honour their ancestors. A poem written by a local teacher is read aloud. Last year the old hall was decorated with paper flowers."
    R("rw_hist", "读传统短文", 11, 4,
      "读一段传统介绍，找出活动目的和大厅的装饰。", "rw_detail", [
        q(_d + " 聚会是为了什么？", "纪念祖先", "庆祝比赛", "修复城墙", "发布博客", "短文写 honour their ancestors。"),
        q(_d + " 诗是谁写的？", "一位当地老师", "李白", "游客", "没有作者", "短文写 written by a local teacher。"),
        q(_d + " 去年大厅怎么样？", "用纸花装饰了", "被雨水冲毁", "改成了体育场", "没有大厅",
          "短文写 decorated with paper flowers。"),
        q(_d + " 哪一句和短文一致？", "Families honour their ancestors",
          "The poem was written by Li Bai", "The hall is a new stadium", "There is no gathering",
          "短文说的是纪念祖先。"),
      ])

    R("wr_hist", "写传统介绍", 11, 4,
      "能按要点选出介绍传统的句子。", "rw_write", [
        q("要点：聚会纪念祖先、朗读当地老师的诗、大厅用纸花装饰。哪一句三个要点都有？",
          "Families gather to honour ancestors, read a poem written by a local teacher, and the hall is decorated with paper flowers",
          "Families gather", "The poem is short", "Paper flowers are red",
          "三个要点都要出现。"),
        q("想用过去分词作定语，哪一句正确？", "The custom kept by the village is old",
          "The custom keeping by the village is old", "The custom keep by the village is old",
          "The custom to kept by the village is old",
          "kept by the village 修饰 custom。"),
        q("哪一句适合作为介绍的开头？", "Let me tell you about a local tradition",
          "Let me tell you about an local tradition", "Let me tell you about a local tardition", "Let me tell you about a local traditoin",
          "介绍开头可以用 Let me tell you about。"),
        q("哪一句的宾补是正确的？", "We found the door closed",
          "We found the door closing by nobody", "We found the door close", "We found closed the door was",
          "door 是被关上的，宾补用 closed。"),
      ])

    V("vo_musicb", "音乐", 11, 5,
      "认读 classical、band、perform 和 audience。",
      [("classical", "古典的"), ("band", "乐队"), ("perform", "表演"), ("audience", "听众")], "vo_world")

    V("vo_band", "演奏", 11, 5,
      "认读 instrument、stage、rhythm 和 composer。",
      [("instrument", "乐器"), ("stage", "舞台"), ("rhythm", "节奏"), ("composer", "作曲家")], "vo_world")

    G("gr_ingattr", "动词 -ing 作定语和表语", 11, 5,
      "能用动词 -ing 作定语或表语，表示主动或事物的性质。", "ing", [
        q("a ___ band 表示正在表演的乐队，横线处填哪一个？", "performing",
          "performed", "perform", "to performing", "正在表演的乐队用 performing 作定语。"),
        q("The news is ___. 表示消息令人兴奋，横线处填哪一个？", "exciting",
          "excited", "excite", "excites", "消息的性质用 exciting 作表语。"),
        q("哪一句是正确的？", "The smiling audience loved the song",
          "The smiled audience loved the song", "The smile audience loved the song",
          "The audience smiling loved are the song",
          "smiling 作定语修饰 audience，表示面带微笑。"),
        q("Her job is ___ the stage. 表示工作是布置舞台，横线处填哪一个？", "designing",
          "designed", "design", "to designed", "is 后面说明工作内容，用 designing 作表语。"),
      ])

    G("gr_ingadv", "动词 -ing 作状语和宾补", 11, 5,
      "能用动词 -ing 作状语或宾语补足语，表示主动。", "ing", [
        q("___ the violin, she walked onto the stage. 横线处填哪一个？", "Playing",
          "Played", "Play", "To played", "她主动拉小提琴，状语用 Playing。"),
        q("I heard someone ___ in the hall. 表示听见某人正在唱歌，横线处填哪一个？", "singing",
          "sung", "sang", "to singing", "someone 主动在唱，宾补用 singing。"),
        q("哪一句是正确的？", "He sat in the audience, listening carefully",
          "He sat in the audience, listened carefully", "He sat in the audience, listen carefully",
          "Listening carefully, the song was beautiful",
          "listening 的逻辑主语是 He。歌曲不能作 listening 的主语。"),
        q("We watched the band ___. 表示看着乐队演奏，横线处填哪一个？", "performing",
          "performed", "perform", "to performed", "band 主动表演，宾补用 performing。"),
      ])

    P("ph_linkhs", "意群中的连读", 11, 5,
      "能识别辅音结尾和元音开头在短语里可以连读。", "link", [
        q("an old instrument 里，哪两个词更容易连读？", "an 和 old",
          "old 和 instrument 的词尾", "instrument 内部的两个辅音", "没有任何词",
          "an 以辅音结尾，old 以元音开头，可以连读。"),
        q("look at it 里，哪一处符合辅音连到元音？", "look 的 /k/ 连到 at",
          "at 的 /t/ 后面没有元音所以必须停", "it 的开头是辅音所以连不上", "三个词都要重读且断开",
          "look 的结尾辅音可以连到 at 的元音。"),
        q("哪一个短语最适合练习连读？", "stand up", "big drums", "classical music", "six bands",
          "stand 以辅音结尾，up 以元音开头。其余相邻处多是辅音接辅音。"),
        q("连读主要发生在什么位置？", "前一个词的辅音和后一个词的元音之间",
          "每个元音字母上面", "句号后面", "两个逗号之间必须停顿",
          "连读是把词尾辅音和词首元音连起来。"),
      ])

    P("ph_ploshs", "不完全爆破", 11, 5,
      "能识别相邻爆破音中前一个音只做口型、不完全爆破。", "link", [
        q("a big band 里，哪个音常常不完全爆破？", "big 末尾的 /g/",
          "band 里的元音", "a 的元音", "没有这样的音",
          "big 的 /g/ 和 band 的 /b/ 都是爆破音，前一个常常不完全爆破。"),
        q("which 一组含有相邻的爆破音？", "good time", "my audience", "high note", "old stage",
          "good 的 /d/ 和 time 的 /t/ 是相邻爆破音。"),
        q("不完全爆破时，前一个爆破音通常怎样？", "口型做到，但气流不完全冲出",
          "必须读得特别长", "改成元音", "直接删掉整个单词",
          "前一个爆破音往往只成阻，不完全释放。"),
        q("sit down 里更容易出现不完全爆破的是哪一个？", "sit 末尾的 /t/",
          "down 的元音", "sit 的元音", "down 末尾的 /n/",
          "/t/ 后面紧接 down 的 /d/，/t/ 常常不完全爆破。"),
      ])

    F("fu_music", "谈论演出", 11, 5,
      "能描述一场演出，并提出一起去听的建议。", "fu_plan", [
        q("想说乐队正在舞台上表演，哪一句合适？", "The band is performing on the stage",
          "The band is performed on the stage", "The band is perform on the stage", "The band is performnig on the stage",
          "乐队主动表演，用 is performing。"),
        q("想邀请同学去听古典音乐会，哪一句合适？", "Shall we go to the classical concert",
          "Shall we go to the calssical concert", "Shall we go to the classiacl concert", "We went tomorrow",
          "邀请用 Shall we go。"),
        q("想描述听众边听边微笑，哪一句合适？", "The audience sat there, smiling",
          "The audience sat there, smiled", "The aduience sat there, smiling", "The audiecne sat there, smiling",
          "smiling 作状语，逻辑主语是 audience。"),
        q("想说明节奏让演出很兴奋，哪一句合适？", "The rhythm made the show exciting",
          "The rhythm made the show excited", "Exciting made the rhythm a person", "Show is exciting made",
          "演出的性质用 exciting，不是人的感受 excited。"),
      ])

    _u = "A student band is performing on the stage. The audience is listening, clapping at the end of each song. The composer of the last piece is a teacher at the school."
    R("rw_music", "读演出短文", 11, 5,
      "读一段演出短文，概括听众在做什么以及作者是否只是在说明。", "rw_main", [
        q(_u + " 谁在舞台上表演？", "一支学生乐队", "作曲家一个人", "听众", "老师的合唱队",
          "短文写 A student band is performing。"),
        q(_u + " 听众在每首歌结束时做什么？", "鼓掌", "离开", "写诗", "修理乐器", "短文写 clapping。"),
        q(_u + " 最后一首曲子的作曲家是谁？", "学校里的一位老师", "一名学生", "没有作曲家", "听众中的游客",
          "短文写 a teacher at the school。"),
        q(_u + " 这段文字主要在做什么？", "说明演出当时的情形", "批评乐队", "招聘猎人", "反对古典音乐",
          "短文只是在描述表演和听众。"),
      ])

    R("wr_music", "写演出通知", 11, 5,
      "能按要点选出演出通知里的句子。", "rw_write", [
        q("要点：学生乐队、周五舞台演出、听众请准时。哪一句三个要点都有？",
          "The student band is performing on the stage on Friday, and the audience should arrive on time",
          "The student band is performing", "Friday is busy", "Please be quiet",
          "三个要点都要出现。"),
        q("通知里用 -ing 作状语描述入场，哪一句正确？", "Entering the hall, please keep quiet",
          "Entered the hall, please keep quiet", "The hall entering, please keep quiet",
          "Keep quiet, the door entering",
          "Entering 的逻辑主语应是听话的人。"),
        q("哪一句适合作为通知标题？", "Student band on stage this Friday",
          "Sutdent band on stage this Friday", "Studnet band on stage this Friday", "Stdent band on stage this Friday",
          "标题可以写 Student band on stage this Friday。"),
        q("哪一句的定语是动词 -ing？", "The performing band needs two more players",
          "The performed band needs two more players", "The band performing needs are players two",
          "Needs the band performing players",
          "performing 作定语，表示正在表演的乐队。"),
      ])
