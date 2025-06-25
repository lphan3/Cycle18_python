# Azure Document Intelligence Sample

This project demonstrates the usage of Azure AI Document Intelligence (formerly Form Recognizer) to analyze and extract information from documents using Python.

## Features

- Document layout analysis
- Handwritten text detection
- Text content extraction
- Table analysis
- Selection marks (checkboxes, radio buttons) detection

## Prerequisites

- Python 3.8 or later
- Azure Document Intelligence resource
- Required packages:
  - azure-ai-documentintelligence
  - azure-core

## Installation

1. Clone this repository:
```bash
git clone https://github.com/lphan3/Doc.int.AI.git
cd Doc.int.AI
```

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

3. Install the required packages:
```bash
# Install all required packages
pip install azure-ai-documentintelligence azure-core

# Verify installation
pip list | findstr azure
```

4. Configure your Azure credentials:
   - Go to [Azure Portal](https://portal.azure.com)
   - Create or select your Document Intelligence resource
   - Copy the endpoint URL and API key
   - Update `Starting.py` with your credentials:
     ```python
     endpoint = "YOUR_ENDPOINT_HERE"  # e.g., "https://your-resource.cognitiveservices.azure.com/"
     key = "YOUR_KEY_HERE"  # Your Azure Document Intelligence API key
     ```

5. Test the installation:
```bash
python Starting.py
```

## Configuration

Before running the code, you need to configure your Azure Document Intelligence credentials:

1. Get your endpoint URL and API key from the Azure Portal
2. Update the following variables in `Starting.py`:
   - `endpoint`: Your Azure Document Intelligence endpoint URL
   - `key`: Your Azure Document Intelligence API key

## Usage

The sample code demonstrates several features:

1. Document Analysis
   - Uses the "prebuilt-layout" model for general document analysis
   - Supports URL-based document analysis
   - Sample document URL provided for testing

2. Style Analysis
   - Detects handwritten content in documents
   - Processes document styles

3. Page Content Analysis
   - Extracts text lines from each page
   - Processes selection marks (checkboxes, radio buttons)
   - Handles UTF-8 encoded content

4. Table Analysis
   - Extracts table structure
   - Processes table cells and their content
   - Provides row and column information

## Sample Output

The code will output:
- Document style information (handwritten content detection)
- Text content from each line
- Selection mark states and confidence levels
- Table dimensions and cell contents

## Code Structure

The code is organized into clear sections:
1. Imports and Dependencies
2. Azure Configuration
3. Sample Document Setup
4. Client Initialization
5. Document Analysis
6. Style Analysis
7. Page Content Analysis
8. Table Analysis

## Resources

- [Azure Document Intelligence Documentation](https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-python)
- [Azure Portal](https://portal.azure.com)

## Note

This is a sample implementation for presentation purposes. For production use, ensure proper error handling and security measures are in place.

## Excel Integration Options

For Excel interaction, you can use the following packages:
## This is base on my research, there're more out there
### 1. pandas
- Most popular and powerful data manipulation library
- Excellent for Excel file handling and lookup operations
- Installation: `pip install pandas openpyxl`
- Features:
  - Read/write Excel files
  - VLOOKUP-like operations using `merge()`
  - Data filtering and transformation
  - Large dataset handling

### 2. openpyxl
- Direct Excel file manipulation
- Installation: `pip install openpyxl`
- Features:
  - Read/write Excel files
  - Cell formatting
  - Formula support
  - Charts and images

### 3. xlwings
- Excel automation with Python
- Installation: `pip install xlwings`
- Features:
  - Interact with Excel application
  - Run Excel macros
  - Real-time Excel updates
  - Excel formula execution

### 4. xlrd and xlwt
- Lightweight Excel file handling
- Installation: `pip install xlrd xlwt`
- Features:
  - Read Excel files (xlrd)
  - Write Excel files (xlwt)
  - Basic Excel operations

### Recommended Setup
For most use cases, we recommend using pandas with openpyxl:
```bash
pip install pandas openpyxl
```

Example usage with pandas for lookup operations:
```python
import pandas as pd

# Read Excel files
df1 = pd.read_excel('source.xlsx')
df2 = pd.read_excel('lookup.xlsx')

# Perform VLOOKUP-like operation
result = pd.merge(df1, df2, on='key_column', how='left')
```
