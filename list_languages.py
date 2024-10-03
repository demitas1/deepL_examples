import deepl
import os

DEEPL_AUTH_KEY = 'DEEPL_AUTH_KEY'
if DEEPL_AUTH_KEY in os.environ:
    auth_key = os.environ[DEEPL_AUTH_KEY]
else:
    print('DEEPL_AUTH_KEY is not set.')
    exit()

translator = deepl.Translator(auth_key)


print("Source languages:")
for language in translator.get_source_languages():
    print(f"{language.name} ({language.code})")  # Example: "German (DE)"

print("Target languages:")
for language in translator.get_target_languages():
    if language.supports_formality:
        print(f"{language.name} ({language.code}) supports formality")
        # Example: "Italian (IT) supports formality"
    else:
        print(f"{language.name} ({language.code})")
        # Example: "Lithuanian (LT)"
