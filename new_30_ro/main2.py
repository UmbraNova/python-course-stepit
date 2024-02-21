import dearpygui.dearpygui as dpg


# def increment():
#     value = int(dpg.get_value("number text"))
#     dpg.set_value("number text", value + 1)

# def decrement():
#     value = int(dpg.get_value("number text"))
#     if value > 0:
#         dpg.set_value("number text", value - 1)


dpg.create_context()
dpg.create_viewport(title='PythonKebab', width=600, height=800)

with dpg.window(label="Example Window", tag="Primary Window"):
    # dpg.add_button(label="INCREMENT +", callback=increment)
    # dpg.add_text(0, tag="number text")
    # dpg.add_button(label="DECREMENT -", callback=decrement)

    dpg.add_text("Python Kebab", color=(255, 100, 25))
    main_color = (255, 0, 255)

    # menu = ["Kebab", "Cartofi", "Sucuri", "Burgeri", "Sosuri"]

    # for product in menu:
    #     with dpg.collapsing_header(label="Menu " + product,default_open=False):
    #         dpg.add_text(product, color=main_color)
    #         dpg.add_button(label="Add product")

    with dpg.collapsing_header(label="Kebab",default_open=False):
        dpg.add_text("Kebab", color=main_color)
        dpg.add_button(label="I'm a child button!")

    with dpg.collapsing_header(label="Cartofi",default_open=False):
        dpg.add_text("Cartofi", color=main_color)
        dpg.add_button(label="I'm a child button!")

    with dpg.collapsing_header(label="Suc",default_open=False):
        dpg.add_text("Suc", color=main_color)
        dpg.add_button(label="I'm a child button!")

    with dpg.collapsing_header(label="Menu",default_open=False):
        dpg.add_text("Menu", color=main_color)
        dpg.add_button(label="I'm a child button!")



dpg.add_button(label="Finalizeaza comanda!")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

