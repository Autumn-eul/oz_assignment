import json

def create_expanded_json(input_file, output_file, multiplier=10):
    with open(input_file, 'r', encoding='utf-8') as f:
        books = json.load(f)

    expanded_books = books * multiplier

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(expanded_books, f, ensure_ascii=False, indent=4)

    print(f"New JSON file with {len(expanded_books)} entries saved to {output_file}")

input_file = 'books_data.json'
output_file = 'amazon_books.json'
create_expanded_json(input_file, output_file)