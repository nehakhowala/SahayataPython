import requests, json


def push_notifications():
    url = 'https://fcm.googleapis.com/fcm/send'
    server_key = 'AAAATNxwK8Q:APA91bGW2ql8h1m92_A5YBWUKkbQ4va4YL9Dax_QWi8vejdl8HXSZjF3IoY-vMLP4GwC4GHE8gU9OEN0HcbgzqvOc_gHRHqy0G94QWFODmSw3LofPSkkYT3hb1XBFdTxW3Fqz3xeJlYm'
    body = {
        "data": {
            "title": "Sahayata",
            "body": "You Are Unsafe",
            "url": url
        },
        "notification": {
            "title": "Sahayata",
            "body": "You Are Unsafe",
            "content_available": "true"
        },
        "to": "erZ-DSFU24g:APA91bEuXBM7b8IcBY0qltKep05g3SGiBJIfPunraTP6zvLn2LczsWWGxh1qWP9sHzgrRih6NlAjblmIu0wsdcyhsgRprgQylIgVYvkCpR9qk79LiWms5OCHwTZX6-YRbw99-aU6vpPL"
    }

    headers = {"Content-Type": "application/json",
               "Authorization": "key=" + server_key}
    requests.post(url, data=json.dumps(body), headers=headers)
    return 'true';