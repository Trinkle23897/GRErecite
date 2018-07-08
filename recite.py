#!/usr/bin/env python3
import json,random,argparse
parser=argparse.ArgumentParser(description='recite')
parser.add_argument('-a', dest='a', default=0, type=int, help='begin')
parser.add_argument('-b', dest='b', default=0, type=int, help='end')
parser.add_argument('-f', dest='file', default='all.json', type=str, help='word file')
parser.add_argument('-o', dest='wrong', default='wrong.json', type=str, help='wrong answer output')
args=parser.parse_args()
js=json.loads(open(args.file).read())
if args.a and args.b:
    js=js[args.a:args.b]
elif args.b:
    js=js[:args.b]
elif args.a:
    js=js[args.a:]
num=len(js)
print('type exit to quit')
while(1):
    wrong=[]
    random.shuffle(js)
    for idx in range(len(js)):
        eng=""
        for i in js[idx]:
            eng=i
        chn=js[idx][eng]
        print('')
        ipt=input("\033[1;34;48m%03d \033[0m %s: "%(idx+1,eng))
        if ipt=='exit' or ipt=='quit':
            break
#       if ipt==ans:
#           print('\033[1;32;48mCorrect!\033[0m')
#       else:
#           print('\033[1;31;48mDamn!\033[0m')
        print('\033[1;32;48m+\033[0m %s'%chn)
        print('\033[1;31;48m-\033[0m %s'%ipt)
        if input('y/[n] : ')!='y':
            wrong.append(js[idx])
            print('add to %s'%args.wrong)
    print('writing wrong answer into %s'%args.wrong)
    open(args.wrong,'w').write(json.dumps(wrong))
