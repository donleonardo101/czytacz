import deepl
import requests

# conda create --name tlumacz python=3.10.12

# conda create --name tlumacz python=3.11.4
# conda activate tlumacz
# pip install --upgrade deepl
# conda install -c conda-forge deepl
# conda install -c conda-forge requests
# python3 -v tlumacz_DL.py

auth_key = "DEEPL_API_KEY"  # zmienna srodowiskowa
translator = deepl.Translator(auth_key)

result = translator.translate_text("Hello, world!", target_lang="FR")
print(result.text)  # "Bonjour, le monde !"

# Translate a formal document from English to German
input_path = "./rosliny.pdf"
output_path = "./rosliny_en.pdf"
try:
    # Using translate_document_from_filepath() with file paths 
    translator.translate_document_from_filepath(
        input_path,
        output_path,
        target_lang="EN",
        formality="more"
    )

    # Alternatively you can use translate_document() with file IO objects
    # with open(input_path, "rb") as in_file, open(output_path, "wb") as out_file:
    #     translator.translate_document(
    #         in_file,
    #         out_file,
    #         target_lang="DE",
    #         formality="more"
    #     )

except deepl.DocumentTranslationException as error:
    # If an error occurs during document translation after the document was
    # already uploaded, a DocumentTranslationException is raised. The
    # document_handle property contains the document handle that may be used to
    # later retrieve the document from the server, or contact DeepL support.
    doc_id = error.document_handle.id
    doc_key = error.document_handle.key
    print(f"Error after uploading ${error}, id: ${doc_id} key: ${doc_key}")
except deepl.DeepLException as error:
    # Errors during upload raise a DeepLException
    print(error)