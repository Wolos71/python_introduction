from datetime import datetime
import time



try:
    while True:
        now = datetime.now()
        formatted = now.strftime("%A, %d %B %Y, %H.%M.%S")
        with open ("/Users/wolos/Documents/nauka/python_introduction/week01/txt.txt", "a") as f:
            f.write(f"{formatted} \n")
        time.sleep(1)
except KeyboardInterrupt:
    print("\n kończymy na dziś")