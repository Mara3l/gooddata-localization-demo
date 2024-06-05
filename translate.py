from os import getenv
from dotenv import load_dotenv
from googletrans import Translator
from gooddata_sdk import GoodDataSdk

load_dotenv()

host = getenv("GOODDATA_HOST")
token = getenv("GOODDATA_TOKEN")


def create_translation_function(target_language):
    def my_translation_function(
        to_translate: str, already_translated=True, old_translation=""
    ):
        if to_translate == "":
            return ""
        try:
            translator = Translator()
            translated_text = translator.translate(to_translate, target_language)
            print(translated_text.text)
            return translated_text.text
        except Exception as e:
            print(f"Translation failed: {e}")
            return old_translation

    return my_translation_function


def translate_workspace(workspace_id: str, target_language: str):

    # Since googletrans doesn't work with regular codes, we need to strip the -XY code at the end.
    # For japanese ("ja-JA") this would yield "ja".
    trans_func = create_translation_function(target_language[:-3])

    sdk = GoodDataSdk.create(host, token)
    sdk.catalog_workspace.add_metadata_locale(
        workspace_id=workspace_id,
        target_language=target_language,
        translator_func=trans_func,
        set_locale=True,
    )


if __name__ == "__main__":
    translate_workspace(workspace_id="", target_language="ja-JA")
