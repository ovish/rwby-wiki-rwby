# wikia-rwbyの翻訳


## 情報
参考にした版は多分、2018-2-24、時間わからない。  
そのあとVolume5が3000文字ぐらい追加されていたけど、無視する。  


## 方針
翻訳と技術作業は分ける    
少しぐらい（かなりでも）変換が難しくなったとしても  
翻訳に労力を使わせない  

### フロー
1. 膳立てフェーズ
  1. プレーンテキスト取ってくる
  1. 章ごとに分割
1. 翻訳フェーズ
  1. とりあえず訳す
  1. 適宜リンク追加[^n]
  1. 翻訳の改善   <<今ここ
    - wikipeの書き方を参考にする
    - wikiaの他のページから書き方を合わせる
    - コミュニティに表現を相談する
1. wikia表記に直すフェーズ
  - wikiaのソース見るoRコミュニティポータルに説明書さがしに行く
  - 早見表作る
  - もしもgfmのままでもよかったならば...
1. 手作業は無理なフェーズ
  1. ソースからリンク抜き出し(Python?)
  1. a-ref, wiki-rink共に結合(Python?)
  1. ウィキリンク、[[link]]、はデータベース作って正規表現で退治する。
1. wikiaフェーズ
  1. アップロード、どのタイミングでやろうかただいま考え中
  1. リストとかインフォボックスの作成
  1. 写真の追加。これは諦める

### git
fix :よくなかったの修正  
add :追加  
cln clean :見た目の整理  
rmv remove :削除  
upd update :よりよく修正  


## 作業のメモ

### 細かいこと
リンクは'[^n]'の形にする

### 保留案件、訳せないもの
unique  
release, publish, premire公開系どう訳す  
original  
original run?  

### 正規表現
#### ==見出し==
'''
={2}[a-z]+={2}$
'''
