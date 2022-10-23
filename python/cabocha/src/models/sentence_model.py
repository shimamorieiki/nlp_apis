"""_summary_
"""
from typing import Optional

from pydantic import BaseModel


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
