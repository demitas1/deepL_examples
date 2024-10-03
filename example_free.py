import deepl
import os

DEEPL_AUTH_KEY = 'DEEPL_AUTH_KEY'
if DEEPL_AUTH_KEY in os.environ:
    auth_key = os.environ[DEEPL_AUTH_KEY]
else:
    print('DEEPL_AUTH_KEY is not set.')
    exit()

translator = deepl.Translator(auth_key)

result = translator.translate_text("Hello, world!", target_lang="FR")
print(result.text)  # "Bonjour, le monde !"

result = translator.translate_text("Hello, world!", target_lang="DE")
print(result.text)

result = translator.translate_text("Hello, world!", target_lang="JA")
print(result.text)

result = translator.translate_text("Hello, world!", target_lang="ZH-HANS")
print(result.text)

result = translator.translate_text("Hello, world!", target_lang="ZH-HANT")
print(result.text)

result = translator.translate_text("Hello, world!", target_lang="KO")
print(result.text)
