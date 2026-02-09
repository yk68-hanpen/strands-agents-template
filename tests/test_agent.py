"""シンプルなエージェントのテスト"""
import pytest
from pathlib import Path
import sys

# srcディレクトリをパスに追加
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from tools.basic_tools import get_current_time, calculate, greet


def test_get_current_time():
    """時刻取得ツールのテスト"""
    result = get_current_time()
    
    assert isinstance(result, str)
    assert len(result) > 0
    # 日付フォーマットの確認（YYYY-MM-DD HH:MM:SS）
    assert "-" in result
    assert ":" in result


def test_calculate():
    """計算ツールのテスト"""
    # 正常な計算
    result = calculate("2 + 2")
    assert "4" in result
    
    result = calculate("10 * 5")
    assert "50" in result
    
    result = calculate("100 - 25")
    assert "75" in result
    
    # エラーケース
    result = calculate("invalid")
    assert "計算できませんでした" in result


def test_greet():
    """挨拶ツールのテスト"""
    result = greet("太郎")
    
    assert "太郎" in result
    assert "こんにちは" in result
    
    # 別の名前でもテスト
    result = greet("花子")
    assert "花子" in result
