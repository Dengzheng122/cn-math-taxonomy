# -*- coding: utf-8 -*-
"""三年级上、下。人教 PEP 三年级起点的常见单元顺序，册次待核。"""
from en_tx import V, S, P, G, F, R

# ---------- 三上 ----------

P("ph_alpha", "英语字母表", 3, "上", 1,
  "按顺序认读英语字母表中的 26 个字母。", "letters", [
    ("n", "英语字母表一共有多少个字母？", 26, "英语字母表从 A 到 Z，一共 26 个字母。"),
    ("c", "字母表里，紧挨在 D 后面的是哪一个？", "the letter E",
     ["the letter C", "the letter F", "the letter B"], "D 的下一个字母是 E。"),
    ("c", "下面哪一组是按字母表顺序排列的？", "A, B, C, D",
     ["A, C, B, D", "B, A, D, C", "D, C, B, A"], "字母表开头是 A、B、C、D。"),
    ("c", "哪个是字母表的最后一个字母？", "the letter Z",
     ["the letter Y", "the letter X", "the letter A"], "字母表的最后一个字母是 Z。"),
])

P("ph_case", "字母的大写和小写", 3, "上", 1,
  "能把同一个字母的大写和小写配成一对。", "letters", [
    ("c", "哪一组是同一个字母的大写和小写？", "Gg",
     ["Dp", "Bt", "Qm"], "G 的大写是 G，小写是 g，所以是 Gg。"),
    ("c", "哪个是小写字母？", "the small letter h",
     ["the capital letter H", "the capital letter B", "the capital letter M"],
     "h 是小写，H、B、M 是大写。"),
    ("n", "英语大写字母有多少个？", 26, "大写字母从 A 到 Z，一共 26 个。"),
    ("c", "单词 bag 的第一个字母是哪一种写法？", "the small letter b",
     ["the capital letter B", "the small letter d", "the capital letter D"],
     "bag 以小写 b 开头。"),
])

P("ph_vowel", "元音字母", 3, "上", 1,
  "能指出元音字母 a、e、i、o、u。", "vowel_letter", [
    ("c", "哪个是元音字母？", "the letter A",
     ["the letter B", "the letter C", "the letter D"], "A 是元音字母，B、C、D 不是。"),
    ("n", "英语元音字母有几个？", 5, "元音字母是 a、e、i、o、u，一共 5 个。"),
    ("c", "哪个不是元音字母？", "the letter T",
     ["the letter A", "the letter E", "the letter U"], "T 是辅音字母。"),
    ("c", "下面哪一组全是元音字母？", "A, E, I, O, U",
     ["A, E, I, O, B", "B, C, D, F, G", "A, B, C, D, E"], "五个元音字母是 A、E、I、O、U。"),
])

S("ph_cons", "辅音字母 b 的开头音", 3, "上", 1,
  "能把辅音字母 b 和单词开头的读音对上，例如 bag、bed、bus、box。",
  "字母 b 的开头音", ["bag", "bed", "bus", "box"], ["cat", "dog", "pen", "sun"],
  "consonant", mode="start")

V("vo_greet", "问候用语", 3, "上", 1,
  "认读 hello、hi、goodbye 和 thanks。",
  [("hello", "你好"), ("hi", "嗨"), ("goodbye", "再见"), ("thanks", "谢谢")])

G("gr_am", "be 动词 am", 3, "上", 1,
  "用 am 和 I 搭配，介绍自己的名字或年龄。", "be", [
    ("c", "I ____ ten. 横线上应填哪个词？", "am",
     ["is", "are", "be"], "I 和 am 搭配，所以是 I am ten。"),
    ("c", "You ____ a student. 横线上应填哪个词？", "are",
     ["am", "is", "be"], "You 和 are 搭配。"),
    ("c", "哪一句是正确的？", "I am Amy.",
     ["I are Amy.", "I be Amy.", "Am I Amy name."], "介绍自己要说 I am Amy。"),
    ("c", "My name ____ Chen Jie. 横线上应填哪个词？", "is",
     ["am", "are", "be"], "name 和 is 搭配。"),
])

F("fu_greet", "问候、告别和致谢", 3, "上", 1,
  "用 Hello、Goodbye 和 Thank you 完成问候、告别和致谢。", "func_greet", [
    ("c", "见到老师，应说哪一句？", "Hello!",
     ["Goodbye!", "Thank you!", "I am ten."], "见面时说 Hello。"),
    ("c", "要离开了，应说哪一句？", "Goodbye!",
     ["Hello!", "Thank you!", "I am Amy."], "告别说 Goodbye。"),
    ("c", "别人帮了你，应说哪一句？", "Thank you!",
     ["Hello!", "Goodbye!", "I am five."], "致谢说 Thank you。"),
    ("c", "想告诉对方自己的名字，应说哪一句？", "I am Mike.",
     ["Goodbye, Mike.", "Thank you, Mike.", "Hello is Mike."], "介绍名字说 I am Mike。"),
])

