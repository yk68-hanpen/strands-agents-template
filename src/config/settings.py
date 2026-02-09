"""設定管理モジュール"""
import os
from pathlib import Path
from typing import List
from dotenv import load_dotenv

# .envファイルを読み込み
load_dotenv()


class Settings:
    """アプリケーション設定クラス
    
    環境変数から設定を読み込み、アプリケーション全体で使用する設定を管理します。
    """
    
    # AWS設定
    AWS_REGION: str = os.getenv("AWS_REGION", "us-east-1")
    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID", "")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY", "")
    
    # モデル設定
    MODEL_ID: str = os.getenv("MODEL_ID", "us.anthropic.claude-sonnet-4-20250514-v1:0")
    
    # GitHub設定
    GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN", "")
    
    # 出力設定
    OUTPUT_DIR: Path = Path(os.getenv("OUTPUT_DIR", "output"))
    
    @classmethod
    def validate(cls) -> tuple[bool, List[str]]:
        """
        必須設定の検証
        
        Returns:
            tuple[bool, List[str]]: (検証結果, 不足している設定のリスト)
        """
        missing = []
        
        if not cls.AWS_REGION:
            missing.append("AWS_REGION")
        if not cls.AWS_ACCESS_KEY_ID:
            missing.append("AWS_ACCESS_KEY_ID")
        if not cls.AWS_SECRET_ACCESS_KEY:
            missing.append("AWS_SECRET_ACCESS_KEY")
        
        return len(missing) == 0, missing
    
    @classmethod
    def get_summary(cls) -> str:
        """設定のサマリーを取得（デバッグ用）"""
        return f"""
Settings Summary:
  AWS Region: {cls.AWS_REGION}
  Model ID: {cls.MODEL_ID}
  Output Dir: {cls.OUTPUT_DIR}
  GitHub Token: {'設定済み' if cls.GITHUB_TOKEN else '未設定'}
"""


settings = Settings()
