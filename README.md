# GRErecite
GRE 再要你命3K 背单词小程序

## Usage

```
n+e:~/GRErecite ./recite.py --help
usage: recite.py [-h] [-a A] [-b B] [-f FILE] [-o WRONG]

recite

optional arguments:
  -h, --help  show this help message and exit
  -a A        begin
  -b B        end
  -f FILE     word file
  -o WRONG    wrong answer output
```

总共3064个单词，比如某天想背list16的100个单词，并且将不熟悉的单词导出到16.txt中：

```
./recite.py -a 1500 -b 1600 -f all.json -o 16.txt
```
