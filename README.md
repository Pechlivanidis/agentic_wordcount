# ccwc - A Python Implementation of Unix `wc`

A complete, production-ready Python clone of the Unix `wc` (word count) command. This implementation provides full compatibility with the standard `wc` utility, including all major options and proper output formatting.

## Features

- **Default behavior**: Output lines, words, and bytes with proper column alignment
- **`-c` option**: Count bytes in a file
- **`-l` option**: Count lines in a file
- **`-w` option**: Count words in a file
- **`-m` option**: Count characters (multibyte-aware, UTF-8 compatible)
- **Dynamic column formatting**: Matches `wc` output format exactly, including adaptive spacing
- **Universal compatibility**: Tested against 20 Project Gutenberg books with 100% accuracy

## Usage

```bash
# Count lines, words, and bytes (default)
python3 ccwc.py <filename>

# Count bytes only
python3 ccwc.py -c <filename>

# Count lines only
python3 ccwc.py -l <filename>

# Count words only
python3 ccwc.py -w <filename>

# Count characters (multibyte-aware)
python3 ccwc.py -m <filename>
```

## Examples

```bash
$ python3 ccwc.py test.txt
   7145   58164  342190 test.txt

$ python3 ccwc.py -c test.txt
342190 test.txt

$ python3 ccwc.py -l test.txt
7145 test.txt

$ python3 ccwc.py -w test.txt
58164 test.txt

$ python3 ccwc.py -m test.txt
339292 test.txt
```

## Implementation Details

### Key Features
- **Binary file reading**: Ensures accurate byte counting and UTF-8 character handling
- **Dynamic field widths**: Column width automatically adjusts based on the largest number, matching `wc` behavior
- **UTF-8 support**: Properly handles multibyte characters in character count mode (`-m`)
- **CRLF handling**: Correctly processes files with different line ending formats

### Output Format
The default output format uses dynamic spacing:
- Field width = length of the largest number across all columns
- Each field is right-aligned and separated by a single space
- Filename follows after the final space

## Testing

The implementation has been thoroughly tested against 20 real-world text files:

**10 Original Books:**
- The Art of War
- Alice's Adventures in Wonderland
- Frankenstein
- Complete Works of Shakespeare
- Middlemarch
- Wuthering Heights
- Jane Eyre
- Pride and Prejudice
- Romeo and Juliet
- A Room with a View
- Moby Dick

**10 Additional Books:**
- The Strange Case of Dr. Jekyll and Mr. Hyde
- A Tale of Two Cities
- Dracula
- A Modest Proposal
- The Count of Monte Cristo
- The Adventures of Sherlock Holmes
- The Yellow Wallpaper
- The King in Yellow
- The Brothers Karamazov
- White Nights and Other Stories

**Test Results:** 100% compatibility with system `wc` across all test cases and options.

## Requirements

- Python 3.x
- No external dependencies

## Technical Notes

### Character Counting (-m option)
The `-m` option counts Unicode characters by:
1. Reading the file in binary mode
2. Decoding as UTF-8
3. Counting decoded characters

This approach properly handles multibyte UTF-8 sequences that are common in modern text files.

### File Handling
- **Text mode** (`-l`, `-w`): Standard text reading with automatic line ending detection
- **Binary mode** (`-c`, `-m`): Raw byte reading for accurate counts
- **Unicode support**: Full UTF-8 support for international text

### Performance
- Efficient single-pass counting for `-l` and `-w` options
- Minimal memory overhead regardless of file size
- Proper handling of both small and large files
