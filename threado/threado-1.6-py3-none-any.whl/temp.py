import urllib.request
import string

from threado.simple_thread_runner import SimpleThreadsRunner

actions = list(string.ascii_lowercase)
sr = SimpleThreadsRunner(lambda x: print("Thread output char:" + x))
sr.run_threads(5, iter_data=actions)
