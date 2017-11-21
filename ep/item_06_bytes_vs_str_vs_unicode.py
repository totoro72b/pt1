# in python 3, bytes are 8-bit values and unicode are sequence of Unicode characters
# NOTE: Unicode gets *encoded* to bytes. Bytes get *decoded* to Unicode.


def to_str(bytes_or_string):
    """if bytes, return the decoded string (unicode here in python3). else return itself"""
    if isinstance(bytes_or_string, bytes):
        return bytes_or_string.decode('utf-8')
    return bytes_or_string

def to_bytes(bytes_or_string):
    """if string, return the encoded bytes. else return itself"""
    if isinstance(bytes_or_string, str):
        return bytes_or_string.encode('utf-8')
    return bytes_or_string

