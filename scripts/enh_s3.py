# -*- coding: utf-8 -*-
"""人教版（2019）选择性必修第三册。单元名按通行目录，册次待核。"""
from enh_tx import V, G, F, R, q


def load():
    V("vo_art", "艺术", 15, 1,
      "认读 sculpture、gallery、exhibition 和 visual。",
      [("sculpture", "雕塑"), ("gallery", "美术馆"), ("exhibition", "展览"), ("visual", "视觉的")], "vo_mind")

    V("vo_gallery", "艺术评论", 15, 1,
      "认读 brush、canvas、realistic 和 abstract。",
      [("brush", "画笔"), ("canvas", "画布"), ("realistic", "写实的"), ("abstract", "抽象的")], "vo_mind")

    G("gr_invneg", "否定副词倒装", 15, 1,
      "能在否定副词放在句首时使用部分倒装。", "invert", [
        q("Never ___ such a sculpture. 表示我从未见过，横线处填哪一个？", "have I seen",
          "I have seen", "did I saw", "I saw", "Never 放在句首，用 have I seen。"),
        q("哪一句是正确的倒装？", "Seldom does she miss an exhibition",
          "Seldom she does miss an exhibition", "Seldom does she misses an exhibition",
          "Seldom misses she an exhibition",
          "Seldom 开头，助动词 does 放在主语前，动词用原形 miss。"),
        q("Little ___ the painter was so young. 横线处填哪一个？", "did we know",
          "we knew", "we did know", "knew we", "Little 放在句首，用 did we know。"),
        q("哪一句没有倒装所以不适合放在否定词开头之后？", "I have never seen the canvas",
          "Never have I seen the canvas", "Rarely do we see such colours", "Not until then did he speak",
          "I have never seen 是否定词在句中，不是句首倒装。"),
      ])

    G("gr_hardly", "hardly 倒装", 15, 1,
      "能用 Hardly had ... when 表示一……就……。", "invert", [
        q("Hardly ___ the gallery when the talk began. 横线处填哪一个？", "had we entered",
          "we had entered", "did we enter", "have we entered", "Hardly 开头用 had we entered，后面接 when。"),
        q("哪一句是正确的？", "Hardly had she finished the painting when the visitors arrived",
          "Hardly she had finished the painting when the visitors arrived",
          "Hardly had she finished the painting than the visitors arrived",
          "Hardly finished she the painting when visitors",
          "Hardly had ... when，不用 than。"),
        q("No sooner ___ down than the lights went out. 横线处填哪一个？", "had the artist sat",
          "the artist had sat", "did the artist sat", "sat the artist",
          "No sooner 用 had the artist sat，后面接 than。"),
        q("Hardly 倒装句里，when 从句通常用什么时态？", "一般过去时", "将来时", "现在完成时", "动词原形",
          "when the visitors arrived 用一般过去时。"),
      ])

    F("fu_art", "描述艺术作品", 15, 1,
      "能描述一幅画或一座雕塑，并说明它是写实还是抽象。", "fu_desc", [
        q("想说从未见过这样的雕塑，并用倒装，哪一句合适？", "Never have I seen such a sculpture",
          "Never I have seen such a sculpture", "Seen have I never such", "Never saw I have such",
          "Never have I seen 是部分倒装。"),
        q("想说一进美术馆讲解就开始了，哪一句合适？", "Hardly had we entered the gallery when the talk began",
          "Hardly we had entered the gallery when the talk began",
          "Hardly had we entered the gallery than the talk began", "Entered hardly we when began",
          "Hardly had we entered when。"),
        q("想说明这幅画是抽象的，哪一句合适？", "The painting is abstract rather than realistic",
          "The painting are abstract rather than realistic", "The painting is abstract rather than raelistic", "The painting is abstract rather than realisitc",
          "rather than 用来对比两种风格。"),
        q("想按步骤看展览，哪一句适合作为第一步？", "First, look at the whole canvas",
          "First, look at the whole cnavas", "Look whole the canvas first does", "First, look at the whole canavs",
          "First 用来开始步骤。"),
      ])

    _a = "Never have I seen such bright colours. Hardly had we entered the gallery when a guide began to explain the sculpture. The painting is abstract, while the statue is realistic."
    R("rw_art", "读艺术短文", 15, 1,
      "推断画和雕像的区别，以及哪一句使用了倒装。", "rw_infer", [
        q(_a + " 作者对颜色的感受是什么？", "从未见过这么鲜艳的", "觉得太暗", "没有看见", "只喜欢雕像",
          "Never have I seen such bright colours。"),
        q(_a + " 讲解什么时候开始？", "他们一进美术馆", "离开之后", "第二天才开始", "没有讲解",
          "Hardly had we entered when a guide began。"),
        q(_a + " 画和雕像有什么不同？", "画是抽象的，雕像是写实的", "都是抽象的", "都是写实的", "短文没有比较",
          "abstract, while the statue is realistic。"),
        q(_a + " 哪一句是倒装？", "Never have I seen such bright colours",
          "The painting is abstract", "The statue is realistic", "A guide began to explain",
          "Never have I seen 把助动词放在主语前。"),
      ])

    R("wr_art", "写观展笔记", 15, 1,
      "能按要点选出笔记中的句子。", "rw_write_s", [
        q("要点：从未见过这种颜色、一进馆就开始讲解、画抽象而雕像写实。哪一句三个要点都有？",
          "Never have I seen such colours, hardly had we entered when the talk began, and the painting is abstract while the statue is realistic",
          "The colours are bright", "The guide spoke", "I like art",
          "三个要点都要出现。"),
        q("笔记用否定词倒装，哪一句正确？", "Rarely do we see this kind of brushwork",
          "Rarely we do see this kind of brushwork", "Rarely does we see this kind", "See we rarely this kind",
          "Rarely do we see，动词用原形。"),
        q("哪一句适合作为笔记的第一句？", "This note records one visit to a gallery",
          "This note record one visit to a gallery", "This note records one visit to an gallery", "This note rceords one visit to a gallery",
          "笔记可以先写 This note records。"),
        q("哪一句 Hardly 用对了？", "Hardly had the talk ended when we left",
          "Hardly the talk had ended when we left", "Hardly had the talk ended than we left",
          "Hardly ended the talk when we",
          "Hardly had ... when。"),
      ])

    V("vo_lifestyle", "健康生活", 15, 2,
      "认读 lifestyle、stress、routine 和 balance。",
      [("lifestyle", "生活方式"), ("stress", "压力"), ("routine", "日常安排"), ("balance", "平衡")], "vo_mind")

    V("vo_stressw", "身心习惯", 15, 2,
      "认读 anxiety、nutrition、sufficient 和 refresh。",
      [("anxiety", "焦虑"), ("nutrition", "营养"), ("sufficient", "充足的"), ("refresh", "使恢复精神")], "vo_mind")

    G("gr_invonly", "only 与 so、neither 倒装", 15, 2,
      "能在 only 加状语、so 和 neither 开头时倒装。", "invert", [
        q("Only then ___ how tired he was. 横线处填哪一个？", "did he realise",
          "he realised", "he did realise", "realised he", "Only then 开头，用 did he realise。"),
        q("I need sufficient sleep. 对方也是，哪一句正确？", "So do I",
          "So I do", "So did I am", "Neither do I", "同样需要，用 So do I。So I do 是强调我确实如此，主语没倒。"),
        q("He cannot keep the routine. 她也不能，哪一句正确？", "Neither can she",
          "Neither she can", "So can she", "Neither can't she",
          "否定的“也不”用 Neither can she。"),
        q("哪一句是正确的？", "Only after a walk did she feel refreshed",
          "Only after a walk she felt refreshed", "Only after a walk did she felt refreshed",
          "Only she felt refreshed after a walk as inversion",
          "Only after a walk 是状语提前，用 did she feel。"),
      ])

    G("gr_invthere", "there 与方位倒装", 15, 2,
      "能用 There 或地点副词放在句首，把主语放到动词后面。", "invert", [
        q("There ___ a quiet garden behind the gym. 横线处填哪一个？", "stands",
          "stand", "standing", "is stand", "主语 a quiet garden 是单数，用 stands。"),
        q("哪一句是倒装？", "In front of the library stands an old tree",
          "An old tree stands in front of the library", "Stands in front an old tree the",
          "In front of the library an old tree stands it",
          "地点短语在句首，动词 stands 在主语前面。"),
        q("On the wall ___ two posters about nutrition. 横线处填哪一个？", "hang",
          "hangs", "hanging", "is hang", "主语 two posters 是复数，用 hang。"),
        q("这种倒装通常放在句首的是什么？", "地点或 there", "否定的人名", "only 加主语", "so 加形容词",
          "地点状语或 there 提前，主语后置。"),
      ], "inferred")

    F("fu_healths", "讨论健康习惯", 15, 2,
      "能说明压力、睡眠和营养，并给出有依据的建议。", "fu_argue", [
        q("想说直到那时他才意识到自己的压力，哪一句合适？", "Only then did he realise his stress",
          "Only then he realised his stress", "Then only realised he stress", "Did he realise only then not",
          "Only then did he realise。"),
        q("对方说需要充足睡眠，你也一样，应回答什么？", "So do I",
          "So I do if you mean I really do and the grammar is the short answer of agreement wait no",
          "Neither do I", "So did sleep I",
          "同意对方的需要，用 So do I。"),
        q("想说图书馆前有一棵树，并用倒装，哪一句合适？", "In front of the library stands an old tree",
          "In front of the library an old tree stands quietly as normal order", "Stands an old tree front in",
          "There stand an old tree",
          "地点在句首时动词在单数主语前。There stand 与单数主语不一致。"),
        q("想建议用步行缓解焦虑，哪一句合适？", "A short walk can refresh you and reduce anxiety",
          "A short walk can refreshed you and reduce anxiety", "A short walk can to refresh you and reduce anxiety", "A short walk can rferesh you and reduce anxiety",
          "can refresh 说明建议的依据。"),
      ])

    _h = "Only after he changed his routine did Tom sleep well. He says he needs sufficient nutrition, and so does his sister. Behind the dormitory stands a garden where they walk."
    R("rw_healths", "读健康短文", 15, 2,
      "找出改变习惯之后的结果，以及 so 倒装所指的人。", "rw_argue", [
        q(_h + " Tom 什么时候才睡得好？", "改变日常安排之后", "改变之前", "只在花园里吃饭时", "短文没说",
          "Only after he changed his routine。"),
        q(_h + " 他妹妹和谁有同样的需要？", "和 Tom 一样需要充足营养", "不需要营养", "只需要步行", "没有妹妹",
          "so does his sister 指前面的需要营养。"),
        q(_h + " 宿舍后面有什么？", "一座花园", "一家医院", "一幅抽象画", "没有地方", "短文写 stands a garden。"),
        q(_h + " 哪一句是 only 倒装？", "Only after he changed his routine did Tom sleep well",
          "He says he needs sufficient nutrition", "Behind the dormitory stands a garden", "They walk in the garden",
          "did Tom sleep 是 only 状语提前造成的倒装。"),
      ])

    R("wr_healths", "写健康建议", 15, 2,
      "能按要点选出建议中的句子。", "rw_write_s", [
        q("要点：改变安排后才睡好、妹妹也需要营养、宿舍后有花园。哪一句三个要点都有？",
          "Only after he changed his routine did he sleep well, so does his sister need good nutrition, and behind the dormitory stands a garden",
          "He sleeps well", "His sister is busy", "Gardens are quiet",
          "三个要点都要出现。"),
        q("建议里用 only 倒装，哪一句正确？", "Only by walking did she reduce her anxiety",
          "Only by walking she reduced her anxiety", "Only by walking did she reduced her anxiety",
          "Reduced she only by walking",
          "Only by walking did she reduce。"),
        q("哪一句适合作为建议的第一句？", "A balanced routine can reduce stress",
          "A balanced routine can reduced stress", "A balanced routine can to reduce stress", "A blaanced routine can reduce stress",
          "建议可以先给出总的看法。"),
        q("对方说自己不能早睡，你也不能，哪一句正确？", "Neither can I",
          "So can I", "Neither I can", "Neither can't I",
          "否定的“也不”用 Neither can I。"),
      ])

    V("vo_climate", "环境保护", 15, 3,
      "认读 climate、carbon、emission 和 renewable。",
      [("climate", "气候"), ("carbon", "碳"), ("emission", "排放"), ("renewable", "可再生的")], "vo_mind")

    V("vo_pollute", "污染", 15, 3,
      "认读 pollution、drought、policy 和 sustainable。",
      [("pollution", "污染"), ("policy", "政策"), ("sustainable", "可持续的"), ("melt", "融化")], "vo_mind")

    G("gr_cleft", "强调句", 15, 3,
      "能用 It is 或 It was 加被强调部分加 that 或 who。", "emph", [
        q("是政策改变了排放，而不是口号。强调政策，哪一句正确？", "It is the policy that changes the emissions",
          "It is the policy which changes the emissions as a cleft", "It was the policy what changed",
          "That it is the policy changes",
          "强调句用 It is ... that。"),
        q("昨天是林提交了报告。强调 Lin，哪一句正确？", "It was Lin who submitted the report",
          "It was Lin which submitted the report", "It was Lin whom submitted the report",
          "It was Lin submitted the report",
          "强调人可以用 who，不能漏掉 who 或 that。"),
        q("她在实验室发现了问题。强调地点，哪一句正确？", "It was in the lab that she found the problem",
          "It was in the lab where she found the problem", "It was in the lab which she found the problem",
          "It was the lab where she found as if it were only a relative clause without It was matching",
          "强调地点状语用 It was in the lab that，不用 where。"),
        q("去掉 It is 或 It was 和 that 之后，剩下的部分应当怎样？", "仍然是一个完整的句子",
          "必须剩下一个名词", "必须变成疑问句", "不能有动词",
          "It was Lin that submitted it 去掉框架后是 Lin submitted it。"),
      ])

    G("gr_cleftvs", "强调句和定语从句", 15, 3,
      "能把 It is ... that 强调句和 It is ... that 容易混淆的定语从句分开。", "emph", [
        q("哪一句是强调句？", "It was the drought that forced them to move",
          "It is a policy that few people like", "It is a problem which we can solve",
          "The policy that he wrote is new",
          "去掉 It was 和 that 后，the drought forced them to move 仍然完整，所以是强调句。"),
        q("哪一句是定语从句？", "It is a report that explains carbon emissions",
          "It was carbon that the report explained", "It is today that the policy starts",
          "It was she who wrote the report",
          "a report that explains 里 that 在从句中作主语，不能整段去掉后仍成句。"),
        q("It was in 2020 ___ the emissions fell. 强调时间，横线处填哪一个？", "that",
          "when", "which", "where", "强调句即使强调时间也用 that，不用 when。"),
        q("判断强调句的一个办法是什么？", "去掉 It is 或 It was 和 that 后句子仍然完整",
          "看见 that 就一定是定语从句", "句首有 It 就一定是强调", "必须用 which",
          "能还原成普通句子的是强调句。"),
      ], "inferred")

    F("fu_env", "讨论环境政策", 15, 3,
      "能说明排放、干旱和政策，并强调真正起作用的因素。", "fu_argue", [
        q("想强调是可再生能源降低了排放，哪一句合适？", "It is renewable energy that reduces the emissions",
          "It is renewable energy which reduces the emissions in a cleft", "Renewable energy that it is reduces",
          "It is renewable energy what reduces",
          "强调句用 that。"),
        q("想说是干旱迫使人们搬家，哪一句合适？", "It was the drought that forced people to move",
          "It was the drought which forced people as a relative only", "The drought it was forced people",
          "Forced the drought people that",
          "It was the drought that forced。"),
        q("想建议政策应当可持续，哪一句合适？", "The policy should be sustainable",
          "The policy should be ssutainable", "The policy should be sustainalbe", "The policy should be sutainable",
          "should be sustainable 用来提出看法。"),
        q("想区分强调句和定语从句，哪一句是强调时间？", "It was last winter that the ice melted faster",
          "It was a winter that nobody liked", "Last winter melted the ice", "It was last winter when the ice as a cleft wrongly",
          "强调时间用 that，不用 when。"),
      ])

    _e = "It is the new policy that cuts carbon emissions. It was the long drought that made the lake smaller. Renewable energy is useful, but the policy decides how fast it is used."
    R("rw_env", "读环境短文", 15, 3,
      "找出作者认为真正起作用的因素，以及论点与依据。", "rw_argue", [
        q(_e + " 什么在削减碳排放？", "新政策", "干旱", "湖", "短文没有说", "It is the new policy that cuts。"),
        q(_e + " 湖变小的原因是什么？", "长期干旱", "新政策", "可再生能源", "没有原因",
          "It was the long drought that made the lake smaller。"),
        q(_e + " 作者认为决定使用速度的是什么？", "政策", "只有天气", "湖本身", "没有决定因素",
          "the policy decides how fast。"),
        q(_e + " 这段的论点更接近哪一种？", "可再生能源有用，但政策决定推进速度",
          "干旱比政策更有用", "排放已经与政策无关", "湖变小是政策造成的",
          "useful, but the policy decides 是论点。"),
      ])

    R("wr_env", "写环境评论", 15, 3,
      "能按要点选出评论中的句子。", "rw_write_s", [
        q("要点：政策削减排放、干旱让湖变小、政策决定推进速度。哪一句三个要点都有？",
          "It is the policy that cuts emissions, it was the drought that made the lake smaller, and the policy decides the speed",
          "The policy is new", "The lake is smaller", "Energy is renewable",
          "三个要点都要出现。"),
        q("评论强调人，哪一句正确？", "It was Dr Lin who explained the data",
          "It was Dr Lin which explained the data", "It was Dr Lin whom explained the data",
          "It was Dr Lin explained the data",
          "强调人用 who 或 that。"),
        q("哪一句适合作为评论的第一句？", "The evidence points to policy, not only to weather",
          "The evidence point to policy, not only to weather", "The eivdence points to policy, not only to weather", "The evidecne points to policy, not only to weather",
          "评论可以先写出论点。"),
        q("哪一句是强调句而不是定语从句？", "It was in this town that the emissions fell",
          "It is a town that suffers from pollution", "The town that we visited is small",
          "Pollution which we measured is high",
          "去掉 It was 和 that 后 this town 加 the emissions fell 需要 in，但 in this town the emissions fell 完整，所以是强调地点。"),
      ])

    V("vo_brave", "逆境", 15, 4,
      "认读 adversity、courage、survive 和 despair。",
      [("adversity", "逆境"), ("courage", "勇气"), ("survive", "幸存"), ("despair", "绝望")], "vo_mind")

    V("vo_survive", "坚持", 15, 4,
      "认读 perseverance、crew、hope 和 ordeal。",
      [("perseverance", "毅力"), ("crew", "全体船员"), ("hope", "希望"), ("ordeal", "磨难")], "vo_mind")

    G("gr_doemph", "用 do 强调谓语", 15, 4,
      "能用 do、does 或 did 强调谓语，表示确实如此。", "emph", [
        q("她当时确实活了下来。强调谓语，哪一句正确？", "She did survive the ordeal",
          "She did survived the ordeal", "She does survived the ordeal", "Did she survive the ordeal as a statement of emphasis without inversion question mark only",
          "did 后面用原形 survive。"),
        q("我现在确实希望他们平安。哪一句正确？", "I do hope they are safe",
          "I do hoped they are safe", "I does hope they are safe", "Hope do I they are",
          "主语是 I，用 do hope。"),
        q("哪一句在强调谓语？", "The crew did reach the island",
          "It was the crew that reached the island", "The crew reached the island", "Did the crew reach the island",
          "did reach 是用助动词强调谓语。It was the crew that 是强调主语。"),
        q("does 强调时，后面的动词用什么形式？", "原形", "第三人称单数", "过去式", "过去分词",
          "does 已经表示第三人称，后面用 hope 这样的原形。"),
      ])

    G("gr_invif", "省略 if 的倒装", 15, 4,
      "能把虚拟条件句的 if 省去，把 had、were 或 should 放到句首。", "invert", [
        q("如果当时知道危险，他们就会改变航线。省略 if，哪一句正确？",
          "Had they known the danger, they would have changed course",
          "Had they known the danger, they would change course yesterday",
          "If had they known the danger, they would have changed",
          "Did they know the danger, they would have changed",
          "Had they known 等于 If they had known。"),
        q("Were I in their place, I ___ the same. 表示现在，横线处填哪一个？", "would do",
          "would have done", "did", "had done", "Were I 表示与现在相反，主句用 would do。"),
        q("哪一句省略了 if？", "Should the storm return, we would stay on the island",
          "If the storm should return, we would stay", "The storm should return and we stay",
          "Return the storm if we would",
          "Should the storm return 是省略 if 的倒装。"),
        q("Had I listened 还原成带 if 的从句是哪一个？", "If I had listened",
          "If I listened", "If I have listened", "If had I listened",
          "Had I listened 对应 If I had listened。"),
      ])

    F("fu_adv", "讨论逆境", 15, 4,
      "能说明人物如何面对磨难，并强调确实做到的事。", "fu_argue", [
        q("想强调船员确实到达了岛上，哪一句合适？", "The crew did reach the island",
          "The crew did reached the island", "Reached did the crew", "The crew does reached",
          "did reach 强调谓语。"),
        q("想说如果当时知道就会改变航线，并省略 if，哪一句合适？",
          "Had they known, they would have changed course",
          "Had they known, they changed course", "If had they known, they would have changed",
          "Known had they, they would changed",
          "Had they known 等于 If they had known。"),
        q("想说毅力给了他们希望，哪一句合适？", "Perseverance gave them hope",
          "Preseverance gave them hope", "Gave perseverance them", "Perseveracne gave them hope",
          "gave them hope 说明毅力的作用。"),
        q("想用强调句强调是勇气而不是运气，哪一句合适？", "It was courage that kept them going",
          "It was courage which kept them going as a cleft", "Courage that it was kept",
          "It was courage what kept",
          "强调用 It was courage that。"),
      ])

    _d = "Had the crew lost hope, they would not have survived. They did keep a small fire at night. It was perseverance that carried them through the ordeal."
    R("rw_adv", "读逆境短文", 15, 4,
      "推断哪一句是假设，哪一句是作者强调的事实。", "rw_infer", [
        q(_d + " 如果船员失去希望，结果会怎样？", "就不会幸存", "仍然会生火", "毅力会消失", "短文说他们失去了希望",
          "would not have survived 是假设的结果。"),
        q(_d + " 他们夜里确实做了什么？", "保持了一小堆火", "离开了岛", "放弃了", "没有做事",
          "did keep a small fire 表示确实保持了火。"),
        q(_d + " 作者强调是什么支撑他们度过磨难？", "毅力", "运气", "火本身单独", "绝望",
          "It was perseverance that carried them。"),
        q(_d + " 哪一句是已经发生的事实？", "他们夜里留着火", "他们失去了希望", "他们没有幸存", "毅力没有起作用",
          "did keep 是事实。Had the crew lost hope 是假设。"),
      ])

    R("wr_adv", "写读后感", 15, 4,
      "能按要点选出生后感中的句子。", "rw_write_s", [
        q("要点：失去希望就不会幸存、夜里确实留了火、毅力支撑他们。哪一句三个要点都有？",
          "Had they lost hope they would not have survived, they did keep a fire, and it was perseverance that carried them",
          "They kept a fire", "Hope matters", "The ordeal was long",
          "三个要点都要出现。"),
        q("读后感省略 if，哪一句正确？", "Were I there, I would try to help",
          "Were I there, I would have tried tomorrow as now", "If were I there, I would try",
          "Was I there, I would try",
          "Were I there 等于 If I were there。"),
        q("哪一句适合作为读后感的第一句？", "The story shows courage in adversity",
          "The story show courage in adversity", "The story shows courage in avdersity", "The story shows courage in adverstiy",
          "读后感可以先写出主题。"),
        q("哪一句用 do 强调谓语？", "I do admire their perseverance",
          "It is perseverance that I admire", "I admire their perseverance", "Do I admire their perseverance",
          "do admire 是强调谓语。问句 Do I admire 不是强调。"),
      ])

    V("vo_poemw", "诗歌", 15, 5,
      "认读 poem、rhyme、verse 和 imagery。",
      [("poem", "诗"), ("rhyme", "韵"), ("verse", "诗行"), ("imagery", "意象")], "vo_mind")

    V("vo_rhyme", "诗歌赏析", 15, 5,
      "认读 metaphor、rhythm、recite 和 emotion。",
      [("metaphor", "比喻"), ("rhythm", "节奏"), ("recite", "朗诵"), ("emotion", "情感")], "vo_mind")

    G("gr_ellip", "省略", 15, 5,
      "能省略重复的动词，并在不定式里保留 to。", "ellip", [
        q("I wanted to recite the poem, and he wanted ___. 横线处填哪一个？", "to",
          "to recite the poem again in full", "recite", "/",
          "省略不定式时保留 to。"),
        q("哪一句省略得正确？", "She can recite, and so can he",
          "She can recite, and so he", "She can recite, and so can", "She can, and he can recite so",
          "so can he 省略了 recite。"),
        q("He didn't join the reading, but I wanted him ___. 横线处填哪一个？", "to",
          "to join", "join", "joining", "wanted him to 可以省去后面的 join，但要留 to。题目只留 to 是完整的省略。"),
        q("哪一句不该把 to 省掉？", "I asked her to, but she refused",
          "I can swim and she can too", "He is tired and she is too", "Some stayed and others left",
          "asked her to 的 to 要保留。其余几句省略的是重复的动词或表语，本来就没有 to。"),
      ])

    G("gr_ellipcmp", "比较句中的省略", 15, 5,
      "能在比较结构里省略重复的谓语，避免把比较对象写错。", "ellip", [
        q("这首诗比那首更难朗诵。哪一句正确？", "This poem is harder to recite than that one is",
          "This poem is harder to recite than that one", "This poem is more harder to recite than that",
          "This poem is harder to recite than recite that one",
          "than that one is 省略了 hard，比较对象是另一首诗。"),
        q("她读得比以前好。哪一句正确？", "She reads better than she did before",
          "She reads better than before she did the poem", "She reads more better than she did",
          "She reads better than did",
          "than she did before 里 did 代替 read。"),
        q("哪一句的比较对象是清楚的？", "The rhythm is stronger than the imagery is",
          "The rhythm is stronger than the imagery", "Stronger the rhythm is than", "The rhythm is more strong than imagery is it",
          "than the imagery is 明确在比较节奏和意象。"),
        q("比较句里省略的主要目的是什么？", "避免重复已经出现的动词或形容词", "让句子变成倒装疑问", "取消比较对象", "强调虚拟",
          "省略是为了不重复，但比较对象要还在。"),
      ], "inferred")

    F("fu_poem", "谈论诗歌", 15, 5,
      "能描述一首诗的意象和节奏，并比较两首诗。", "fu_desc", [
        q("想说自己也想朗诵，并省略重复动词，哪一句合适？", "She wants to recite, and I want to as well",
          "She wants to recite, and I want as well", "She wants to recite, and I want to recite to",
          "Want to I and she recite",
          "I want to 保留 to，省去 recite。"),
        q("想说这首比那首节奏更强，哪一句合适？", "This poem has a stronger rhythm than that one does",
          "This poem has a stronger rhythm than that one", "This poem has more stronger rhythm than that",
          "Stronger has this poem than does",
          "than that one does 代替 has a strong rhythm。"),
        q("想说明比喻表达了情感，哪一句合适？", "The metaphor carries the emotion of the verse",
          "The metaphor carrie the emotion of the verse", "The mteaphor carries the emotion of the verse", "The metapohr carries the emotion of the verse",
          "carries the emotion 用来解释比喻的作用。"),
        q("朋友背得出，你也背得出，哪一句省略得对？", "He can recite the verse, and so can I",
          "He can recite the verse, and so I", "He can recite, and so can", "So can I recite he",
          "so can I 省略 recite the verse。"),
      ])

    _p = "The first poem is harder to recite than the second is. Lin wanted to try the long verse, and her friend wanted to as well. Its imagery is quiet, but the rhythm is strong."
    R("rw_poem", "读诗歌短文", 15, 5,
      "推断哪一首更难，以及省略掉的动词是什么。", "rw_infer", [
        q(_p + " 哪一首更难朗诵？", "第一首", "第二首", "两首一样", "短文没有比较",
          "The first poem is harder ... than the second。"),
        q(_p + " 朋友也想做什么？", "试一试那首长诗", "放弃朗诵", "改写节奏", "只看意象",
          "wanted to as well 省去的是 try the long verse。"),
        q(_p + " 意象和节奏分别怎样？", "意象安静，节奏强", "都很安静", "节奏很弱", "没有意象",
          "imagery is quiet, but the rhythm is strong。"),
        q(_p + " wanted to 后面省去的是哪一个意思？", "试那首长诗", "比第二首难", "节奏很强", "没有省略",
          "and her friend wanted to 承接 wanted to try the long verse。"),
      ])

    R("wr_poem", "写赏析句", 15, 5,
      "能按要点选出赏析中的句子。", "rw_write_s", [
        q("要点：第一首更难朗诵、朋友也想试长诗、意象安静但节奏强。哪一句三个要点都有？",
          "The first is harder to recite than the second is, her friend wanted to try the long verse too, and the imagery is quiet but the rhythm is strong",
          "The first poem is hard", "Her friend likes poetry", "Rhythm matters",
          "三个要点都要出现。"),
        q("赏析里省略不定式，哪一句正确？", "I hoped to read it aloud, and she hoped to as well",
          "I hoped to read it aloud, and she hoped as well", "I hoped to, and she hoped recite",
          "Hoped to she and I",
          "hoped to 保留 to。"),
        q("哪一句适合作为赏析的第一句？", "The poem uses quiet imagery and a strong rhythm",
          "The poem uses quiet imagery and an strong rhythm", "The poem uses quiet iamgery and a strong rhythm", "The poem uses quiet imagrey and a strong rhythm",
          "赏析可以先概括意象和节奏。"),
        q("哪一句的比较是清楚的？", "She recites more clearly than she did last year",
          "She recites more clearly than last year she did the poem better", "She recites more clearer than she did",
          "More clearly she recites than did",
          "than she did last year 代替 recited。"),
      ])
