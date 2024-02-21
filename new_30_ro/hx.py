import dearpygui.dearpygui as dpg


order = []

def button_callback(sender, app_data, select):
    if select == "Kebab":
        order.append("Kebab")

    elif select == "Cartofi":
        order.append("Cartofi")

    elif select == "Suc":
        order.append("Suc")

    elif select == "Meniu":
        order.append("Meniu")


def print_order():
    print(order)


dpg.create_context()

with dpg.window(label="Custom Super Nice Window", tag = "Primary Window"):
    dpg.add_text("Python Kebab", color=(243, 156, 22))

    with dpg.collapsing_header(label="Kebab",default_open=False):
        dpg.add_text("Meniu Kebab", color=(239,219,167))
        dpg.add_button(label="Add", callback=button_callback, user_data="Kebab")

    with dpg.collapsing_header(label="Cartofi",default_open=False):
        dpg.add_text("Cartofi", color=((255,255,0)))
        dpg.add_button(label="Add", callback=button_callback, user_data="Cartofi")

    with dpg.collapsing_header(label="Suc",default_open=False):
        dpg.add_text("Suc", color=((0,92,184)))
        dpg.add_button(label="Add", callback=button_callback, user_data="Suc")

    with dpg.collapsing_header(label="Meniu",default_open=False):
        dpg.add_text("Meniu", color=(184, 229, 250))
        dpg.add_button(label="Add", callback=button_callback, user_data="Meniu")

    dpg.add_button(label="Finalizeaza comanda", callback=print_order)


dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()