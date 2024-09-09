
# Markdown to JSON Converter GitHub Action

![GitHub release (latest by date)](https://img.shields.io/github/v/release/alokVishu/gh-action-md-to-json)
![GitHub](https://img.shields.io/github/license/alokVishu/gh-action-md-to-json)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/alokVishu/gh-action-md-to-json/convert-markdown.yml)

A custom GitHub Action that converts a Markdown changelog file into a structured JSON format. This action is ideal for developers who want to automate the conversion of changelog files to JSON format, making it easier to integrate with other tools and workflows.

## Features

- **Automatic Conversion**: Converts Markdown changelog files to JSON format.
- **Supports Common Markdown Formats**: Handles headings, bullet points, and other elements.
- **Easy Integration**: Can be integrated into any GitHub workflow.
- **Customizable**: Allows specifying the input and output file paths.

## Supported Markdown Formats

This action supports converting Markdown changelog files formatted like:

```markdown
## v1.1.0 (2024-07-25)

### Added

- Added Kanban app

### Updated

- Updated all the packages to the latest version

### Fixed

- Fixed apps & front-pages bugs
```

## Inputs

- **`markdown_file`**: (Required) The path to the Markdown file to be converted.
  - Default: `changelog.md`
- **`output_file`**: (Optional) The path where the JSON output should be saved.
  - Default: `changelog.json`

## Outputs

- **`json_file`**: The path to the generated JSON file.

## Usage

To use this GitHub Action, create a workflow file (e.g., `.github/workflows/convert-markdown.yml`) in your repository with the following content:

```yaml
name: Convert Markdown to JSON

on:
  workflow_dispatch:

jobs:
  convert:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Convert Markdown to JSON
        uses: alokVishu/gh-action-md-to-json@main
        with:
          markdown_file: "CHANGELOG.md"
          output_file: "changelog.json"

      - name: Upload new changelog
        uses: appleboy/scp-action@master
        with:
          host: ${{ secrets.HOST }}
          username: ${{ secrets.USERNAME }}
          port: ${{ secrets.PORT }}
          key: ${{ secrets.SSHKEY }}
          source: changelog.json
          target: ${{ secrets.PROD_DIR }}
```

Replace `alokVishu/gh-action-md-to-json@main` with the path to your action, and adjust the input parameters as needed.

## Example Workflow

This example workflow converts a `CHANGELOG.md` file into a `changelog.json` file. The workflow then uploads the JSON file to a server using `scp`:

```yaml
name: "📋 Deploy - Changelog"

on: workflow_dispatch

jobs:
  deployment:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Convert Markdown to JSON
        uses: alokVishu/gh-action-md-to-json@main
        with:
          markdown_file: "CHANGELOG.md"
          output_file: "changelog.json"

      - name: Upload new changelog
        uses: appleboy/scp-action@master
        with:
          host: ${{ secrets.HOST }}
          username: ${{ secrets.USERNAME }}
          port: ${{ secrets.PORT }}
          key: ${{ secrets.SSHKEY }}
          source: changelog.json
          target: ${{ secrets.PROD_DIR }}
```

## Installation

To use this action, simply reference it in your workflow by adding the following step:

```yaml
uses: alokVishu/gh-action-md-to-json@main
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check out the [issues page](https://github.com/alokVishu/gh-action-md-to-json/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need to automate changelog conversion in development workflows.
