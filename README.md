# 35_diff_service

The task is make differ service for html pages.According challenge we should use diff.py,
the script divide each tag as list object and use difflib for compare.For example we have 2 htmls

First html
```html
    <li>Автор: Григорьев П.А.</li>
    <li>Сумма: 126000 руб.</li> 
```
Second html
```html
    <li>Автор: Григорьев П.А.</li>
    <li>Дата: 26.12.14</li>
```
And during compare if htmls same,the script takes extra tag(in our case it is **li**)
```html
<li>Автор: Григорьев П.А.</li><li>---Script takes extra tag
```
So the script was modified and now one row will divide as list object

#### For easy use,the service has been implemented as web interface
![35_task](https://user-images.githubusercontent.com/22424468/35378468-1b3be28a-01dd-11e8-918f-c9def6310bdf.PNG)


### Deploy on localhost

Example of frontend launch on Linux, Python 3.5:

```bash

python3 server.py
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
