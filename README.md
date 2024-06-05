# GoodData Localization Demo

This script provides functionality to translate the metadata of a GoodData workspace into a specified target language using the Google Translate API. The translated metadata can then be set as the locale for the workspace.

This repository only works as a demo, and should be used as such. It is not to be used in production.

## Installation

1. Clone the repository.
1. Create the development venv with `make dev` and enable it with `source .venv/bin/activate`.

## Setup

Create .env in the root directory of the project and add the host and token variable:

```
GOODDATA_HOST=your_gooddata_host
GOODDATA_TOKEN=your_gooddata_token
```

## Usage

To use the script, you can either import it in another file, or you can run the `translate.py` after a minor tweak, where you should change the `workspace_id` and `target_language`.

## Available Languages
The script uses Google Translate, so any language supported by Google Translate can be used as the target language. Common examples include:

`de-DE` for German
`fr-FR` for French
`es-ES` for Spanish
`ja-JP` for Japanese

For the complete list of supported languages, check the [documentation](https://www.gooddata.com/docs/cloud/customize-appearance/change-display-language/#ChangeDisplayLanguage-ChangetheLanguage).
