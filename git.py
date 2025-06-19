class Notifier:
    def send(self, message):
        raise NotImplementedError("Этот метод должен быть реализован в подклассе")

class EmailNotifier(Notifier):
    def _init_(self, email):
        self.email = email
    
    def send(self, message):
        print(f"Отправлено письмо на {self.email}: {message}")

class TelegramNotifier(Notifier):
    def _init_(self, username):
        self.username = username
    
    def send(self, message):
        print(f"Отправлено сообщение в Telegram @{self.username}: {message}")

class User:
    def _init_(self, name, notifier):
        self.name = name
        self.notifier = notifier

def send_notifications(users, message):
    for user in users:
        user.notifier.send(message)


users = [
    User("Alice", EmailNotifier("alice@mail.com")),
    User("Bob", TelegramNotifier("bob123"))
]

send_notifications(users, "Добро пожаловать!")


