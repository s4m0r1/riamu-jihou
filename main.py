import schedule
import time

def main(args):
    schedule.every().monday.at("19:55").do(job1)
    schedule.every().tuesday.at("19:55").do(job1)
    schedule.every().wedneday.at("19:55").do(job1)
    schedule.every().thursday.at("19:55").do(job1)
    schedule.every().friday.at("19:55").do(job1)
    while True():
        schedule.run_pending()
        time.sleep(1)
        

def job1():
    exec("aplay --device=hw:1,0 jiho.wav")

if __name__ == "__main__":
    main()
    