# 第4回 解答

## 演習

- 基準別の一致率（直す前）：根拠　7/9　、範囲　10/10　、ヒント　10/10　、分かりやすさ　9/10　、回の表示　8/10　
- 要確認の件数（直す前）：1
- 直した基準と、書き足した方針：There is only one that was judged as unsure iby model, which is the "not in the dictionary" one. I followed the instruction and delete the final line of the rubric.md and added the lin in 根拠.
- 基準別の一致率と要確認の件数（直した後）：
基準別の一致率（自分のラベルと LLM の判定、10 件）
  根拠                8/10
  範囲               10/10
  ヒント             10/10
  分かりやすさ       10/10
  回の表示（コード）  8/10
総合の一致率   7/10   （自動判定できた 10/10 件 = coverage 100%）
- 講師のラベルと自分のラベルで判定が違った項目と、そう判定した理由： It was almost my fault that I didn't check the japanese in detail so I messed up something. 
- 気づき・疑問：I don't have a lot of in 演習. 

## 宿題

- 取り組んだレベル：基礎
- やったこと：I let changed the code to let the model change the order of the output of judgment and reason. I added a line in #根拠 to let the model mark a fail in Q3 to deny the action of guessing the name of the term by its katakana.
- 結果：The order in output changed as I wished, yet, the judgement of the #根拠 in Q3 doesnt change.
- 気づき・疑問：I am confused that the judgement of Q3 didn't change. I wrote it quite clear that it is not allowed for llm to guess the term by its katakana.
