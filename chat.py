from openai import OpenAI

with open("key.txt", "r", encoding="utf-8") as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

messages = []

while True:
    q = input("\n你：")
    if q in ("q", "退出"):
        break

    messages.append({"role": "user", "content": q})

    stream = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        stream=True,          # ← 关键：不是等全部生成完
    )

    print("AI：", end="", flush=True)
    answer = ""
    for chunk in stream:                       # ← 服务器一小段一小段往回吐
        if not chunk.choices:
            continue
        piece = chunk.choices[0].delta.content
        if piece:
            answer += piece
            print(piece, end="", flush=True)   # ← flush 让它立刻显示，不攒着
    print()

    messages.append({"role": "assistant", "content": answer})