def ls(sys_state, args = None):
    return sorted(sys_state)

def mkdir(sys_state, args):
    directory_name = args[0]
    if directory_name in sys_state:
        assert "Directory already exists!"
    sys_state.append(directory_name)
    return f"Directory '{directory_name}' Created!"

def touch(sys_state, args):
    file_name = args[0]
    if file_name in sys_state:
        assert "File already exists!"
    sys_state.append(file_name)
    return f"File '{file_name}' Created!"

def unix_filter(sys_state, args):
    pattern = args[0]
    if pattern == "/":
        output = [i for i in sys_state if i.startswith(pattern)]
        return output
    else:
        output = [i for i in sys_state if i.endswith(pattern)]
        return output


def process_command(sys_state, command):
    split_command = command.strip().split()
    op, args = split_command[0].upper(), split_command[1:]
    if op == "LS":
        output = ls(sys_state)
    elif op == "MKDIR":
        output = mkdir(sys_state, args)
    elif op == "TOUCH":
        output = touch(sys_state, args)
    elif op == "FILTER":
        output = unix_filter(sys_state, args)
    else:
        assert "Unknown Command!"
    return output
    

def user_interface(sys_state):
    while True:
        full_command = input("$ ").strip() 
        output = process_command(sys_state, full_command)
        print(output)

if __name__ == "__main__":
    init_state = ['/Desktop', '/Documents', '/home', 'test.txt']
    user_interface(init_state)