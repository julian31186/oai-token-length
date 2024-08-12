import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

def count_tokens():
    with open("text_input.txt", "r") as f:
        return len(encoder.encode(f.read()))

if __name__ == "__main__":
    print(f'Number of Tokens -> {count_tokens()}')