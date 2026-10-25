# -*- coding: utf-8 -*-
"""人教版（2019）选择性必修第一册。单元名按通行目录，册次待核。"""
from enh_tx import V, G, F, R, q


def load():
    V("vo_achieve", "人物成就", 13, 1,
      "认读 achievement、genius、career 和 honour。",
      [("achievement", "成就"), ("genius", "天赋"), ("career", "事业"), ("honour", "荣誉")], "vo_people")

    V("vo_nobel", "科学家与贡献", 13, 1,
      "认读 Nobel、discover、theory 和 devote。",
      [("Nobel", "诺贝尔奖"), ("discover", "发现"), ("theory", "理论"), ("devote", "奉献")], "vo_people")

    G("gr_subjcls", "that 引导主语从句", 13, 1,
      "能用 that 引导主语从句，或用 it 作形式主语。", "nouncls", [
        q("___ he refused the prize surprised us. 横线处填哪一个？", "That",
          "What", "Which", "Who", "主语从句不缺成分、表示一件事，用 That。"),
        q("哪一句用 it 作形式主语？", "It is clear that she devoted her life to research",
          "That is clear she devoted her life", "Clear that she devoted is it", "It clear that she devoted",
          "It is clear that 后面才是真正的主语从句。"),
        q("___ he discovered is still unknown. 从句缺少发现的内容，横线处填哪一个？", "What",
          "That", "Which", "If", "从句缺少宾语时用 What，不能用 That。"),
        q("哪一句是正确的？", "That the theory works has been proved",
          "The theory works has been proved", "That the theory works have been proved",
          "Which the theory works has been proved",
          "That 从句作主语时，谓语用单数 has。"),
      ])

    G("gr_ifsubj", "whether 引导主语从句", 13, 1,
      "能用 whether 引导主语从句，并使用陈述语序。", "nouncls", [
        q("___ she will accept the honour is unknown. 横线处填哪一个？", "Whether",
          "If", "That", "What", "主语从句放在句首表示“是否”时用 Whether，不用 If。"),
        q("哪一句语序正确？", "Whether he is a genius is not important",
          "Whether is he a genius is not important", "If he is a genius is not important",
          "Whether he a genius is",
          "whether 从句用陈述语序 he is。"),
        q("It is uncertain ___ they discovered the cause. 横线处填哪一个？", "whether",
          "that", "which", "who", "不确定“是否”用 whether。"),
        q("哪一句不能放在句首？", "If she will come is unknown",
          "Whether she will come is unknown", "That she will come is certain",
          "What she will say is unknown",
          "If 不能引导放在句首的主语从句。"),
      ])

    F("fu_people", "描述人物成就", 13, 1,
      "能按时间说明人物做了什么，并给出评价。", "fu_desc", [
        q("想说她把一生献给了研究，哪一句合适？", "She devoted her life to research",
          "Devoted she life research to", "She not devoted her life to research", "She devoted her life to rseearch",
          "devoted her life to 用来概括事业。"),
        q("想说她是否得奖还不清楚，哪一句合适？", "Whether she will get the honour is unknown",
          "If she will get the honour is unknown", "Whether will she get the honour is unknown",
          "Unknown whether will she",
          "句首用 Whether，语序是 she will get。"),
        q("想先给结论再说事实，哪一句合适？", "It is clear that his discovery changed medicine",
          "It is clear his discovery changed that", "Clear is that it discovery", "That clear it is",
          "It is clear that 先给评价。"),
        q("想按步骤介绍人物，哪一句适合作为第二步？", "Next, he published the theory",
          "Next, he pbulished the theory", "Published he next the", "Next, he publisehd the theory",
          "Next 用来连接步骤。"),
      ])

    _p = "Tu Youyou devoted many years to research. It is now clear that her discovery saved a great number of patients. Whether every student knows her story is another question."
    R("rw_people", "读人物短文", 13, 1,
      "根据短文推断作者没有直接说满的态度，并找出事实。", "rw_infer", [
        q(_p + " 她把许多年用在了什么上？", "研究", "表演", "旅行", "贷款", "短文写 devoted many years to research。"),
        q(_p + " 她的发现带来了什么？", "挽救了许多病人", "取消了理论", "破坏了实验室", "短文没有结果",
          "短文写 saved a great number of patients。"),
        q(_p + " 哪一件事作者说还不一定？", "是不是每个学生都知道她的故事", "发现有没有用", "她有没有做研究", "病人有没有获救",
          "Whether every student knows her story 表示这件事不确定。"),
        q(_p + " 作者对这项发现的态度更接近哪一种？", "认为它很重要", "认为它没有价值", "只在怀疑病人", "没有态度",
          "saved a great number of patients 说明作者认为发现重要。"),
      ])

    R("wr_people", "写人物简介", 13, 1,
      "能按要点选出人物简介中的句子。", "rw_write_s", [
        q("要点：多年研究、发现挽救病人、不是每个学生都知道。哪一句三个要点都有？",
          "She devoted years to research, her discovery saved patients, and whether every student knows her is uncertain",
          "She did research", "Patients recovered", "Students are busy",
          "三个要点都要出现。"),
        q("简介用形式主语评价发现，哪一句正确？", "It is important that we remember this achievement",
          "It is important we remember that this", "Important that it we remember", "That important is it",
          "It is important that 后面用陈述句。"),
        q("哪一句适合作为简介的第一句？", "This paragraph introduces a scientist",
          "This paragraph introduce a scientist", "This paragraph introduces an scientist", "This paragraph itnroduces a scientist",
          "简介可以先说明 This paragraph introduces。"),
        q("哪一句的主语从句用了 Whether？", "Whether the story is widely known matters",
          "If the story is widely known matters", "Whether is the story known matters", "Matters whether is the story",
          "句首用 Whether，语序是 the story is。"),
      ])

    V("vo_robot", "未来生活", 13, 2,
      "认读 robot、automatic、predict 和 innovation。",
      [("robot", "机器人"), ("automatic", "自动的"), ("predict", "预测"), ("innovation", "创新")], "vo_people")

    V("vo_smart", "智能设备", 13, 2,
      "认读 sensor、remote、appliance 和 warning。",
      [("sensor", "传感器"), ("remote", "远程的"), ("appliance", "家用电器"), ("network", "网络")], "vo_people")

    G("gr_predcls", "表语从句", 13, 2,
      "能用 that、whether 或疑问词引导表语从句。", "nouncls", [
        q("The problem is ___ the sensor fails at night. 横线处填哪一个？", "that",
          "which", "what", "who", "从句不缺成分，表语从句用 that。"),
        q("The question is ___ the robot can cook. 表示“是否”，横线处填哪一个？", "whether",
          "that", "which", "who", "表示是否用 whether。"),
        q("哪一句语序正确？", "That is why the appliance stops",
          "That is why does the appliance stop", "That is why stops the appliance", "Why that is the appliance stops",
          "表语从句用陈述语序 the appliance stops。"),
        q("What I need is ___ the network is stable. 横线处填哪一个？", "that",
          "what", "which", "if", "is 后面的从句不缺成分，用 that。"),
      ])

    G("gr_appos", "同位语从句", 13, 2,
      "能用 that 引导同位语从句，并把它和定语从句分开。", "nouncls", [
        q("The news ___ the robot won a prize is true. that 在从句中不充当成分，横线处填哪一个？", "that",
          "which", "what", "who", "news 的内容是一整件事，用 that 引导同位语从句。"),
        q("哪一句是同位语从句？", "The fact that the sensor failed surprised them",
          "The sensor that failed was new", "The robot which we bought is small", "The prize which he won is gold",
          "that the sensor failed 是 fact 的内容，that 不作成分。"),
        q("哪一句是定语从句而不是同位语从句？", "The report which he wrote is short",
          "The report that he was late is false", "The idea that robots will cook is new",
          "The news that she won is true",
          "which he wrote 里 which 作 wrote 的宾语，是定语从句。"),
        q("We heard the warning ___ the network might break. 横线处填哪一个？", "that",
          "which", "where", "whom", "warning 的具体内容用 that 同位语从句。"),
      ])

    F("fu_future", "描述未来设备", 13, 2,
      "能按步骤说明一台设备如何工作。", "fu_desc", [
        q("想按步骤说明机器人如何做饭，哪一句适合作为第一步？", "First, the sensor checks the food",
          "First, the snesor checks the food", "First, the senosr checks the food", "First, the sesor checks the food",
          "First 用来开始步骤。"),
        q("想说问题在于网络不稳定，哪一句合适？", "The problem is that the network is not stable",
          "The problem is that is the network not stable", "The problem is why does it stop",
          "Problem that the network",
          "表语从句用 that 加陈述语序。"),
        q("想转述一个消息的内容，哪一句是同位语从句？", "The news that the appliance can be controlled remotely is exciting",
          "The appliance that we bought is remote", "The news which excited us is short",
          "Exciting news is the appliance",
          "that the appliance can be controlled 是 news 的内容。"),
        q("想预测这项创新会节省时间，哪一句合适？", "I predict that the innovation will save time",
          "I predict that will the innovation save time", "Predict I innovation time", "Save will time that",
          "predict that 后面用陈述语序。"),
      ])

    _u = "The new robot cooks by itself. The fact that its sensor failed yesterday explains the delay. The question is whether the network can be repaired today."
    R("rw_future", "读未来生活短文", 13, 2,
      "根据上下文推断 sensor 出了什么问题，以及作者还不确定什么。", "rw_infer", [
        q(_u + " 机器人会做什么？", "自己做饭", "修理网络", "写新闻", "发射火箭", "短文写 cooks by itself。"),
        q(_u + " 昨天什么部件出了故障？", "传感器", "烤箱门", "预算", "灯笼", "短文写 its sensor failed。"),
        q(_u + " 延误的原因是什么？", "传感器失灵", "网络已经修好", "机器人不会做饭", "没有原因",
          "The fact that its sensor failed explains the delay。"),
        q(_u + " 作者还不确定哪一件事？", "网络今天能不能修好", "机器人会不会做饭", "传感器昨天有没有坏", "有没有延误",
          "whether the network can be repaired 是还不确定的问题。"),
      ])

    R("wr_future", "写步骤说明", 13, 2,
      "能按要点选出步骤说明中的句子。", "rw_write_s", [
        q("要点：机器人会做饭、传感器昨天失灵、网络能否修好还未知。哪一句三个要点都有？",
          "The robot can cook, the sensor failed yesterday, and whether the network can be repaired is unknown",
          "The robot can cook", "Networks are useful", "Yesterday was busy",
          "三个要点都要出现。"),
        q("说明里用同位语从句，哪一句正确？", "The fact that the sensor failed explains the delay",
          "The fact which the sensor failed explains the delay", "The fact that failed the sensor explains",
          "Fact the that sensor failed",
          "fact 的内容用 that 从句，that 不作成分。"),
        q("哪一句适合作为步骤的第二句？", "Second, check whether the network is on",
          "Second, check wehther the network is on", "Whether check second is", "On the network whether",
          "Second 连接下一步，whether 从句用陈述语序。"),
        q("哪一句的表语从句是正确的？", "The problem is that the appliance stops suddenly",
          "The problem is that does the appliance stop", "The problem is why does it stop suddenly",
          "Is the problem that stops it",
          "that 从句用陈述语序 the appliance stops。"),
      ])

    V("vo_park", "公园", 13, 3,
      "认读 park、wildlife、boundary 和 ranger。",
      [("park", "公园"), ("boundary", "边界"), ("ranger", "护林员"), ("trail", "步道")], "vo_people")

    V("vo_reserve", "自然保护", 13, 3,
      "认读 wetland、species、prohibit 和 ecology。",
      [("wetland", "湿地"), ("ecology", "生态"), ("prohibit", "禁止"), ("binoculars", "望远镜")], "vo_people")

    G("gr_ingperf", "动词 -ing 的完成式", 13, 3,
      "能用 having done 表示该动作先于主句动作。", "nonfin", [
        q("___ the trail, they entered the wetland. 表示先走完步道，横线处填哪一个？", "Having walked",
          "Walking", "Walked", "To walk", "走步道在进入湿地之前，用 Having walked。"),
        q("哪一句表示先完成再离开？", "Having closed the gate, the ranger left",
          "Closing the gate, the ranger had already left", "Closed the gate, the ranger leaving",
          "The ranger left, having the gate close",
          "Having closed 发生在 left 之前。"),
        q("___ warned, visitors still fed the birds. 表示已经被警告过，横线处填哪一个？", "Having been",
          "Having", "Been having", "To have", "被警告用 Having been warned。"),
        q("哪一句的 -ing 和主语搭配错了？", "Having flown away, the ranger looked up",
          "Having flown away, the birds left the tree", "The ranger, having checked the trail, rested",
          "Having been prohibited, the action stopped",
          "飞走的应该是鸟，不是护林员。"),
      ])

    G("gr_with", "with 复合结构", 13, 3,
      "能用 with 加宾语再加补语，表示伴随的状态。", "nonfin", [
        q("He waited, with the lights ___. 表示灯亮着，横线处填哪一个？", "on",
          "turned", "to on", "were on", "with the lights on 是复合结构，on 作补语。"),
        q("With the problem ___, they went on. 表示问题已经被解决，横线处填哪一个？", "solved",
          "solving", "solve", "to solving", "problem 是被解决的，用 solved。"),
        q("哪一句是正确的？", "She entered with a map in her hand",
          "She entered with a map was in her hand", "She entered with a map being was",
          "With a map was in her hand, she entered",
          "with a map in her hand 不再加 was。"),
        q("With the ranger ___ the way, we did not get lost. 表示护林员正在带路，横线处填哪一个？", "leading",
          "led", "lead", "to lead", "ranger 主动带路，用 leading。"),
      ], "inferred")

    F("fu_park", "描述公园规则", 13, 3,
      "能按顺序说明参观公园的做法和禁止事项。", "fu_desc", [
        q("想按顺序说明先关门再进入湿地，哪一句合适？", "Having closed the gate, enter the wetland quietly",
          "Closing after entered the gate", "Enter, having the gate close later", "Gate closed having enter",
          "Having closed 表示先关门。"),
        q("想说禁止投喂，哪一句合适？", "Feeding animals is prohibited",
          "Prohibited feeding are animals", "Feeding animals is porhibited", "Feeding animals is prohibietd",
          "is prohibited 用来说明禁止。"),
        q("想描述手里拿着望远镜看鸟，哪一句合适？", "She watched the birds with binoculars in her hand",
          "She watched with binoculars were in her hand", "With binoculars were, she watched",
          "Binoculars in hand were with",
          "with binoculars in her hand 不再用 were。"),
        q("想说明边界已经标出，哪一句合适？", "The boundary has been marked on the map",
          "The boundary has marked the map", "Marked has been the boundary", "Boundary marking the map has",
          "已经被标出用 has been marked。"),
      ])

    _k = "Having checked the map, we followed the trail into the wetland. Feeding birds is prohibited. With the ranger leading us, we stayed inside the boundary."
    R("rw_park", "读公园短文", 13, 3,
      "读短文，判断哪一条是规则，哪一条是已经做完的动作。", "rw_argue", [
        q(_k + " 他们进入湿地之前做了什么？", "核对了地图", "投喂了鸟", "离开了边界", "关上了灯",
          "Having checked the map 发生在 followed 之前。"),
        q(_k + " 什么是被禁止的？", "给鸟投喂", "看地图", "走步道", "跟随护林员", "短文写 Feeding birds is prohibited。"),
        q(_k + " 谁在带路？", "护林员", "鸟", "地图", "边界", "短文写 With the ranger leading us。"),
        q(_k + " 哪一句是短文中的规则而不是已经发生的事？", "不要给鸟投喂",
          "他们已经核对地图", "他们已经沿着步道走", "护林员已经在带路",
          "is prohibited 是规则。Having checked 是已经做的事。"),
      ])

    R("wr_park", "写参观说明", 13, 3,
      "能按要点选出参观说明中的句子。", "rw_write_s", [
        q("要点：先看地图、禁止投喂、护林员带路。哪一句三个要点都有？",
          "Having checked the map, remember that feeding is prohibited, and follow the ranger",
          "Check the map", "Feeding is bad", "Rangers are helpful",
          "三个要点都要出现。"),
        q("说明里表示先完成再前进，哪一句正确？", "Having read the rules, start along the trail",
          "Reading the rules after you finish the trail first", "Read having the rules, start",
          "The trail having read you",
          "Having read 表示先读完规则。"),
        q("哪一句适合作为说明的标题？", "How to visit the wetland",
          "How to visiting the wetland", "How to visits the wetland", "How to visit the wteland",
          "步骤说明可以用 How to visit。"),
        q("哪一句的 with 结构是正确的？", "Walk with the map in your pocket",
          "Walk with the map is in your pocket", "With the map is, walk", "Pocket with map is walk",
          "with the map in your pocket 不加 is。"),
      ])

    V("vo_body", "肢体语言", 13, 4,
      "认读 gesture、posture、expression 和 contact。",
      [("gesture", "手势"), ("posture", "姿势"), ("expression", "表情"), ("contact", "接触")], "vo_people")

    V("vo_gesture", "表情与距离", 13, 4,
      "认读 frown、nod、distance 和 interpret。",
      [("frown", "皱眉"), ("nod", "点头"), ("distance", "距离"), ("interpret", "解读")], "vo_people")

    G("gr_havedone", "非谓语的完成式和被动式", 13, 4,
      "能在语境中使用 having been done，表示先被完成。", "nonfin", [
        q("___ by the host, the guests sat down. 表示已经被迎接过，横线处填哪一个？", "Having been greeted",
          "Having greeted", "Greeted having", "To have greeting",
          "客人是被迎接的，而且发生在坐下之前，用 Having been greeted。"),
        q("哪一句表示先被询问再回答？", "Having been asked, she nodded",
          "Having asked, she was nodded", "Asked having been, nodded she", "Being ask, she nodded",
          "Having been asked 是先被问。"),
        q("The man seemed ___ the gesture. 表示似乎已经误会了手势，横线处填哪一个？", "to have misunderstood",
          "to misunderstand yesterday", "misunderstanding been", "have misunderstand",
          "发生在 seemed 之前用 to have misunderstood。"),
        q("哪一句把主动和被动用反了？", "Having been nodded, the head smiled",
          "Having nodded, he sat down", "Having been shown the sign, she understood",
          "The guest, having been invited, arrived",
          "点头的是人，不是头被点头以后自己微笑。"),
      ])

    G("gr_sense", "感官动词后的宾补", 13, 4,
      "能在 see、hear、notice 后面选择省略 to 的不定式或 -ing。", "nonfin", [
        q("I saw her ___ . 表示看见她点头的全过程，横线处填哪一个？", "nod",
          "to nod", "nodded", "to nodding", "see 后面表示全过程用省略 to 的 nod。"),
        q("I saw her ___ at me when I entered. 表示进来时正看见她在皱眉，横线处填哪一个？", "frowning",
          "frown", "to frown", "frowned", "强调正在进行用 frowning。"),
        q("哪一句是正确的？", "We heard someone calling his name",
          "We heard someone to call his name", "We heard someone called to his name",
          "We heard someone to calling",
          "hear 后面不能加 to call，进行中用 calling。"),
        q("她被看见进了房间。被动句哪一句正确？", "She was seen to enter the room",
          "She was seen enter the room", "She was seen entering to the room", "Seen was she enter",
          "主动 see sb do，被动要还原 to：was seen to enter。"),
      ], "inferred")

    F("fu_body", "描述肢体语言", 13, 4,
      "能描述一个手势或表情，并说明它可能表示什么。", "fu_desc", [
        q("想说点头常常表示同意，哪一句合适？", "A nod often means agreement",
          "A nod often mean agreement", "A nod often means argeement", "A nod often means agreemnet",
          "means agreement 用来解释手势。"),
        q("想说我看见她皱了一下眉，强调全过程，哪一句合适？", "I saw her frown",
          "I saw her to frown", "I saw her frowned", "Saw I her to frown",
          "see her frown 省略 to。"),
        q("想说客人被问候之后才坐下，哪一句合适？", "Having been greeted, the guests sat down",
          "Having greeted, the guests were sat by the host", "Greeted having been the guests sat",
          "The guests sat, having greet",
          "Having been greeted 表示先被问候。"),
        q("想提醒对方距离太近，哪一句合适？", "Please keep a comfortable distance",
          "Please keep an comfortable distance", "Keep is an expression", "Please keep a cmofortable distance",
          "祈使句 Please keep 用来提醒。"),
      ])

    _b = "Having been greeted, the guests sat down. I saw the host nod, which I interpreted as agreement. A frown, however, made the speaker keep a greater distance."
    R("rw_body", "读肢体语言短文", 13, 4,
      "根据上下文推断 nod 和 frown 分别暗示什么。", "rw_infer", [
        q(_b + " 客人坐下之前发生了什么？", "他们被问候了", "他们皱眉了", "他们离开了", "他们点头拒绝了",
          "Having been greeted 在 sat down 之前。"),
        q(_b + " 作者把点头理解成什么？", "同意", "拒绝", "距离太远", "没有理解", "短文写 interpreted as agreement。"),
        q(_b + " 皱眉让说话人做了什么？", "保持更远的距离", "马上坐下", "继续靠近", "开始点头",
          "短文写 keep a greater distance。"),
        q(_b + " 文中 which 更可能指什么？", "主人点头这件事", "客人这个人", "距离这个词", "皱眉的人",
          "which I interpreted 紧接 nod，指点头这个动作。"),
      ])

    R("wr_body", "写观察笔记", 13, 4,
      "能按要点选出观察笔记中的句子。", "rw_write_s", [
        q("要点：先被问候、点头表示同意、皱眉后拉开距离。哪一句三个要点都有？",
          "Having been greeted they sat down, a nod meant agreement, and a frown made the speaker keep a distance",
          "They sat down", "A nod is a gesture", "Distance matters",
          "三个要点都要出现。"),
        q("笔记里表示看见全过程，哪一句正确？", "I saw her nod once",
          "I saw her to nod once", "I saw her nodded once", "Saw her I to nod",
          "see her nod 不带 to。"),
        q("哪一句适合作为笔记的第一句？", "I watched how people used gestures",
          "I watched how people used gsetures", "I watched how people used gestuers", "I watched how people used getures",
          "笔记可以先写 I watched how。"),
        q("被动句要还原 to，哪一句正确？", "He was noticed to leave early",
          "He was noticed leave early", "He was noticed to leaving early", "Noticed was he leave",
          "was noticed 后面用 to leave。"),
      ])

    V("vo_farm", "农业", 13, 5,
      "认读 agriculture、crop、soil 和 harvest。",
      [("agriculture", "农业"), ("crop", "作物"), ("soil", "土壤"), ("harvest", "收获")], "vo_people")

    V("vo_crop", "耕作", 13, 5,
      "认读 fertilizer、irrigation、yield 和 organic。",
      [("fertilizer", "肥料"), ("irrigation", "灌溉"), ("yield", "产量"), ("organic", "有机的")], "vo_people")

    G("gr_topass", "不定式的被动式", 13, 5,
      "能用 to be done 表示将要被做或应该被做。", "nonfin", [
        q("The crops are ___ tomorrow. 表示明天将被收割，横线处填哪一个？", "to be harvested",
          "to harvest", "harvesting", "harvested be", "作物是被收割的，用 to be harvested。"),
        q("哪一句是正确的？", "The soil needs to be tested",
          "The soil needs to test", "The soil needs to be test", "The soil needs tested be",
          "soil 是被检测的对象，用 to be tested。"),
        q("There is a report ___ before Friday. 表示报告将被完成，横线处填哪一个？", "to be finished",
          "to finish", "finishing", "finished to", "report 是被完成的，定语用 to be finished。"),
        q("哪一句把主动和被动用反了？", "The farmer is to be grown by the wheat",
          "The wheat is to be grown by the farmer", "The farmer hopes to grow wheat",
          "The field is to be irrigated",
          "被种植的是小麦，不是农民。"),
      ])

    G("gr_abs", "独立主格", 13, 5,
      "能识别独立主格：名词加上分词，逻辑主语和主句主语不同。", "nonfin", [
        q("Weather ___, we will start the harvest. 表示如果天气允许，横线处填哪一个？", "permitting",
          "permitted", "permits", "to permitting", "weather 自己允许，用 permitting，这是独立主格。"),
        q("The work ___, the farmers went home. 表示工作已经被做完，横线处填哪一个？", "finished",
          "finishing", "finish", "to finish", "work 是被完成的，用 finished。"),
        q("哪一句是独立主格而不是普通状语？", "The soil tested, they chose the fertilizer",
          "Having tested the soil, they chose the fertilizer", "Tested by them, the soil was poor",
          "They tested the soil and chose the fertilizer",
          "The soil tested 的逻辑主语 soil 和主句主语 they 不同。"),
        q("哪一句是正确的？", "Time permitting, we will check the irrigation",
          "Time permitted, we will check if time allows us now as a person", "Permitting time, the clock left",
          "Time permitting we will to check",
          "Time permitting 表示如果时间允许。"),
      ], "inferred")

    F("fu_farm", "说明农事过程", 13, 5,
      "能说明耕作步骤，并就产量和土壤给出有依据的看法。", "fu_argue", [
        q("想说土壤需要被检测，哪一句合适？", "The soil needs to be tested",
          "The soil needs to test the farmer", "Tested to be needs the soil", "Soil is testing the lab",
          "needs to be tested 表示被检测。"),
        q("想说如果天气允许就开始收割，哪一句合适？", "Weather permitting, we will start the harvest",
          "Weather permitted by us, the sky starts", "Permitting weather we start to", "Harvest permits the weather",
          "Weather permitting 是独立主格。"),
        q("想说明有机肥可能提高产量，哪一句合适？", "Organic fertilizer may increase the yield",
          "Organic fertilizer may increased the yield", "Organic fertilizer may to increase the yield", "Organic fretilizer may increase the yield",
          "may increase 用来提出有依据的可能。"),
        q("想反驳过度施肥，哪一句合适？", "Too much fertilizer can damage the soil",
          "Damage can the soil fertilizer too", "Fertilizer is always harmless", "Soil damages the sentence",
          "can damage 说明反对的理由。"),
      ])

    _g = "The wheat is to be harvested next week. Soil samples need to be tested first. Weather permitting, the farmers will finish the work in three days."
    R("rw_farm", "读农业短文", 13, 5,
      "读短文，找出必须先做的事和仍然取决于天气的事。", "rw_argue", [
        q(_g + " 小麦什么时候将被收割？", "下周", "昨天", "三年后", "不会收割", "短文写 next week。"),
        q(_g + " 什么需要先被检测？", "土壤样本", "天气", "农民", "灌溉设备的价格", "短文写 Soil samples need to be tested。"),
        q(_g + " 三天内做完取决于什么？", "天气允许", "检测已经失败", "小麦自己决定", "没有条件",
          "Weather permitting 表示取决于天气。"),
        q(_g + " 哪一件事是被做的而不是农民主动发出的动作？", "土壤样本被检测",
          "农民将完成工作", "农民决定日期", "短文没有被动",
          "samples need to be tested 是被动。farmers will finish 是主动。"),
      ])

    R("wr_farm", "写农事安排", 13, 5,
      "能按要点选出安排说明中的句子。", "rw_write_s", [
        q("要点：下周收割、先检测土壤、天气允许就三天做完。哪一句三个要点都有？",
          "The wheat is to be harvested next week, the soil is to be tested first, and weather permitting they will finish in three days",
          "The wheat is ripe", "Soil is important", "Three days is short",
          "三个要点都要出现。"),
        q("安排里用不定式被动，哪一句正确？", "The field is to be irrigated tonight",
          "The field is to irrigate tonight", "The field is to be irrigate tonight", "Irrigated is to the field be",
          "is to be irrigated 表示将被灌溉。"),
        q("哪一句适合作为安排的第一句？", "Here is the plan for the harvest",
          "Here are the plan for the harvest", "Here is the plan for the hravest", "Here is the plan for the harvset",
          "安排可以先写 Here is the plan。"),
        q("哪一句是独立主格？", "Time permitting, we will test two more fields",
          "Having time, we will test two more fields", "We permit the time to test", "Permitting, time tests us",
          "Time permitting 的主语 time 和主句主语 we 不同。"),
      ])