R("rw_hello", "读懂自我介绍", 3, "上", 1,
  "读一句自我介绍，找出名字。", "read_short", [
    ("c", "读一读：Hello! I am Sarah. 这个人叫什么？", "Sarah",
     ["Mike", "Amy", "John"], "句子写的是 I am Sarah。"),
    ("c", "读一读：Hi! I am John. 哪一句和短文意思相同？", "他叫 John。",
     ["他叫 Sarah。", "他要告别。", "他在说谢谢。"], "短文说 I am John。"),
    ("c", "读一读：Goodbye, Amy! Amy 在做什么？", "告别",
     ["问候", "致谢", "介绍年龄"], "Goodbye 是告别。"),
    ("c", "读一读：I am Chen Jie. Thank you! 哪一句是短文里有的？", "I am Chen Jie.",
     ["I am Sarah.", "I am Mike.", "I am John."], "短文写的名字是 Chen Jie。"),
])

V("vo_colour", "颜色", 3, "上", 2,
  "认读 red、yellow、green 和 blue。",
  [("red", "红色"), ("yellow", "黄色"), ("green", "绿色"), ("blue", "蓝色")])

G("gr_itis", "It is 说明颜色", 3, "上", 2,
  "用 It is 加上颜色词说明物品的颜色。", "be", [
    ("c", "It ____ red. 横线上应填哪个词？", "is",
     ["am", "are", "be"], "It 和 is 搭配。"),
    ("c", "哪一句是正确的？", "It is blue.",
     ["It are blue.", "It am blue.", "It be blue."], "说颜色要用 It is blue。"),
    ("c", "The apple ____ green. 横线上应填哪个词？", "is",
     ["am", "are", "be"], "apple 是单数物品，用 is。"),
    ("c", "哪一句用来说明物品是黄色的？", "It is yellow.",
     ["I yellow.", "Yellow it.", "It yellow is."], "完整的句子是 It is yellow。"),
])

F("fu_colour", "询问颜色", 3, "上", 2,
  "用 What colour is it? 询问颜色，并用 It is 回答。", "func_daily", [
    ("c", "想问「它是什么颜色」，应说哪一句？", "What colour is it?",
     ["What is your name?", "How are you?", "Goodbye!"], "问颜色说 What colour is it?"),
    ("c", "What colour is it? 若它是红色的，应回答哪一句？", "It is red.",
     ["It is blue.", "I am red.", "It are red."], "红色是 red，句子是 It is red。"),
    ("c", "Show me green. 这句是在说什么？", "给我看看绿色",
     ["给我看看红色", "给我看看黄色", "给我看看蓝色"], "green 是绿色。"),
    ("c", "It is blue and yellow. 这里有几种颜色？", "蓝色和黄色",
     ["红色和绿色", "只有蓝色", "只有黄色"], "句子写了 blue 和 yellow。"),
])

R("rw_colour", "看图认颜色", 3, "上", 2,
  "根据写明的颜色选出与文字一致的一项。图的颜色以文字为准。", "read_pic", [
    ("c", "文字：Look at the apple. It is blue. 苹果是什么颜色？", "蓝色",
     ["红色", "绿色", "黄色"], "文字写的是 blue，所以是蓝色。"),
    ("c", "文字：The bag is yellow. 哪一句和文字一致？", "书包是黄色的。",
     ["书包是绿色的。", "书包是红色的。", "书包是蓝色的。"], "yellow 是黄色。"),
    ("c", "文字：I see a red bird. 鸟是什么颜色？", "红色",
     ["黄色", "绿色", "蓝色"], "文字写的是 red。"),
    ("c", "文字：The pen is green. 哪一句是对的？", "It is green.",
     ["It is red.", "It is blue.", "It is yellow."], "pen 的颜色写的是 green。"),
])

V("vo_body", "身体部位", 3, "上", 3,
  "认读 face、eye、nose 和 mouth。",
  [("face", "脸"), ("eye", "眼睛"), ("nose", "鼻子"), ("mouth", "嘴巴")])

