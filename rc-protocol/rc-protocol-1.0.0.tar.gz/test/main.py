from rc_protocol import get_checksum
from rc_protocol import validate_checksum

SHARED_SECRET = "s3cr3t_p@ssw0rd"

my_dict = {
    "key1": "value1",
    "key2": "value2"
}

checksum = get_checksum(my_dict, SHARED_SECRET)
assert validate_checksum(my_dict, checksum, SHARED_SECRET)

checksum = get_checksum(my_dict, SHARED_SECRET, salt="Dies ist ein TestJP™")
assert validate_checksum(my_dict, checksum, SHARED_SECRET, salt="Dies ist ein TestJP™")
