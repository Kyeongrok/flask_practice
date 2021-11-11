from task_env import TaskEnv
from threading import Thread
import os, time

taskEnv = TaskEnv()


class Program(Thread):
    def __init__(self, task_env):
        Thread.__init__(self)
        self.consumer = taskEnv.kafka.consumer
        self.consumer.subscribe(['adc-100'])
        print('program')

    def run(self):
        while True:
            msg = self.consumer.poll(timeout=1.0)
            if msg != None:
                print(msg.value())
            else:
                print('Msg is none.')

            time.sleep(0.1)

if __name__ == '__main__':
    for t in [Program(taskEnv)]:
        t.start()