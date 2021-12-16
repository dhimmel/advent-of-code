"""
Day 16: Packet Decoder
https://adventofcode.com/2021/day/16
"""
from pathlib import Path

# @dataclass
# class Packet:
#     binary_string: str

#     @classmethod
#     def from_hex(cls, hex_string):
#         binary_string = bin(int(hex_string, 16))[2:]
#         instance = cls(binary_string=binary_string)
#         return instance

#     @property
#     def version(self):
#         return int(self.binary_string[:3], base=2)

#     @property
#     def packet_type(self):
#         return int(self.binary_string[3:6], base=2)

#     @property
#     def is_literal(self):
#         return self.packet_type == 4

#     @property
#     def is_operator(self):
#         return self.packet_type != 4

# class LiteralPacket(Packet):


# class OperatorPacket(Packet):


def read_input(test: bool = True):
    path = Path(__file__).parent.joinpath("test_input.txt" if test else "input.txt")
    text = Path(path).read_text().strip()
    return text


def hex_to_bit_string(hex_string):
    hex_len = len(hex_string) * 4
    bin_string = bin(int(hex_string, 16))[2:]
    return bin_string.zfill(hex_len)


def parse_literal(remainder):
    parts = []
    while True:
        start_bit = remainder[0]
        part = remainder[1:5]
        parts.append(part)
        remainder = remainder[5:]
        if start_bit == "0":
            break
    if not remainder or int(remainder, 2) == 0:
        remainder = ""
    value = int("".join(parts), base=2)
    print(f"parsed literal with value {value}")
    return remainder, value


def parse_operator(input, version_sum):
    print(f"parse operator {input}")
    length_type_id = int(input[0])
    remainder = input[1:]
    if length_type_id == 0:
        total_length = int(remainder[:15], base=2)
        remainder = remainder[15:]
        remainder, version_sum = parse_packets(remainder[:total_length], version_sum)
    else:
        n_subpackets = int(remainder[:11], base=2)
        remainder = remainder[11:]
        for i in range(n_subpackets):
            remainder, version_sum = parse_packets(
                remainder, version_sum, recurse=False
            )
    return remainder, version_sum


def parse_packets(input, version_sum=0, recurse=True):
    if not input:
        return input, version_sum
    print(f"parse_packets {input}")
    version = int(input[:3], base=2)
    version_sum += version
    packet_type = int(input[3:6], base=2)
    print(f"version {version}, packet type {packet_type}")
    remainder = input[6:]
    if packet_type == 4:
        # packet type ID, 4, which means the packet is a literal value.
        print(f"remainder {remainder}")
        remainder, literal = parse_literal(remainder)
        if remainder and recurse:
            remainder, version_sum = parse_packets(remainder, version_sum)
    else:
        # operator that performs some calculation on one or more sub-packets contained within
        remainder, version_sum = parse_operator(remainder, version_sum)
    return remainder, version_sum


def get_version_sum(hex_string):
    bit_string = hex_to_bit_string(hex_string)
    remainder, version_sum = parse_packets(bit_string)
    print("final remainder", remainder)
    return version_sum


# assert 16 == get_version_sum("8A004A801A8002F478")
# assert 31 == get_version_sum("A0016C880162017C3686B18A3D4780")
print(get_version_sum("620080001611562C8802118E34"))
# assert 12 == get_version_sum("620080001611562C8802118E34")


# input = hex_to_bit_string("D2FE28")
# input = hex_to_bit_string("8A004A801A8002F478")
# # print(input)
# print(parse_packets(hex_to_bit_string("EE00D40C823060")))
# assert 12 == parse_packets(hex_to_bit_string("620080001611562C8802118E34"))
# print(f"version_sum {version_sum}")
# print(version, packet_type)
# input = read_input(test=True)
# print(input)
# print(literal)

# import binascii
# print(bin(binascii.unhexlify("D2FE28")))

print()
