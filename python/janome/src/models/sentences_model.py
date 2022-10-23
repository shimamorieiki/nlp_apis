"""_summary_
"""

from typing import List, Optional

from pydantic import BaseModel


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
