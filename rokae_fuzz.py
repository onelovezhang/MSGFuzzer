from fuzz_func import *
from generate_fuzz_module import *
from ROKAEMes import *

rokaemes = ROKAEMes()
rokaemes.connect(IP = "192.168.0.160", Port=5050)
rokaemes.send_messages(rokaemes.switch_auto, is_print=True)
time.sleep(1)
rokaemes.send_messages(rokaemes.switch_motor_on, is_print=True)
time.sleep(1)
rokaemes.disconnect()
time.sleep(1)


# network_monitor = NetworkMonitor(host="192.168.0.160", port=5050)
# Messages = ROKAEBlock()
session = Session(
    target=Target(connection=TCPSocketConnection("192.168.0.160", 5050),
                  # monitors=[network_monitor]
                  ),
    # receive_data_after_each_request=True,
    # check_data_received_each_request=True,
    # receive_data_after_fuzz = True,
    sleep_time=0.01,
    # post_test_case_callbacks=[post_send],
    # pre_send_callbacks=[pre_send],
    ignore_connection_reset=True,
    ignore_connection_issues_when_sending_fuzz_data=True
)



test_block = get_fuzz_module("rl_task_pp_to_main", max_len=300)
session.connect(test_block, callback=check_response)
print(session.num_mutations())
session.fuzz()

# rokaemes.send_messages(rokaemes.rl_task_stop, is_print=True)
# time.sleep(2)
# rokaemes.send_messages(rokaemes.rl_task_pp_to_main, is_print=True)
# time.sleep(2)








