import socket
import time

class ROKAEMes():

    def __init__(self) -> None:
        self.sender = None

        self.switch_motor_on = b'\x00c\x00\x00\x00]\x02\x00{"command":"state.switch_motor_on","id":"dc303cda5d3008f7f02c5d88fceda839","module":"system"}'

        self.jog_start_Y_P = b'\x00\x7b\x00\x00\x00\x75\x02\x00{"command":"jog.start","data":{"direction":true,"index":2},"id":"d69fc0dd85afe60730bdc20ecbd3f9e0","module":"motion"}'

        self.jog_start_Y_N = b'\x00\x7c\x00\x00\x00\x76\x02\x00{"command":"jog.start","data":{"direction":false,"index":2},"id":"d69fc0dd85afe60730bdc20ecbd3f9e0","module":"motion"}'

        self.move_stop = b'\x00m\x00\x00\x00g\x02\x00{"command":"move.stop","data":{"stoptype":1},"id":"427d8c76371095af1ee60c7235f931e7","module":"motion"}'

        self.switch_motor_off = b'\x00d\x00\x00\x00^\x02\x00{"command":"state.switch_motor_off","id":"a6b3b6b9e4f59dbd35dc6d00015ecc83","module":"system"}'

        self.set_params_step_continuous = b'\x00\x8b\x00\x00\x00\x85\x02\x00{"command":"jog.set_params","data":{"override":0.23,"space":2,"step":1000},"id":"f01b5e42d4c9bb247f0992dd94a38a40","module":"motion"}'

        self.set_params_step_10 = b'\x00\x89\x00\x00\x00\x83\x02\x00{"command":"jog.set_params","data":{"override":0.23,"space":2,"step":10},"id":"f01b5e42d4c9bb247f0992dd94a38a40","module":"motion"}'

        self.set_params_step_1 = b'\x00\x88\x00\x00\x00\x82\x02\x00{"command":"jog.set_params","data":{"override":0.23,"space":2,"step":1},"id":"f01b5e42d4c9bb247f0992dd94a38a40","module":"motion"}'

        self.get_state = b'\x00]\x00\x00\x00W\x02\x00{"command":"state.get_state","id":"bb70b9b456c568f419311d04729cf6ba","module":"system"}'

        self.without_tp = b'\x00|\x00\x00\x00v\x02\x00{"command":"state.set_tp_mode","data":{"tp_mode":"without"},"id":"2339b3c9e0b0c05608ad69f3c6798675","module":"system"}'

        self.with_tp = b'\x00\x79\x00\x00\x00\x73\x02\x00{"command":"state.set_tp_mode","data":{"tp_mode":"with"},"id":"2339b3c9e0b0c05608ad69f3c6798675","module":"system"}'

        self.heart_pakage = b'\x00Y\x00\x00\x00S\x02\x00{"command":"controller.heart","id":"#10#system.controller.heart","module":"system"}'

        self.admin_login = b'\x00\xa3\x00\x00\x00\x9d\x02\x00{"command":"user.login","data":{"password":"1d11910e369662bd53d6fae3d8918dfa","user_name":"Admin"},"id":"48ba17344a1f430efa302e709038dba2","module":"system"}'

        self.switch_manual = b'\x00a\x00\x00\x00[\x02\x00{"command":"state.switch_manual","id":"7babc49c27d177a469475b70e21017de","module":"system"}'

        self.switch_auto = b'\x00_\x00\x00\x00Y\x02\x00{"command":"state.switch_auto","id":"60180583fd00c6d9f66687e8508705b3","module":"system"}'

        self.overview_reload = b'\x00\xaf\x00\x00\x00\xa9\x02\x00{"command":"overview.reload","data":{"prj_path":"aizhi_0911/_build/aizhi_0911.prj","tasks":["task0","task1"]},"id":"0e3bd61f5b3b055a17819f8d16f7e109","module":"project"}'

        self.rl_task_run = b'\x00}\x00\x00\x00w\x02\x00{"command":"rl_task.run","data":{"tasks":["task0","task1"]},"id":"d77cd1ba5d81336828edfb76f88407c1","module":"project"}'

        self.rl_task_stop = b'\x00~\x00\x00\x00x\x02\x00{"command":"rl_task.stop","data":{"tasks":["task0","task1"]},"id":"286d117897683aba492aa6b7d9ff25a3","module":"project"}'

        self.rl_task_pp_to_main = b'\x00\x83\x00\x00\x00}\x02\x00{"command":"rl_task.pp_to_main","data":{"tasks":["task0","task1"]},"id":"#170#project.rl_task.pp_to_main","module":"project"}'
        self.rl_task_get_pointer = b'\x00\x7f\x00\x00\x00y\x02\x00{"command":"rl_task.get_pointer","data":{"task_name":"task0"},"id":"#171#project.rl_task.get_pointer","module":"project"}'


    def connect(self, IP, Port):
        if not self.sender:
            self.sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sender.connect((IP, Port))
            print(f"session create on {IP}:{Port}")
            return True
        else:
            print("there is an socket has created, please close it at first")
            return False

    def send_messages(self, message, is_recv = True, is_print = False):
        if self.sender:
            self.sender.send(message)
            print(f"send_message:{message}")
            if is_recv:
                response = self.sender.recv(1024)
                if is_print:
                    print(response)
                return response
        else:
            print("session have not created")
    
    def disconnect(self):
        if self.sender:
            self.sender.close()
            self.sender = None
            print("session closed")
    
    def send_one_message(self, IP, Port, message, is_recv = True, is_print = True):
        if self.connect(IP, Port):
            self.sender.send(message)
            print(f"send_message:{message}")
            if is_recv:
                response = self.sender.recv(1024)
                if is_print:
                    print(response)
            self.disconnect()
            return response
        
    def __del__(self):
        if self.sender:
            self.disconnect()





if __name__ == "__main__":
    rokaemes = ROKAEMes()
    print(rokaemes.rl_task_get_pointer)
















