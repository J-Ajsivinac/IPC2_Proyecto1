class Alert:
    def __init__(self, a_type, message):
        self.a_type = a_type
        self.message = message
        self.show_message()

    def show_message(self):
        temp_type = ""
        temp_message = ""
        if self.a_type == "exito":
            temp_type = "\033[42m ✔ Operación Exitosa \033[0m"
            temp_message = f"\033[32m {self.message} \033[0m"
        elif self.a_type == "advertencia":
            temp_type = "\033[43m ⚠ Advertencia \033[0m"
            temp_message = f"\033[33m {self.message} \033[0m"
        elif self.a_type == "error":
            temp_type = "\033[41m ✖ Error \033[0m"
            temp_message = f"\033[31m {self.message} \033[0m"
        elif self.a_type == "procesando":
            temp_type = "\033[44m ♦ Procesando \033[0m"
            temp_message = f"\033[34m {self.message} \033[0m"
        print(f"{temp_type}{temp_message}")
