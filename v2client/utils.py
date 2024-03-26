import re
import uuid

from google.protobuf.message import Message
from google.protobuf import any_pb2


def to_any_type(message: Message) -> any_pb2.Any:
    """
    Convert a protobuf message to an any_pb2.Any.
    V2Ray requires any_pb2.Any for some API calls.
    :param message: A protobuf message.
    :return: an any_pb2.Any.
    """
    return any_pb2.Any(type_url=message.DESCRIPTOR.full_name, value=message.SerializeToString())


def is_email_valid(email: str) -> bool:
    """
    Check if an email is valid.
    :param email: An email address.
    :return: True if the email is valid, False otherwise.
    """
    return re.match(r"[a-zA-Z\d_.+-]+@[a-zA-Z\d-]+\.[a-zA-Z\d-.]+$", email) is not None


def random_uuid() -> str:
    """
    Generate a random UUID.
    :return: A UUID.
    """
    return str(uuid.uuid4())