G("gr_this", "This is 与 That is", 3, "上", 3,
  "用 This is 指近处，用 That is 指远处。", "pointer", [
    ("c", "指着近处的钢笔，哪一句是对的？", "This is a pen.",
     ["These is a pen.", "This are a pen.", "This be a pen."], "近处的一件物品说 This is。"),
    ("c", "指着远处的尺子，哪一句是对的？", "That is a ruler.",
     ["This are a ruler.", "That am a ruler.", "That be a ruler."], "远处的一件物品说 That is。"),
    ("c", "This is my nose. 这句里的 This 用来指什么？", "近处的这一个",
     ["远处的那一个", "好几个", "过去的一个"], "This 指近处。"),
    ("c", "That is a cat. 这句里的 That 用来指什么？", "远处的那一个",
     ["近处的这一个", "许多个", "自己的名字"], "That 指远处。"),
])

F("fu_body", "介绍身体部位", 3, "上", 3,
  "用 This is my 介绍自己的五官。", "func_daily", [
    ("c", "指着自己的眼睛，应说哪一句？", "This is my eye.",
     ["This is my nose.", "This is my mouth.", "This is my face."], "眼睛是 eye。"),
    ("c", "This is my mouth. 这句在介绍什么？", "嘴巴",
     ["眼睛", "鼻子", "脸"], "mouth 是嘴巴。"),
    ("c", "Look at me. This is my face. 这句在看什么？", "脸",
     ["书", "苹果", "书包"], "face 是脸。"),
    ("c", "想请对方看自己的鼻子，应说哪一句？", "Look at my nose.",
     ["Look at my ear.", "Look at my hand.", "Look at my foot."], "鼻子是 nose。"),
])

R("rw_body", "读懂五官介绍", 3, "上", 3,
  "读介绍五官的句子，找出说到的部位。", "read_pic", [
    ("c", "文字：This is my face. It is red. 脸是什么颜色？", "红色",
     ["黄色", "绿色", "蓝色"], "文字写 It is red。"),
    ("c", "文字：This is my nose. 哪一句和文字一致？", "这是我的鼻子。",
     ["这是我的嘴巴。", "这是我的眼睛。", "这是我的耳朵。"], "nose 是鼻子。"),
    ("c", "文字：Look at my eye. It is blue. 蓝色的是什么？", "眼睛",
     ["鼻子", "嘴巴", "脸"], "eye 是眼睛，颜色是 blue。"),
    ("c", "文字：This is my mouth. 哪一句是文字里有的？", "This is my mouth.",
     ["This is my nose.", "This is my eye.", "This is my face."], "文字写的是 mouth。"),
])

V("vo_animal", "动物", 3, "上", 4,
  "认读 cat、dog、bird 和 duck。",
  [("cat", "猫"), ("dog", "狗"), ("bird", "鸟"), ("duck", "鸭子")])

F("fu_thisanimal", "用 This is a 介绍动物", 3, "上", 4,
  "用 This is a 加上动物名词介绍一只动物。", "func_daily", [
    ("c", "介绍一只猫，应说哪一句？", "This is a cat.",
     ["This is a dog.", "This is a bird.", "This is a duck."], "猫是 cat。"),
    ("c", "This is a duck. 这是什么动物？", "鸭子",
     ["猫", "狗", "鸟"], "duck 是鸭子。"),
    ("c", "What is this? 若答案是狗，应说哪一句？", "It is a dog.",
     ["It is a cat.", "It is a bird.", "It is a duck."], "狗是 dog。"),
    ("c", "Look! That is a bird. 远处的是什么？", "鸟",
     ["猫", "狗", "鸭子"], "bird 是鸟。"),
])

R("rw_animal", "读懂动物句子", 3, "上", 4,
  "读介绍动物的句子，找出动物和颜色。", "read_short", [
    ("c", "读一读：This is a cat. It is black. 这是什么？", "猫",
     ["狗", "鸟", "鸭子"], "cat 是猫。"),
    ("c", "读一读：That is a duck. It is yellow. 鸭子是什么颜色？", "黄色",
     ["黑色", "蓝色", "绿色"], "文字写 It is yellow。"),
    ("c", "读一读：I see a dog. 哪一句和文字一致？", "我看见一只狗。",
     ["我看见一只猫。", "我看见一只鸟。", "我看见一只鸭子。"], "dog 是狗。"),
    ("c", "读一读：This is a bird. It is blue. 哪一句是对的？", "鸟是蓝色的。",
     ["鸟是红色的。", "猫是蓝色的。", "鸭子是蓝色的。"], "文字说的是 bird，颜色是 blue。"),
])

V("vo_food", "食物", 3, "上", 5,
  "认读 bread、egg、rice 和 milk。",
  [("bread", "面包"), ("egg", "鸡蛋"), ("rice", "米饭"), ("milk", "牛奶")])

