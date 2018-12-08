from onesignal import OneSignal, SegmentNotification
import os
import environ


def enviar(mensagem, url=''):
    env = environ.Env()
    environ.Env.read_env('.env')
    APP_ID = env('APP_ID_ONESIGNAL')
    API_KEY = env('API_KEY_ONESIGNAL')

    client = OneSignal(APP_ID, API_KEY)
    notification_to_all_users = SegmentNotification(
        contents={
            "en": mensagem,
            "pt": mensagem,
        },
        url=url,
        included_segments=[SegmentNotification.ALL],
    )
    client.send(notification_to_all_users)
