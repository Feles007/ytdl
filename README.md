# ytdl
Basically just an easier, but dumbed-down "front-end" for youtube-dl.<br>
IDK what to call this so...
## Usage
Simply input a file, with links on each line. If it can be interpreted by youtube-dl, it should work.
Use the custom syntax if you need it.<br>
Speaking of:
## Syntax
Blank lines are skipped.<br>
There are two commands: `$PRE` `$POST`<br>
They indicate the PRE and POST values for all succeeding lines.<br>
For example, an input file of:
```
$PRE
https://youtu.be/
$POST
/

d0tGBCCE0lc
ub82Xb1C8os
iik25wqIuFo
```
will result in the following links downloaded by youtube-dl:
```
https://youtu.be/d0tGBCCE0lc/
https://youtu.be/ub82Xb1C8os/
https://youtu.be/iik25wqIuFo/
```
I might add more in the future, but for now, that is all.
