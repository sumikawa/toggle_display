## これは何

Macbookの内蔵ディスプレイの無効/有効を切り替えるスクリプトです。
以下の場合に便利です。

- 外部ディスプレイ利用時にクラムシェルモードしたいが、Touch IDを使うためMacbookのディスプレイを閉じたくない
- XREALなどのARグラス利用時に、内蔵ディスプレイを無効化したい

## 使い方

スクリプトを適当な実行パスにコピーしてください

```
cp toggle_display.py /somewhere/path/bin/
```

後はスクリプトを実行するだけです

```
toggle_display.py
```

## 注意

外部ディスプレイが接続されていない状況でこのコマンドを実行したり、内部ディスプレイを無効化したまま外部ディスプレイのない環境に移動した場合、何もできなくなり詰みます。

[Karabiner-Elements](https://karabiner-elements.pqrs.org/)と組み合わせて、適当なキーに本スクリプトをアサインすることをお勧めします。私は下記のルールを書いてCommand + Lに割り当てています。

```
  "rules": [
    {
      "description": "Command + L で 内蔵ディスプレイの有効/無効を切り替える",
      "manipulators": [
        {
          "from": {
            "key_code": "l",
            "modifiers": {
              "mandatory": [
                "left_command"
              ],
              "optional": [
                "any"
              ]
            }
          },
          "to": [
            {
              "shell_command": "PATH=$PATH:$HOME/usr/bin:/opt/homebrew/bin toggle_display.py"
            }
          ],
          "type": "basic"
        }
      ]
    }]
```
