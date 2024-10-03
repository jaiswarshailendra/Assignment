import time,threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Employee)
def my_signal_handler(sender, instance, **kwargs):
    current_thread = threading.current_thread().name
    print(f"Signal handler thread: {current_thread}")

    print("Signal handler started")
    time.sleep(5)  # show the delay between 2 print functions
    print("Signal handler finished")

