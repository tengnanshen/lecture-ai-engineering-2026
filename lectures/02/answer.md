# 第2回 解答

## 演習

- 使ったモデル・設定（`result.json` の `config` から）："base_model": "Qwen/Qwen3.5-0.8B"
- 自分で学習を実行したか（`executed_training_myself`）：はい 
- 学習前：`format_rate` =　0.09523809523809523 / `content_rate` =　0.0
- 学習後：`format_rate` =　1.0 / `content_rate` =　 0.9047619047619048
- 退行した質問：成績はいつ出ますか/オフィスアワーは事前予約が必要ですか
- 学習後に残った失敗と、その型（根拠なしの質問に断定した / 根拠ありの質問に確認要求で逃げた / 形式の崩れ）：根拠なしの質問に断定した
- 知識を問う質問（セクション 6）の結果（学習前の分類 → 学習後の分類）と気づいたこと：It is not mentioned that this work is the final work but the model doesn't notice that. 
- 学習で変わったこと・変わらなかったこと：The model can really know what is loaded on training data, yet it still cannot anwser those was not loaded and some times there is illusion.

## 宿題

- 取り組んだレベル：基礎 
- 変えた設定やデータ：lora_r を変更した。
- 結果（比較表や数字）：after:seconds は43.4から48.5に上がった。
- ファインチューニングが向く場面・向かない場面についての考察：lora_rを上がったら、やはり反応時間を増えたまま、結果はあんまり変更していないので、別のパラメータを変更しましょう。
