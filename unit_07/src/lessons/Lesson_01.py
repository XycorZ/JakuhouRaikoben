import os
import base64

def get_current_working_directory():
  return os.getcwd()

def encode_string(str_to_encode):
  based = base64.b64encode(str_to_encode.encode("ascii"))
  unbased = based.decode("ascii")
  return unbased

def decode_string(base64_str_to_decode):
  unbased = base64.b64decode(base64_str_to_decode)
  based = unbased.decode("ascii")
  return based



if __name__ == "__main__":
  print(get_current_working_directory())
  print(encode_string("Python is a cool programming language!"))
  # should print UHl0aG9uIGlzIGEgY29vbCBwcm9ncmFtbWluZyBsYW5ndWFnZSE=
  str_to_decode = "UHl0aG9uIGlzIGEgY29vbCBwcm9ncmFtbWluZyBsYW5ndWFnZSE="
  print(decode_string(str_to_decode))
  # should print Python is a cool programming language!