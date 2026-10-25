# 英语题干扰项与课标抽查

只改了错误选项的文字。正确答案、选项字母、题目 id、题干、解析和 `verify` 都没有动。没有 push，也没有部署。

## 改了多少

英语选择题一共 2779 道（`cne_p` / `cne_j` / `cne_h`）。这次只改明显不通、可以一眼排除的干扰项，已经像学习者错误的选项留着。

| 学段 | 改动的题 | 改动的选项 |
|---|---:|---:|
| 小学 `cne_p` | 0 | 0 |
| 初中 `cne_j` | 3 | 5 |
| 高中 `cne_h` | 120 | 323 |
| 合计 | 123 | 328 |

小学题里的干扰项本来就是数、颜色、家庭称谓或主谓一致这类错误，没有改。初中只动了三道里的胡话（`cne_j005_q1`、`cne_j005_q3`、`cne_j011_q4`）。高中功能句和写作要点里集中了一批「The stadium ran me」一类的句子，是这次的主体。

同一批替换写进了 `data/questions.json`，也写进了生成这些题的 `scripts/enj_g7a.py`、`scripts/enh_b1.py` 至 `scripts/enh_s4.py`，避免以后按脚本重编又变回去。

## 怎么改

干扰项和正确答案用同一句话的骨架，只放一个典型错误：主谓一致、动词形式、冠词、介词搭配、多写的 to、不定式后误加 -s、拼写相近（相邻字母对调或少一个字母）、相邻词的语序。要点题如果只改语法，句子里三个要点还在，仍可能算对，所以改掉其中一个要点用词。和短文「一致」的阅读题没有改写成另一句也对的话。

没有新造 earthquake、ate、Please 加名词这类词。集合名词（如 band）不做 is/are 对调，因为两种都有人接受。

### 例子

问候和应答（初中、高中基础）：

- `cne_j005_q1`：`I am a book.` → `Nice to meeting you, too.`（to 后面误用 -ing）。留下的 `Good night.`、`See you yesterday.` 本来就是错误的客套和时态，没动。
- `cne_j005_q3`：`Good evening is a book.` / `What is your pen?` / `Sit on the name.` → `Good mornings.` / `Good moning.` / `Good monring.`（复数、少字母、相邻字母对调）。
- `cne_h005_q1`：`I ate the classroom` → `Hi, my name Lin is`；`Please earthquake the book` → `Hi, my name are Lin`。

一致、冠词、介词（高中）：

- `cne_h005_q3`：`I am in a flood` → `I am at Class 3`；`Class 3 is eating` → `I is in Class 3`。
- `cne_h007_q2`：`You are a new earthquake` → `I is a new student at this school`；另一项是 `I am an new student at this school`。
- `cne_h015_q3`：`I would liked to join the debate club`、`I would like to joining the debate club`、`I would to like to join the debate club`（情态动词后的形式、to + -ing、多写 to）。

要点题不能只改语法：

- `cne_h007_q1` 要求姓名林晓、三班、喜欢音乐都出现。`Class 3 likes Monday` 改成 `I am Lin Xiao in Class 3, and I like football`。名字和班级还在，音乐被换成足球，三个要点不齐。原来缺要点的两项（`I am Lin Xiao in Class 3`、`I like music and football`）保留。

拼写相近，用在句子里已经没有更合适的语法钩子时：

- `cne_h007_q4`：`Hello, let me introduce myself` 的三个错项改成 `itnroduce`、`introdcue`、`inroduce`。词还是那个词，句子不再成立。

阅读里本来就是通顺英语、只是和短文事实不符的句子没有改。例如 `cne_h035_q4` 的 `The earthquake hit on Monday`（短文是 Friday）。附加疑问句 `He is a coach, doesn't he?` 也不是胡话，没有改。

## 课标和册次抽查

抽查的都是标了「待核」的条目或册次。没有打开教育部 PDF 逐页对原文，所以**一处都没有改，也没有去掉「待核」**。

对照过、和现有映射一致的：

- 人教版（2019）必修第一册单元名。百度百科「高中英语必修第一册」课文目录，以及一份 2019 年配套练习册目录（`ynmdfz.net` 上的 contents：Welcome Unit、Teenage Life、Travelling Around、Sports and Fitness、Natural Disasters、Languages Around the World），与 `scripts/enh_build.py` 里高一（grade 10）的 `TITLES` 一致。
- 人教版（2019）选择性必修第一册。临汾升学考试网 2022-11-23 转载的目录：Unit 1 People of Achievement、Unit 2 Looking into the Future、Unit 3 Fascinating Parks、Unit 4 Body Language、Unit 5 Working the Land。与 `TITLES` 里 grade 13 一致。21 世纪教育网的课件标题也用同一套单元名。
- 人教新目标（Go for it）七年级上册。教习网把 Unit 2 标为 This is my sister，Unit 3 标为 Is this your pencil；给力英语的七年级上册课文页也是 Unit 2 This is my sister。与 `scripts/enj_build.py` 的 `UNITS` 一致。网上有的博客把这两单元对调，和这两处不一致，没有把它当成足够证据去改册次。

看过、但不能据此改字或消掉「待核」的课标条目：

- `ces-2022:1.PH.01` 至 `1.PH.03`：字母大小写、元音字母和闭音节。读起来像公开转述，`verbatim` 仍是 false。
- `ces-2017:H.B.GR.01` 至 `03`：句子成分、短语、时态。同样是转述，不是课标原文。
- `ces-2017` 选择性必修词汇里有一条把科幻、地标、海洋探索、公益和职业规划写进「课标」表述，正文自己写了「本条为转述」。这更像教材单元主题，不是已核对的课标原句。没有 PDF，就不能改写成另一句并声称那才是原文。

`docs/standards-mapping.md` 第 11、12 节已经写明这些英语课标没有逐页核对。`enh_build.py` 和 `enj_build.py` 的说明也写着册次待核。这些说明保持原样。

## 仍不确定的

- 上面抽到的课标句子都没有和教育部 PDF 对过页，`page_or_ref` 继续是「待核」。
- 高中七册只对了必修第一册和选择性必修第一册的单元标题，没有逐页对语法点落在哪一课。附加疑问句放在必修第一册第 3 单元，这次没有用教材页码复核。
- 小学 PEP（三年级起点）的单元名看起来是常见的 2012 序列（三年级上从 Hello 到 Happy birthday），这次没有打开课本目录页，所以小学册次也仍是待核。
- 初中其余册次、高中必修二、三和选择性必修二至四，只沿用了同一套已知目录，没有逐册打开课本。
- 2779 道选择题里，没有改的那些是抽查时看起来已经像学习者错误。不是逐题由人工重写过。
- 高中有些错项是拼写对调（如 `itnroduce`）或最后两个词换位。它们不合格，也排除了「换完仍然是一句正确的话」的情况，但比真正的搭配错误好认。
- `He is in Class 3` 这类人称错项语法上成立，但完不成题干里「说出自己……」的任务，所以不是第二个正确答案。
