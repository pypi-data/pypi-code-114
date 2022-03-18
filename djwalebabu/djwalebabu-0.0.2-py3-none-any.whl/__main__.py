# Using the built-in webbrowser library
import webbrowser

def request():
    
    usr_inp = input('What song do you want to hear?\n')

    # Found from here 
    # https://superuser.com/questions/1496083/google-feeling-lucky-url-causing-redirect-notice
    if usr_inp != '':
        webbrowser.open(f'https://www.google.com/search?q={usr_inp}&btnI=&sourceid=navclient&gfns=1')
    else:
        webbrowser.open(f'https://www.youtube.com/watch?v=OulN7vTDq1I&ab_channel=SonyMusicIndia')    

    print('This is your boy Hargun Singh Oberoi here and you\'re listening to radio ai[0]')            
if __name__ == '__main__':
    request()
