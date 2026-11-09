# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：The answer in the first lecture was literally nothing to do with the right answer, which means that AI was actually guessing what it was. This time, it responses faster and clear, and very exact.
- `--trace` で見えたツール呼び出し（ツール名と引数）：
Tool name: search_glossary
Parameter: it is a dictionary data, which includes the thing AI wish to search and the related parameter name "query" in the list of glossary.
Below is what was printed by --list-tools.
[search_glossary]
  講座の用語集から用語を検索し、定義と、どの回で扱うかを返す。
  
  AIエンジニアリングの用語や、この講座（AIE2026）に固有の言葉について
  答える前に使うこと。query には調べたい用語を1つだけ入れる（例: "LoRA"）。
  引数: {"query": {"type": "string"}}
- 1つの質問での LLM 呼び出し回数（`requests`）：2
- 追加したツールと、docstring に書いた説明： """指定した回の確認問題を作るときに使う。用語を1つ選び、問題と答えを返す。"""

## 宿題

- 取り組んだレベル：発展（a）
- やったこと：I vibe coded a ADK version of program with a "--trace" function, and I ran "LoRAとQLoRAの違いは？" and "第2回の内容から確認問題を1問出して" with it.
- 結果：it ran well, all i have done is just prompt it. ADK version seems more close to the AI I use in my daily life. I found that ADK version of it seemed to give extra information (for example "OK I will tell you that!") before it anwser the question in "第2回の内容から確認問題を1問出して". I see difference in "LoRAとQLoRAの違いは？" question in that "ADK" version decorated the answer by itself. In "--trace" function, they showed the similar pattern.
- 気づき・疑問：
