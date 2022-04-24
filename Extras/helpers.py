import uuid
import base64

def generate_22char_uuid():
    my_uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    return my_uuid[0:22]