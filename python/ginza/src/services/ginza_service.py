"""_summary_
"""

import subprocess
from typing import Dict, List


class GinzaService:
    """_summary_"""

    def parse_sentence(self, sentence: str) -> List[Dict]:
        """_summary_
        ja_ginza_electraでパースする
        とは書いたが、現状は内部で ja_ginza_electra と
        ja_ginza のどっちが動いているのかわからない
        """

        result = subprocess.run(
            f"echo {sentence} | ginza -f cabocha",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf8",
            check=True,
        )

        ginza_dtos: List[Dict] = []
        bnst_id: str = "0"
        bnst_parent_id: str = "0"

        for parsed_items in result.stdout.split("\n"):

            if parsed_items == "EOS" or len(parsed_items) == 0:
                # EOS要素or空要素のときは何もしない
                continue

            if parsed_items[0] == "*":
                # "* 3 4D 0/0 1.985818"
                bnst_info = parsed_items.split(" ")
                bnst_id = bnst_info[1]
                bnst_parent_id = bnst_info[2][:-1]

                continue

            ginza_dto_bnst_id = int(bnst_id)
            ginza_dto_parent_id = int(bnst_parent_id)

            morph_info: List[str] = parsed_items.replace("\t", ",").split(",")
            if len(morph_info) == 11:
                ginza_dict = {
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
                    "bnst_id": ginza_dto_bnst_id,
                    "parent_id": ginza_dto_parent_id,
                }
                ginza_dtos.append(ginza_dict)

            elif len(morph_info) == 9:
                # 多分未定義語だと思うが要素が8つしか無いものがある
                # ['エコーロケーション', '名詞', '固有名詞', '組織', '*', '*', '*', '*']
                ginza_dict = {
                    "midasi": morph_info[0],
                    "hinsi": morph_info[1],
                    "detail_large": morph_info[2],
                    "detail_middle": morph_info[3],
                    "detail_small": morph_info[4],
                    "katuyou_type": morph_info[5],
                    "katuyou_form": morph_info[6],
                    "genkei": morph_info[7],
                    "bnst_id": ginza_dto_bnst_id,
                    "parent_id": ginza_dto_parent_id,
                    "yomi": None,
                    "hatuon": None,
                }
                ginza_dtos.append(ginza_dict)
            else:
                raise ValueError("要素の数が異なる。")

        return ginza_dtos

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

    @DeprecationWarning
    def parse_ja_ginza_electra(self, sentence: str):
        """_summary_
        ja_ginza_electraでパースする
        とは書いたが、現状は内部で ja_ginza_electra と
        ja_ginza のどっちが動いているのかわからない
        """

    @DeprecationWarning
    def parse_ja_ginza(self, sentence: str):
        """_summary_
        ja_ginzaでパースする
        spaCyのコマンドからCaboChaの出力を出せるようになってから作る
        """
