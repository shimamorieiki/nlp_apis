"""_summary_

Returns:
    _type_: _description_
"""
from typing import Dict, List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from src.services.cabocha_service import CaboChaService


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
    cabocha_parsed: List[Dict] = CaboChaService().parse(
        target_sentence=sentense_model.sentence
    )

    return cabocha_parsed
