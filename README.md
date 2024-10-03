# DeepL Translation API Examples

This repository contains examples of how to use the DeepL Translation API with Python.

## Prerequisites

- Python 3.6 or higher
- A DeepL API authentication key (sign up at [www.deepl.com](https://www.deepl.com))

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/deepl-translation-examples.git
   cd deepl-translation-examples
   ```

2. Install the DeepL Python client library:
   ```
   pip install deepl
   ```

3. Set up your API authentication key:
   - Create a file named `secrets.sh` in the project root.
   - Add your DeepL API key to the file:
     ```
     export DEEPL_AUTH_KEY="your_api_key_here"
     ```

## Usage

1. Source the authentication key file:
   ```
   source secrets.sh
   ```

2. Run the example script:
   ```
   python example_free.py
   ```

This script demonstrates translating "Hello, world!" into various languages using the DeepL API.

## Example Output

The `example_free.py` script will output translations of "Hello, world!" in:
- French (FR)
- German (DE)
- Japanese (JA)
- Simplified Chinese (ZH-HANS)
- Traditional Chinese (ZH-HANT)
- Korean (KO)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
