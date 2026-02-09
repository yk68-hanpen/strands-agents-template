"""エントリーポイント

このファイルは、エージェントを実行するためのメインスクリプトです。
コマンドライン引数でプロンプトを指定できます。
"""
import sys
import logging
from pathlib import Path

# srcディレクトリをパスに追加
sys.path.insert(0, str(Path(__file__).parent))

from agents.simple_agent import run_agent
from config.settings import settings

# ロガーの設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def validate_environment() -> bool:
    """
    環境設定を検証
    
    Returns:
        bool: 検証が成功したかどうか
    """
    is_valid, missing = settings.validate()
    
    if not is_valid:
        logger.error("必須の環境変数が設定されていません")
        logger.error(f"不足している設定: {', '.join(missing)}")
        logger.error("詳細は .env.example を参照してください")
        return False
    
    return True


def get_prompt_from_args() -> str:
    """
    コマンドライン引数からプロンプトを取得
    
    Returns:
        str: ユーザーのプロンプト
    """
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:])
    return "こんにちは！今何時ですか？"


def main() -> None:
    """メイン処理"""
    try:
        # 環境設定の検証
        if not validate_environment():
            sys.exit(1)
        
        # プロンプトの取得
        prompt = get_prompt_from_args()
        logger.info(f"プロンプト: {prompt}")
        
        # エージェント実行
        result = run_agent(prompt)
        
        # 結果を表示
        print("\n" + "="*50)
        print("エージェントの応答:")
        print("="*50)
        print(result)
        print("="*50 + "\n")
        
    except KeyboardInterrupt:
        logger.info("\n処理が中断されました")
        sys.exit(0)
    except Exception as e:
        logger.error(f"エラーが発生しました: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
