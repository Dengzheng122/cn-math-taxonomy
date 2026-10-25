# -*- coding: utf-8 -*-
"""人教版（2019）选择性必修第四册。单元名按通行目录，册次待核。"""
from enh_tx import V, P, G, F, R, q


def load():
    V("vo_fiction", "科幻作品", 16, 1,
      "认读 fiction、android、clone 和 alien。",
      [("fiction", "小说"), ("android", "仿生人"), ("clone", "克隆体"), ("alien", "外星人")], "vo_work")

    V("vo_android", "未来科技", 16, 1,
      "认读 spacecraft、gravity、dimension 和 experiment。",
      [("spacecraft", "宇宙飞船"), ("gravity", "重力"), ("dimension", "维度"), ("experiment", "实验")], "vo_work")

    G("gr_nonfinmix", "非谓语的选择", 16, 1,
      "能在语境中选择 to do、doing 或 done。", "nonfin", [
        q("The android needs ___ before the next flight. 表示需要被检查，横线处填哪一个？", "to be checked",
          "to checking", "check", "checked it",
          "needs 后面用 to be checked，表示仿生人需要被检查。"),
        q("哪一句里 written 作定语？", "The fiction written last year is still popular",
          "The fiction writing last year is still popular", "Written the fiction last year is popular",
          "The fiction to writing last year is popular",
          "written last year 修饰 fiction，表示这本小说是去年被写的。"),
        q("She remembers ___ the spacecraft door. 表示记得已经关上，横线处填哪一个？", "closing",
          "to close", "closed it yesterday as a finite verb", "to closing",
          "remember doing 表示记得做过。remember to do 表示记得要去做。"),
        q("表示很高兴被邀请上船，哪一句正确？", "I am glad to be invited aboard",
          "I am glad to inviting aboard", "I am glad inviting aboard as the whole predicate",
          "I am glad be invited aboard",
          "glad 后面用 to be invited，是不定式的被动式。"),
      ])

    G("gr_donevs", "非谓语完成式和被动式", 16, 1,
      "能区分 having done、having been done 和 being done。", "nonfin", [
        q("___ the experiment, the crew left the lab. 实验已经做完，横线处填哪一个？", "Having finished",
          "Having been finished", "Being finished", "Finished by them now",
          "crew 自己做完实验，用 Having finished。"),
        q("The clone, ___ in secret for years, was finally found. 多年来一直被藏着，横线处填哪一个？",
          "having been hidden", "having hidden", "hiding the lab", "to hide",
          "clone 是被藏的，而且发生在 was found 之前，用 having been hidden。"),
        q("哪一句表示门正在被修？", "The door being repaired cannot be used",
          "The door having repaired cannot be used", "The door to repairing cannot be used",
          "Repairing the door cannot be used as if the door repairs itself",
          "being repaired 表示正在被修理。"),
        q("Having been tested twice 和 being tested 的差别是什么？", "前者是已经被检测过，后者是正在被检测",
          "两者都表示将来主动去做", "前者是疑问句，后者是虚拟语气", "两者都只能作谓语",
          "having been tested 是完成被动，being tested 是进行被动。"),
      ], "inferred")

    F("fu_scifi", "讨论科幻情节", 16, 1,
      "能用一两句说明科幻故事里谁做了什么、什么已经被完成。", "fu_argue", [
        q("想说仿生人需要先被检查，哪一句合适？", "The android needs to be checked first",
          "The android needs to checking first", "Checked needs the android", "The android checking needs",
          "needs to be checked 表示需要被检查。"),
        q("想说做完实验后船员离开了，哪一句合适？", "Having finished the experiment, the crew left",
          "Having been finished the experiment, the crew left", "The experiment having the crew left",
          "Finished the crew the experiment",
          "船员是动作发出者，用 Having finished。"),
        q("想说这本去年写的小说仍受欢迎，哪一句合适？", "The fiction written last year is still popular",
          "The fiction writing last year is still popular", "Written is the fiction popular last",
          "The fiction to writing is popular",
          "written last year 作定语。"),
        q("想提醒对方记得去关舱门，事情还没做，哪一句合适？", "Please remember to close the spacecraft door",
          "Please remember closing the spacecraft door yesterday", "Remember closed the door",
          "To closing remember the door",
          "还没做，用 remember to close。已经做过才用 remember closing。"),
      ])

    _sf = "The fiction written in 2019 follows an android. Having finished a gravity experiment, the crew found the clone hidden in the lab. The spacecraft door being repaired cannot open yet."
    R("rw_scifi", "读科幻短文", 16, 1,
      "能分清谁做了实验、什么已经被藏起来、什么正在被修理。", "rw_infer", [
        q(_sf + " 这本小说写于哪一年？", "2019 年", "今年正在写", "船员出发那年没有写出", "短文没有年份",
          "written in 2019 说明写于 2019 年。"),
        q(_sf + " 船员在发现克隆体之前做了什么？", "做完了一次重力实验", "正在修舱门", "藏起了仿生人", "打开了已经修好的门",
          "Having finished a gravity experiment 发生在 found 之前。"),
        q(_sf + " 克隆体当时是什么状态？", "被藏在实验室里", "正在做实验", "正在修门", "已经离开飞船",
          "the clone hidden in the lab。"),
        q(_sf + " 舱门为什么还不能开？", "正在被修理", "已经修理完了", "船员忘了做实验", "小说还没写完",
          "being repaired 表示正在被修理。"),
      ])

    R("wr_scifi", "写科幻概要", 16, 1,
      "能按要点选出概要中的句子。", "rw_write_s", [
        q("要点：2019 年写成的小说、船员做完重力实验、舱门正在被修理。哪一句三个要点都有？",
          "The fiction written in 2019 shows a crew having finished a gravity experiment, while the door is being repaired",
          "The fiction is new", "The crew left", "The door is a door",
          "三个要点都要出现。"),
        q("概要里表示克隆体被藏了很多年，哪一句正确？", "The clone, having been hidden for years, was found",
          "The clone, having hidden for years, was found as if it hid itself",
          "The clone being hide was found", "Hidden having the clone was",
          "clone 是被藏的，用 having been hidden。"),
        q("哪一句适合作为概要的第一句？", "This science fiction follows an android on a spacecraft",
          "This science fiction follow an android on a spacecraft", "This science fiction follows an android on an spacecraft", "This science fiction follows an android on a sapcecraft",
          "概要可以先点出人物和场景。"),
        q("表示记得已经关上门，哪一句正确？", "She remembers closing the door",
          "She remembers to close the door yesterday as a finished act", "She remembers closed the door",
          "Closing remembers she the door",
          "remembers closing 表示记得做过。"),
      ])

    V("vo_landmark", "地标", 16, 2,
      "认读 landmark、statue、temple 和 tower。",
      [("landmark", "地标"), ("statue", "雕像"), ("temple", "寺庙"), ("tower", "塔")], "vo_work")

    V("vo_sight", "名胜", 16, 2,
      "认读 attraction、scenery、guide 和 queue。",
      [("attraction", "景点"), ("scenery", "景色"), ("guide", "导游"), ("queue", "排队")], "vo_work")

    G("gr_nomatter", "no matter 与 -ever", 16, 2,
      "能用 no matter who 或 whoever 引导让步状语从句。", "advcls", [
        q("无论谁来当导游，我们都九点出发。哪一句正确？", "No matter who the guide is, we leave at nine",
          "No matter who is the guide, we leave at nine", "Whoever the guide is the queue",
          "No matter whom the guide is he, we leave",
          "who 在从句里作表语，语序是 the guide is，不是疑问语序。"),
        q("___ you visit, take a photo of the statue. 表示无论参观哪里，横线处填哪一个？", "Wherever",
          "Wherever place", "No matter wherever", "Where",
          "Wherever 等于 no matter where。Where 只表示某个地方，没有“无论”。"),
        q("哪一句和 No matter what the scenery is 意思相同？", "Whatever the scenery is, we will stop",
          "What the scenery is, we will stop", "No matter whatever the scenery is",
          "Whatever is the scenery we stop as a question",
          "Whatever 可以替换 no matter what。"),
        q("whoever 在让步句里相当于哪一个？", "no matter who", "only the person who", "the place where", "because",
          "让步用法的 whoever 等于 no matter who。"),
      ], "inferred")

    G("gr_wherecls", "where 引导状语从句", 16, 2,
      "能判断 where 是在引导地点状语从句，还是在定语从句里修饰前面的名词。", "advcls", [
        q("哪一句的 where 引导地点状语从句？", "Where there is a tower, there is a queue",
          "The tower where we waited is old", "This is the temple where we prayed",
          "The place where we met is quiet",
          "句首 Where there is a tower 没有先行词，是地点状语从句。其余 where 前面都有名词。"),
        q("Put the statue ___ it can be seen. 横线处填哪一个？", "where",
          "which", "what", "wherever place",
          "where 引导地点状语从句，说明放在能被看见的地方。"),
        q("The landmark where we took photos 里，where 修饰哪一个词？", "landmark",
          "整句，没有先行词", "photos", "took",
          "where 紧跟 landmark，是定语从句，不是状语从句。"),
        q("哪里有寺庙，哪里就有游客。哪一句正确？", "Where there is a temple, there are visitors",
          "The temple where there are visitors is where", "Where a temple there is visitors",
          "There is a temple where there, visitors",
          "Where there is a temple 是地点状语从句。"),
      ], "inferred")

    F("fu_sight", "介绍名胜", 16, 2,
      "能介绍地标，并说明无论谁来、把东西放在哪里。", "fu_desc", [
        q("想说无论谁当导游都九点集合，哪一句合适？", "Whoever the guide is, we meet at nine",
          "Whoever is the guide, we meet at nine as a question order", "No matter whoever the guide",
          "Who the guide is we meet",
          "Whoever the guide is 是让步从句，用陈述语序。"),
        q("想告诉游客把包放在能看见雕像的地方，哪一句合适？", "Leave your bag where you can see the statue",
          "Leave your bag which you can see the statue", "Leave your bag what you can see",
          "Where leave your bag the statue",
          "where you can see the statue 是地点状语从句。"),
        q("想介绍这座塔是城市地标，哪一句合适？", "The tower is a landmark of the city",
          "The tower are a landmark of the city", "The tower is an landmark of the city", "The tower is a lnadmark of the city",
          "is a landmark 用来介绍地标。"),
        q("想说无论景色如何都会停留，哪一句合适？", "Whatever the scenery is, we will stop",
          "What the scenery is we stop", "No matter whatever we stop", "Scenery is whatever stop",
          "Whatever the scenery is 表示无论景色怎样。"),
      ])

    _sg = "Where there is a tower, visitors queue for photos. Whoever the guide is, the group meets at the statue. The temple where they prayed is older than the tower."
    R("rw_sight", "读名胜短文", 16, 2,
      "能分清地点状语从句和修饰名词的 where。", "rw_infer", [
        q(_sg + " 游客在什么地方排队拍照？", "有塔的地方", "寺庙里面才排队", "导游家里", "短文没有写排队",
          "Where there is a tower, visitors queue。"),
        q(_sg + " 集合地点是哪里？", "雕像那里", "塔顶", "任何寺庙", "没有集合",
          "the group meets at the statue。"),
        q(_sg + " the temple where they prayed 里的 where 修饰什么？", "temple", "整句的地点状语", "tower", "visitors",
          "where 前面有 temple，是定语从句。"),
        q(_sg + " 导游换了人，集合时间会变吗？", "不会，无论谁当导游都在雕像处集合", "会改到塔上", "短文说取消集合", "只有原导游才集合",
          "Whoever the guide is 表示无论导游是谁。"),
      ])

    R("wr_sight", "写游览说明", 16, 2,
      "能按要点选出说明中的句子。", "rw_write_s", [
        q("要点：有塔就排队、无论谁当导游都在雕像处集合、他们祈祷过的寺庙更古老。哪一句三个要点都有？",
          "Where there is a tower people queue, whoever the guide is the group meets at the statue, and the temple where they prayed is older",
          "The tower is tall", "People like photos", "The temple is old",
          "三个要点都要出现。"),
        q("说明里告诉游客把票放在能看见的地方，哪一句正确？", "Keep the ticket where you can see it",
          "Keep the ticket which you can see it", "Keep the ticket what you can see",
          "Where keep the ticket you",
          "where you can see it 是地点状语从句。"),
        q("哪一句适合作为说明的第一句？", "This walk starts at the city landmark",
          "This walk start at the city landmark", "This walk starts at the city lnadmark", "This walk starts at the city landmrak",
          "说明可以先写出起点。"),
        q("表示无论景色如何都拍照，哪一句正确？", "Whatever the scenery is, take a photo",
          "What the scenery is, take a photo", "No matter whatever take a photo", "Scenery whatever is take",
          "Whatever the scenery is 表示无论景色怎样。"),
      ])

    V("vo_ocean", "海洋", 16, 3,
      "认读 ocean、voyage、harbour 和 tide。",
      [("ocean", "海洋"), ("voyage", "航行"), ("harbour", "港口"), ("tide", "潮汐")], "vo_work")

    V("vo_voyage", "航海", 16, 3,
      "认读 sailor、compass、storm 和 anchor。",
      [("sailor", "水手"), ("compass", "罗盘"), ("storm", "暴风雨"), ("anchor", "锚")], "vo_work")

    G("gr_advconc", "although 与 while 让步", 16, 3,
      "能用 although 或 while 表示让步和对比。", "advcls", [
        q("虽然有暴风雨，水手还是起航了。哪一句正确？", "Although there was a storm, the sailors set out",
          "Although there was a storm, but the sailors set out", "Although a storm, the sailors set out",
          "Despite although the storm, sailors set",
          "although 不和 but 连用。"),
        q("While the tide was high, ___ . 表示尽管潮水很高仍留在港内，横线处填哪一个？",
          "the ship stayed in the harbour", "but the ship stayed in the harbour", "so the ship stayed and although",
          "stayed the ship although",
          "while 这里表示让步，主句直接写 the ship stayed，不加 but。"),
        q("哪一句用 while 表示对比？", "The compass worked, while the radio failed",
          "While the compass worked, but the radio failed", "The compass worked while but the radio",
          "While compass, radio failed but",
          "while 连接两件相反的事，表示对比。"),
        q("although 和 but 可以怎样用？", "用了 although 就不要再加 but", "两词必须同时出现", "but 要放在 although 前面",
          "although 只能修饰名词",
          "although 已经表示转折，不再加 but。"),
      ])

    G("gr_advso", "so that 与 in case", 16, 3,
      "能用 so that 表示目的，用 in case 表示以防万一。", "advcls", [
        q("他们早起航，以便赶上潮水。哪一句正确？", "They left early so that they could catch the tide",
          "They left early so that they can caught the tide", "They left early in case they could catch the tide as their purpose only",
          "So that they left early catch the tide",
          "so that 加 could catch 表示目的。"),
        q("Take a compass ___ you get lost. 表示以防迷路，横线处填哪一个？", "in case",
          "so that", "although", "while",
          "in case 表示以防万一。so that 表示为了达到某个目的。"),
        q("哪一句是目的而不是以防万一？", "She checked the anchor so that the ship would not drift",
          "She checked the anchor in case the ship drifted", "Although she checked the anchor, it held",
          "While she checked the anchor, he watched",
          "so that the ship would not drift 是目的。in case 是防备漂移真的发生。"),
        q("in case 引导的从句主要表达什么？", "以防某种情况发生", "已经发生的原因", "和 although 相同的让步", "定语从句",
          "in case 表示以防万一。"),
      ])

    F("fu_sea", "说明航海安排", 16, 3,
      "能说明尽管有风浪仍出航，以及为了什么、以防什么。", "fu_desc", [
        q("想说虽然有暴风雨仍要起航，哪一句合适？", "Although there is a storm, we will set out",
          "Although there is a storm, but we will set out", "Despite although the storm we set",
          "Although storm we but set",
          "although 不和 but 连用。"),
        q("想说早走是为了赶上潮水，哪一句合适？", "We leave early so that we can catch the tide",
          "We leave early in case we can catch the tide", "So that we leave early catch",
          "We leave early although we can catch the tide",
          "so that 表示目的。"),
        q("想提醒带上罗盘以防迷路，哪一句合适？", "Take a compass in case you get lost",
          "Take a compass so that you get lost", "Take a compass although you get lost",
          "In case take a compass you lost",
          "in case you get lost 表示以防迷路。"),
        q("想对比罗盘还能用、无线电坏了，哪一句合适？", "The compass works, while the radio has failed",
          "The compass works, while but the radio has failed", "While the compass works but the radio",
          "The compass works although but the radio failed",
          "while 可以表示对比，不加 but。"),
      ])

    _sea = "Although the storm was close, the sailors left harbour early so that they could catch the tide. They took a compass in case the radio failed. The anchor held, while the small boat did not."
    R("rw_sea", "读航海短文", 16, 3,
      "能找出让步、目的和防备分别指什么。", "rw_infer", [
        q(_sea + " 暴风雨临近时，水手做了什么？", "仍然早早离开港口", "留在港里", "丢掉罗盘", "只有小船出发",
          "Although the storm was close, the sailors left。"),
        q(_sea + " 他们为什么早离开？", "为了赶上潮水", "以防无线电坏掉", "因为锚断了", "为了对比小船",
          "so that they could catch the tide 是目的。"),
        q(_sea + " 带罗盘是为了什么？", "以防无线电失灵", "为了赶上潮水", "为了让小船失败", "因为暴风雨已经结束",
          "in case the radio failed。"),
        q(_sea + " while 对比的是哪两件事？", "锚稳住了，小船没有", "暴风雨和潮水", "罗盘和港口", "水手和无线电的目的",
          "The anchor held, while the small boat did not。"),
      ])

    R("wr_sea", "写航海备忘", 16, 3,
      "能按要点选出备忘中的句子。", "rw_write_s", [
        q("要点：尽管暴风雨仍离港、早走为了赶潮、带罗盘以防无线电失灵。哪一句三个要点都有？",
          "Although a storm was close they left so that they could catch the tide, and they took a compass in case the radio failed",
          "They left the harbour", "The tide was high", "They had a compass",
          "三个要点都要出现。"),
        q("备忘里表示锚稳住了而小船没有，哪一句正确？", "The anchor held, while the small boat did not",
          "The anchor held, while but the small boat did not", "Although the anchor held, but the boat did not",
          "While the anchor held but the boat",
          "while 表示对比，不加 but。"),
        q("哪一句适合作为备忘的第一句？", "Check the tide before the voyage",
          "Check the tide before the vyoage", "Check the tide before the voygae", "Check the tide before the voage",
          "备忘可以先写要检查的事。"),
        q("表示早起以便看清航线，哪一句正确？", "Start early so that you can see the route",
          "Start early in case you can see the route as your only purpose", "Start early although you can see the route",
          "So that start early you see",
          "so that you can see 是目的。"),
      ])

    V("vo_donate", "公益分享", 16, 4,
      "认读 donate、volunteer、charity 和 share。",
      [("donate", "捐赠"), ("volunteer", "志愿者"), ("charity", "慈善机构"), ("share", "分享")], "vo_work")

    V("vo_community", "社区服务", 16, 4,
      "认读 community、shelter、fundraising 和 neighbour。",
      [("community", "社区"), ("shelter", "庇护所"), ("fundraising", "募捐"), ("neighbour", "邻居")], "vo_work")

    G("gr_mixcls", "同位语从句和定语从句", 16, 4,
      "能区分 that 引导的同位语从句和定语从句。", "nouncls", [
        q("哪一句的 that 引导同位语从句？", "The news that the shelter will open spread quickly",
          "The shelter that opened last year is small", "The volunteer that we met is kind",
          "The charity that raised money is local",
          "news 后面的 that 从句说明消息的内容，that 不作成分。其余 that 都在从句里作主语或宾语，修饰名词。"),
        q("The fact ___ more neighbours donated money surprised us. 横线处填哪一个？", "that",
          "which", "what", "whose",
          "fact 后面用 that 引导同位语从句，说明事实的内容。"),
        q("The book that you donated 里，that 在从句中作什么？", "宾语", "不作成份，只连接同位语", "主语", "状语",
          "donated 缺少宾语，that 指 book，所以这是定语从句。"),
        q("哪一个名词后面更常见同位语从句？", "news、fact、idea 这类表示内容的名词", "只修饰人的 who", "地点状语 where",
          "比较级 than",
          "同位语从句说明 news、fact、idea 的具体内容。"),
      ])

    G("gr_whatnom", "what 引导名词性从句", 16, 4,
      "能用 what 引导主语从句或宾语从句，并让 what 在从句中充当成分。", "nouncls", [
        q("___ the volunteers need is more blankets. 横线处填哪一个？", "What",
          "That", "Which", "Whatever the thing",
          "从句缺宾语，用 What。That 引导的主语从句不缺成分。"),
        q("She asked ___ we could share. 表示问我们能分享的东西，横线处填哪一个？", "what",
          "that", "which the blankets", "what that",
          "asked 后面的宾语从句缺 share 的宾语，用 what。"),
        q("哪一句的 what 在从句中作主语？", "What surprised the neighbours was the fundraising",
          "That surprised the neighbours was the fundraising", "What the neighbours surprised was",
          "The news what surprised them was true",
          "What surprised the neighbours 里 what 是从句的主语。news 后面不能用 what 引导同位语从句。"),
        q("what 和 that 引导名词性从句时，主要差别是什么？", "what 在从句中充当成分，that 不充当",
          "what 永远不能作主语", "that 必须充当宾语", "两者都只能引导定语从句",
          "what 有意义并作成分，that 只起连接作用。"),
      ])

    F("fu_share", "安排公益活动", 16, 4,
      "能说明一条消息的内容，并说出志愿者需要什么。", "fu_plan_s", [
        q("想转告庇护所将开放这个消息，哪一句合适？", "The news that the shelter will open is true",
          "The news which the shelter will open is true", "The news what the shelter will open is true",
          "That the news the shelter will open",
          "news 后面用 that 同位语从句，不用 what 或 which。"),
        q("想说志愿者需要的是毯子，哪一句合适？", "What the volunteers need is blankets",
          "That the volunteers need is blankets", "What need the volunteers is blankets",
          "The fact what they need is blankets",
          "What the volunteers need 是主语从句，what 作 need 的宾语。"),
        q("想请邻居周六来帮忙，哪一句合适？", "Could you volunteer on Saturday",
          "Could you volunteer in Saturday", "Could you vlounteer on Saturday", "Could you vounteer on Saturday",
          "Could you volunteer 用来提出请求。"),
        q("想说明募捐这个事实让人惊讶，哪一句合适？", "The fact that the fundraising grew so fast surprised us",
          "The fact which the fundraising grew so fast surprised us", "The fact what grew surprised",
          "Fact that the surprised fundraising",
          "fact 后面用 that 说明事实内容。"),
      ])

    _sh = "The news that the shelter will open on Saturday surprised the neighbours. What the volunteers need is blankets. The charity that organised the fundraising thanked every donor."
    R("rw_share", "读公益短文", 16, 4,
      "能分清哪一句在说明消息内容，哪一句在修饰名词。", "rw_infer", [
        q(_sh + " 让邻居惊讶的消息是什么？", "庇护所周六开放", "志愿者不需要毯子", "慈善机构没有募捐", "短文没有消息",
          "The news that the shelter will open。"),
        q(_sh + " 志愿者需要什么？", "毯子", "一座新塔", "罗盘", "更多消息从句",
          "What the volunteers need is blankets。"),
        q(_sh + " The charity that organised the fundraising 里，that 是什么从句？", "定语从句", "同位语从句", "主语从句", "地点状语从句",
          "that 指 charity，并在从句中作 organised 的主语，是定语从句。"),
        q(_sh + " news 后面的 that 从句做什么？", "说明消息的内容", "修饰 Saturday 这个词", "代替 blankets", "表示让步",
          "that the shelter will open 是 news 的同位语。"),
      ])

    R("wr_share", "写招募启事", 16, 4,
      "能按要点选出启事中的句子。", "rw_write_s", [
        q("要点：庇护所周六开放、志愿者需要毯子、组织募捐的慈善机构表示感谢。哪一句三个要点都有？",
          "The news is that the shelter opens on Saturday, what the volunteers need is blankets, and the charity that organised the fundraising says thank you",
          "The shelter opens", "Blankets are useful", "The charity is kind",
          "三个要点都要出现。"),
        q("启事里说明事实内容，哪一句正确？", "The fact that we still need coats should be shared",
          "The fact which we still need coats should be shared", "The fact what we need coats should",
          "Fact that should coats",
          "fact 后面用 that 同位语从句。"),
        q("哪一句适合作为启事的第一句？", "We need volunteers for the community shelter",
          "We needs volunteers for the community shelter", "We need vlounteers for the community shelter", "We need volunteres for the community shelter",
          "启事可以先写出需要的人。"),
        q("表示“他们分享的东西帮了庇护所”，哪一句正确？", "What they shared helped the shelter",
          "That they shared helped the shelter", "What helped they shared the shelter",
          "The news what they shared helped",
          "What they shared 作主语，what 是 shared 的宾语。"),
      ])

    V("vo_career", "职业规划", 16, 5,
      "认读 career、applicant、interview 和 qualification。",
      [("career", "职业"), ("applicant", "申请人"), ("interview", "面试"), ("qualification", "资格")], "vo_work")

    V("vo_resume", "申请材料", 16, 5,
      "认读 résumé、reference、deadline 和 employ。",
      [("résumé", "简历"), ("reference", "推荐信"), ("deadline", "截止日期"), ("employ", "雇用")], "vo_work")

    G("gr_tensemix", "语篇中的时态选择", 16, 5,
      "能在一段叙述里判断一般过去时、现在完成时和一般将来时。", "mix", [
        q("She ___ three interviews since Monday, and the next one is on Friday. 横线处填哪一个？", "has had",
          "had", "will have", "is having had",
          "since Monday 到现在，用现在完成时 has had。"),
        q("By the time the deadline arrived, she ___ the résumé. 截止日期到来之前已经寄出，横线处填哪一个？",
          "had sent", "has sent", "sends", "will send",
          "arrived 是过去，寄出比它更早，用 had sent。"),
        q("哪一句的时态和时间状语一致？", "I have worked here since June",
          "I have worked here in June 2019", "I work here since June", "I had worked here since June now",
          "since June 持续到现在，用现在完成时。in June 2019 是过去的一点，不用 have worked。"),
        q("面试在下周五。哪一句正确？", "The interview will take place next Friday",
          "The interview took place next Friday", "The interview has taken place next Friday",
          "The interview takes place next Friday as a finished past event",
          "next Friday 是将来，用 will take place。"),
      ])

    G("gr_provided", "provided that 条件", 16, 5,
      "能用 provided that 表示“只要满足某个条件”。", "advcls", [
        q("只要你在截止日期前交简历，他们就会看。哪一句正确？",
          "They will read it provided that you send it before the deadline",
          "They will read it provided that you sent it before the deadline next week",
          "Provided that you will send it, they read it yesterday",
          "They read it provided what you send",
          "provided that 引导条件，主句是将来，从句用现在时 send。"),
        q("You can get the job ___ you pass the interview. 表示只要通过面试，横线处填哪一个？", "provided that",
          "so that", "although", "in case",
          "provided that 表示只要。so that 是目的，although 是让步，in case 是以防。"),
        q("哪一句的条件是“有两封推荐信”？", "We will employ her provided that she has two references",
          "We employed her provided that she has two references next year",
          "Provided that she had two references, we employ her yesterday",
          "We employ her so that she has two references",
          "provided that she has two references 是雇用的条件。"),
        q("provided that 更接近哪一个意思？", "as long as", "although", "so that", "in case",
          "provided that 表示只要，和 as long as 相近。"),
      ], "inferred")

    P("ph_weak", "功能词弱读", 16, 5,
      "能识别句子里冠词、介词和连词常常弱读。", "weak", [
        q("bread and butter 里，and 在正常语流中常常怎样？", "弱读，元音变得很轻", "必须重读并且拖长", "改成升调疑问", "不能和前后的词连起来",
          "and 是功能词，句中常弱读。"),
        q("哪一类词更常弱读？", "冠词、介词、连词和助动词", "句中的名词实词一律弱读", "人名必须弱读", "句末的实义动词",
          "功能词常常弱读，实词通常保留重音。"),
        q("I want to apply 里，to 在不强调时通常读成什么？", "轻读的 /tə/", "和 two 一样的长元音", "必须重读成 toe", "省略后变成升调",
          "to 不强调时元音常弱化成 /ə/。"),
        q("如果要强调就是这一份申请，可以重读哪一个词？", "this，而不是把 of 读重", "只重读 of", "只重读 a", "把 and 读得最重",
          "强调的信息落在实词 this 上，功能词 of 和 a 仍可弱读。"),
      ])

    F("fu_job", "谈论求职", 16, 5,
      "能说明已经完成的申请、下一步，以及对方开出的条件。", "fu_plan_s", [
        q("想说周一以来已经参加了三次面试，哪一句合适？", "I have had three interviews since Monday",
          "I had three interviews since Monday", "I have three interviews since Monday as a past point",
          "I will have three interviews since Monday",
          "since Monday 到现在，用 have had。"),
        q("想说只要在截止日期前交简历就会被看，哪一句合适？",
          "They will read it provided that you send it before the deadline",
          "They read it yesterday provided that you will send it", "Provided that send you, they will read",
          "They will read it although you send it before the deadline",
          "provided that you send 表示只要寄出。"),
        q("想礼貌地问能否在周五前面试，哪一句合适？", "Could I come for an interview before Friday",
          "Could I come for an itnerview before Friday", "Could I come for an interveiw before Friday", "Could I come for an inerview before Friday",
          "Could I come 用来礼貌地询问安排。"),
        q("想说截止日期到来之前简历已经寄出，哪一句合适？", "I had sent the résumé before the deadline arrived",
          "I have sent the résumé before the deadline arrived", "I send the résumé before the deadline arrived",
          "I will send the résumé before the deadline arrived",
          "寄出比 arrived 更早，用 had sent。"),
      ])

    _job = "Lin has had two interviews since Monday. She had sent her résumé before the deadline arrived. The company will employ her provided that the references arrive this week. The next interview will take place on Friday."
    R("rw_job", "读招聘短文", 16, 5,
      "能判断哪些申请步骤已经完成，哪一件还要满足条件。", "rw_argue", [
        q(_job + " 自从周一起，Lin 参加了几次面试？", "两次", "三次并且都在将来", "一次也没有", "短文没有写面试次数",
          "has had two interviews since Monday。"),
        q(_job + " 截止日期到来时，简历是什么状态？", "已经寄出", "还没写", "周五才寄", "公司拒绝接收",
          "had sent her résumé before the deadline arrived。"),
        q(_job + " 公司雇用她的条件是什么？", "推荐信本周寄到", "她再写一份简历", "面试改到周一", "没有条件",
          "provided that the references arrive this week。"),
        q(_job + " 下一次面试在什么时候？", "周五", "周一以前", "截止日期当天已经结束", "短文没写时间",
          "will take place on Friday。"),
      ])

    R("wr_job", "写申请邮件", 16, 5,
      "能按要点选出邮件中的句子。", "rw_write_s", [
        q("要点：周一起已有两次面试、截止日期前寄出了简历、只要推荐信本周到就会被雇用。哪一句三个要点都有？",
          "She has had two interviews since Monday, she had sent the résumé before the deadline, and they will employ her provided that the references arrive this week",
          "She had an interview", "The résumé was sent", "References matter",
          "三个要点都要出现。"),
        q("邮件里表示下一次面试在周五，哪一句正确？", "The next interview will take place on Friday",
          "The next interview took place on Friday", "The next interview has taken place on Friday",
          "The next interview takes place on Friday last year",
          "周五还未到，用 will take place。"),
        q("哪一句适合作为邮件的第一句？", "I am writing to apply for the post",
          "I am write to apply for the post", "I am writing to applying for the post", "I am writing to applys for the post",
          "申请邮件可以先说明目的。"),
        q("表示只要通过面试就可以开始，哪一句正确？", "You can start provided that you pass the interview",
          "You can start so that you pass the interview", "You started yesterday provided that you pass",
          "Provided that you passed, you can start next week as a past failure",
          "provided that you pass 是开始工作的条件。"),
      ])
