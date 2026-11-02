"""第1回: 素のLLMと会話するスクリプト。

使い方:
    uv run python -m app.ask "LoRAとは何ですか？"
    uv run python -m app.ask            # 質問を省略すると、講座に固有の質問をする

ツールは使わず、会話履歴を保って応答する。
講座に固有のことを聞くと、「分からない」と答えるか、一般論でもっともらしく答える
（講座の実際とは違う）ことを確かめよう。
（第3回で、用語集を検索できるエージェントにして改善する）
"""

import argparse
from time import perf_counter

from google import genai
from google.genai.chats import Chat
from google.genai import errors
from google.genai import types

from app.config import MODEL, TEMPERATURE, api_error_message, get_api_key

# 講座に固有の質問。正しい答えは data/glossary.json の homework-levels にある
DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"


def create_chat(client: genai.Client, temperature: float | None = None) -> Chat:
    if temperature is None:
        return client.chats.create(model=MODEL)
    return client.chats.create(
        model=MODEL,
        config=types.GenerateContentConfig(temperature=temperature),
    )


def ask(question: str, chat: Chat) -> str:
    started_at = perf_counter()
    response = chat.send_message(question)
    elapsed = perf_counter() - started_at
    usage = response.usage_metadata
    if usage is not None:
        print(f"[入力トークン] {usage.prompt_token_count}")
        print(f"[出力トークン] {usage.candidates_token_count}")
    print(f"[応答時間] {elapsed:.2f} 秒")

    return response.text


def chat_with_user(first_question: str, chat: Chat) -> None:
    question = first_question
    while True:
        print(f"[質問] {question}\n")
        print(ask(question, chat))
        print("\n続けて質問を入力するか、「STOPSTOP」と入力して終了してください。")
        question = input("> ")
        if question == "STOPSTOP":
            print("対話を終了します。")
            return


def main() -> None:
    parser = argparse.ArgumentParser(description="素のLLMに質問する")
    parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    parser.add_argument(
        "--temperature",
        type=float,
        default=TEMPERATURE,
        metavar="0..2",
        help="生成の temperature（省略時はAIE_TEMPERATUREまたはGeminiの既定値）",
    )
    args = parser.parse_args()
    if args.temperature is not None and not 0 <= args.temperature <= 2:
        parser.error("--temperature は 0 から 2 の範囲で指定してください")

    print(f"[model] {MODEL}")
    if args.temperature is not None:
        print(f"[temperature] {args.temperature}")
    try:
        with genai.Client(api_key=get_api_key()) as client:
            chat = create_chat(client, temperature=args.temperature)
            chat_with_user(args.question, chat)
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
