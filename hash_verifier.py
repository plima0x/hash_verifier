#!/usr/bin/python3

import hashlib
import argparse


def generate_hash(byte_obj: bytes, hash_alg: str) -> str:
    print("[+] Calculating hash \n")
    m = hashlib.new(hash_alg)
    m.update(byte_obj)
    obj_hash = m.hexdigest()
    print(f"Calculated {hash_alg} hash: {obj_hash}\n")
    return obj_hash


def get_file_content(base_file: str) -> bytes:
    with open(base_file, mode="rb") as f:
        file_content = f.read()
    return file_content


def compare_file(file: str, hash_to_use: str):
    bin_file_content = get_file_content(file)
    informed_hash = input("Enter the file hash informed by the origin: ")
    real_hash = generate_hash(bin_file_content, hash_to_use)
    if informed_hash == real_hash:
        print("[+] They have the same hash!")
    else:
        print("[+] *** They have different hashes ***")


def write_file(output_filepath: str, output_content: str):
    print(f"[+] Saving the hash in {output_filepath}")
    with open(output_filepath, mode="w") as out_file:
        out_file.write(output_content)
    print(f"[+] Content saved!")


def main():
    parser = argparse.ArgumentParser(
        prog="hasher",
        description="Simple program to generate hash."
    )

    parser.add_argument("-a", "--alg",
                        dest="hash_alg",
                        required=True,
                        choices=hashlib.algorithms_available,
                        help="the hash algorith to use")
    parser.add_argument("-f", "--file",
                        dest="file_name",
                        required=True,
                        help="file to generate the hash")
    parser.add_argument("-c", "--compare",
                        dest="should_compare",
                        action="store_true",
                        help="file to generate the hash and compare with")
    parser.add_argument("-w", "--write",
                        dest="output_file",
                        help="filename to write the output hash")

    args = parser.parse_args()
    if args.should_compare and not args.output_file:
        compare_file(args.file_name, args.hash_alg)
    elif args.output_file and not args.should_compare:
        binary_content = get_file_content(args.file_name)
        file_hash = generate_hash(binary_content, args.hash_alg)
        write_file(args.output_file, file_hash)
    else:
        print("[!] Enter a valid operation!")


if __name__ == "__main__":
    main()
