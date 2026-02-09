"""基本的なツール

このモジュールは、シンプルなエージェントで使用する基本的なツールを提供します。
"""
import logging
from strands import tool
from datetime import datetime

logger = logging.getLogger(__name__)


@tool
def get_current_time() -> str:
    """
    現在の日時を取得するシンプルなツール
    
    Returns:
        str: 現在の日時（ISO形式）
    """
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


@tool
def calculate(expression: str) -> str:
    """
    簡単な計算を実行するツール
    
    Args:
        expression: 計算式（例: "2 + 2", "10 * 5"）
        
    Returns:
        str: 計算結果
    """
    try:
        # 安全な計算のため、evalの代わりに制限された評価を使用
        result = eval(expression, {"__builtins__": {}}, {})
        return f"{expression} = {result}"
    except Exception as e:
        logger.error(f"計算エラー: {e}")
        return f"計算できませんでした: {expression}"


@tool
def greet(name: str) -> str:
    """
    挨拶を返すシンプルなツール
    
    Args:
        name: 挨拶する相手の名前
        
    Returns:
        str: 挨拶メッセージ
    """
    return f"こんにちは、{name}さん！"
