# 盲解说明（第二轮，更仔细）

你是初中数学解题者。任务：独立解一批题，**不知道也不要去找标准答案**。工作目录 /Users/a111/projects/cn-math-taxonomy。下面把你的批次号记作 NN（两位数，如 03）。

输入：data/_second_pass/blind_b_NN.json（用 Read 读取；JSON 数组，每项有 id、type、prompt，选择题还有 choices，数值题可能有 note）。
输出两个文件：
1. data/_second_pass/ans_b_NN.json —— 对象 {"题目id": "你的答案"}，覆盖输入里的每一题，值一律是字符串。
2. data/_second_pass/work_b_NN.json —— 对象 {"题目id": "一两句话的推导/检验要点"}，每题都要有（例如关键算式、中间结果；选择题写明你对每个选项的判断依据）。

答案格式：
- type=numeric：只写数（整数、小数、分数 a/b、负数）；多个答案用全角「，」隔开（按题干要求的顺序，题干没规定顺序就从小到大）。不要带单位、根号、π、百分号、"x=" 前缀。题干指定了保留位数/最简分数就照做。
- type=choice：只写选项字母，如 "B"。必须把**每个选项**逐一检验；只有一个选项严格成立才作答。
- type=short：写最简短的答案。

严格规则（这是独立复核，破坏独立性就失去意义）：
1. **只能读** 你的 blind_b_NN.json 和本说明文件。不要读取、搜索、grep：data/questions.json、data/_qbatches/、data/verification_report.json、data/second_pass_log.json、data/_second_pass/ 下的其它文件、scripts/、topics.json 里的 diagnostic_question。
2. **不要一口气凭直觉全写出来**：分成若干小批（比如每 10 题一批）逐题推理，非平凡的算术、方程、几何计算、概率计数一律用 Bash 里的 python3 实际算一遍（fractions.Fraction 做精确运算，math 算三角和根式，itertools 数排列组合），再写答案。把每批答案和推导追加进上述两个文件（最后保证两个文件是完整合法的 JSON）。
3. 几何题只按题干文字给出的条件作答，不要自己添加条件；如果题干有歧义、条件矛盾、或选择题没有正确选项/有多个正确选项，仍给出你认为最合理的答案，并在 work 里该题的推导开头加上「【存疑】」。
4. 写好后自检：id 是否全覆盖、两个文件是否合法 JSON（python3 读一下并核对条数）。

完成后只回复一句话：题数、其中标【存疑】的题数。不要贴题目或答案。
