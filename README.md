# Clipboard manager

![Building](https://github.com/Reyuu/clipboard-manager/workflows/Building/badge.svg)

**Clipboard manager** is a simple utility that helps you with managing your clipboard. Say you need to copy and paste the same 2 things over and over but in different places (thus needing human attention), this will help you greatly.

It is intended for usage with **Windows**.

**[Latest release](https://github.com/Reyuu/clipboard-manager/releases/latest)**

## How to use
![image](https://user-images.githubusercontent.com/7038406/87229510-d5604680-c3a8-11ea-8941-37668d0bc1b4.png)

||Description|
|--------|-----------|
|**Add**|Manually add an entry to the list|
|**Remove**|Remove an entry from the list|
|**Enable**|Enable an entry, all entries are enabled by default|
|**Disable**|Disable an entry|
|**Sequential pasting**|When pasting, moves to next **enabled** entry and automatically copies it to clipboard, until the checkbox is disabled.|
|**Clipboard capturing**|Captures every text value that is copied and adds it to the list.|
|**Window opacity**|Changes window opacity.|

By double clicking on the item in the list you can edit the entry.

Main window has stay on top hint set, so it will stay on top of any window. You can minimalize it or use window opacity slider to make it less visible.

## Building from source

```
pip install -r requirements
python setup.py build
```
