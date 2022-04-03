# BOTER
深夜テンションで作った、DiscordBOT操作用クライアント。

# Usage
```sh
python main.py
```
まず、main.pyを実行します。  
次にBotのTOKENを入力します。(そのうちjsonとかにしたいね)  
すると、ログインが行われ、Guild/Channel選択を行います。
Guild/Channelが選択されると、最近20メッセージが表示されます。(ただし時間はUTC。)  
そしたら、`・Send a message to #channel as bot@1234`と表示されるので、そうしたら送信したいメッセージを入力してエンターを押してください。  
特にエラーが表示されずに`Sended!`と表示されれば送信されてます。試しに確認してみてください。  