G("gr_like", "I like 表达喜好", 3, "上", 5,
  "用 I like 和 I do not like 表达喜欢或不喜欢。", "present_basic", [
    ("c", "哪一句表示「我喜欢面包」？", "I like bread.",
     ["I likes bread.", "Like I bread.", "I like am bread."], "喜欢一件事物说 I like bread。"),
    ("c", "I like milk. 这句的意思是？", "我喜欢牛奶",
     ["我不喜欢牛奶", "我有牛奶", "牛奶喜欢我"], "like 在这里是喜欢。"),
    ("c", "哪一句是正确的？", "I like apples.",
     ["I likes apples.", "I like am apples.", "Like I apples."], "I 后面用 like，不加 s。"),
    ("c", "I do not like rice. 这句的意思是？", "我不喜欢米饭",
     ["我喜欢米饭", "我没有米饭", "米饭不喜欢我"], "do not like 表示不喜欢。"),
])

F("fu_food", "表达想吃什么", 3, "上", 5,
  "用 I like 和 Have some 谈论食物。", "func_daily", [
    ("c", "想说自己喜欢鸡蛋，应说哪一句？", "I like eggs.",
     ["I like milk.", "I like rice.", "I like bread."], "鸡蛋是 egg，复数是 eggs。"),
    ("c", "Have some bread. 这句是在说什么？", "吃些面包吧",
     ["吃些米饭吧", "喝些牛奶吧", "吃些鸡蛋吧"], "bread 是面包。"),
    ("c", "Can I have some milk? 这句是在问什么？", "我可以喝些牛奶吗",
     ["我可以吃些面包吗", "牛奶在哪里", "你喜欢牛奶吗"], "have some milk 是要一些牛奶。"),
    ("c", "哪一句表示「我喜欢米饭」？", "I like rice.",
     ["I like bread.", "I like eggs.", "I like milk."], "米饭是 rice。"),
])

R("rw_food", "读懂喜好短文", 3, "上", 5,
  "读人物自己说的喜好，找出喜欢的食物。", "read_short", [
    ("c", "读一读：Sarah says, \"I like bananas.\" Sarah 喜欢什么？", "香蕉",
     ["苹果", "面包", "米饭"], "引号里写的是 bananas。"),
    ("c", "读一读：Mike says, \"I like milk.\" 哪一句和短文一致？", "Mike 喜欢牛奶。",
     ["Mike 喜欢米饭。", "Mike 不喜欢牛奶。", "Sarah 喜欢牛奶。"], "说话的是 Mike，喜欢的是 milk。"),
    ("c", "读一读：I like bread. I do not like eggs. 这个人不喜欢什么？", "鸡蛋",
     ["面包", "牛奶", "米饭"], "do not like eggs 是不喜欢鸡蛋。"),
    ("c", "读一读：Chen Jie says, \"I like rice.\" 哪一句是短文里的意思？", "Chen Jie 喜欢米饭。",
     ["Chen Jie 喜欢面包。", "Chen Jie 喜欢牛奶。", "Chen Jie 不喜欢米饭。"], "引号里是 I like rice。"),
])

V("vo_num", "1 到 10", 3, "上", 6,
  "认读 one、two、three 和 ten。",
  [("one", "一"), ("two", "二"), ("three", "三"), ("ten", "十")])

V("vo_toy", "玩具和礼物", 3, "上", 6,
  "认读 ball、doll、kite 和 boat。",
  [("ball", "球"), ("doll", "玩具娃娃"), ("kite", "风筝"), ("boat", "小船")])

G("gr_howmany", "How many 问数量", 3, "上", 6,
  "用 1 到 10 和 How many 询问数量。", "number_q", [
    ("c", "想问「你有多少个气球」，应选哪一句？", "How many balloons?",
     ["How old balloons?", "What many balloons?", "How many balloon is?"], "问数量用 How many。"),
    ("n", "one、two、three 的下一个数是几？", 4, "three 的下一个数是 four，也就是 4。"),
    ("c", "How many cakes? 这句是在问什么？", "有多少个蛋糕",
     ["蛋糕是什么颜色", "蛋糕在哪里", "谁要蛋糕"], "How many 问的是数量。"),
    ("c", "I have five books. 一共有多少本书？", "5 本",
     ["4 本", "6 本", "10 本"], "five 是 5。"),
])

F("fu_bday", "询问年龄", 3, "上", 6,
  "用 How old are you? 询问年龄，并用 I am 回答。", "func_greet", [
    ("c", "想问对方几岁，应说哪一句？", "How old are you?",
     ["How are you?", "How many are you?", "What is your name?"], "问年龄说 How old are you?"),
    ("c", "How old are you? 若是 9 岁，应回答哪一句？", "I am nine.",
     ["I am ten.", "I am five.", "I am six."], "9 是 nine。"),
    ("c", "Happy birthday! 这句用在什么时候？", "生日",
     ["告别", "问路", "购物"], "Happy birthday 是生日祝福。"),
    ("c", "This is a gift for you. 这句的意思是？", "这是给你的礼物",
     ["这是我的气球", "你几岁了", "再见"], "gift 是礼物。"),
])

