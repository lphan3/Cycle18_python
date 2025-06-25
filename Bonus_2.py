"""
BONUS 2: Beginner-Friendly Azure Document Intelligence Example
This script shows how to use the real Azure Document Intelligence API in a simple way.

Steps:
1. Install the required package: pip install azure-ai-documentintelligence
2. Get your Azure endpoint and API key from the Azure Portal
3. Run this script to analyze a sample document and print table data
"""

# 1. Import the necessary packages
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

# 2. Set up your Azure endpoint and key
# Replace these with your own values from the Azure Portal
endpoint = "https://test-c18.cognitiveservices.azure.com/"  # Example: https://my-resource.cognitiveservices.azure.com/
key = "ARmok5JWQ2Tu3Yr7yLGqsdLHZuDhyX899vwLYq24sO1E36TdrF9hJQQJ99BEACYeBjFXJ3w3AAALACOGr3Cf"  # Example: "1234567890abcdef..."

# 3. Choose a document to analyze (we'll use a sample PDF from Microsoft)
formUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf"

# 4. Create the client
client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# 5. Start the analysis (using the prebuilt-layout model)
print("Analyzing document... (this may take a few seconds)")
poller = client.begin_analyze_document(
    "prebuilt-layout", AnalyzeDocumentRequest(url_source=formUrl)
)
result = poller.result()  # Wait for the analysis to finish

# 6. Print out table data found in the document
if result.tables:
    print(f"Found {len(result.tables)} table(s) in the document.")
    for table_idx, table in enumerate(result.tables):
        print(f"\nTable #{table_idx} ({table.row_count} rows, {table.column_count} columns):")
        # Build a 2D array for the table
        table_matrix = [["" for _ in range(table.column_count)] for _ in range(table.row_count)]
        for cell in table.cells:
            table_matrix[cell.row_index][cell.column_index] = cell.content
        for row in table_matrix:
            print(row)
else:
    print("No tables found in the document.")

print("\nDone! You just used the real Azure Document Intelligence API.") 