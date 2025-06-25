# BONUS: Connecting Python Basics to Document Intelligence
# This script shows how Room_1 to Room_6 concepts help in document analysis tasks

# Room_1: Type checking (is this a valid document?)
document = {'type': 'pdf', 'pages': 2, 'tables': 1}
if isinstance(document, dict) and document.get('type') == 'pdf':
    print('Valid PDF document!')
else:
    print('Invalid document.')

# Room_3: List of tables (like result.tables in Azure)
tables = [
    {'rows': 2, 'columns': 2, 'cells': [['A1', 'A2'], ['B1', 'B2']]},
    {'rows': 1, 'columns': 3, 'cells': [['C1', 'C2', 'C3']]}
]

# Room_4: Counting tables using a loop
real_count = 0
for table in tables:
    if isinstance(table, dict):
        real_count += 1
print(f'Total tables found: {real_count}')

# Room_5: Conditional logic (do we have any tables?)
if real_count > 0:
    print('Tables detected in document!')
else:
    print('No tables found.')

# Room_6: Using a class to represent a Table
class Table:
    def __init__(self, rows, columns, cells):
        self.rows = rows
        self.columns = columns
        self.cells = cells

# Create a Table object from the first table in the list
first_table = Table(
    rows=tables[0]['rows'],
    columns=tables[0]['columns'],
    cells=tables[0]['cells']
)

# Print the table's cells (like printing table content in document_intelligence_with_notes.py)
print('First table content:')
for row in first_table.cells:
    print(row)

# This bonus file shows how basic Python skills are used in real document analysis tasks!
