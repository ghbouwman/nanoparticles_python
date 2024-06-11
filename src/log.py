import datetime

class Logger:
    
    def __init__(self, run_name):
        self.logfile = f"../output/{run_name}_log.txt"
        with open(self.logfile, 'w') as f:
            f.write(f"begin of logfile for {run_name}\n")

    def __call__(self, text):
        with open(self.logfile, 'a') as f:
            now = datetime.datetime.now()
            f.write(f"[{now}] {text}\n")
            