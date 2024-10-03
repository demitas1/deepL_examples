import deepl
import yaml
import re
import argparse
import os


def translate_markdown(api_key, input_file, output_file, target_language):
    # Initialize the DeepL translator
    translator = deepl.Translator(api_key)

    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the frontmatter and the markdown content
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)

    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        markdown_content = content[frontmatter_match.end():]
        has_frontmatter = True
    else:
        frontmatter = ""
        markdown_content = content
        has_frontmatter = False

    # Translate the markdown content
    translated_content = translator.translate_text(markdown_content, target_lang=target_language)

    if has_frontmatter:
        # Parse and translate the frontmatter
        frontmatter_data = yaml.safe_load(frontmatter)
        for key, value in frontmatter_data.items():
            if isinstance(value, str):
                frontmatter_data[key] = translator.translate_text(value, target_lang=target_language).text

        # Reconstruct the document with frontmatter
        translated_frontmatter = yaml.dump(frontmatter_data, allow_unicode=True, default_flow_style=False)
        translated_document = f"---\n{translated_frontmatter}---\n\n{translated_content.text}"
    else:
        # Use only the translated content for pure markdown
        translated_document = translated_content.text

    # Write the translated content to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_document)

    print(f"Translation complete. Output saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Translate Markdown files using DeepL API.')
    parser.add_argument('input_file', help='Input Markdown file')
    parser.add_argument('-o', '--output', help='Output file (optional)')
    parser.add_argument('-l', '--language', default='JA', help='Target language code (default: JA)')
    parser.add_argument('-k', '--api_key', default='', help='DeepL API key')

    args = parser.parse_args()

    if args.api_key:
        api_key = args.api_key
    else:
        # get API from os envrion
        DEEPL_AUTH_KEY = 'DEEPL_AUTH_KEY'
        if DEEPL_AUTH_KEY in os.environ:
            api_key = os.environ[DEEPL_AUTH_KEY]
        else:
            print('DEEPL_AUTH_KEY is not set. set it or give in arguments.')
            exit()

    # Generate output filename if not provided
    if args.output:
        output_file = args.output
    else:
        base, ext = os.path.splitext(args.input_file)
        output_file = f"{base}-{args.language}{ext}"

    translate_markdown(api_key, args.input_file, output_file, args.language)


if __name__ == "__main__":
    main()
