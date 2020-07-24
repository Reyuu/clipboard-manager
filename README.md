# Clipboard manager

![Building](https://github.com/Reyuu/clipboard-manager/workflows/Building/badge.svg)

**Clipboard manager** is a simple utility that helps you with managing your clipboard. Say you need to copy and paste the same 2 things over and over but in different places (thus needing human attention), this will help you greatly.

It is intended for usage with **Windows**.

**[Latest release](https://github.com/Reyuu/clipboard-manager/releases/latest)**

## How to use
![image](https://user-images.githubusercontent.com/7038406/88442216-02ceda80-ce14-11ea-9909-3b4b7b8e7544.png)
![image](https://user-images.githubusercontent.com/7038406/88442212-fd719000-ce13-11ea-8bc5-85fdc2ca278c.png)

### Interface

|Icon|Description|
|--------|-----------|
|➕|Manually add an entry to the list|
|➖|Remove an entry from the list|
|✅|Enable an entry, all entries are enabled by default|
|❎|Disable an entry|
|⚙|Show additional options|

### Additional options

|Option|Description|
|----|----|
|**Sequential pasting**|`Toggles an option.` When pasting, moves to next **enabled** entry and automatically copies it to clipboard, until the checkbox is disabled.|
|**Clipboard capturing**|`Toggles an option.` Captures every text value that is copied and adds it to the list.|
|**Show window opacity**|`Toggles an option.` Shows a slider that controls winodw opacity.|
|**Save clipboard**|Saves current clipboard to a JSON file.|
|**Load clipboard**|Loads clipboard from JSON file.|
|**Add program to autostart**|Adds program to autostart, which makes it launch upon system startup.|
|**Exit**|Closes the program.|

By double clicking on the item in the list you can edit the entry.

Main window has stay on top hint set, so it will stay on top of any window. You can minimalize it or use window opacity slider to make it less visible.

### Text commands

Clipboard manager now supports limited scripting by typing in correct command when editing the entry.
|Command|Argument|Description|Example|
|-|-|-|-|
|**!\*\*hide**|string to hide|Replaces the current string with stars ⭐ while preserving the ability to copy the underlying hidden string.|**!\*\*hide**myverystrongpassword|
|**!\*\*current_date**|format of the date (use https://strftime.org/ for reference)|Gets current date 📅 based on the format given. This will not update the time, it only gets time that's present in the moment of writing the command.|**!\*\*current_date**%m/%d/%Y|

### Disclaimer

Currently the program **DOES NOT** encrypt your clipboard or encrypts the saved clipboard in any way.

## Building from source

```bash
pip install -r requirements
python setup.py build
```

## Other

|Item|License|Link|
|-|-|-|
|Icons used by **Cole Bemis**|MIT|**https://github.com/feathericons/feather**|
