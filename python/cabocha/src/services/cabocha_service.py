"""_summary_
"""

from typing import Dict, List
import CaboCha as ca


class CaboChaService:
    """_summary_"""

    def parse_sentence(self, sentence: str) -> List[Dict]:
        """_summary_
        cabochaを使用して係り受け解析を行う(1文)
        """

        cabocha_dtos: List[Dict] = []
        bnst_id: str = "0"
        bnst_parent_id: str = "0"
        cabocha = ca.Parser("")

        try:  # パースする
            tree = cabocha.parse(sentence)
            parsed_items_list: List[str] = tree.toString(
                ca.CABOCHA_FORMAT_LATTICE
            ).split("\n")
        except Exception as ex:
            raise ex

        for parsed_items in parsed_items_list:

            if parsed_items == "EOS" or len(parsed_items) == 0:
                # EOS要素or空要素のときは何もしない
                continue

            if parsed_items[0] == "*":
                # "* 3 4D 0/0 1.985818"
                bnst_info = parsed_items.split(" ")
                bnst_id = bnst_info[1]
                bnst_parent_id = bnst_info[2][:-1]

                continue

            cabocha_dto_bnst_id = int(bnst_id)
            cabocha_dto_parent_id = int(bnst_parent_id)

            morph_info: List[str] = parsed_items.replace("\t", ",").split(",")

            if len(morph_info) == 10:
                cabocha_dict = {
                    "midasi": morph_info[0],
                    "hinsi": morph_info[1],
                    "detail_large": morph_info[2],
                    "detail_middle": morph_info[3],
                    "detail_small": morph_info[4],
                    "katuyou_type": morph_info[5],
                    "katuyou_form": morph_info[6],
                    "genkei": morph_info[7],
                    "yomi": morph_info[8],
                    "hatuon": morph_info[9],
                    "bnst_id": cabocha_dto_bnst_id,
                    "parent_id": cabocha_dto_parent_id,
                }
                cabocha_dtos.append(cabocha_dict)

            elif len(morph_info) == 8:
                # 多分未定義語だと思うが要素が8つしか無いものがある
                # ['エコーロケーション', '名詞', '固有名詞', '組織', '*', '*', '*', '*']
                cabocha_dict = {
                    "midasi": morph_info[0],
                    "hinsi": morph_info[1],
                    "detail_large": morph_info[2],
                    "detail_middle": morph_info[3],
                    "detail_small": morph_info[4],
                    "katuyou_type": morph_info[5],
                    "katuyou_form": morph_info[6],
                    "genkei": morph_info[7],
                    "bnst_id": cabocha_dto_bnst_id,
                    "parent_id": cabocha_dto_parent_id,
                    "yomi": None,
                    "hatuon": None,
                }
                cabocha_dtos.append(cabocha_dict)

        return cabocha_dtos

    def parse_sentences(self, sentences: List[str]) -> List[List[Dict]]:
        """_summary_
        cabochaを使用して係り受け解析を行う(複数文)
        """
        parsed_sentences: List[List[Dict]] = []
        for sentence in sentences:
            parsed_sentences.append(self.parse_sentence(sentence=sentence))

        return parsed_sentences