R("rw_num", "读懂数量", 3, "上", 6,
  "从句子里找出物品的数量。", "read_short", [
    ("c", "读一读：I have three balls. 有几个球？", "3 个",
     ["2 个", "4 个", "10 个"], "three 是 3。"),
    ("c", "读一读：I see ten kites. 哪一句和文字一致？", "我看见 10 个风筝。",
     ["我看见 5 个风筝。", "我看见 10 个球。", "我看见 1 个风筝。"], "ten kites 是 10 个风筝。"),
    ("n", "读一读：This is a boat. I have one boat. 有几艘小船？", 1, "one 是 1。"),
    ("c", "读一读：I am six. I have two dolls. 玩具娃娃有几个？", "2 个",
     ["6 个", "1 个", "3 个"], "two dolls 是 2 个；six 是年龄。"),
])

# ---------- 三下 ----------

S("ph_a", "短元音 a", 3, "下", 1,
  "能认出重读闭音节里的短元音 a，例如 cat、bag、map、hat。",
  "短元音 a", ["cat", "bag", "map", "hat"], ["he", "kite", "nose", "me"], "short_vowel")

V("vo_country", "国家和来自哪里", 3, "下", 1,
  "认读 China、Canada、UK 和 USA。",
  [("China", "中国"), ("Canada", "加拿大"), ("UK", "英国"), ("USA", "美国")])

G("gr_from", "I am from 说明来自哪里", 3, "下", 1,
  "用 am 或 is 加上 from 说明自己或他人来自哪里。", "be", [
    ("c", "I ____ from China. 横线上应填哪个词？", "am",
     ["is", "are", "be"], "I 和 am 搭配。"),
    ("c", "哪一句表示「我来自加拿大」？", "I am from Canada.",
     ["I are from Canada.", "I from Canada am.", "Am from I Canada."], "正确的句子是 I am from Canada。"),
    ("c", "Where are you from? 这句是在问什么？", "你来自哪里",
     ["你几岁", "你叫什么", "你喜欢什么"], "Where are you from 问来自哪里。"),
    ("c", "She ____ from the UK. 横线上应填哪个词？", "is",
     ["am", "are", "be"], "She 和 is 搭配。"),
])

F("fu_from", "询问来自哪里", 3, "下", 1,
  "用 Where are you from? 询问，并用 I am from 回答。", "func_greet", [
    ("c", "想问对方来自哪里，应说哪一句？", "Where are you from?",
     ["What is your name?", "How old are you?", "How are you?"], "问籍贯说 Where are you from?"),
    ("c", "Where are you from? 若来自中国，应回答哪一句？", "I am from China.",
     ["I am from Canada.", "I am from the UK.", "I am from the USA."], "中国是 China。"),
    ("c", "He is from the USA. 他来自哪里？", "美国",
     ["中国", "加拿大", "英国"], "the USA 是美国。"),
    ("c", "Welcome back to school! 这句最可能出现在什么时候？", "回到学校",
     ["离开学校", "吃晚饭", "买东西"], "Welcome back to school 是欢迎回到学校。"),
])

R("rw_from", "读懂来自哪里", 3, "下", 1,
  "读自我介绍，找出来自哪个国家。", "read_short", [
    ("c", "读一读：Hello! I am Amy. I am from the UK. Amy 来自哪里？", "英国",
     ["中国", "加拿大", "美国"], "the UK 是英国。"),
    ("c", "读一读：I am Zhang Peng. I am from China. 哪一句和短文一致？", "Zhang Peng 来自中国。",
     ["Zhang Peng 来自加拿大。", "Amy 来自中国。", "Zhang Peng 来自美国。"], "名字是 Zhang Peng，国家是 China。"),
    ("c", "读一读：She is from Canada. 她来自哪里？", "加拿大",
     ["英国", "中国", "美国"], "Canada 是加拿大。"),
    ("c", "读一读：Mike says, \"I am from the USA.\" Mike 来自哪里？", "美国",
     ["英国", "中国", "加拿大"], "引号里是 the USA。"),
])

S("ph_e", "短元音 e", 3, "下", 2,
  "能认出短元音 e，例如 ten、pen、red、leg。",
  "短元音 e", ["ten", "pen", "red", "leg"], ["cat", "cake", "kite", "nose"], "short_vowel")

V("vo_family", "家庭成员", 3, "下", 2,
  "认读 father、mother、brother 和 sister。",
  [("father", "爸爸"), ("mother", "妈妈"), ("brother", "哥哥或弟弟"), ("sister", "姐姐或妹妹")])

