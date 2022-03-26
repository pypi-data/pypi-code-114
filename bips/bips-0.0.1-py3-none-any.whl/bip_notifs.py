import winsound
import time

# frequency = 2500 ##set frequency in hertz
# duration = 1000 ##set duration in milliseconds

def error_beep( ):
    for i in range( 0, 7 ):
        winsound.Beep( 1500, 300 )


def done_status_beep( ):
    for i in range( 0, 2 ):
        winsound.Beep(400, 300)

    time.sleep( 1 )

    for i in range( 0, 2 ):
        winsound.Beep( 800, 300 )


def success_beep( ):
    for i in range( 0, 1 ):
        winsound.Beep( 800, 1500 )

    time.sleep( 0.1 )

    for i in range( 0, 2 ):
        winsound.Beep( 800, 300 )
