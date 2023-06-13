import dearpygui.dearpygui as gui
import os

def on_unlock(sender, app_data):
    added_number = 0
    gui.set_value("error_message", "")
    gui.set_value("end_message", "")
    path = gui.get_value("game_path")
    collection_file = os.path.join(path, "CHARS", "COLLECTION.txt")

    if path != "D:\SteamLibrary\steamapps\common\LEGO Batman 2":
        if os.path.isdir(os.path.join(path, "__DLC1__")):
            if not "// Characters added by Lego DLC Character Unlocker" in open(collection_file).read():
                for root, dirs, files in os.walk(path):
                    for directory in dirs:
                        if directory.startswith("__DLC"):
                            chars_dir = os.path.join(root, directory, "Chars")
                            if os.path.exists(chars_dir):
                                for file in os.listdir(chars_dir):
                                    if file.startswith("DLCCOLLECTION"):
                                        file_path = os.path.join(chars_dir, file)
                                        with open(file_path, "r") as f:
                                            lines = f.readlines()
                                            with open(collection_file, "a") as collection:
                                                if not "// Characters added by Lego DLC Character Unlocker" in open(collection_file).read():
                                                    collection.write("\n// Characters added by Lego DLC Character Unlocker\n")
                                                for line in lines:
                                                    if line.startswith("collect"):
                                                        line = line.replace("dlc_only", "")
                                                        collection.write(line)
                                                        added_number = added_number + 1
                                                        gui.set_value("end_message", f"{added_number} Characters has been added !")
            else:
                gui.set_value("error_message", "Error: DLC Characters are already unlocked")
        else:
            gui.set_value("error_message", "Error: Invalid game path or the game\nis not extracted with Quickbms\n(or the game has no DLC)")
    else:
        gui.set_value("error_message", "Error: Please enter the correct game path")

def on_reset(sender, app_data):
    gui.set_value("error_message", "")
    gui.set_value("end_message", "")
    path = gui.get_value("game_path")
    collection_file = os.path.join(path, "CHARS", "COLLECTION.txt")

    if path != "D:\SteamLibrary\steamapps\common\LEGO Batman 2":
        if os.path.isdir(os.path.join(path, "__DLC1__")):
            if "// Characters added by Lego DLC Character Unlocker" in open(collection_file).read():
                with open(collection_file, "r+") as file:
                    lines = file.readlines()
                    for i, line in enumerate(lines):
                        if line.strip() == "// Characters added by Lego DLC Character Unlocker":
                            file.truncate(i)
                            gui.set_value("end_message", "Unlocked DLC characters have been removed!")
                            break
            else:
                gui.set_value("error_message", "Error: Nothing to reset")
        else:
            gui.set_value("error_message", "Error: Invalid game path")
    else:
        gui.set_value("error_message", "Error: Please enter the correct game path")

gui.create_context()
gui.create_viewport(title='Lego DLC Character Unlocker', decorated=True, width=380, height=280)
gui.set_viewport_resizable(False)
gui.setup_dearpygui()
gui.set_viewport_always_top(True)

with gui.window(label='Nexus', width=380, height=280, no_title_bar=True, no_resize=True, no_move=True):
    with gui.tab_bar(label='Tabs'):

        with gui.tab(label='Game Selection'):
            gui.add_text("Enter the game directory :")
            gui.add_input_text(tag="game_path", width=350, default_value="D:\SteamLibrary\steamapps\common\LEGO Batman 2")
            gui.add_text("")
            gui.add_button(label="Unlock DLC Characters", callback=on_unlock)
            gui.add_button(label="Reset DLC Characters", callback=on_reset)
            error_message = gui.add_text("", tag="error_message", color=(255, 0, 0))
            end_message = gui.add_text("", tag="end_message", color=(0, 255, 0))


        with gui.tab(label="About"):
            gui.add_text("Version : 1.0.1")
            # 
            gui.add_text("GitHub Page : github.com/Calvineries\n/Lego-DLC-Character-Unlocker")            
            gui.add_text("")
            gui.add_text("Author : Calvineries")
            gui.add_text("Contributors: ...")
gui.show_viewport()
gui.start_dearpygui()
gui.destroy_context()
