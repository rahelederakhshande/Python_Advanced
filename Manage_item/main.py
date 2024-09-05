from Manager import *
def main():
    manager1 = InventoryManager()
    while True:
        cmd = input("add/remove/edit/display/search/detail/exit: ")
        if cmd == "add":
            id_i, name, numbers, price = input("info: ").split(",")
            #1,p1,4,200
            item = manager1.create_item(id_i, name, int(numbers), int(price))
            manager1.add_item(item)
        elif cmd == "edit":
            id_i = input("id for edit: ")
            manager1.edit_item(id_i)
        elif cmd == "remove":
            id_i = input("id for remove: ")
            manager1.remove_item(id_i)
        elif cmd == "display":
            manager1.display_item()
        elif cmd == "search":
            name = input("name for search: ")
            manager1.search(name)
        elif cmd == "detail":
            manager1.details()
        elif cmd == "exit":
            break
        elif cmd == "":
            continue
        else:
            print(f"{cmd}: not found!")
if __name__ == "__main__":
    main()