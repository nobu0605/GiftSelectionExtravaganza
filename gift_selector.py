#!/usr/bin/env python3
import sys
from urllib.parse import parse_qs

gifts = [
    "Book", "Toy", "Gadget", "Video Game", "Headphones",
    "Smartphone", "Laptop", "Watch", "Shoes", "Wallet",
    "Headset", "Camera", "Drone", "Smart Watch", "Bluetooth Speaker"
]

def calculate_gift_code(selected_indices):
    code = 0
    for index in selected_indices:
        code |= (1 << index)
    return code

def generate_html(selected_gifts, gift_code):
    html_template = f"""
    <h2>Selected Gifts</h2>
    <p><strong>Selected Gifts:</strong> {', '.join(selected_gifts)}</p>
    <p><strong>Unique Gift Code:</strong> {gift_code}</p>
    <a href='/gift_selector.php'>Go back</a>
    """
    return html_template

if __name__ == "__main__":
    query_string = sys.argv[1]
    query_params = parse_qs(query_string)

    if 'indices[]' in query_params:
        input_indices = query_params['indices[]']
    elif 'indices' in query_params:  
        input_indices = query_params['indices']
    else:
        print("Content-Type: text/html\n")
        print("<h1>Error: No indices provided.</h1>")
        sys.exit(1)

    try:
        selected_indices = [int(index.strip()) for index in input_indices]
        selected_gifts = [gifts[index] for index in selected_indices]
        gift_code = calculate_gift_code(selected_indices)

        html_output = generate_html(selected_gifts, gift_code)
        print("Content-Type: text/html\n")
        print(html_output)
    except (ValueError, IndexError):
        print("Content-Type: text/html\n")
        print("<h1>Error: Invalid indices provided. Please try again.</h1>")
