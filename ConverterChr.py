import re

def string_to_vba_chr(input_string, max_line_length=255):
    """Converts a string into a sequence of VBA Chr(), breaking lines if necessary"""
    vba_sequence = [f"Chr({ord(char)})" for char in input_string]
    
    # Join the sequence into a single string
    vba_string = " & ".join(vba_sequence)
    
    # Split the string into lines with a maximum length of max_line_length characters
    lines = []
    while len(vba_string) > max_line_length:
        # Find the nearest point before the limit where we can split
        split_point = vba_string[:max_line_length].rfind(" & ")
        lines.append(vba_string[:split_point])
        vba_string = vba_string[split_point + 3:]  # 3 to skip " & "
    
    # Add the remaining part
    lines.append(vba_string)
    
    # Return the string with continuation at the end of each line using "_"
    return " & _\n".join(lines)

def vba_chr_to_string(vba_sequence):
    """Decodes a VBA Chr() sequence into a string"""
    numbers = re.findall(r"Chr\((\d+)\)", vba_sequence)
    decoded_string = ''.join(chr(int(num)) for num in numbers)
    return decoded_string

# Example usage
if __name__ == "__main__":
    # String to be converted
    str = "This is a test string for VBA Chr() conversion"

    # Convert the string into VBA Chr()
    vba_result = string_to_vba_chr(str)
    print("VBA Chr() sequence:")
    print(vba_result)
    print("\n")

    # Decode a VBA Chr() sequence
    decoded_string = vba_chr_to_string(vba_result)
    print("Decoded string:")
    print(decoded_string)
