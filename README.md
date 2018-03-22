# wikia-rwbyの翻訳


## メタ情報
参考にした版は多分、2018-2-24、時間わからない。  
そのあとVolume5が3000文字ぐらい追加されていたけど、無視する。  

### ファイル
- e(num)-word.md : 英語プレーンテキスト  
- j(num)-word.md : e(num)の翻訳  
- a(num)-word.md : ソースファイル、結局使ってない
- source.md : ページ丸々のソース、あとで使う
- その他　: 名前の通りの機能

### 方針
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
    1. ソースからリンク抜き出し(Python?)->下に正規表現
    1. <ref tag /ref>は人力で置き換え+classをjrk[num]する
    1. a-ref, wiki-rink共に結合(Python?)
    1. ウィキリンク、[[link]]、はデータベース作って正規表現で退治する。
1. wikiaフェーズ
    1. アップロード、どのタイミングでやろうかただいま考え中
    1. リストとかインフォボックスの作成
    1. 写真の追加。これは諦める


## 作業のメモ

### git
fix :よくなかったの修正  
add :追加  
cln clean :見た目の整理  
rmv remove :削除  
upd update :よりよく修正  

### 正規表現
#### ==見出し==
'''
={2}[a-z]+={2}$
'''
#### refタグ
<ref.\*?>(.+?)<\/ref>

### 文章

#### 記号の表記
- リンクは'[^n]'の形にする
- 箇条書きは、作業[-]、wikia[\*]
- [wikia表記](http://kaze.wikia.com/wiki/編集の仕方)

#### 単語の表記
- unique  
- release, publish, premire公開系どう訳す  
- original  
- original run?  

#### wikiaローカルルール
- 人名は英語

### 参考にするソース
あくまでファンコミュニティのwikiであるということを念頭に置いて、wikipeとは違い創作物により入れ込んでいい利点を意識しながら翻訳する。  というかwikipe、ENGwikiaから文章を一部取ってきてるんじゃ...まあライセンス的には全く問題ないはず

[表記ガイド](https://ja.wikipedia.org/wiki/Wikipedia:表記ガイド)  
[スタイルマニュアルフィクション](https://ja.wikipedia.org/wiki/Wikipedia:スタイルマニュアル_(フィクション関連))  
[翻訳ガイドライン](https://ja.wikipedia.org/wiki/Wikipedia:翻訳のガイドライン)  
[言葉を濁さない](https://ja.wikipedia.org/wiki/Wikipedia:言葉を濁さない)  
[ストーリー文体](https://ja.wikipedia.org/wiki/Wikipedia:ウィキペディアにふさわしいストーリー紹介の文体)  
