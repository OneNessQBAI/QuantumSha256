import hashlib

def classical_sha256(message):
    # Compute the SHA-256 hash of the input message
    sha256_hash = hashlib.sha256(message.encode()).hexdigest()
    return sha256_hash

def main():
    # Ask for user input
    message = input("Enter a message to hash using Classical SHA-256: ")
    
    # Calculate the SHA-256 hash
    hash_result = classical_sha256(message)
    
    # Print the result
    print(f"Classical SHA-256 hash: {hash_result}")

if __name__ == "__main__":
    main()
