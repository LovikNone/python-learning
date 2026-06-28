tasks = []
print("Команды: !показать, !удалить, !добавить, !изменить, !количество, !очистить")
while True:
    start = input("Введи команду + задачу:")
    parts = start.split()

    try:
        if parts[0] == "!добавить":
            task = " ".join(parts[1:])
            tasks.append(task)
            print("Задача добавлена") 
          
        elif parts[0] == "!показать":
            if tasks == []:
                print("Список пуст")
                continue
            for index, task in enumerate(tasks, 1):
                print(f"{index}) {task}")
        
        elif parts[0] == "!удалить":
            index = int(parts[1])
            if index < 1 or index > len(tasks):
                print(f"Задачи {index} не существует")
                continue
            else:
                deleted_task = tasks.pop(index - 1)
                print(f"Удалена задача: {deleted_task}")
        
        elif parts[0] == "!изменить":
            index = int(parts[1])
            if index < 1 or index > len(tasks):
                print(f"Задачи {index} не существует")
                continue
            else:
                task = " ".join(parts[2:])
                tasks[index - 1] = task
                print(f"Задача {index} изменина: {task}")

        elif parts[0] == "!количество":
            if tasks == []:
                print("Список пуст")
                continue
            else:
                print(len(tasks)) 
        
    except Exception as e:
        print(f"Ошибка кода: {e}")
    
    