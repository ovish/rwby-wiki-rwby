# wikia-rwbyの翻訳


## メタ情報
参考にした版は多分、2018-2-24、時間わからない。  
そのあとVolume5が3000文字ぐらい追加されていたけど、無視する。
そのあと3000文字ぐらい消されてた。

### ファイル
- 翻訳するやつら
    - e(num)-word.md : 英語プレーンテキスト  
    - j(num)-word.md : e(num)の翻訳  
    - a(num)-word.md : ソースファイル
    - c(num)-word.md : j(num)の改変
    - source.md : ページ丸々のソース、あとで使う
- スクリプト、この順にやればjpnSource.mdができる。そのうち一つのコマンドでできるようにファイルをまとめるつもり。
    - combi.py : j(num)-word.mdをがっちゃんこする
    - title.py : jpnCombiのタイトルを[#title]->[=title=]
    - link.py : jpnCombiに引用リンクを書き換え

### 方針
翻訳と技術作業は分ける    
少しぐらい（かなりでも）変換が難しくなったとしても  
翻訳に労力を使わせない
直訳と翻訳のファイルは分ける?

### フロー
1. 膳立てフェーズ =fin
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
    - jpnCombiの段階で書き換える(jpnSourceまで進むと、urlが邪魔して置換できない)
    - 手作業めんどくさかったので、自動化する。タイトルだけでも ==done
1. 手作業は無理なフェーズ  =fin
    1. ソースからリンク抜き出し(Python?)->下に正規表現
    1. <ref tag /ref>は人力で置き換え+classをjrk[num]する
        - j6に5
        - j7に1
        - リンクを取得するソースから抜いとかないと誤反応する。
        - link.pyで処理する方針にした
        - source.mdのピュラgalleryをコメントアウト。リンクを含むため。
    1. a-ref, wiki-rink共に結合(Python?)
    1. ウィキリンク、[[link]]、はデータベース作って正規表現で退治する。=yet
1. 発生してしまった作業フェーズ
    - 8章目である参考リンク集を英ソースから作った日ソースに貼り付け
    - その前に自動化が生み出したnone==noneを消す
1. wikiaフェーズ
    1. アップロード、どのタイミングでやろうかただいま考え中　=done
    1. リストとかインフォボックスの作成 =そのうち
    1. 写真の追加。これは諦める


## 作業のメモ

### git
fix :よくなかったの修正  
add :追加  
cln clean :見た目の整理  
rmv remove :削除  
upd update :よりよく修正  

### 正規表現
正規表現なんてうごけばいいんだしぃ...(よくわかってない)
#### ==見出し==
'''
={2}[a-z]+={2}$
'''
#### refタグ
<ref.\*?>(.+?)<\/ref>
#### [^num]
\[\^\d+\]
#### <!--コメント-->コメント
<\!--.+-->

### 文章

#### 記号の表記
- かっこは半角
- リンクは'[^n]'の形にする => あとで置き換える
- 箇条書きは、作業[-] -> [\*] ==done
- [wikia表記](http://kaze.wikia.com/wiki/編集の仕方)
- [:]で段落下げ => [>]->[:] ==done
- タイトル　[#title] -> [=title=]
- 箇条書きのタイトル [####] -> [;]　このテンプレ使える? ==一応done
- だった、なった、あった、とかの促音がなんとなく気持ち悪くなってきたのでなるべく使いたくない
- に、へ、を続かせない為に、他の言葉を混ぜる　=保留
- 過去形じゃないとダメなんだっけか？よくわからないから一旦放置。もしかしたらずっと。
- 詳細は次の記事なんとか、を揃えるあとでやる　=done
- 人名を無機物の指示語で指し示しちゃってるけど確認がほっといていいかな
こいつを最後に追記
'''
==Links==
* [http://roosterteeth.com/show/rwby Rooster Teeth ''RWBY'' Page]
* [http://teamrwby.com/ ''RWBY'' Theatrical Release Site]
* [http://rwby.jp/news.html ''RWBY'' Japanese Official Site]
* [https://www.facebook.com/RT.RWBY/?fref=ts ''RWBY'' Official Facebook Page]

==References==
{{reflist|2}}
'''

#### 単語の表記
- A, B, C and D -> A、B、CとD、 oR AとBとCとD　=?三つまでは'と'でつなぐ -> 最後の後に半角スペース入れればよくない？
- Academy -> アカデミー、x学園 =こっちの方がいい
- series -> シリーズ oR x番組
- show -> ?番組 oR ショー
- anime -> アニメ =日本文化の影響を色濃く受けたアニメーションの一分類のこと
- animation -> アニメーション oR 動画　=アニメとは明確に区別する
- produce -> 制作、映像系なので
- create -> 創作 oR !創る oR 創り出す　oR 生み出す　==未定
- plot -> 話、x話の筋 =冗長ゆえ
- the way -> 物語の
- character -> ?登場人物 oR キャラクター  ==未定
- evil -> 災難　oR ?害悪 oR 悪
- at PLACE -> おいて oR おける oR にて　oR での　=?場所ごとに分けるか
- の　oR　である
- なされた oR 行われた ==未定
- innate energy ->　?気 oR 生来のエネルギー
- premiere -> 封切り
- unique -> それぞれ違った
- trailer -> ?予告編　oR トレイラー
- episode -> エピソード
- first episode -> 初話、1話、第一話、初回、初回1話　=コミュニティに投げる
- air -> 放送
- Chibi styled character -> ? SDキャラ oR ちびキャラ
- simulcast -> 同時に放送　=アニメ1話は放送、映画は放映、にしてわける
- announce -> 報告　OR　公表 oR ?アナウンス oR 告知(すでに分かっている事の詳細)　oR 発表(新しいの) =x段落の一つ目は発表でそれ以降は告知にする=o日時指定は告知、日時非指定は発表　=なんとなくdone
- confirmed -> 確認 oR 認める ==使い分ける
- take place -> 始まる
- revealed -> 明らかにす
- Rooster Teeth FIRST -> FIRST =英語圏ではないので厳密にしなくても伝わる+長い
- every -> それぞれの
- streamed -> 配信
- hype -> =?意味がわからない
- objects -> ?建築
- sneak peek -> =訳を思いつかぬ
- cameo -> ?カメオ　oR 特別
- some -> いくつか　oR 幾ら
- play -> 演じる、演じた
- cast as -> 担当　＝も一度点検する
- role -> 役を演じる
- director -> 監督　=訳せていない、要確認=done
- voice -> 声を当てた
- release, publish, premire公開系どう訳す  
- original = 本来の　oR 特別な =場面に合わせて考える
- original run　= !本放送　oR 初回放送

#### wikiaローカルルール
- 人名は英語
- キャラ名は[・]で区切る

### 参考にするソース
あくまでファンコミュニティのwikiであるということを念頭に置いて、wikipeとは違い創作物により入れ込んでいい利点を意識しながら翻訳する。  というかwikipe、ENGwikiaから文章を一部取ってきてるんじゃ...まあライセンス的には全く問題ないはず、？継承必要

[表記ガイド](https://ja.wikipedia.org/wiki/Wikipedia:表記ガイド)  
[スタイルマニュアルフィクション](https://ja.wikipedia.org/wiki/Wikipedia:スタイルマニュアル_(フィクション関連))  
[翻訳ガイドライン](https://ja.wikipedia.org/wiki/Wikipedia:翻訳のガイドライン)  
[言葉を濁さない](https://ja.wikipedia.org/wiki/Wikipedia:言葉を濁さない)  
[ストーリー文体](https://ja.wikipedia.org/wiki/Wikipedia:ウィキペディアにふさわしいストーリー紹介の文体)  

## ライセンス
- 翻訳はrwby wiki jpn aND eng の CC-BY-SA
- スクリプトはMIT

## 感想
- brewがpythonでのインストールを2から3にしたらしいので、うにコード民として嬉しい。遅いとか問題じゃない、だって早いのは別の言葉で書けばいいんだもん。これでこれからはわざわざ3指定して実行しなくて良くなるかな？まだ無理だった、というかパスの通し方がわからない
- RWBYの作業してるとやっぱruby使うべきかと書くたびに思う。良いサイトとか面白い本ないですかね？
- コーヒー自棄飲みしたらめちゃめちゃ気持ち悪い。
- electronよかった。一瞬でデスクトップアプリ作れた。でも,c,c++,go,nim,,rust,clisp,haskell,らへんの速そうなのはかけるようになりたいと思う。どれにしようかな。手続きガリガリ型一個と関数型一個かな？javaはなんとなく嫌だ。pythonは早い書き方調べて考えんのめんどい、
- この前emacsのlisp初めていじったらエラー吐かれたのでそのうちinit.elをいじり直さなきゃならない。
- Michael Henry & Justin Robinett
- ペイパルってクレジットカード必要なんですねぇ、持ってないッ、ゔあ"あ"あ"あ"あ"あ"
