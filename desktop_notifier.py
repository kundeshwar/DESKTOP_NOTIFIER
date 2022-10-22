
from plyer import notification
import time



if __name__ == '__main__':
    notification.notify( 
        title="*****Take Rest******",
        message="you will take rest",
        #app_icon = ".ico" 
        timeout= 5
        )

    time.sleep(20)
