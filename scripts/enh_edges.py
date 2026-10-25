# -*- coding: utf-8 -*-
"""高中英语里真正依赖才记硬先修。顺序软边由编译脚本按册连接。

指向初中写成 j:初中的 key，指向小学写成 p:小学的 key。不连数学。
跨学段的边以软先修为主；下面的 SOFT 是额外软边，硬边只留给直接要用到的形式。
"""
from en_lib import hard

SOFT = []


def soft(topic, prereq, reason):
    SOFT.append((topic, prereq, reason))

# 硬边：后面的结构直接用到前面的形式。
hard("gr_futcont", "j:gr_ing7", "用现在进行时表示将来之前，要先会 am、is、are 加 -ing。")
hard("gr_taghs", "j:gr_tag", "高中附加疑问句承接初中已经学过的反意疑问句。")
hard("gr_relpro", "j:gr_attr", "关系代词引导的定语从句承接初中的 who、which、that。")
hard("gr_relwhose", "gr_relpro", "whose 和 whom 是在关系代词定语从句上的细分。")
hard("gr_reladv", "gr_relpro", "关系副词定语从句要先会用关系代词修饰名词。")
hard("gr_relprep", "gr_reladv", "介词加关系代词要先会关系副词和关系代词。")
hard("gr_nonrest", "gr_relpro", "非限制性定语从句要先会限制性定语从句。")
hard("gr_passcont", "j:gr_pass", "现在进行时的被动语态要先会 be 加过去分词。")
hard("gr_passcont", "j:gr_ing7", "进行时被动仍要用 be 加 -ing 这一套助动词。")
hard("gr_passperf", "j:gr_pass", "完成时被动要先会被动语态的过去分词。")
hard("gr_passperf", "j:gr_pp", "现在完成时的被动要先会 have 加过去分词。")
hard("gr_ppattr", "j:gr_pass", "过去分词作定语之前，要先在被动语态里见过过去分词。")
hard("gr_ppcomp", "gr_ppattr", "过去分词作宾补和作定语是同一种非谓语形式。")
hard("gr_ingattr", "j:gr_ger", "动词 -ing 作定语承接初中对动名词和 -ing 的区分。")
hard("gr_ingadv", "gr_ingattr", "动词 -ing 作状语要先会它作定语和表语。")
hard("gr_toattr", "j:gr_to", "不定式作定语承接初中不定式作宾语。")
hard("gr_topurp", "j:gr_purpose", "不定式作目的状语承接初中已经学过的 to do 表目的。")
hard("gr_toform", "gr_toattr", "it 作形式主语再接不定式，要先会不定式本身。")
hard("gr_modperf", "j:gr_mustbe", "情态动词加 have done 承接初中用 must 表示推测。")
hard("gr_report", "j:gr_that", "间接引语里的宾语从句要先会 that 从句。")
hard("gr_subjcls", "j:gr_that", "主语从句里的 that 承接初中的宾语从句。")
hard("gr_predcls", "gr_subjcls", "表语从句和主语从句都是名词性从句，先会主语从句。")
hard("gr_appos", "gr_predcls", "同位语从句要先会 that 引导的名词性从句，才好和定语从句分开。")
hard("gr_ifsubj", "j:gr_whobj", "whether 引导的主语从句承接初中疑问词宾语从句的陈述语序。")
hard("gr_ingperf", "gr_ingadv", "having done 是动词 -ing 作状语的完成式。")
hard("gr_topass", "gr_toform", "不定式的被动式要先会不定式作主语和表语。")
hard("gr_subnow", "j:gr_if", "与现在事实相反的虚拟语气承接初中的 if 条件句。")
hard("gr_subpast", "gr_subnow", "与过去事实相反的虚拟语气要先会与现在事实相反的形式。")
hard("gr_subpast", "j:gr_ppast", "从句用 had done，要先会过去完成时。")
hard("gr_subfut", "gr_subnow", "与将来事实相反的虚拟语气沿用 would 加原形的主句。")
hard("gr_wish", "gr_subnow", "wish 后面的虚拟语气和 if 虚拟用同一套时间错位。")
hard("gr_suggest", "gr_wish", "表示建议的虚拟语气要先会 wish 这类专门的虚拟从句。")
hard("gr_invneg", "gr_subnow", "否定副词倒装常和虚拟、强调一起出现，先会虚拟语气的助动词。")
hard("gr_invonly", "gr_invneg", "only 和 so、neither 的倒装与否定副词倒装是同一类部分倒装。")
hard("gr_invif", "gr_subpast", "省略 if 的倒装要先会与过去事实相反的 had done。")
hard("gr_cleft", "gr_relpro", "强调句的 that 容易和定语从句混淆，要先会关系代词。")
hard("gr_doemph", "gr_cleft", "用 do 强调谓语是在句式强调之后的另一种强调。")
hard("gr_ellip", "gr_toform", "省略不定式时要保留 to，先会不定式的完整形式。")
hard("gr_advconc", "j:gr_although", "although 与 while 的让步用法承接初中的让步状语从句。")
hard("gr_advso", "j:gr_sothat", "so that 与 in case 承接初中的目的状语从句。")
hard("gr_nonfinmix", "gr_ingperf", "比较 to do、doing 和 done 时，要先会 -ing 的完成式。")
hard("gr_nonfinmix", "gr_topass", "非谓语综合选择也要会不定式的被动式。")
hard("gr_mixcls", "gr_appos", "名词性从句综合要先能分开同位语从句和定语从句。")
hard("gr_tensemix", "j:gr_review", "语篇里选时态承接初中已经做过的时态选择。")

# 软边：连回初中或小学，多数语法点各连一条，避免全图只靠一条主干。
soft("gr_sentmem", "j:gr_be7", "分析句子成分之前，要先会用 am、is、are 组成句子。")
soft("gr_np", "j:gr_plural7", "名词短语里常有复数，先会名词复数再看整个短语。")
soft("gr_adjp", "j:gr_comp8", "形容词短语里会遇到比较，先会比较级的词形。")
soft("gr_svoc", "j:gr_make", "宾补结构里常见 make 加宾语加动词，先会这个初中句型。")
soft("gr_used3", "j:gr_used", "辨析 used to 和 be used to 之前，要先会 used to 表示过去习惯。")
soft("gr_suggest", "j:gr_should8", "表示建议的从句和初中的 should 是同一类建议语气。")
soft("gr_wouldrather", "j:gr_if", "would rather 的虚拟用法沿用 if 条件句里的时间错位。")
soft("rw_news", "j:gr_past8", "读已经发生的新闻之前，要先会用一般过去时叙述。")
soft("ph_stresshs", "j:ph_stress", "多音节词重音承接初中已经辨过的单词重音。")
soft("ph_linkhs", "j:ph_link", "高中连读承接初中在短语里听过的连读。")
soft("ph_pausehs", "j:ph_pause", "按意群停顿承接初中已经学过的停顿。")
soft("ph_ploshs", "j:ph_plos", "不完全爆破承接初中听过的爆破音相邻。")
soft("ph_toneb", "p:ph_tone", "句末升降调承接小学已经学过的陈述句和疑问句语调。")
soft("ph_weak", "j:ph_tone7", "弱读和语调都是句子里的语音变化，先会句末升降调。")
soft("vo_affix", "j:gr_plural7", "看后缀如何改变词性之前，要先会词尾变化这种意识。")
