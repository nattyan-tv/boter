# BOTER
深夜テンションで作った、DiscordBOT操作用クライアント。

# Usage
1. まず、`temp.setting.json`を参考にして`setting.json`を作成してください。  
TOKENは複数保存しておくことが可能です。  
また、`language`の欄には`ja`と入力することで、日本語にできます。

2. `main.py`を実行して、TOKENを選択します。

3. ログインが行われたら、GuildおよびChannelを選択します。

4. メッセージを入力してエンターを押すと送信されます。

5. 再度Guild/Channelを選択しなおすには、`/change`と入力してください。  
他にも`/help`と入力することで、コマンド一覧が表示されます。  
また、最初にスラッシュを含むメッセージを送信したい場合は、最初のスラッシュを2回にすることで2文字目からのメッセージが送信されます。  
- Example
```
[/help - ヘルプ表示]
・#Channel に TestBot@1234としてメッセージを送信
/help

BOTER - ヘルプ

/help - ヘルプを表示
/exit - ログアウトする
/change - サーバー/チャンネルを変更する
/load - 再度メッセージを読み込む

[/help - ヘルプ表示]
・#Channel に TestBot@1234としてメッセージを送信
//<-This is slash!
# TestBot@1234 04/01 12:34(UTC)
/<-This is slash!

[/help - ヘルプ表示]
・#Channel に TestBot@1234としてメッセージを送信
```

