# Strands Agents Template

Strands Agentsを使ったAIエージェント開発のテンプレートプロジェクトです。

## 概要

このテンプレートは、Strands Agentsを使用したシンプルなエージェントの実装例を提供します。
基本的なツールの使い方を学び、独自のエージェントを作成する際の出発点として使用できます。

### 主な機能

- 🤖 シンプルなエージェントの実装例
- 🛠️ 基本的なツール（時刻取得、計算、挨拶）
- 🐳 Dockerコンテナでの実行環境
- 🔧 拡張しやすい設計
- 📚 GitHub Actionsの汎用テンプレート

## ディレクトリ構造

```
strands-agents-template/
├── .github/
│   └── workflows/
│       ├── issue-agent.yml        # Issue作成時にエージェント実行
│       ├── pr-agent.yml           # PR作成時にエージェント実行
│       └── scheduled-agent.yml    # 定期実行
├── src/
│   ├── agents/
│   │   └── simple_agent.py       # シンプルなエージェント
│   ├── tools/
│   │   └── basic_tools.py        # 基本的なツール（時刻、計算、挨拶）
│   ├── config/
│   │   └── settings.py           # 設定管理
│   └── main.py                   # エントリーポイント
├── tests/
│   └── test_agent.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

## 技術スタック

- **Python**: 3.14+
- **Strands Agents**: AIエージェントフレームワーク
- **AWS Bedrock**: LLMモデル（Claude 4 Sonnet）
- **Docker**: コンテナ化
- **GitHub Actions**: CI/CD自動化

## セットアップ

### 1. 環境変数の設定

`.env.example`をコピーして`.env`を作成し、必要な値を設定します：

```bash
cp .env.example .env
```

`.env`ファイルを編集：

```env
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
MODEL_ID=us.anthropic.claude-sonnet-4-20250514-v1:0
GITHUB_TOKEN=your_github_token
```

### 2. ローカル実行

#### Python環境で実行

```bash
# 依存関係のインストール
pip install -r requirements.txt

# デフォルトのプロンプトで実行
python src/main.py

# カスタムプロンプトで実行
python src/main.py "こんにちは！今何時ですか？"

# 計算を依頼
python src/main.py "100 * 25 を計算してください"
```

#### Dockerで実行

```bash
# イメージのビルドと実行
docker-compose up --build

# または個別に実行
docker build -t simple-agent .
docker run --env-file .env simple-agent
```

### 3. GitHub Actionsの設定

リポジトリのSecretsに以下を設定：

- `AWS_REGION`
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `MODEL_ID`
- `GITHUB_TOKEN`（自動的に利用可能）

## 使い方

### シンプルなエージェント

デフォルトでは、`simple_agent.py`が実行されます。このエージェントは`tools/basic_tools.py`で定義された以下のツールを使用します：

- **get_current_time**: 現在の日時を取得
- **calculate**: 簡単な計算を実行
- **greet**: 挨拶を返す

```bash
# 実行例
python src/main.py "こんにちは！今何時ですか？また、10 * 25 を計算してください。"
```

### GitHub Actionsでの自動実行

#### 1. Issueトリガー

`agent-request`ラベルを付けたIssueを作成すると、Issueの内容をプロンプトとしてエージェントを実行します。

#### 2. PRトリガー

PRを作成すると、変更内容を分析してコメントを投稿します（カスタマイズ可能）。

#### 3. 定期実行

毎週月曜日の9:00 (UTC)に自動的にエージェントを実行します。手動実行も可能です。

```bash
# GitHub UIから手動実行
Actions → Scheduled Agent → Run workflow
```

## カスタマイズ

### 独自のツールを追加

`src/tools/basic_tools.py`に新しいツールを追加するか、新しいファイルを作成：

```python
# src/tools/basic_tools.py に追加
from strands import tool

@tool
def my_custom_tool(param: str) -> str:
    """
    独自のツールの説明
    
    Args:
        param: パラメータの説明
        
    Returns:
        str: 結果
    """
    # ツールのロジックを実装
    return f"結果: {param}"
```

`src/agents/simple_agent.py`でツールをインポートして使用：

```python
from tools.basic_tools import get_current_time, calculate, greet, my_custom_tool

# エージェント作成時にツールを追加
agent = Agent(
    name="SimpleAgent",
    model=model,
    tools=[get_current_time, calculate, greet, my_custom_tool],
    system_prompt="..."
)
```

### エージェントのプロンプト調整

`src/agents/simple_agent.py`の`system_prompt`を編集して、エージェントの振る舞いを変更できます。

### GitHub Actionsワークフローの拡張

`.github/workflows/`のYAMLファイルを編集して、独自の自動化フローを追加できます。

## テスト

```bash
pytest tests/
```

すべてのツールが正しく動作することを確認できます。

## トラブルシューティング

### 環境変数が設定されていない

```
Error: 必須の環境変数が設定されていません
```

→ `.env`ファイルを作成し、必要な環境変数を設定してください。

### モデルIDのエラー

```
ValidationException: Invocation of model ID ... isn't supported
```

→ `.env`の`MODEL_ID`を正しいInference Profile IDに変更してください：
```
MODEL_ID=us.anthropic.claude-sonnet-4-20250514-v1:0
```

## ライセンス

MIT License

## 貢献

プルリクエストを歓迎します！

## サポート

問題が発生した場合は、Issueを作成してください。
