# -*- coding: utf-8 -*-
"""按教学顺序登记小学英语知识点。顺序就是软先修的主干。"""
from en_lib import TOPICS
import en_g3  # noqa: F401
import en_g4  # noqa: F401
import en_g5  # noqa: F401
import en_g6  # noqa: F401
import en_edges  # noqa: F401

SPINE = [
    "ph_alpha", "ph_case", "ph_vowel", "ph_cons", "vo_greet", "gr_am", "fu_greet", "rw_hello",
    "vo_colour", "gr_itis", "fu_colour", "rw_colour",
    "vo_body", "gr_this", "fu_body", "rw_body",
    "vo_animal", "fu_thisanimal", "rw_animal",
    "vo_food", "gr_like", "fu_food", "rw_food",
    "vo_num", "vo_toy", "gr_howmany", "fu_bday", "rw_num",
    "ph_a", "vo_country", "gr_from", "fu_from", "rw_from",
    "ph_e", "vo_family", "gr_who", "fu_family", "rw_family",
    "ph_i", "vo_size", "gr_size", "rw_zoo",
    "ph_o", "vo_roomobj", "gr_prep", "fu_where", "rw_where",
    "ph_u", "ph_shortrev", "vo_fruit", "gr_doyou", "gr_plural", "rw_fruit",
    "vo_num20", "gr_howmany2", "rw_count",
    "ph_ae", "vo_class", "gr_lets", "fu_class", "rw_class",
    "ph_ie", "vo_bag", "fu_bag", "rw_bag",
    "ph_oe", "vo_friend", "gr_has", "fu_friend", "rw_friend",
    "ph_ue", "vo_home", "gr_isin", "fu_home", "rw_home",
    "ph_longe", "vo_dinner", "fu_would", "rw_dinner",
    "vo_job", "gr_job", "fu_job", "rw_job",
    "vo_school", "gr_floor", "fu_school", "rw_school",
    "vo_timew", "gr_time", "fu_time", "rw_time",
    "vo_weather", "gr_weather", "fu_weather", "rw_weather",
    "vo_farm", "gr_these", "fu_farm", "rw_farm",
    "vo_clothes", "gr_whose", "fu_clothes", "rw_clothes",
    "vo_shop", "gr_price", "fu_shop", "rw_price",
    "ph_blend", "vo_char", "gr_like_person", "fu_teacher", "rw_teacher",
    "vo_week", "gr_haveon", "vo_weekend_act", "fu_often", "rw_week",
    "vo_meal", "fu_would2", "rw_meal",
    "vo_can", "gr_can", "fu_can", "rw_can",
    "vo_room5", "gr_there", "fu_there", "rw_room",
    "vo_nature", "gr_isthere", "fu_park", "rw_park",
    "vo_routine", "gr_when", "fu_day", "rw_day",
    "vo_season", "fu_season", "rw_season",
    "vo_month", "gr_month", "fu_holiday", "rw_cal",
    "gr_ord", "fu_date", "rw_date",
    "gr_poss", "gr_ing", "fu_whose", "rw_doing",
    "vo_rule", "gr_imp", "fu_rule", "rw_rule",
    "vo_city", "gr_turn", "fu_way", "rw_way",
    "vo_trans", "gr_must", "fu_come", "rw_traffic",
    "vo_plan", "gr_going", "fu_plan", "rw_plan",
    "vo_hobby", "gr_does", "fu_pen", "rw_pen",
    "vo_job6", "gr_work", "fu_work", "rw_work",
    "vo_feel", "gr_should", "fu_feel", "rw_feel",
    "ph_tone", "vo_measure", "gr_comp", "gr_than", "fu_tall", "rw_cmp",
    "gr_past", "gr_did", "fu_weekend", "rw_weekend",
    "gr_irr", "fu_trip", "rw_trip",
    "vo_change", "gr_was", "fu_now", "rw_now",
    "vo_confuse", "rw_letter",
]

_got = [t["key"] for t in TOPICS]
if _got != SPINE:
    missing = [k for k in SPINE if k not in _got]
    extra = [k for k in _got if k not in SPINE]
    raise SystemExit("知识点顺序与主干不一致。缺：%s 多：%s 实际 %d 期望 %d" % (
        "、".join(missing), "、".join(extra), len(_got), len(SPINE)))