G("gr_who", "Who is 询问是谁", 3, "下", 2,
  "用 Who is he 或 Who is she 询问，并用 He is、She is 介绍家人。", "pronoun", [
    ("c", "问「他是谁」，应选哪一句？", "Who is he?",
     ["Who are he?", "Who he is name?", "What is he who?"], "问男性是谁说 Who is he?"),
    ("c", "Who is she? 这句是在问什么？", "她是谁",
     ["她在哪里", "她几岁", "她喜欢什么"], "Who is she 问她是谁。"),
    ("c", "He ____ my father. 横线上应填哪个词？", "is",
     ["am", "are", "be"], "He 和 is 搭配。"),
    ("c", "哪一句是正确的？", "She is my mother.",
     ["She are my mother.", "She am my mother.", "She be my mother."], "She 后面用 is。"),
])

F("fu_family", "介绍家人", 3, "下", 2,
  "用 This is my 介绍家人。", "func_daily", [
    ("c", "介绍自己的爸爸，应说哪一句？", "This is my father.",
     ["This is my mother.", "This is my sister.", "This is my brother."], "爸爸是 father。"),
    ("c", "This is my sister. 这是谁？", "姐姐或妹妹",
     ["爸爸", "妈妈", "哥哥或弟弟"], "sister 是姐姐或妹妹。"),
    ("c", "Who is he? 若他是哥哥，应回答哪一句？", "He is my brother.",
     ["She is my sister.", "She is my mother.", "He is my father."], "哥哥说 He is my brother。"),
    ("c", "This is my family. 这句的意思是？", "这是我的家庭",
     ["这是我的朋友", "这是我的学校", "这是我的书"], "family 是家庭。"),
])

R("rw_family", "读懂家人介绍", 3, "下", 2,
  "读介绍家人的句子，找出是谁。", "read_short", [
    ("c", "读一读：This is my father. He is from China. 这是谁？", "爸爸",
     ["妈妈", "姐姐或妹妹", "朋友"], "father 是爸爸。"),
    ("c", "读一读：She is my mother. 哪一句和文字一致？", "她是我的妈妈。",
     ["他是我的爸爸。", "她是我的姐姐。", "他是我的弟弟。"], "She is my mother 是妈妈。"),
    ("c", "读一读：This is my brother. He is ten. 弟弟或哥哥几岁？", "10 岁",
     ["6 岁", "9 岁", "8 岁"], "He is ten 是 10 岁。"),
    ("c", "读一读：Sarah says, \"This is my sister.\" 哪一句是对的？", "Sarah 在介绍姐姐或妹妹。",
     ["Sarah 在介绍爸爸。", "Sarah 在介绍妈妈。", "Sarah 在介绍老师。"], "sister 是姐姐或妹妹。"),
])

S("ph_i", "短元音 i", 3, "下", 3,
  "能认出短元音 i，例如 big、pig、sit、fish。",
  "短元音 i", ["big", "pig", "sit", "fish"], ["cake", "he", "nose", "cat"], "short_vowel")

V("vo_size", "大小和高矮", 3, "下", 3,
  "认读 big、small、tall 和 short。这里的 short 是矮的。",
  [("big", "大的"), ("small", "小的"), ("tall", "高的"), ("short", "矮的")])

G("gr_size", "用形容词说大小高矮", 3, "下", 3,
  "用 It is 加上 big、small、tall 或 short 描述动物。", "be", [
    ("c", "哪一句表示「它很小」？", "It is small.",
     ["It is tall.", "It is big.", "It is long."], "小的是 small。"),
    ("c", "Look at the elephant. It is big. 大象怎么样？", "很大",
     ["很小", "很矮", "很短"], "big 是大的。"),
    ("c", "The giraffe is tall. 长颈鹿怎么样？", "很高",
     ["很矮", "很小", "很短"], "tall 是高的。"),
    ("c", "It is short. 这句的意思是？", "它很矮",
     ["它很高", "它很大", "它很长"], "在这一课里 short 是矮的。"),
])

R("rw_zoo", "读懂动物园的句子", 3, "下", 3,
  "读描述动物大小的句子，按文字判断。", "read_pic", [
    ("c", "文字：Look at the bear. It is big. 熊怎么样？", "很大",
     ["很小", "很矮", "很瘦"], "文字写 It is big。"),
    ("c", "文字：The monkey is small. 哪一句和文字一致？", "猴子很小。",
     ["猴子很大。", "猴子很高。", "熊很小。"], "monkey 是猴子，small 是小。"),
    ("c", "文字：The giraffe is tall. The cat is short. 谁很高？", "长颈鹿",
     ["猫", "熊", "猴子"], "giraffe is tall。"),
    ("c", "文字：It is a pig. It is big. 又大的动物是什么？", "猪",
     ["猫", "鸟", "鸭子"], "pig 是猪。"),
])

