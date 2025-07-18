processes = {}

def add_process(pid, name):
    processes[pid] = name

def end_process(pid):
    if pid in processes:
        del processes[pid]

def list_processes():
    for pid, name in processes.items():
        print(f"{pid}: {name}")

add_process(101, "Edge")
add_process(102, "Word")
end_process(101)
list_processes()
