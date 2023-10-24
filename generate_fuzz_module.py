from boofuzz import *
from ROKAEMes import *
import json


def write_fuzz_module(message_byets: bytes, module_name, fuzzable = True):
    data_field = message_byets[8:]
    print(data_field)
    data_modules = get_data_module(data_field, fuzzable=fuzzable)
    with open("./fuzz_module/" + module_name + ".json", mode="w") as f:
        json.dump(data_modules, f, indent=4)
    return data_modules


def get_data_module(data_bytes: bytes, fuzzable) -> list:
    data_bytes_str = str(data_bytes,encoding='utf-8')
    # print(data_bytes)
    delim_list = [",", ":", "{", "}", "[", "]"]
    data_module_list = []
    data_bytes = ""
    for bytes_index in data_bytes_str:
        if bytes_index in delim_list:

            if data_bytes:
                data_module_list.append({
                    "bytes_data":data_bytes,
                    "types": 'string',
                    "fuzzable": fuzzable
                })
            
            data_module_list.append({
                "bytes_data":bytes_index,
                "types": 'delim',
                "fuzzable": fuzzable
            })
            data_bytes = ""
        else:
            data_bytes = data_bytes + bytes_index
    if data_bytes:
        data_module_list.append({
                    "bytes_data":data_bytes,
                    "types": 'string',
                    "fuzzable": fuzzable
                })
    return data_module_list


def read_data_module(module_name):
    data_module_list = json.load(open("./fuzz_module/" + module_name + ".json"))
    return data_module_list


def get_fuzz_module(module_name, head = True, max_len = None, repeat = False):
    data_module_list = read_data_module(module_name)
    s_initialize(module_name)
    if head:
        if s_block_start("head"):
            s_size("data", length=2, fuzzable=False, endian=">")
            if s_block_start("data"):
                s_word(0x0000,  endian=">", fuzzable=False)
                s_size("request", length=2, fuzzable=False, endian=">")
                s_word(0x0200, endian=">", fuzzable=False)
                if s_block_start("request"):
                    # delim:{
                    s_string(data_module_list[0]["bytes_data"], fuzzable=data_module_list[0]["fuzzable"], max_len=max_len)
                    if s_block_start("key-value"):
                        for module_string in data_module_list[1:-1]:
                            if module_string["types"] == "string":
                                s_string(module_string["bytes_data"], fuzzable=module_string["fuzzable"], max_len=max_len)
                            else:
                                s_delim(module_string["bytes_data"], fuzzable=module_string["fuzzable"])
                    s_block_end()
                    if repeat:
                        s_repeat("key-value", max_reps=1000)
                    # delim
                    s_string(data_module_list[-1]["bytes_data"], fuzzable=data_module_list[-1]["fuzzable"], max_len=max_len)
                s_block_end()
            s_block_end()
        s_block_end()
    else:
        if s_block_start("request"):
            # delim:{
            s_string(data_module_list[0]["bytes_data"], fuzzable=data_module_list[0]["fuzzable"], max_len=max_len)
            if s_block_start("key-value"):
                for module_string in data_module_list[1:-1]:
                    if module_string["types"] == "string":
                        s_string(module_string["bytes_data"], fuzzable=module_string["fuzzable"], max_len=max_len)
                    else:
                        s_delim(module_string["bytes_data"], fuzzable=module_string["fuzzable"], max_len=max_len)
            if repeat:
                s_repeat("key-value")
            # delim
            s_string(data_module_list[-1]["bytes_data"], fuzzable=data_module_list[-1]["fuzzable"], max_len=max_len)
        s_block_end()
    return s_get(module_name)



if __name__ == "__main__":

    rokaemes = ROKAEMes()
    module_name = "rl_task_pp_to_main"
    exec(f"print(rokaemes.{module_name})")
    exec(f'write_fuzz_module(rokaemes.{module_name}, "{module_name}", fuzzable=True)')
    read_data_module(module_name)









