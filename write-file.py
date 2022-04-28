def main():
    inFile = open('lines.txt', 'rt')
    outFile = open('lines-copy.txt', 'wt')

    for lines in inFile:
        print(lines.rstrip(), file=outFile)
        print('.', end='.', flush=True)

    outFile.close()
    print("\nDone")

main()