from optimeed.core import obj_to_json, json_to_obj


class Foo:
    x: float

    def __init__(self):
        self.x = 3.0


class Bar(Foo):
    y: float

    def __init__(self):
        super().__init__()
        self.y = 2.0


if __name__ == "__main__":
    obj = Bar()

    obj2json = obj_to_json(obj)
    print(obj2json)
    # obj_obj2 = json_to_obj(obj2_json)
