# CSV Data Extractor

This project is a Python-based command-line tool designed to extract and display structured information from a CSV file. It supports detecting and formatting various data types including full names, email addresses, phone numbers (landline and mobile), CPF numbers (Brazilian individual taxpayer registry identification), and dates of birth.

## Features

- Extract and format:
  - Full names
  - Email addresses
  - Landline and mobile phone numbers
  - CPF numbers (Brazilian format)
  - Dates of birth
- Outputs results to the terminal grouped by category
- Easily extensible architecture using an abstract base class

## File Overview

- `main.py`: Entry point for the program. Accepts a CSV file as a command-line argument.
- `imprime_resultados.py`: Orchestrates the execution of all extractors and prints the results.
- `extrator_base.py`: Abstract base class that defines the interface and shared functionality for all extractors.
- `busca_nome.py`: Extracts full names from the CSV.
- `busca_email.py`: Extracts email addresses using regex.
- `busca_telefone.py`: Extracts and categorizes landline and mobile numbers.
- `busca_cpf.py`: Extracts and formats Brazilian CPF numbers.
- `busca_data.py`: Extracts and sorts dates in various formats.
- `database.csv`: Sample data file used as input.

## Usage

### Command-line Execution

```bash
python main.py [csv_filename]
```

If no filename is provided, it defaults to `database.csv`.

### Example

```bash
python main.py database.csv
```

## Requirements

- Python 3.x

No external libraries are required beyond the Python Standard Library.

## Structure

Each data type extractor implements:
- `_get_regex()` – defines the regular expression used
- `_processar_matches(matches)` – processes and formats the matches
- `_get_titulo()` – defines the section title for the output
- `executar()` – executes the extraction process

## License

This project is open-source and distributed under the MIT License.

## Author

Developed by Galahad.
