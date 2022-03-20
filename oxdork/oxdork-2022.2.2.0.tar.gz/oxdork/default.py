from oxdork import colors, output
from googlesearch import search

def dork(args,logging):
   number=0
   counter=0
   if args.verbose:
   	logging.info(f"{colors.white}Fetching [{colors.green}{args.count}{colors.white}] dorks. Please wait...{colors.reset}")
   for results in search(args.query, num=int(args.count),start=0,stop=None,lang="en",tld="com", pause=2.5):
       number+=1
       counter+=1
       logging.info(f"[{counter}] {colors.green}{results}{colors.reset}")
       
       if args.output:
           output.write(args,results,counter)
           
       if number >= int(args.count):
       	break