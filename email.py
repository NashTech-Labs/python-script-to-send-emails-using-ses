import boto3

def send_email(user):
    ses = boto3.client("ses")
    ses.send_email(
        Source="yournotifier@yourdomain.com",
        Destination={
            "ToAddresses": [
                f"{user}@yourdomain.com"
            ]
        },
        Message={
            "Subject": {
                "Data": "Your subject"
            },
            "Body": {
                "Text": {
                    "Data": f"""
Your body data.
                """
                }
            }
        }
    )
