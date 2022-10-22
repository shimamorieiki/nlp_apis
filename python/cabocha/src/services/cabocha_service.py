"""_summary_
"""

from typing import Dict, List, Optional
from src.morph_list.src.v3.morph_list import MorphListV3 as MorphList
from src.morph_list.src.v3.morph import MorphV3 as Morph


class CaboChaService:
    """_summary_"""

    def morph_to_dict(
        self, morph: Morph
    ) -> Dict[str, str | int | List[str] | Optional[int]]:
        """_summary_
            元のcabochaの要素のみを出力する
        Args:
            morph_list (MorphList): _description_
        """
        return {
            "midasi": morph.midasi,
            "genkei": morph.genkei,
            "yomi": morph.yomi,
            "hatuon": morph.hatuon,
            "hinsi": morph.hinsi,
            "katuyou_type": morph.katuyou_type,
            "katuyou_form": morph.katuyou_form,
            "detail_large": morph.detail_large,
            "detail_middle": morph.detail_middle,
            "detail_small": morph.detail_small,
            "bnst_id": morph.bnst_id,
            "parent_id": morph.parent_id,
        }

    def to_original_dict(self, morph_list: MorphList):
        """_summary_
            MorphListをもともとCaboChaに存在する要素のdictに変換する
        Args:
            morph_list (MorphList): _description_
        """
        morph_dicts_list: List[Dict] = []

        for morph in morph_list:
            morph_dicts_list.append(self.morph_to_dict(morph))
        return morph_dicts_list

    def parse(self, target_sentence: str):
        """_summary_"""
        morph_list: MorphList = MorphList.from_str(input_sentence=target_sentence)
        morph_list.print()
        return self.to_original_dict(morph_list=morph_list)
