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