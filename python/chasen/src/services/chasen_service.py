"""_summary_
"""

import subprocess
from typing import Dict, List


class ChasenService:
    """_summary_"""

    def parse_sentence(self, sentence: str) -> List[Dict]:
        """_summary_
        ja_chasen_electraでパースする
        とは書いたが、現状は内部で ja_chasen_electra と
        ja_chasen のどっちが動いているのかわからない
        """

        result = subprocess.run(
            f"echo {sentence} | chasen",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf8",
            check=True,
        )
        chasen_dtos: List[Dict] = []
        for parsed_items in result.stdout.split("\n"):

            if parsed_items == "EOS" or len(parsed_items) == 0:
                # EOS要素or空要素のときは何もしない
                continue

            morph_info: List[str] = parsed_items.replace("\t", ",").split(",")
            details: List[str] = morph_info[3].split("-")
            if len(details) >= 5 or len(details) == 0:
                raise ValueError("品詞詳細が正しくありません")

            if len(details) == 4:
                hinsi = details[0]
                detail_large = details[1]
                detail_middle = details[2]
                detail_small = details[3]
            elif len(details) == 3:
                hinsi = details[0]
                detail_large = details[1]
                detail_middle = details[2]
                detail_small = "*"
            elif len(details) == 2:
                hinsi = details[0]
                detail_large = details[1]
                detail_middle = "*"
                detail_small = "*"
            else:
                hinsi = details[0]
                detail_large = "*"
                detail_middle = "*"
                detail_small = "*"

            if len(morph_info) == 4:
                chasen_dict = {
                    "midasi": morph_info[0],
                    "yomi": morph_info[1],
                    "genkei": morph_info[2],
                    "hinsi": hinsi,
                    "detail_large": detail_large,
                    "detail_middle": detail_middle,
                    "detail_small": detail_small,
                    "katuyou_type": "*",
                    "katuyou_form": "*",
                }
                chasen_dtos.append(chasen_dict)

            elif len(morph_info) == 6:
                chasen_dict = {
                    "midasi": morph_info[0],
                    "yomi": morph_info[1],
                    "genkei": morph_info[2],
                    "hinsi": hinsi,
                    "detail_large": detail_large,
                    "detail_middle": detail_middle,
                    "detail_small": detail_small,
                    "katuyou_type": morph_info[4],
                    "katuyou_form": morph_info[5],
                }
                chasen_dtos.append(chasen_dict)
            else:
                raise ValueError("要素の数が異なる。")

        return chasen_dtos

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
