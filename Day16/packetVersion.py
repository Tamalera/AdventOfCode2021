input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

binary = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

binary_sequence = ''
for line in all_lines:
    res = line.strip('\n')
    for char in res:
        binary_sequence = binary_sequence + binary[char]
    # Strip tailing zeroes
    binary_sequence = binary_sequence.rstrip('0')

versions = []

# CONSTANTS
version_length = 3
type_length = 3
type_id_length = 1
total_length_of_bits_shifter = 15
total_number_of_packets_shifter = 11

def figure_out_packets(binary_sequence):
    global type, type_id, shifter, number_of_packets
    how_to_proceed = ''
    versions.append(int(binary_sequence[0: version_length], 2))
    type = int(binary_sequence[version_length: version_length + type_length], 2)
    type_id = None
    if type == 4:
        how_to_proceed = 'LITERAL'
    else:
        type_id = int(binary_sequence[version_length + type_length: version_length + type_length + type_id_length], 2)
    shifter = 0
    number_of_packets = 0
    if type_id != None and type_id == 0:
        shifter = int(binary_sequence[
                      version_length + type_length + type_id_length: version_length + type_length + type_id_length * total_length_of_bits_shifter + 1],
                      2)
        how_to_proceed = 'SHIFT'
    elif type_id != None and type_id == 1:
        number_of_packets = int(binary_sequence[
                                version_length + type_length + type_id_length: version_length + type_length + type_id_length * total_number_of_packets_shifter + 1],
                                2)
        how_to_proceed = 'PACKET-NO'
    else:
        if type != 4:
            raise Exception("No TypeId matches for Packets ot Type != 4")
    return how_to_proceed

def cut_literal_package(sub_packet):
    counter = 0
    stepper = 5
    first = 2
    content = sub_packet[version_length + type_length:]
    while first != 0:
        if int(content[counter * stepper: (counter + 1) * stepper][0]) == 0:
            first = 0
        else:
            counter = counter + 1
    return (version_length + type_length) + ((counter + 1) * stepper)

def truncate_packages_depending_on_type(next_step, sub_packets):
    if next_step == 'SHIFT':
        sub_packets = sub_packets[version_length + type_length + type_id_length * total_length_of_bits_shifter + 1:]
    elif next_step == 'LITERAL':
        sub_packets = sub_packets[cut_literal_package(sub_packets):]
    elif next_step == 'PACKET-NO':
        sub_packets = sub_packets[version_length + type_length + type_id_length * total_number_of_packets_shifter + 1:]

    return sub_packets

# We know that the root packet contains all others -> cannot be literal
next_step = figure_out_packets(binary_sequence)
sub_packets = truncate_packages_depending_on_type(next_step, binary_sequence)

# The inner packet needs to be analysed
while len(sub_packets) > 0:
    next_step = figure_out_packets(sub_packets)
    sub_packets = truncate_packages_depending_on_type(next_step, sub_packets)

sum = 0
for version in versions:
    sum = sum + int(version)
print(str(sum))
