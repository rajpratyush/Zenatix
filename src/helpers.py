import psutil


# function to return processes and their corresponding information
def listOfProcesses():
    processDatabase = []
    # iterate over the list
    for proc in psutil.process_iter(attrs=("name", "pid", "cpu_percent", "memory_percent")):
        info = {
            "PID": proc.info["pid"],
            "Name": proc.info["name"],
            "CPU in Use": f"{proc.info['cpu_percent']}%",
            "Memory in Use": f"{(mem := proc.info['memory_percent']):.5f}%",
            "Memory Usage": psutil.virtual_memory().total * (mem / 100) / (1024 ** 3),
        }
        processDatabase.append(info)
    return processDatabase
