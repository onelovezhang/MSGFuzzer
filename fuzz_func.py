from boofuzz import *
import time

fuzz_time_start = time.time()

def post_send(target: Target, fuzz_data_logger, session, sock):
    print("post send callback")


def pre_send(target, fuzz_data_logger, session, sock):
    print("pre send callback")
    

def check_response(target: Target, fuzz_data_logger: IFuzzLogger, session: Session, test_case_context: ProtocolSession, *args, **kwargs):
    global fuzz_time_start
    print("check response callback")
    heart_package = b'\x00Y\x00\x00\x00S\x02\x00{"command":"controller.heart","id":"#10#system.controller.heart","module":"system"}'
    call_back_recive = ""
    for i in range(8):
        try:
            target.send(heart_package)
            call_back_recive = target.recv(1024)
            if call_back_recive:
                break
            else:
                print("have not recive response, try again")
                time.sleep(2)
        except:
            # target.send(heart_package)
            # call_back_recive = target.recv(1024)
            if i == 7:
                print("connection reset by peer, jump this testcase")
            else:
                pass


    print(f"callback recive:{call_back_recive}")
    if not call_back_recive:
        print("have not get response, check remote host")
        print(f"fuzz_time:{time.time() - fuzz_time_start}")
        s = input("continue? 0:exit, else: continue fuzz\n")
        if s == "0":
            exit()
        else:
            test = ""
            while test != "yes":
                test = input("record the crash and time? restart the host? if you ready for that, input 'yes'\n")
            # 更新fuzz时间
            fuzz_time_start = time.time()

    else:
        print("check pass")