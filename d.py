# constructor
def constructor(self, arg):
    self.constructor_arg = arg


# method
def displayMethod(self, arg):
    print(arg)


# class method
@classmethod
def classMethod(cls, arg):
    print(arg)


# creating class dynamically
Geeks = type(
    "Geeks",
    (object,),
    {
        # constructor
        "__init__": constructor,
        # data members
        "string_attribute": "Geeks 4 geeks !",
        "int_attribute": 1706256,
        # member functions
        "func_arg": displayMethod,
        "class_func": classMethod,
    },
)

obj = Geeks("constructor argument")
print(obj.constructor_arg)
print(obj.string_attribute)
print(obj.int_attribute)
obj.func_arg("Geeks for Geeks")
Geeks.class_func("Class Dynamically Created !")

from dotenv import load_dotenv

load_dotenv()

def set_device(self, data):
    self.component = data["components"][0]["id"]
    for capabilities in data["components"][0]["capabilities"][0]:
        for key, value in capabilities.items():
            setattr(self, key, value)
    self.label = data["label"]

Device = type("Device", (object,), {
    "__init__": set_device,

})