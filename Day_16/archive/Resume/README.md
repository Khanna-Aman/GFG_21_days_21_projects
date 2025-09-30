# Resume Dataset

## File Information

**File:** `Resume.csv.zip`  
**Original Size:** 53.67 MB  
**Compressed Size:** 7.74 MB  
**Compression Ratio:** 86% reduction

## Usage

To use this dataset, extract the ZIP file:

### Windows (PowerShell)
```powershell
Expand-Archive -Path Resume.csv.zip -DestinationPath .
```

### Windows (Command Prompt)
```cmd
tar -xf Resume.csv.zip
```

### Linux/Mac
```bash
unzip Resume.csv.zip
```

### Python
```python
import zipfile
with zipfile.ZipFile('Resume.csv.zip', 'r') as zip_ref:
    zip_ref.extractall('.')
```

## Why Compressed?

The original CSV file exceeded GitHub's recommended 50 MB limit. To optimize repository size and clone speed, the file has been compressed. The compressed version is 86% smaller while maintaining all data integrity.

## Dataset Description

This dataset contains resume information used for the Day 16 Smart OCR Bot project, which performs intelligent document classification and text extraction.

