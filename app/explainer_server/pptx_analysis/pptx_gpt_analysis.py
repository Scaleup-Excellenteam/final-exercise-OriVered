import argparse
import engine
import os


def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Python script to call engine.py module.')

    # Add the arguments
    parser.add_argument('FilePath', metavar='path', type=str, help='the path to the file')
    parser.add_argument('OutputPath', metavar='output', type=str, help='the path to output the results')

    # Parse the arguments
    args = parser.parse_args()

    # Check if the file exists
    if not os.path.isfile(args.FilePath):
        print(f"Error: The file '{args.FilePath}' does not exist.")
        exit(1)

    # Call the function in engine.py module
    try:
        engine.process_pptx(args.FilePath, args.OutputPath)
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")


if __name__ == "__main__":
    main()
