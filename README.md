# wikia-rwbyの翻訳


## メタ情報
参考にした版は多分、2018-2-24、時間わからない。  
そのあとVolume5が3000文字ぐらい追加されていたけど、無視する。  

### ファイル
- 翻訳するやつら
    - e(num)-word.md : 英語プレーンテキスト  
    - j(num)-word.md : e(num)の翻訳  
    - a(num)-word.md : ソースファイル、結局使ってない
    - source.md : ページ丸々のソース、あとで使う
- スクリプト、この順にやればjpnSource.mdができる。そのうち人コマンドでできるようにまとめるつもり。
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
    1. a-ref, wiki-rink共に結合(Python?)
    1. ウィキリンク、[[link]]、はデータベース作って正規表現で退治する。=yet
1. 発生してしまった作業フェーズ
    - 8章目である参考リンク集を英ソースから作った日ソースに貼り付け
    - その前に自動化が生み出したnone==noneを消す
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
- リンクは'[^n]'の形にする => あとで置き換える
- 箇条書きは、作業[-] -> [\*] ==done
- [wikia表記](http://kaze.wikia.com/wiki/編集の仕方)
- [:]で段落下げ => [>]->[:] ==done
- タイトル　[#title] -> [=title=]
- 箇条書きのタイトル [####] -> [;]　このテンプレ使える? ==一応done
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

## ライセンス
- 翻訳はrwby wiki jpn aND eng の CC-BY-SA
- スクリプトはMIT

## 感想
- brewがpythonでのインストールを2から3にしたらしいので、うにコード民として嬉しい。遅いとか問題じゃない、だって早いのは別の言葉で書けばいいんだもん。これでこれからはわざわざ3指定して実行しなくて良くなるかな？
- RWBYの作業してるとやっぱruby使うべきかと書くたびに思う。良いサイトとか面白い本ないですかね？
- コーヒー自棄飲みしたらめちゃめちゃ気持ち悪い。
- electronよかった。一瞬でデスクトップアプリ作れた。でも,c,c++,go,nim,,rust,clisp,haskell,らへんの速そうなのはかけるようになりたいと思う。どれにしようかな。手続きガリガリ型一個と関数型一個かな？javaはなんとなく嫌だ。pythonは早い書き方調べて考えんのめんどい、
- emacsのlisp初めていじったらエラー吐かれたのでそのうちinit.elをいじり直さなきゃならない。ふぅわー
