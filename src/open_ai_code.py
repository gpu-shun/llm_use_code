# OpenAIのAPIを利用するための基本コード
from openai import OpenAI

client = OpenAI(
    api_key="API_KEY" # 適宜変更する
)

completion = client.chat.completions.create(
    model="gpt-4o-mini", # 適切なモデル名を指定
    messages=[
        {"role": "system", "content": "あたなはとても優秀な日本人のアシスタントです。"},
        {
            "role": "user",
            "content": "世界で一番賢いAIを教えてください"
        }
    ]
)

print(completion.choices[0].message.content)
