import dearpygui.dearpygui as dpg


order = []

def button_callback(sender, app_data, user_data):
    if user_data == "Kebab":
        order.append("Kebab")

def print_order():
    print(order)


dpg.create_context()

with dpg.window(label="Custom Super Nice Window", tag = "Primary Window"):
    main_color = (243, 10, 25)
    dpg.add_text("Python Kebab", color=(243, 156, 22))

    with dpg.collapsing_header(label="Kebab", default_open=False):
        dpg.add_text("Meniu Kebab", color=main_color)
        dpg.add_button(label="Add", callback=button_callback, user_data="Kebab")

    with dpg.collapsing_header(label="Cartofi", default_open=False):
        dpg.add_text("Cartofi", color=main_color)
        dpg.add_button(label="Add")

    with dpg.collapsing_header(label="Suc", default_open=False):
        dpg.add_text("Suc", color=main_color)
        dpg.add_button(label="Add")

    with dpg.collapsing_header(label="Meniu", default_open=False):
        dpg.add_text("Meniu", color=main_color)
        dpg.add_button(label="Add")

    dpg.add_button(label="Finalizeaza comanda", callback=print_order)


dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()