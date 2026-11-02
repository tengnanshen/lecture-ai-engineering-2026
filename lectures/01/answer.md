# 第1回 解答

## 演習

- 講座に固有の質問（宿題の3レベル）へのモデルの回答（要約でよい）：Default model output 3 ways to explain that, and Gemini 3.5 and 3.6 output 2 ways of the question. 3.6 specifically tell me how to confirm that. When I tried a higher temperature(1.3), it outputs only one way to explain that and tell me to confirm the correct answer again.
- 用語集の正しい意味と比べて気づいたこと：they all did it in two ways in "for an AI beginner learner" and "for business courses".
- 表示できたトークン数（入力 / 出力）：3.5/3.6/3.5-lite(default) with 1.3 temperature:596/774/459

## 宿題

- 取り組んだレベル：発展
- やったこと：Except for the output of the token number. I tried to add the function of the output of the reaction time. Also, I added the function that the chat would last until the users input exactly "STOPSTOP", with a notice showing that "keep questioning or 'STOPSTOP'" in Japanese. The model version and the temperature would be set only when they start the chat.
- 結果： They all worked. Seems that vibecoding is powerful enough in this stage.
- 気づき・疑問：There's a bug when i first test the 'lasting-chat' function. It is because that the coding doesn't contain the part of "with" function, it was fixed by copilot as soon as it find out the problem.
