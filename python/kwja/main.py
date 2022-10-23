"""_summary_
Returns:
    _type_: _description_
"""
from typing import Dict, List

from fastapi import FastAPI

from src.models.sentence_model import SentenceModel
from src.models.sentences_model import SentencesModel
from src.services.kwja_service import KWJAService

app = FastAPI()


@app.get("/")
async def get_api_name():
    """_summary_
        api_name を返す
    Returns:
        _type_: _description_
    """
    return {"api_name": "kwja"}


@app.post("/sentence")
async def post_sentence(sentense_model: SentenceModel):
    """_summary_
        Sentence型を受け取りそのまま返す
    Args:
        sentense (Sentence): _description_
    Returns:
        _type_: _description_
    """
    kwja_parsed: List[Dict] = KWJAService().parse_sentence(
        sentence=sentense_model.sentence
    )

    return kwja_parsed


@app.post("/sentences")
async def post_sentences(sentenses_model: SentencesModel):
    """_summary_
        Sentence型を受け取りそのまま返す
    Args:
        sentense (Sentence): _description_
    Returns:
        _type_: _description_
    """
    kwja_parsed: List[List[Dict]] = KWJAService().parse_sentences(
        sentences=sentenses_model.sentences
    )

    return kwja_parsed
