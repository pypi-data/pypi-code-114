import sys
import os
from upload import uploader 



if __name__=="__main__":
    
    file_path=sys.argv[1]



    if sys.argv[1]=='twine':
        os.system('python setup.py sdist bdist_wheel')
        os.system('python -m twine upload dist/*')
    else : 
        if len(sys.argv)!=2:
            print("Insufficient arguments")
            sys.exit()

        f=open("README.md",'w')
        f.close()
        f=open("setup.py",'w')
        f.close()
        f=open("LICENSE",'w')
        f.close()
            
        print("note the follows")

        upload_1=uploader()
        upload_1.up()
        upload_1.load()
        

        os.system('python setup.py sdist bdist_wheel')