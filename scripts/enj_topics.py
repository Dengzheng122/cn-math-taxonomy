# -*- coding: utf-8 -*-
"""按教学顺序登记初中英语知识点。顺序就是软先修的主干。"""
from en_lib import TOPICS
import enj_g7a  # noqa: F401
import enj_g7b  # noqa: F401
import enj_g8a  # noqa: F401
import enj_g8b  # noqa: F401
import enj_g9  # noqa: F401
import enj_edges  # noqa: F401

SPINE = [
    "ph_stress", "ph_tone7", "vo_name", "gr_be7", "fu_intro", "rw_intro", "vo_family7", "gr_this7",
    "gr_plural7", "ph_s", "fu_family7", "rw_family7", "vo_school7", "gr_poss7", "gr_yesno",
    "fu_lost", "rw_notice", "vo_room7", "gr_prep7", "fu_where7", "rw_room7", "vo_ball", "gr_have",
    "gr_do", "fu_ball", "rw_ball", "vo_food7", "gr_count", "gr_like7", "fu_food7", "rw_food7",
    "vo_clothes7", "gr_much", "fu_shop7", "rw_shop7", "vo_date", "gr_when7", "fu_bday7", "rw_cal7",
    "vo_subj", "gr_because", "fu_subj", "rw_subj", "vo_talent", "gr_can7", "fu_club", "rw_ad",
    "vo_daily", "gr_clock", "gr_often", "fu_time7", "rw_day7", "vo_trans7", "gr_howfar",
    "fu_trans7", "rw_trans7", "vo_rule7", "gr_imp7", "gr_must7", "fu_rule7", "rw_rule7",
    "vo_animal7", "gr_why7", "gr_desc", "fu_zoo", "rw_zoo7", "vo_now", "gr_ing7", "fu_now",
    "rw_now7", "vo_weather7", "gr_excl", "fu_weather7", "rw_weather7", "vo_place", "gr_there7",
    "fu_way7", "rw_way7", "vo_look", "gr_look", "fu_look", "rw_look", "vo_noodle", "gr_would7",
    "fu_order", "rw_order", "vo_trip7", "gr_was7", "gr_ed", "ph_ed", "fu_trip7", "rw_diary",
    "vo_wknd", "gr_did7", "gr_irr7", "fu_wknd", "rw_wknd", "ph_link", "vo_vac", "gr_past8",
    "fu_vac", "rw_vac", "vo_habit", "gr_howoften", "fu_habit", "rw_habit", "ph_plos", "vo_person",
    "gr_comp8", "gr_than8", "fu_cmp", "rw_cmp", "vo_town", "gr_super", "fu_best", "rw_best",
    "vo_show", "gr_to", "fu_show", "rw_show", "vo_job8", "gr_going8", "fu_dream", "rw_dream",
    "vo_future", "gr_will", "fu_predict", "rw_future", "vo_cook", "gr_seq", "fu_recipe",
    "rw_recipe", "vo_party", "gr_invite", "fu_invite", "rw_invite", "ph_pause", "vo_advice",
    "gr_if", "fu_if", "rw_if", "vo_health", "gr_should8", "fu_health", "rw_health", "vo_vol",
    "gr_purpose", "fu_help", "rw_help", "vo_chore", "gr_could", "fu_chore", "rw_chore", "vo_mood",
    "gr_although", "fu_advice8", "rw_letter8", "vo_storm", "gr_pasting", "gr_whenwhile",
    "fu_storm", "rw_storm", "vo_story", "gr_unless", "gr_sothat", "fu_story", "rw_story", "vo_geo",
    "gr_high", "fu_fact", "rw_fact", "rw_cloze8", "vo_book", "gr_pp", "gr_yet", "fu_book",
    "rw_book", "vo_museum", "gr_ever", "gr_been", "fu_ever", "rw_museum", "vo_own", "gr_since",
    "fu_since", "rw_since", "vo_learn", "gr_by", "fu_learn", "rw_learn", "vo_fest", "gr_that",
    "gr_ifwhether", "fu_fest", "rw_fest", "vo_polite", "gr_whobj", "fu_polite", "rw_polite",
    "vo_change9", "gr_used", "fu_used", "rw_used", "vo_material", "gr_pass", "fu_made", "rw_made",
    "vo_invent", "gr_passpast", "fu_invent", "rw_invent", "vo_teen", "gr_allow", "fu_allow",
    "rw_allow", "vo_owner", "gr_mustbe", "fu_guess", "rw_guess", "vo_music", "gr_attr", "fu_music",
    "rw_music", "vo_custom", "gr_supposed", "fu_custom", "rw_custom", "vo_emotion", "gr_make",
    "fu_feel9", "rw_movie", "vo_unexp", "gr_ppast", "fu_unexp", "rw_unexp", "vo_earth",
    "gr_review", "fu_earth", "rw_earth", "rw_cloze9", "vo_memory", "gr_ger", "gr_tag", "fu_memory",
    "rw_write"
]

_got = [t["key"] for t in TOPICS]
if _got != SPINE:
    missing = [k for k in SPINE if k not in _got]
    extra = [k for k in _got if k not in SPINE]
    raise SystemExit("知识点顺序与主干不一致。缺：%s 多：%s 实际 %d 期望 %d" % (
        "、".join(missing), "、".join(extra), len(_got), len(SPINE)))
