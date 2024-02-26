                  _               _                      _  __ _           
                 | |             | |                    (_)/ _(_)          
                 | |__   __ _ ___| |__   __   _____ _ __ _| |_ _  ___ _ __ 
                 | '_ \ / _` / __| '_ \  \ \ / / _ \ '__| |  _| |/ _ \ '__|
                 | | | | (_| \__ \ | | |  \ V /  __/ |  | | | | |  __/ |   
                 |_| |_|\__,_|___/_| |_|   \_/ \___|_|  |_|_| |_|\___|_|   
                                                                           



## What is it?

**hash verifier** is a python program that verifies the hash of a file. 

It uses the library [argparse](https://docs.python.org/3/library/argparse.html#module-argparse) to process the command-line arguments. 

And, It uses the library [hashlib](https://docs.python.org/3/library/hashlib.html) to generate the hash using the available algorithms.

## Getting started:

#### Generate the file hash and compare it with the provider's hash:

```

python3 hash_verifier.py -a sha256 -f test/file.txt -c

```

**-a, --alg: specify the hash algorithm to be used.**

**-f, --file: specify which file to generate the hash from.**

**-c, --compare: with this option, the generated hash will be compared with the file provider's hash.**


#### Generate the file hash and write the content to hash_file_output.txt:

```

python3 hash_verifier.py -a sha256 -f test/file.txt -w hash_file_output.txt 

```

**-w, --write: specify the file to write the generated hash.**


#### The program supports sha224, sha256, sha512, md5 and a variety of other hash algorithms. Use the -h option to see a full list:

```

python3 hash_verifier.py -h


```




                                                            
