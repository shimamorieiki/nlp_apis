"""_summary_
"""

from typing import Dict, List

from janome.tokenizer import Tokenizer


class JanomeService:
    """_summary_"""

    def parse_sentence(self, sentence: str) -> List[Dict]:
        """_summary_
        kwjaでパースする
        """
        janome_dtos: List[Dict] = []
        tokenizer = Tokenizer()
        for token in tokenizer.tokenize(sentence):
            if isinstance(token, str):
                break

            janome_dict = {
                "midasi": token.surface,
                "hinsi": token.part_of_speech.split(",")[0],
                "detail_large": token.part_of_speech.split(",")[1],
                "detail_middle": token.part_of_speech.split(",")[2],
                "detail_small": token.part_of_speech.split(",")[3],
                "katuyou_type": token.infl_type,
                "katuyou_form": token.infl_form,
                "genkei": token.base_form,
                "yomi": token.reading,
                "hatuon": token.phonetic,
            }

            janome_dtos.append(janome_dict)

        return janome_dtos

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