S("ph_o", "短元音 o", 3, "下", 4,
  "能认出短元音 o，例如 dog、box、hot、not。",
  "短元音 o", ["dog", "box", "hot", "not"], ["note", "nose", "cake", "he"], "short_vowel")

V("vo_roomobj", "房间里的物品", 3, "下", 4,
  "认读 desk、chair、bag 和 book。",
  [("desk", "书桌"), ("chair", "椅子"), ("bag", "书包"), ("book", "书")])

G("gr_prep", "in、on、under", 3, "下", 4,
  "用 in、on、under 说明物品在里面、上面或下面。", "pointer", [
    ("c", "书在书桌里面，应选哪一句？", "The book is in the desk.",
     ["The book is on the desk.", "The book is under the desk.", "The book is desk."], "里面用 in。"),
    ("c", "The ball is under the chair. 球在哪里？", "在椅子下面",
     ["在椅子上面", "在椅子里面", "在椅子旁边"], "under 是在下面。"),
    ("c", "The cat is on the box. 猫在哪里？", "在盒子上面",
     ["在盒子里面", "在盒子下面", "在盒子后面"], "on 是在上面。"),
    ("c", "Where is my car? 这句是在问什么？", "我的小汽车在哪里",
     ["这是谁的小汽车", "小汽车是什么颜色", "你喜欢小汽车吗"], "Where is 问位置。"),
])

F("fu_where", "询问位置", 3, "下", 4,
  "用 Where is 询问物品在哪里。", "func_daily", [
    ("c", "想问书包在哪里，应说哪一句？", "Where is my bag?",
     ["What is my bag?", "Who is my bag?", "How is my bag?"], "问位置用 Where is。"),
    ("c", "Where is the book? 若书在椅子上面，应回答哪一句？", "It is on the chair.",
     ["It is in the chair.", "It is under the chair.", "It is the chair."], "上面用 on。"),
    ("c", "It is in the desk. 东西在哪里？", "在书桌里面",
     ["在书桌上面", "在书桌下面", "在椅子旁边"], "in the desk 是在书桌里面。"),
    ("c", "The ball is under the chair. 哪一句和这句话意思相同？", "球在椅子下面。",
     ["球在椅子上面。", "书在椅子下面。", "球在书桌里面。"], "ball 是球，under the chair 是在椅子下面。"),
])

R("rw_where", "读懂位置", 3, "下", 4,
  "读位置句子，找出物品在哪里。", "read_pic", [
    ("c", "文字：The book is on the desk. 书在哪里？", "在书桌上面",
     ["在书桌里面", "在书桌下面", "在椅子上面"], "on the desk 是在书桌上面。"),
    ("c", "文字：My bag is under the chair. 哪一句和文字一致？", "书包在椅子下面。",
     ["书包在椅子上面。", "书在椅子下面。", "书包在书桌里面。"], "bag 是书包，under the chair 是椅子下面。"),
    ("c", "文字：The pen is in the bag. 钢笔在哪里？", "在书包里面",
     ["在书包上面", "在书包下面", "在书桌上"], "in the bag 是在书包里面。"),
    ("c", "文字：Where is the car? It is under the desk. 小汽车在哪里？", "在书桌下面",
     ["在书桌上面", "在椅子上面", "在书包里面"], "回答写的是 under the desk。"),
])

S("ph_u", "短元音 u", 3, "下", 5,
  "能认出短元音 u，例如 fun、run、cup、sun。",
  "短元音 u", ["fun", "run", "cup", "sun"], ["use", "cute", "cake", "he"], "short_vowel")

P("ph_shortrev", "五个短元音复习", 3, "下", 5,
  "能区分 cat 一类的短元音和 cake 一类的长元音。", "short_vowel", [
    ("c", "哪个单词里的 a 和 cat 里的 a 读音相同？", "bag",
     ["cake", "name", "face"], "bag 和 cat 都是短元音 a。"),
    ("c", "哪个单词里的元音和 cake 不同？", "cat",
     ["name", "face", "make"], "cat 是短元音，name、face、make 是 a-e。"),
    ("c", "big 和哪个词的元音不同？", "bike",
     ["pig", "sit", "fish"], "bike 是 i-e，big、pig、sit、fish 是短元音 i。"),
    ("c", "sun 和哪个词的元音相同？", "cup",
     ["use", "cute", "tube"], "sun 和 cup 都是短元音 u。"),
])

V("vo_fruit", "水果", 3, "下", 5,
  "认读 pear、apple、banana 和 orange。这里的 orange 是橙子。",
  [("pear", "梨"), ("apple", "苹果"), ("banana", "香蕉"), ("orange", "橙子")])

