import sys
Language="en"
ENGLISH={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}
CHINA={0:"零",1:"一",2:"二",3:"三",4:"四",5:"五",6:"六",7:"七",8:"八",9:"九",10:"十"}
def print_digits(digits):
    dictionary=ENGLISH if Language=="en" else CHINA
    for digit in digits:
        print(dictionary[int(digit)]+" ")
def main():
    if len(sys.argv)==1 or sys.argv[1] in {"-h","-help"}:
        print("usage:{0} [en|ch] number".format(sys.argv[0]))
        sys.exit()
    args=sys.argv[1:]
    if args[0] in {"en","ch"}:
        global Language
        Language=args.pop(0)
    print_digits(args.pop(0))
#这一行不能少。。。
main()