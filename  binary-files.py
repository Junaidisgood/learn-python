def main():
    # we're using rb/wb here - the b stands for binary while rt is used in text files, t- text
    infile = open('cat.jpg', 'rb')
    outfile = open('cat-copy.jpg', 'wb')

    while True:
        # create buffer and read(buffer size) - 10GB here
        buf = infile.read(10240)
        if buf:
            # if buffer is true, write the buffer
            outfile.write(buf)
            print('.', end='.', flush=True)
        else:
            break

    outfile.close()
    print("\nDone")

if __name__ == "__main__":
    main()