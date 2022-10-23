"""_summary_

Returns:
    _type_: _description_
"""
from typing import Dict, List
from fastapi import FastAPI
from src.models.sentence_model import SentenceModel
from src.models.sentences_model import SentencesModel
from src.services.cabocha_service import CaboChaService


app = FastAPI()


@app.get("/")
async def get_api_name():
    """_summary_
        api_name を返す
    Returns:
        _type_: _description_
    """
    return {"api_name": "cabocha"}


@app.post("/")
async def post_sentence(sentense_model: SentenceModel):
    """_summary_
        Sentence型を受け取りそのまま返す
    Args:
        sentense (Sentence): _description_

    Returns:
        _type_: _description_
    """
    cabocha_parsed: List[Dict] = CaboChaService().parse_sentence(
        sentence=sentense_model.sentence
    )

    return cabocha_parsed


@app.post("/sentences")
async def post_sentences(sentenses_model: SentencesModel):
    """_summary_
        Sentence型を受け取りそのまま返す
    Args:
        sentense (Sentence): _description_
    Returns:
        _type_: _description_
    """
    knp_parsed: List[List[Dict]] = CaboChaService().parse_sentences(
        sentences=sentenses_model.sentences
    )

    return knp_parsed
