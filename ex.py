class examenGrillll():
    def __init__(self, data):
        self.data = data

    def make_data_go_insane(self):
        print(f"======== {self.data}")


test = examenGrillll("Shakalaka-boom")
test.make_data_go_insane()