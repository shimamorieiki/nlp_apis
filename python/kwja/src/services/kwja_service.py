"""_summary_
"""

from typing import Dict, List

import rhoknp


class KWJAService:
    """_summary_"""

    def parse_sentence(self, sentence: str) -> List[Dict]:
        """_summary_
        kwjaでパースする
        """
        kwja = rhoknp.KWJA()
        analyzed_sentence: rhoknp.Sentence = kwja.apply_to_sentence(sentence=sentence)

        kwja_dtos: List[Dict] = []

        for phrase in analyzed_sentence.phrases:
            for morpheme in phrase.morphemes:
                kwja_dict = {
                    "phrase_index": phrase.index,
                    "phrase_parent_index": phrase.parent_index,
                    "phrase_dep_type": phrase.dep_type,
                    "phrase_features": phrase.features,
                    "morpheme_surf": morpheme.surf,
                    "morpheme_reading": morpheme.reading,
                    "morpheme_lemma": morpheme.lemma,
                    "morpheme_canon": morpheme.canon,
                    "morpheme_pos": morpheme.pos,
                    "morpheme_subpos": morpheme.subpos,
                    "morpheme_conjtype": morpheme.conjtype,
                    "morpheme_conjform": morpheme.conjform,
                    "morpheme_sstring": morpheme.sstring,
                    "morpheme_fstring": morpheme.fstring,
                }

                kwja_dtos.append(kwja_dict)

        return kwja_dtos

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
