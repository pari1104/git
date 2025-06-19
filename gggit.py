

class SecureFile:
    def _init_(self, name):
        self._name = name
    
    def _get_(self, instance, owner):
        return self._name
    
    def _set_(self, instance, value):
        raise AttributeError("Изменение имени файла запрещено")

class LogFile:
    name = SecureFile(None)

    def _init_(self, filename):
        self.name = filename  
        self._class_.name._name = filename

    def filter_lines(self, keyword):
        with open(self.name, encoding='utf-8') as f:
            for line in f:
                if keyword in line:
                    yield line.rstrip('\n')


log = LogFile("log.txt")
for line in log.filter_lines("ERROR"):
print(line)