G("gr_doyou", "Do you like 一般疑问句", 3, "下", 5,
  "用 Do you like 询问喜好，并用 Yes, I do. 或 No, I do not. 回答。", "present_basic", [
    ("c", "问对方喜不喜欢梨，应选哪一句？", "Do you like pears?",
     ["Does you like pears?", "Do you likes pears?", "Are you like pears?"], "you 前面用 Do。"),
    ("c", "Do you like apples? 肯定回答应选哪一句？", "Yes, I do.",
     ["Yes, I does.", "Yes, I am.", "Yes, I like do."], "Do 的肯定回答是 Yes, I do。"),
    ("c", "Do you like bananas? 否定回答应选哪一句？", "No, I do not.",
     ["No, I does not.", "No, I am not.", "No, I not like."], "Do 的否定回答是 No, I do not。"),
    ("c", "Do you like oranges? 这句是在问什么？", "你喜欢橙子吗",
     ["橙子在哪里", "橙子是什么颜色", "你有几个橙子"], "Do you like 问的是喜不喜欢。"),
])

G("gr_plural", "可数名词复数", 3, "下", 5,
  "能把 cat、box 这类名词变成常见的复数形式。", "plural", [
    ("c", "cat 的复数是哪一个？", "cats",
     ["cates", "caties", "cat"], "一般直接加 s，cats。"),
    ("c", "box 的复数是哪一个？", "boxes",
     ["boxs", "boxies", "box"], "以 x 结尾加 es，boxes。"),
    ("n", "two dogs 里有几只狗？", 2, "two 表示 2。"),
    ("c", "哪一句的名词是复数？", "I see three birds.",
     ["I see one bird.", "I see a bird.", "I see the bird."], "three birds 是复数。"),
])

R("rw_fruit", "读懂水果喜好", 3, "下", 5,
  "读 Do you like 的小对话，找出喜欢的水果。", "read_short", [
    ("c", "读一读：Do you like pears? Yes, I do. 这个人喜欢梨吗？", "喜欢",
     ["不喜欢", "没说", "只喜欢苹果"], "回答是 Yes, I do。"),
    ("c", "读一读：Do you like apples? No, I do not. 哪一句和对话一致？", "这个人不喜欢苹果。",
     ["这个人喜欢苹果。", "这个人喜欢梨。", "这个人有三个苹果。"], "No, I do not 表示不喜欢。"),
    ("c", "读一读：I like bananas. I see four bananas. 有几根香蕉？", "4 根",
     ["3 根", "5 根", "2 根"], "four 是 4。"),
    ("c", "读一读：I have an orange. 这里的 orange 是什么？", "橙子",
     ["橙色", "苹果", "梨"], "在水果这一课里 an orange 是一个橙子。"),
])

V("vo_num20", "11 到 20", 3, "下", 6,
  "认读 eleven、twelve、thirteen 和 twenty。",
  [("eleven", "十一"), ("twelve", "十二"), ("thirteen", "十三"), ("twenty", "二十")])

G("gr_howmany2", "How many 与 11 到 20", 3, "下", 6,
  "用 How many 和 11 到 20 的数词说出看到的数量。", "number_q", [
    ("c", "How many apples do you see? 这句是在问什么？", "你看见多少个苹果",
     ["你喜欢苹果吗", "苹果是什么颜色", "苹果在哪里"], "How many 问数量。"),
    ("n", "eleven 是多少？", 11, "eleven 是 11。"),
    ("c", "I see fifteen kites. 一共有多少个风筝？", "15 个",
     ["14 个", "16 个", "50 个"], "fifteen 是 15。"),
    ("c", "twelve 的下一个数是哪一个？", "thirteen",
     ["eleven", "twenty", "fourteen"], "twelve 后面是 thirteen。"),
])

R("rw_count", "读懂 11 到 20 的数量", 3, "下", 6,
  "从句子里读出 11 到 20 的数量。", "read_short", [
    ("c", "读一读：I see eleven birds. 有几只鸟？", "11 只",
     ["10 只", "12 只", "20 只"], "eleven 是 11。"),
    ("n", "读一读：How many cars do you see? I see twenty. 看见几辆小汽车？", 20, "twenty 是 20。"),
    ("c", "读一读：I have twelve crayons. 哪一句和文字一致？", "我有 12 支蜡笔。",
     ["我有 11 支蜡笔。", "我有 13 支蜡笔。", "我有 20 支蜡笔。"], "twelve 是 12。"),
    ("c", "读一读：I see thirteen kites and eleven birds. 风筝有几个？", "13 个",
     ["11 个", "12 个", "20 个"], "kites 的数量是 thirteen。"),
])
