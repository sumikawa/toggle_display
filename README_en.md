## What is this?

This is a script to toggle the enabling and disabling of a Macbook's built-in display.
It is useful in the following cases:

- When you want to use clamshell mode with an external display but don't want to close the Macbook's lid to use Touch ID.
- When you want to disable the built-in display while using AR glasses like XREAL.

## How to use

Copy the script to a suitable executable path:

```
cp toggle_display.py /somewhere/path/bin/
```

Then, just run the script:

```
toggle_display.py
```

## Caution

If you run this command without an external display connected, or if you move to an environment without an external display while the internal display is disabled, you will be stuck with no way to see what you are doing.

It is recommended to use this script in combination with [Karabiner-Elements](https://karabiner-elements.pqrs.org/) to assign it to a convenient key. I use the following rule to assign it to Command + L.

```
{
  "title": "Toggle Display",
  "rules": [
    {
      "description": "Toggle the enabling and disabling of a built-in display",
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
    }
  ]
}
```
