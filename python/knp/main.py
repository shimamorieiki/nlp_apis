"""_summary_
Returns:
    _type_: _description_
"""
from typing import Dict, List, Optional
from fastapi import FastAPI
from pydantic import BaseModel


from src.services.knp_service import KNPService


class SentenceModel(BaseModel):
    """_summary_
        Sentenceクラス
    Args:
        BaseModel (_type_): _description_
    """

    # 解析対象の文
    sentence: str
    # 説明
    description: Optional[str] = None


class SentencesModel(BaseModel):
    """_summary_
        Sentenceクラス
    Args:
        BaseModel (_type_): _description_
    """

    # 解析対象の文のリスト
    sentences: List[str]
    # 説明
    description: Optional[str] = None


app = FastAPI()


@app.get("/")
async def get_api_name():
    """_summary_
        api_name を返す
    Returns:
        _type_: _description_
    """
    return {"api_name": "ginza"}


@app.post("/sentence")
async def post_sentence(sentense_model: SentenceModel):
    """_summary_
        Sentence型を受け取りそのまま返す
    Args:
        sentense (Sentence): _description_
    Returns:
        _type_: _description_
    """
    knp_parsed: List[Dict] = KNPService().parse_sentence(
        sentence=sentense_model.sentence
    )
    return knp_parsed


@app.post("/sentences")
async def post_sentences(sentenses_model: SentencesModel):
    """_summary_
        Sentence型を受け取りそのまま返す
    Args:
        sentense (Sentence): _description_
    Returns:
        _type_: _description_
    """
    knp_parsed: List[List[Dict]] = KNPService().parse_sentences(
        sentences=sentenses_model.sentences
    )

    return knp_parsed
