
# OpenAI + LangChain サンプルコード集

このリポジトリは、OpenAI の API を直接利用するコードと、LangChain を経由して利用するコードの 2 種類のサンプルをまとめたものです。  
シンプルながら実践的なサンプルとして活用いただけるように作成しています。

---

## 目次
- [ディレクトリ構成](#ディレクトリ構成)
- [使用技術](#使用技術)
- [インストール](#インストール)
- [使い方](#使い方)
- [コードの詳細](#コードの詳細)
  - [src/open_ai_code.py](#srcopen_ai_codepy)
  - [src/openai_langchain_code](#srcopenai_langchain_code)
- [ライセンス](#ライセンス)

---

## ディレクトリ構成

```bash
.
├── src
│   ├── open_ai_code.py
│   └── openai_langchain_code
└── README.md
```

- **open_ai_code.py**  
  OpenAI の API を直接呼び出すためのサンプルコード  

- **openai_langchain_code**  
  LangChain を利用して OpenAI の API を呼び出すためのサンプルコード  

---

## 使用技術
- Python 3.9+
- [OpenAI Python Library](https://github.com/openai/openai-python)
- [LangChain](https://github.com/hwchase17/langchain) (オプション)

---

## インストール

以下は基本的なセットアップ例です。すでに環境が整っている場合は適宜スキップしてください。

1. **リポジトリをクローン**
   ```bash
   git clone https://example.com/your-repo-url.git
   cd your-repo
   ```

2. **仮想環境を作成 (任意)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # .\venv\Scripts\activate  # Windows
   ```

3. **依存関係をインストール**
   ```bash
   pip install openai
   pip install langchain
   # 必要に応じてその他のライブラリもインストール
   ```

---

## 使い方

1. **API キーの設定**  
   - `open_ai_code.py` と `openai_langchain_code` 内の `API_KEY` を、あなたの OpenAI の API キーに置き換えてください。

2. **実行**  
   - 直接 OpenAI API を呼び出す場合:
     ```bash
     python src/open_ai_code.py
     ```
   - LangChain 経由で呼び出す場合:
     ```bash
     python src/openai_langchain_code
     ```

3. **出力の確認**  
   - コンソールに API のレスポンス（アシスタントの返答）が表示されます。

---

## コードの詳細

### src/open_ai_code.py

以下は OpenAI の API を直接呼び出すための最小限のサンプルコードです。

```python
# OpenAIのAPIを利用するための基本コード
from openai import OpenAI

client = OpenAI(
    api_key="API_KEY"  # 適宜変更する
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",  # 適切なモデル名を指定
    messages=[
        {"role": "system", "content": "あたなはとても優秀な日本人のアシスタントです。"},
        {
            "role": "user",
            "content": "世界で一番賢いAIを教えてください"
        }
    ]
)

print(completion.choices[0].message.content)
```

### src/openai_langchain_code

以下は LangChain を利用して OpenAI API を呼び出すサンプルコードです。

```python
# OpenAIのAPIをLangChain経由で利用するための基本コード
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# ChatOpenAIクライアントの設定
llm = ChatOpenAI(
    model="gpt-4o-mini",  # 適切なモデル名を指定
    openai_api_key="API_KEY"  # OpenAIのAPIキーを設定
)

# メッセージの構築
messages = [
    SystemMessage(content="あなたはとても優秀な日本人のアシスタントです"),
    HumanMessage(content="夏に見える一番きれな星座を教えてください")
]

# LLMでのチャット実行
response = llm.invoke(messages)

# 結果の出力
print(response.content)
```

---

## ライセンス

本リポジトリは MIT License にて公開しています。詳細は [LICENSE](LICENSE) ファイルをご確認ください。

---

> **Note**  
> 本コードはサンプルとして提供しており、本番運用を行う際はセキュリティ・エラー処理・リトライ機構などの実装を検討してください。  
> また、OpenAI のモデルやプランにより料金やレスポンス内容が変わる場合がありますのでご注意ください。
```

# OpenAI + LangChain サンプルコード集

このリポジトリは、OpenAI の API を直接利用するコードと、LangChain を経由して利用するコードの 2 種類のサンプルをまとめたものです。  
シンプルながら実践的なサンプルとして活用いただけるように作成しています。

---

## 目次
- [ディレクトリ構成](#ディレクトリ構成)
- [使用技術](#使用技術)
- [インストール](#インストール)
- [使い方](#使い方)
- [コードの詳細](#コードの詳細)
  - [src/open_ai_code.py](#srcopen_ai_codepy)
  - [src/openai_langchain_code](#srcopenai_langchain_code)
- [ライセンス](#ライセンス)

---

## ディレクトリ構成

```bash
.
├── src
│   ├── open_ai_code.py
│   └── openai_langchain_code
└── README.md
```

- **open_ai_code.py**  
  OpenAI の API を直接呼び出すためのサンプルコード  

- **openai_langchain_code**  
  LangChain を利用して OpenAI の API を呼び出すためのサンプルコード  

---

## 使用技術
- Python 3.9+
- [OpenAI Python Library](https://github.com/openai/openai-python)
- [LangChain](https://github.com/hwchase17/langchain) (オプション)

---

## インストール

以下は基本的なセットアップ例です。すでに環境が整っている場合は適宜スキップしてください。

1. **リポジトリをクローン**
   ```bash
   git clone https://example.com/your-repo-url.git
   cd your-repo
   ```

2. **仮想環境を作成 (任意)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # .\venv\Scripts\activate  # Windows
   ```

3. **依存関係をインストール**
   ```bash
   pip install openai
   pip install langchain
   # 必要に応じてその他のライブラリもインストール
   ```

---

## 使い方

1. **API キーの設定**  
   - `open_ai_code.py` と `openai_langchain_code` 内の `API_KEY` を、あなたの OpenAI の API キーに置き換えてください。

2. **実行**  
   - 直接 OpenAI API を呼び出す場合:
     ```bash
     python src/open_ai_code.py
     ```
   - LangChain 経由で呼び出す場合:
     ```bash
     python src/openai_langchain_code
     ```

3. **出力の確認**  
   - コンソールに API のレスポンス（アシスタントの返答）が表示されます。

---

## コードの詳細

### src/open_ai_code.py

以下は OpenAI の API を直接呼び出すための最小限のサンプルコードです。

```python
# OpenAIのAPIを利用するための基本コード
from openai import OpenAI

client = OpenAI(
    api_key="API_KEY"  # 適宜変更する
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",  # 適切なモデル名を指定
    messages=[
        {"role": "system", "content": "あたなはとても優秀な日本人のアシスタントです。"},
        {
            "role": "user",
            "content": "世界で一番賢いAIを教えてください"
        }
    ]
)

print(completion.choices[0].message.content)
```

### src/openai_langchain_code

以下は LangChain を利用して OpenAI API を呼び出すサンプルコードです。

```python
# OpenAIのAPIをLangChain経由で利用するための基本コード
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# ChatOpenAIクライアントの設定
llm = ChatOpenAI(
    model="gpt-4o-mini",  # 適切なモデル名を指定
    openai_api_key="API_KEY"  # OpenAIのAPIキーを設定
)

# メッセージの構築
messages = [
    SystemMessage(content="あなたはとても優秀な日本人のアシスタントです"),
    HumanMessage(content="夏に見える一番きれな星座を教えてください")
]

# LLMでのチャット実行
response = llm.invoke(messages)

# 結果の出力
print(response.content)
```

---

## ライセンス

本リポジトリは MIT License にて公開しています。詳細は [LICENSE](LICENSE) ファイルをご確認ください。

---

> **Note**  
> 本コードはサンプルとして提供しており、本番運用を行う際はセキュリティ・エラー処理・リトライ機構などの実装を検討してください。  
> また、OpenAI のモデルやプランにより料金やレスポンス内容が変わる場合がありますのでご注意ください。
```
