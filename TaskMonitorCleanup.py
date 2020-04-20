import datetime, sys


args = sys.argv[1:]
N = 2

date_N_days_ago = datetime.datetime.today() - datetime.timedelta(days=N)

pastDate = str(date_N_days_ago).rpartition(" ")[0]
dateP = datetime.datetime.strptime(pastDate, "%Y-%m-%d")

taskList = alltask.getTasks()

for task in taskList:
    if task.state == TaskExecutionState.EXECUTED:
        format = str(task.completionDate).rpartition("T")[0]
        date = datetime.datetime.strptime(format, "%Y-%m-%d")
        if date <= dateP:
            alltask.archive(task.id)
