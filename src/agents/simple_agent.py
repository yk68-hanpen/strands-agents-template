"""シンプルなエージェント

このモジュールは、Strands Agentsの基本的な使い方を示すシンプルな例です。
テンプレートとして使用し、独自のエージェントを作成する際の参考にしてください。
"""
import logging
from strands import Agent
from strands.models import BedrockModel

from tools.basic_tools import get_current_time, calculate, greet
from config.settings import settings

logger = logging.getLogger(__name__)


def create_simple_agent() -> Agent:
    """
    シンプルなエージェントを作成
    
    このエージェントは基本的なツールを使用して、
    ユーザーの質問に答えます。
    
    Returns:
        Agent: 設定済みのエージェントインスタンス
    """
    logger.info("シンプルなエージェントを作成中...")
    
    # モデルの初期化
    model = BedrockModel(model_id=settings.MODEL_ID)
    
    # エージェントの作成
    agent = Agent(
        name="SimpleAgent",
        model=model,
        tools=[get_current_time, calculate, greet],
        system_prompt="""あなたは親切なアシスタントです。

利用可能なツール：
- get_current_time: 現在の日時を取得
- calculate: 簡単な計算を実行
- greet: 挨拶を返す

ユーザーの質問に対して、適切なツールを使用して回答してください。"""
    )
    
    logger.info("エージェントの作成が完了しました")
    return agent


def run_agent(prompt: str) -> str:
    """
    エージェントを実行
    
    Args:
        prompt: ユーザーからの質問やリクエスト
        
    Returns:
        str: エージェントからの応答
    """
    logger.info(f"エージェントを実行: {prompt}")
    
    try:
        agent = create_simple_agent()
        response = agent(prompt)
        
        result = str(response.message)
        logger.info("エージェントの実行が完了しました")
        return result
        
    except Exception as e:
        logger.error(f"エージェント実行中にエラーが発生: {e}")
        raise
