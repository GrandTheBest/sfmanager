# SFManager 

[![PyPI version](https://img.shields.io/pypi/v/sfmanager)](https://pypi.org/project/openai/)

## This library is not that useful. Perhaps someday it will become great.

## Python super filemanager

SFManager - this is library for work with files!

By this library you can work with text, image and other files.

You can read, set, add and replace content in text files.

Also you can create, copy, move, rename and remove any files.

## Examples

> [!NOTE]
> Terminal commands
> ```sh
> sfmanager
> ```
> `sfmanager` - print in terminal information about library
##
> [!NOTE]
> Create filemanager object
> ```python
> import sfmanager
> 
> f = sfmanager.FileManager(filename="data.txt", level=5)
> ```
> `filename` - filename or path to file \
> `level` - access level, where `1` - read only, `2` - add content(for text files only), `3` - replace and set content(for text files only), `4` - rename, copy, move file, `5` - remove file
##
> [!NOTE]
> Work with text files
> ```python
> f.readline() # read one line(for text files only) - 1 level
> f.readlines() # read all lines as JSON array(text files only) - 1 level
> f.add(text="Hello world!", sep=" ") # add text to file (text files only) - 2 level
> f.replace(_from="Hello", _to="Hi") # replace certain text on another (ftext files only) - 3 level
> f.set(text="Hi friends!") # replace all content to another (text files only) - 3 level
> ```
> `readline` - print one line from text file \
> `readlines` - print all lines from text file as array \
> `add` - add content to file, where `text` - new text, `sep` - separator between old and new content, DEFAULT = "" \
> `replace` - replace certain text on another, where `_from` - old text, `_to` - new text \
> `set` - replace all content in text file on another, where `text` - new text
##
> [!NOTE]
> Work with any files
> ```python
> f.copy(dst="data2.txt") # - copy file with all metadata - 4 level
> f.rename(name="data1.txt") # rename file - 4 level
> f.move(dst="/home/pc/super.txt") # move file to another directory - 4 level
> f.delete() # remove file - 5 level
> ```
> `copy` - copy file with all metadata, where `dst` - directory and/or name for new file \
> `rename` - rename file, where `name` - new name \
> `move` - move file to another directory, where `dst` - new directory and/or new file name \
> `delete` - remove file

## That's all. Stay tuned!