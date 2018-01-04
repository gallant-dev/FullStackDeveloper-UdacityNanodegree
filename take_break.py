import webbrowser
import time

count = 1
total_breaks = 3

print ("This program start on "+time.ctime())
while (count <= total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=5rAOyh7YmEc")
    count += 1
