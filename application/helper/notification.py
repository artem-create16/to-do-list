import os

from flask_mail import Message

from application import mail


def send_notification(task):
    msg = Message(
        'Task status has changed',
        sender=os.environ['WORK_MAIL'],
        recipients=[os.environ['ADMIN_EMAIL']]
    )
    msg.body = f"The status of the task '{task.subject}' has been changed to '{task.status.value}'"
    mail.send(msg)
