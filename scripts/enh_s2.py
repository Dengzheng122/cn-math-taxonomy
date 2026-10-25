# -*- coding: utf-8 -*-
"""人教版（2019）选择性必修第二册。单元名按通行目录，册次待核。"""
from enh_tx import V, P, G, F, R, q


def load():
    V("vo_lab", "科学研究", 14, 1,
      "认读 hypothesis、experiment、data 和 evidence。",
      [("hypothesis", "假设"), ("experiment", "实验"), ("data", "数据"), ("evidence", "证据")], "vo_life")

    V("vo_theory2", "科学结论", 14, 1,
      "认读 conclude、variable、sample 和 method。",
      [("conclude", "得出结论"), ("variable", "变量"), ("sample", "样本"), ("method", "方法")], "vo_life")

    G("gr_subnow", "虚拟语气", 14, 1,
      "能用 If I were 和 would 加原形表达与现在事实相反的假设。", "subj", [
        q("与现在事实相反：如果我是你，我会先核对数据。哪一句正确？", "If I were you, I would check the data",
          "If I am you, I would check the data", "If I were you, I will check the data",
          "If I were you, I checked the data",
          "与现在相反，从句用 were，主句用 would 加原形。"),
        q("If she ___ more evidence, she would be more certain. 横线处填哪一个？", "had",
          "has", "have", "will have", "与现在相反的从句用过去式 had。"),
        q("哪一句是与现在事实相反的虚拟？", "If he knew the method, he would help us",
          "If he knows the method, he will help us", "If he knew the method, he helps us",
          "If he knows the method, he would help us",
          "knew 配 would help，表示现在并不知道。"),
        q("If I ___ a larger sample, I would trust the result. 横线处填哪一个？", "had",
          "have", "has", "am having", "从句用 had，主句用 would trust。"),
      ])

    G("gr_butfor", "but for 与虚拟", 14, 1,
      "能用 But for 表示“要不是”，并搭配 would have done 或 would do。", "subj", [
        q("要不是你的帮助，我当时就会失败。哪一句正确？", "But for your help, I would have failed",
          "But for your help, I failed", "But for your help, I would fail yesterday",
          "But for your help, I had failed",
          "与过去相反用 would have failed。"),
        q("But for the evidence, we ___ still unsure. 表示现在仍会不确定，横线处填哪一个？", "would be",
          "would have been yesterday only", "are", "were be", "说的是现在的结果，用 would be。"),
        q("哪一句用 but for 表示与过去相反？", "But for the experiment, they would have chosen the wrong method",
          "But for the experiment, they chose the wrong method", "But for the experiment, they will choose",
          "But for the experiment, they had chose",
          "would have chosen 是与过去相反的结果。"),
        q("But for 在这种句子里更接近哪一个意思？", "如果没有", "因为有了所以真实发生", "在……之后", "除了物品清单",
          "But for your help 意思是如果没有你的帮助。"),
      ], "inferred")

    F("fu_sci", "说明科学假设", 14, 1,
      "能说明假设、证据和还不能确定的地方。", "fu_argue", [
        q("想说如果有更多证据就会更确定，哪一句合适？", "If we had more evidence, we would be more certain",
          "If we have more evidence, we would be more certain", "If we had more evidence, we are more certain",
          "If we would have more evidence, we are certain",
          "与现在相反用 had 配 would be。"),
        q("想说要不是那次实验，结论就会不同，哪一句合适？", "But for that experiment, the conclusion would be different",
          "But for that experiment, the conclusion is different in the past wish", "Experiment but for different is",
          "Would be the conclusion but for real",
          "But for 加 would be 表示假如没有。"),
        q("想指出数据还不够，哪一句合适？", "The data are not enough to support the hypothesis",
          "The data are not enough to support the hpyothesis", "The data are not enough to support the hypotheiss", "The data are not enough to support the hyothesis",
          "are not enough to support 用来限定结论。"),
        q("想建议先控制变量，哪一句合适？", "We should control the variables first",
          "Control should the variables we", "We should controlled the variables first", "We should to control the variables first",
          "should control 用来提出下一步。"),
      ])

    _s = "If the team had a larger sample, they would trust the result more. But for one failed experiment, they would have published the paper last month. The data are useful, but they do not prove the whole hypothesis."
    R("rw_sci", "读科学短文", 14, 1,
      "找出论点、还缺少的证据，以及作者没有直接说满的限度。", "rw_argue", [
        q(_s + " 样本更大的话，他们会怎样？", "更信任这个结果", "马上放弃", "不再做实验", "已经发表了",
          "would trust the result more 是假设的结果。"),
        q(_s + " 要不是那次失败的实验，他们上个月会怎样？", "发表论文", "扩大样本", "证明全部假设", "停止研究",
          "would have published the paper last month。"),
        q(_s + " 数据现在能证明什么？", "还不能证明整个假设", "已经证明一切", "没有任何用处", "代替了实验",
          "短文写 do not prove the whole hypothesis。"),
        q(_s + " 作者的论点更接近哪一种？", "数据有用，但还不足以证明全部假设",
          "实验失败所以数据无用", "论文已经发表", "样本已经足够",
          "useful, but they do not prove 是在限定论点。"),
      ])

    R("wr_sci", "写实验评论", 14, 1,
      "能按要点选出评论中的句子。", "rw_write_s", [
        q("要点：样本更大就会更信任、要不是失败实验上个月会发表、数据还不能证明全部假设。哪一句三个要点都有？",
          "If they had a larger sample they would trust it more, but for the failed experiment they would have published, and the data do not prove the whole hypothesis",
          "The sample is small", "The experiment failed", "Data can be useful",
          "三个要点都要出现。"),
        q("评论里表示与现在相反，哪一句正确？", "If I were on the team, I would repeat the test",
          "If I am on the team, I would repeat the test", "If I were on the team, I will repeat the test",
          "If I were on the team, I repeated the test",
          "were 配 would repeat。"),
        q("哪一句适合作为评论的第一句？", "The hypothesis is interesting but not fully proved",
          "The hypothesis is interest but not fully proved", "The hypothesis is itneresting but not fully proved", "The hypothesis is interestnig but not fully proved",
          "评论可以先写出限度 not fully proved。"),
        q("哪一句用 But for 谈过去？", "But for the error, they would have finished",
          "But for the error, they finished", "But for the error, they finish tomorrow",
          "But for the error, they had finish",
          "would have finished 对应过去。"),
      ])

    V("vo_exchange", "跨文化交流", 14, 2,
      "认读 exchange、abroad、adapt 和 homesick。",
      [("exchange", "交流"), ("abroad", "在国外"), ("adapt", "适应"), ("homesick", "想家的")], "vo_life")

    V("vo_host", "寄宿家庭", 14, 2,
      "认读 host、custom、misunderstand 和 fluent。",
      [("host", "主人"), ("custom", "习俗"), ("misunderstand", "误解"), ("fluent", "流利的")], "vo_life")

    G("gr_subpast", "与过去事实相反的虚拟", 14, 2,
      "能在从句用 had done，在主句用 would have done。", "subj", [
        q("如果我当时更努力适应，我就会少一些误会。哪一句正确？",
          "If I had adapted faster, I would have had fewer misunderstandings",
          "If I adapted faster, I would have had fewer misunderstandings",
          "If I had adapted faster, I would have less misunderstandings",
          "If I have adapted faster, I would have fewer misunderstandings",
          "与过去相反：had adapted 配 would have had。fewer 修饰可数的 misunderstandings。"),
        q("If she ___ abroad earlier, she would have been more fluent. 横线处填哪一个？", "had gone",
          "went", "has gone", "would go", "从句用 had gone。"),
        q("哪一句是与过去事实相反？", "If he had asked his host, he would have avoided the mistake",
          "If he asked his host, he would avoid the mistake now", "If he had asked, he will avoid it",
          "If he asks, he would have avoided it",
          "had asked 配 would have avoided。"),
        q("If they ___ the custom, they would not have been so homesick. 横线处填哪一个？", "had understood",
          "understood", "understand", "have understood", "与过去相反的从句用 had understood。"),
      ])

    G("gr_mixsub", "错综时间虚拟", 14, 2,
      "能在从句指过去、主句指现在时，分别使用 had done 和 would do。", "subj", [
        q("如果当时听了主人的建议，我现在就会更流利。哪一句正确？",
          "If I had followed the advice, I would be more fluent now",
          "If I had followed the advice, I would have been more fluent now",
          "If I followed the advice, I would be more fluent now",
          "If I had followed the advice, I am more fluent now",
          "从句是过去，主句是现在，用 had followed 配 would be now。"),
        q("If she had stayed abroad, she ___ the language now. 横线处填哪一个？", "would speak",
          "would have spoken", "spoke", "had spoken", "now 说明结果在现在，用 would speak。"),
        q("哪一句是错综时间？", "If he had learned the custom then, he would not feel confused now",
          "If he had learned the custom, he would not have felt confused then",
          "If he learned the custom, he would not feel confused",
          "If he learns the custom, he will not feel confused",
          "then 在从句，now 在主句，时间不一致。"),
        q("主句有 now 时，更常见的谓语是哪一种？", "would 加原形", "would have 加过去分词", "一般现在时", "had 加过去分词",
          "现在的结果用 would do，不用 would have done。"),
      ], "inferred")

    F("fu_bridge", "比较文化差异", 14, 2,
      "能比较习俗差异，并说明如果当时知道就会怎样。", "fu_argue", [
        q("想说如果当时问了主人就不会误会，哪一句合适？",
          "If I had asked my host, I would not have misunderstood the custom",
          "If I asked my host, I would not have misunderstood", "If I had asked, I will not misunderstand",
          "If I have asked, I would not misunderstood",
          "过去的假设用 had asked 配 would not have misunderstood。"),
        q("想说早知道习俗的话现在不会想家，哪一句合适？",
          "If I had known the custom, I would not feel so homesick now",
          "If I had known the custom, I would not have felt homesick now",
          "If I knew the custom then, I feel fine now", "Had known I, I am not homesick",
          "过去的条件加现在的结果：would not feel now。"),
        q("想礼貌地承认自己还不够流利，哪一句合适？", "I am not fluent yet, so I may misunderstand",
          "I am not fluent yet, so I may misunderstanded", "I am not fluent yet, so I may to misunderstand", "I is not fluent yet, so I may misunderstand",
          "so 连接原因和可能的误会。"),
        q("想建议交换生先了解习俗，哪一句合适？", "Exchange students should learn local customs first",
          "Should learn customs students exchange", "Exchange students should learned local customs first", "Exchange students should to learn local customs first",
          "should learn 用来提建议。"),
      ])

    _e = "If Lin had asked her host, she would not have worn the wrong clothes to the dinner. If she had known that custom, she would feel less embarrassed now. She is still learning, and her host is patient."
    R("rw_bridge", "读交流短文", 14, 2,
      "推断当时发生了什么，以及现在还剩下什么感受。", "rw_infer", [
        q(_e + " 如果当时问了主人，她就不会怎样？", "穿错衣服去吃饭", "感到尴尬到现在", "学习语言", "遇到耐心的主人",
          "would not have worn the wrong clothes 是当时可以避免的事。"),
        q(_e + " 现在还可能有的感受是什么？", "没那么尴尬，如果她当时知道习俗", "已经完全不想家", "不再学习", "主人不耐烦",
          "would feel less embarrassed now 是现在的结果。"),
        q(_e + " 主人是怎样的人？", "有耐心", "很生气", "不在家", "不会说当地话", "短文写 her host is patient。"),
        q(_e + " 哪一句是已经发生的事实，而不是假设？", "她仍在学习，主人有耐心",
          "她当时问了主人", "她没有穿错衣服", "她现在一点也不尴尬",
          "最后一句是事实。前面两句都是 If 假设。"),
      ])

    R("wr_bridge", "写交流反思", 14, 2,
      "能按要点选出反思中的句子。", "rw_write_s", [
        q("要点：当时问了就不会穿错、知道习俗现在会少些尴尬、主人有耐心。哪一句三个要点都有？",
          "If I had asked I would not have worn the wrong clothes, if I had known the custom I would feel less embarrassed now, and my host is patient",
          "I wore the wrong clothes", "I feel embarrassed", "My host is kind",
          "三个要点都要出现。"),
        q("反思里谈过去，哪一句正确？", "If I had listened, I would have avoided the mistake",
          "If I listened, I would have avoided the mistake", "If I had listened, I will avoid the mistake",
          "If I have listened, I would avoided the mistake",
          "had listened 配 would have avoided。"),
        q("哪一句适合作为反思的第一句？", "I misunderstood a custom at dinner",
          "I misunderstood an custom at dinner", "I msiunderstood a custom at dinner", "I miunderstood a custom at dinner",
          "反思可以先写出发生的事。"),
        q("哪一句是错综时间虚拟？", "If I had prepared, I would be calmer now",
          "If I had prepared, I would have been calmer then", "If I prepared, I would be calmer",
          "If I prepare, I will be calmer",
          "had prepared 指过去，would be now 指现在。"),
      ])

    V("vo_dish", "饮食文化", 14, 3,
      "认读 recipe、ingredient、flavour 和 appetite。",
      [("recipe", "食谱"), ("ingredient", "食材"), ("flavour", "风味"), ("appetite", "食欲")], "vo_life")

    V("vo_spice", "餐桌礼仪", 14, 3,
      "认读 spice、banquet、chopstick 和 manner。",
      [("spice", "香料"), ("banquet", "宴会"), ("chopstick", "筷子"), ("manner", "礼仪")], "vo_life")

    G("gr_subfut", "与将来事实相反的虚拟", 14, 3,
      "能用 should、were to 加原形表示与将来事实相反的假设。", "subj", [
        q("万一明天的宴会取消，我们就会在家吃。哪一句正确？",
          "If the banquet should be cancelled, we would eat at home",
          "If the banquet will be cancelled, we would eat at home",
          "If the banquet should be cancelled, we will eat at home",
          "If the banquet is cancelled, we would eat at home",
          "与将来相反可以用 should be cancelled 配 would eat。"),
        q("If it ___ to snow tomorrow, the outdoor meal would stop. 横线处填哪一个？", "were",
          "was", "is", "will be", "were to snow 表示将来不大可能发生。"),
        q("哪一句是与将来事实相反？", "If I were to forget the recipe, I would use a simpler one",
          "If I forget the recipe, I will use a simpler one", "If I forgot the recipe yesterday, I used another",
          "If I am to forget, I would used one",
          "were to forget 配 would use，表示将来的假设。"),
        q("If she should miss the banquet, she ___. 横线处填哪一个？", "would be upset",
          "will be upset", "was upset", "had been upset", "主句用 would be upset。"),
      ])

    G("gr_asif", "as if 虚拟", 14, 3,
      "能在 as if 后面用过去式或 had done，表示好像并非事实。", "subj", [
        q("他谈起这道菜，好像自己是厨师。与现在不符，哪一句正确？", "He talks as if he were a cook",
          "He talks as if he is a cook in a false way that still uses is", "He talks as if he is being a real cook now true",
          "He talks as if he had been a cook tomorrow",
          "与现在不符，as if 后面用 were。"),
        q("她看着桌子，好像刚才看见了很辣的菜。哪一句正确？", "She looked as if she had seen a very hot dish",
          "She looked as if she saw a very hot dish tomorrow", "She looked as if she has seen a hot dish",
          "She looked as if she sees a hot dish",
          "好像已经看见了，用 had seen。"),
        q("哪一句表示好像并不是真的？", "He eats as if he had never tasted spice",
          "He eats as he tastes spice every day", "As if he tastes, he eats real spice", "He eats if as he tasted",
          "had never tasted 表示其实他尝过，只是好像没有。"),
        q("as if 从句与现在事实相反时，be 常用哪一个？", "were", "is", "been", "being",
          "与现在相反时 be 常用 were。"),
      ])

    F("fu_foods", "比较饮食", 14, 3,
      "能比较不同菜肴，并说明自己的口味。", "fu_desc", [
        q("想说这道菜好像没有放盐，哪一句合适？", "This dish tastes as if it had no salt",
          "This dish tastes as if it has no salt and that is the true recipe we measured",
          "Tastes as if had it no salt", "Salt as if the dish no",
          "as if it had no salt 表示尝起来像没有盐。"),
        q("想说万一买不到这种香料就换食谱，哪一句合适？",
          "If the spice should be unavailable, I would change the recipe",
          "If the spice will be unavailable, I would change the recipe",
          "If the spice should be unavailable, I will change the recipe",
          "If the spice unavailable, I would changed",
          "should be unavailable 配 would change。"),
        q("想介绍用筷子的礼仪，哪一句合适？", "It is good manners not to point with chopsticks",
          "It are good manners not to point with chopsticks", "It is good manners not to point with cohpsticks", "It is good manners not to point with chopstikcs",
          "It is good manners not to 用来说明礼仪。"),
        q("想说这道菜会增进食欲，哪一句合适？", "The flavour may improve your appetite",
          "The flavour may improved your appetite", "Improve may the flavour you", "The flavour may to improve your appetite",
          "may improve 用来说明可能的效果。"),
      ])

    _d = "The banquet included a mild soup and a spicy fish. Lin ate as if she had never tasted that spice. If the fish should be too hot, she would drink some soup."
    R("rw_food", "读饮食短文", 14, 3,
      "推断 as if 暗示的真实情况，以及还没发生的打算。", "rw_infer", [
        q(_d + " 宴会上有什么？", "清淡的汤和辣鱼", "只有甜品", "没有鱼", "只有筷子",
          "短文写 a mild soup and a spicy fish。"),
        q(_d + " as if 暗示香料对 Lin 来说怎样？", "她其实可能尝过，只是反应像没尝过", "她是厨师", "她不吃饭", "汤是辣的",
          "as if she had never tasted 表示好像从未尝过。"),
        q(_d + " 如果鱼太辣，她会怎样？", "喝一些汤", "离开宴会", "再要一份鱼", "改用筷子指人",
          "would drink some soup。"),
        q(_d + " 哪一句还是假设，不是已经发生的事？", "鱼太辣的话她会喝汤",
          "宴会上有汤和鱼", "她已经在吃", "短文没有假设",
          "If the fish should be too hot 还是假设。"),
      ])

    R("wr_food", "写饮食说明", 14, 3,
      "能按要点选出说明中的句子。", "rw_write_s", [
        q("要点：有汤和辣鱼、她好像没尝过这种香料、太辣就喝汤。哪一句三个要点都有？",
          "There was soup and spicy fish, she ate as if she had never tasted the spice, and if it should be too hot she would drink soup",
          "There was soup", "The fish was spicy", "Soup is mild",
          "三个要点都要出现。"),
        q("说明里用 as if 谈已经尝过的感觉，哪一句正确？", "He smiled as if he had found a new flavour",
          "He smiled as if he finds a new flavour tomorrow", "He smiled as if he has found a flavour",
          "As if smiled he had found",
          "had found 表示好像已经发现。"),
        q("哪一句适合作为说明的第一句？", "This paragraph describes one banquet",
          "This paragraph describe one banquet", "This praagraph describes one banquet", "This paragrpah describes one banquet",
          "说明可以先写 This paragraph describes。"),
        q("哪一句是与将来相反的虚拟？", "If the soup were to run out, we would cook noodles",
          "If the soup runs out, we will cook noodles", "If the soup ran out yesterday, we cooked noodles",
          "Were the soup runs out, we cook",
          "were to run out 配 would cook。"),
      ])

    V("vo_rail", "长途旅行", 14, 4,
      "认读 rail、carriage、scenery 和 delay。",
      [("rail", "铁路"), ("carriage", "车厢"), ("scenery", "沿途风景"), ("delay", "延误")], "vo_life")

    V("vo_scenery", "旅途见闻", 14, 4,
      "认读 boundless、frost、awesome 和 cross。",
      [("boundless", "一望无际的"), ("frost", "霜"), ("awesome", "令人惊叹的"), ("cross", "穿越")], "vo_life")

    G("gr_wish", "wish 虚拟", 14, 4,
      "能在 wish 后面用过去式表示与现在相反，用 had done 表示与过去相反。", "subj", [
        q("我希望我现在就在那列火车上，但事实上不在。哪一句正确？", "I wish I were on that train",
          "I wish I am on that train", "I wish I were on that train and I really am", "I wish I had been on that train now as a present fact",
          "与现在相反，wish 后面用 were。"),
        q("她希望当时没有误车。哪一句正确？", "She wishes she had not missed the train",
          "She wishes she did not missed the train", "She wishes she has not missed the train",
          "She wishes she missed not the train",
          "与过去相反用 had not missed。"),
        q("I wish the delay ___ shorter. 说的是现在这场延误，横线处填哪一个？", "were",
          "is", "had been", "will be", "希望现在的情况不同，用 were。"),
        q("哪一句表示后悔已经发生的事？", "I wish I had taken more photos",
          "I wish I took more photos now", "I wish I take more photos", "I wish I have more photos",
          "had taken 表示当时没多拍，现在后悔。"),
      ])

    G("gr_ifonly", "if only 虚拟", 14, 4,
      "能用 If only 加过去式或 had done 表示强烈愿望。", "subj", [
        q("要是现在能看见那片一望无际的平原就好了。哪一句正确？", "If only I could see the boundless plain",
          "If only I can see the boundless plain", "If only I could saw the plain", "If only can I see the plain",
          "If only 表示现在不能实现的愿望，用 could see。"),
        q("要是当时带了外套就好了。哪一句正确？", "If only I had brought a coat",
          "If only I brought a coat", "If only I have brought a coat", "If only had I brought a coat as a question",
          "与过去相反用 had brought。"),
        q("If only the train ___ on time now. 横线处填哪一个？", "were",
          "is", "had been", "will be", "希望现在准点，用 were。"),
        q("哪一句是对过去的遗憾？", "If only we had crossed the mountain before the frost",
          "If only we crossed the mountain now", "If only we cross the mountain", "If only do we cross",
          "had crossed 是已经错过的事。"),
      ])

    P("ph_tonehs", "用语调表达态度", 14, 4,
      "能判断升调、降调或重读是在表示犹豫、惊讶还是强调。", "attitude", [
        q("Really? 用明显的升调，更可能表示什么？", "惊讶", "已经完全同意并且结束话题", "在读单词重音", "没有任何态度",
          "Really 的升调常表示惊讶。"),
        q("Well... I am not sure. 把 Well 拖长并略升，更可能表示什么？", "犹豫",
          "愤怒的命令", "高兴地结束对话", "强调火车已经到达", "拖长的 Well 常表示犹豫。"),
        q("I DID see the frost. 重读 DID，更可能表示什么？", "强调自己确实看见了",
          "否定看见了", "询问对方是否看见", "表示与话题无关",
          "重读 did 是在强调谓语，表示确实如此。"),
        q("哪一种读法更礼貌地表示没有听清？", "Sorry? 用升调", "Sorry 用很重的降调并突然停止",
          "把每个词都读成怒气", "完全不读 Sorry",
          "升调的 Sorry 常用来请对方再说一遍，比降调生硬的说法更礼貌。"),
      ])

    F("fu_trip2", "描述旅途", 14, 4,
      "能描述沿途风景，并表达遗憾或愿望。", "fu_desc", [
        q("想说希望自己现在就在车上，哪一句合适？", "I wish I were on the train",
          "I wish I am on the train", "Wish I were I am really there", "I wish I had been now as a fact",
          "wish 后面用 were 表示现在不在车上。"),
        q("想说要是当时拍了霜就好了，哪一句合适？", "If only I had photographed the frost",
          "If only I photographed the frost", "If only I have photographed the frost", "Photographed if only I had",
          "had photographed 表示当时没拍。"),
        q("想描述一望无际的平原，哪一句合适？", "The plain looked boundless",
          "The plain looked buondless", "The plain looked boundlses", "The plain looked bondless",
          "looked boundless 用来描述风景。"),
        q("火车延误时想礼貌地表示失望，哪一句合适？", "I am sorry the train is delayed",
          "I is sorry the train is delayed", "He is sorry the train is delayed", "I am sorry the train is dleayed",
          "I am sorry 用来礼貌地表示失望。"),
      ])

    _r = "The train crossed a boundless plain at dawn. Lin wishes she had sat by the window, because she missed the frost. If only the delay had been shorter."
    R("rw_rail", "读旅途短文", 14, 4,
      "推断 Lin 后悔的是什么，以及哪一句只是愿望。", "rw_infer", [
        q(_r + " 火车黎明时穿越了什么？", "一望无际的平原", "一座城市", "一片湿地", "一个实验室",
          "短文写 a boundless plain at dawn。"),
        q(_r + " Lin 后悔什么？", "没有坐在窗边，错过了霜", "没有坐火车", "延误太短", "平原太小",
          "wishes she had sat by the window 说明她没坐在窗边。"),
        q(_r + " If only 表达的愿望是什么？", "延误更短一些", "平原更小", "不要看见霜", "取消黎明",
          "the delay had been shorter。"),
        q(_r + " 哪一件事是已经发生的？", "火车穿越了平原", "她坐在了窗边", "延误很短", "她拍到了霜",
          "第一句是事实。后面两句是愿望。"),
      ])

    R("wr_rail", "写旅途邮件", 14, 4,
      "能按要点选出邮件中的句子。", "rw_write_s", [
        q("要点：黎明穿越平原、后悔没坐窗边、希望延误更短。哪一句三个要点都有？",
          "We crossed a plain at dawn, I wish I had sat by the window, and if only the delay had been shorter",
          "We crossed a plain", "I like windows", "Trains can be late",
          "三个要点都要出现。"),
        q("邮件里表示后悔，哪一句正确？", "I wish I had brought a camera",
          "I wish I brought a camera now for the past", "I wish I have brought a camera", "Wish I had I brought",
          "had brought 表示当时没带。"),
        q("哪一句适合作为邮件的第一句？", "I am writing to tell you about the journey",
          "I am write to tell you about the journey", "I am writing to telling you about the journey", "I am writing to tells you about the journey",
          "邮件可以先写 I am writing to tell you。"),
        q("哪一句是 If only 对现在的愿望？", "If only the train were here now",
          "If only the train had arrived yesterday as a wish about now using had for present",
          "If only the train is here", "If only is the train here",
          "were here now 表示现在火车还不在。"),
      ])

    V("vo_aid", "急救", 14, 5,
      "认读 first aid、bleed、bandage 和 choke。",
      [("first aid", "急救"), ("bleed", "流血"), ("bandage", "绷带"), ("choke", "窒息")], "vo_life")

    V("vo_wound", "伤情处理", 14, 5,
      "认读 wound、swelling、pressure 和 ambulance。",
      [("wound", "伤口"), ("swelling", "肿胀"), ("pressure", "按压"), ("ambulance", "救护车")], "vo_life")

    G("gr_suggest", "建议命令的虚拟", 14, 5,
      "能在 suggest、insist、order 后面用 should 加原形，should 可以省略。", "subj", [
        q("医生建议她休息。哪一句正确？", "The doctor suggested that she should rest",
          "The doctor suggested that she rests", "The doctor suggested that she rested tomorrow as a fact",
          "The doctor suggested her to rest that",
          "suggest 后面的从句用 should rest，should 也可以省略，但不用 rests。"),
        q("The nurse insisted that the boy ___ still. 横线处填哪一个？", "stay",
          "stays", "stayed", "to stay", "insist 后面用动词原形 stay。"),
        q("哪一句是正确的？", "They ordered that the wound be cleaned",
          "They ordered that the wound was cleaned", "They ordered that the wound is cleaned",
          "They ordered the wound cleaned that be",
          "order 后面可以用 be cleaned，相当于 should be cleaned。"),
        q("suggest 后面的 should 可以怎样？", "可以省略，仍用动词原形", "必须改成过去式", "必须改成 -ing", "不能出现在从句里",
          "should 可以省，但谓语仍用原形。"),
      ])

    G("gr_otherwise", "otherwise 虚拟", 14, 5,
      "能用 otherwise 表示如果不这样就，并搭配 would have done。", "subj", [
        q("他当时在流血，不然他就不会叫救护车。哪一句正确？",
          "He was bleeding; otherwise he would not have called an ambulance",
          "He was bleeding; otherwise he would not call an ambulance yesterday",
          "He was bleeding; otherwise he did not call", "Otherwise he would not have called, and he was not bleeding",
          "otherwise 接 would not have called，表示与过去事实相反。"),
        q("She pressed the wound. Otherwise it ___ worse. 表示否则会更严重，横线处填哪一个？", "would have got",
          "got", "would get yesterday", "had got", "与已经避免的过去结果用 would have got。"),
        q("哪一句用 otherwise 表示虚拟？", "He knew first aid; otherwise the boy would have choked",
          "He knew first aid; otherwise the boy choked", "Otherwise the boy choked because he knew first aid",
          "He knew first aid otherwise would choked",
          "would have choked 不是实际发生的结果。"),
        q("otherwise 在这些句子里更接近哪一个意思？", "否则", "因此事实就是", "在……里面", "比……更",
          "otherwise 表示如果不是前面那种情况。"),
      ], "inferred")

    F("fu_aid", "说明急救步骤", 14, 5,
      "能按步骤说明止血，并建议何时叫救护车。", "fu_argue", [
        q("想按步骤说先按压伤口，哪一句合适？", "First, put pressure on the wound",
          "First, put perssure on the wound", "First, put pressrue on the wound", "First, put prssure on the wound",
          "First 开始步骤。"),
        q("想转述医生要求清洗伤口，哪一句合适？", "The doctor ordered that the wound be cleaned",
          "The doctor ordered that the wound was cleaned", "The doctor ordered the wound to was clean",
          "Ordered that was the wound cleaned",
          "order that 后面用 be cleaned。"),
        q("想说不然情况会更糟，哪一句合适？", "Apply a bandage; otherwise the bleeding would have continued",
          "Apply a bandage; otherwise the bleeding continued as the real result of applying it",
          "Otherwise continued the bleeding because of the bandage", "Would have the bleeding otherwise real",
          "otherwise 加 would have continued 表示倘若没包扎。"),
        q("想建议窒息时立即求助，哪一句合适？", "If someone is choking, call an ambulance at once",
          "Choking call someone if an ambulance", "If someone is choke, call an ambulance at once", "If someone is choking, call an abmulance at once",
          "call an ambulance 是明确建议。"),
      ])

    _a = "The coach suggested that the student sit down. He put pressure on the wound and then used a bandage. Otherwise the bleeding would have become dangerous. An ambulance arrived ten minutes later."
    R("rw_aid", "读急救短文", 14, 5,
      "找出已经做的步骤、建议，以及 otherwise 排除的结果。", "rw_argue", [
        q(_a + " 教练建议学生做什么？", "坐下", "继续跑步", "自己开车", "拆掉绷带",
          "suggested that the student sit down。"),
        q(_a + " 他接着做了哪两件事？", "按压伤口然后用绷带", "只是等待", "让学生奔跑", "取消救护车",
          "put pressure 然后 used a bandage。"),
        q(_a + " otherwise 说明什么被避免了？", "流血变得危险", "救护车到来", "学生坐下", "使用绷带",
          "would have become dangerous 是没有发生的危险结果。"),
        q(_a + " 哪一件事是事实？", "救护车十分钟后到了", "流血已经变得危险", "没有使用绷带", "教练建议他继续跑",
          "最后一句 arrived 是事实。"),
      ])

    R("wr_aid", "写急救步骤", 14, 5,
      "能按要点选出步骤说明中的句子。", "rw_write_s", [
        q("要点：建议坐下、按压并包扎、否则流血会危险。哪一句三个要点都有？",
          "The coach suggested that he sit down, pressure and a bandage were used, and otherwise the bleeding would have become dangerous",
          "He sat down", "A bandage was used", "Ambulances are fast",
          "三个要点都要出现。"),
        q("步骤里转述命令，哪一句正确？", "They insisted that the patient stay awake",
          "They insisted that the patient stayed awake", "They insisted that the patient stays awake",
          "They insisted the patient to stay that",
          "insist 后面用 stay 原形。"),
        q("哪一句适合作为步骤的第一句？", "Follow these steps when someone is bleeding",
          "Follow these steps when someone is bleed", "Follow these steps when someone is beleding", "Follow these steps when someone is bleednig",
          "步骤说明可以先写 Follow these steps。"),
        q("哪一句用 otherwise 表示虚拟？", "Keep the patient warm; otherwise he would have got worse",
          "Keep the patient warm; otherwise he got worse", "Otherwise he got worse because you kept him warm",
          "Would have he got otherwise real",
          "would have got worse 不是保暖之后的真实结果。"),
      ])
