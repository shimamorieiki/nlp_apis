"""_summary_
"""

from typing import Dict, List
from pyknp import KNP


class KNPService:
    """_summary_"""

    def parse_sentence(self, sentence: str) -> List[Dict]:
        """_summary_
        ja_ginza_electraでパースする
        とは書いたが、現状は内部で ja_ginza_electra と
        ja_ginza のどっちが動いているのかわからない
        """

        # Default is JUMAN++.
        # If you use JUMAN, use KNP(jumanpp=False)
        knp = KNP()
        result = knp.parse(sentence=sentence)
        knp_items_list: List[Dict] = []

        # 各文節へのアクセス
        for bnst in result.bnst_list():

            # 各形態素へのアクセス
            for mrph in bnst.mrph_list():
                knp_items_dict = {
                    "mrph_id": mrph.mrph_id,
                    "midasi": mrph.midasi,
                    "yomi": mrph.yomi,
                    "genkei": mrph.genkei,
                    "hinsi": mrph.hinsi,
                    "bunrui": mrph.bunrui,
                    "katuyou1": mrph.katuyou1,
                    "katuyou2": mrph.katuyou2,
                    "imis": mrph.imis,
                    "rename": mrph.repname,
                    "bnst_id": bnst.bnst_id,
                    "parent_id": bnst.parent_id,
                    "dpndtype": bnst.dpndtype,
                    "fstring": bnst.fstring,
                }
                knp_items_list.append(knp_items_dict)

        return knp_items_list

    def parse_sentences(self, sentences: List[str]) -> List[List[Dict]]:
        """_summary_
        ja_ginza_electraでパースする
        とは書いたが、現状は内部で ja_ginza_electra と
        ja_ginza のどっちが動いているのかわからない
        """
        parsed_sentences: List[List[Dict]] = []
        for sentence in sentences:
            parsed_sentences.append(self.parse_sentence(sentence=sentence))

        return parsed_sentences
