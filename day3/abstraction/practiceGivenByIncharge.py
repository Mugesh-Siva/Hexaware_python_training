from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        return "Email notification sent"

class SMSNotification(Notification):
    def send(self):
        return "SMS notification sent"

notification1 = EmailNotification()
notification2=SMSNotification()


print(notification2.send())
print(notification1.send())