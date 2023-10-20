# Firestore CLI Utility

This Firestore CLI utility provides an easy way to interact with Firestore collections, allowing you to sync, delete, add, update, and query documents.

## Functions

- `sync`: Sync documents from a Firestore collection to a local text file.
- `delete`: Delete a document from a Firestore collection.
- `add`: Add a new document to a Firestore collection.
- `update`: Update a document in a Firestore collection.
- `csv`: Add documents to a Firestore collection from a CSV file.
- `query`: Query a Firestore collection based on provided conditions.

## Setup and Authentication

### Using `gcloud`

Before you start using the Firestore CLI utility, ensure that you have the `gcloud` CLI installed and authenticated:

1. **Listing Available Project IDs**:
   To view a list of all your Google Cloud project IDs, run:
```
gcloud projects list
```

2. **Setting Your Desired Project**:
If you have multiple projects and want to set a particular one as the default, use:
```
gcloud config set project YOUR_PROJECT_ID
```

3. **Authenticate**:
Make sure you're authenticated to the correct Google Cloud account:
```
gcloud auth login
```

If using the Firestore CLI utility in a service or automated setup, you'd authenticate differently, e.g., using service accounts.

## Usage

Here are examples of how to use the provided functions:

- **Sync a collection**:
```
main.py --sync COLLECTION_NAME
```

- **Delete a document from a collection**:
```
main.py --delete COLLECTION_NAME DOCUMENT_ID
```

- **Add a new document to a collection**:
```
main.py --add COLLECTION_NAME FIELD1 VALUE1 FIELD2 VALUE2 ...
```

- **Update a document in a collection**:
```
main.py --update COLLECTION_NAME DOCUMENT_ID FIELD1 VALUE1 FIELD2 VALUE2 ...
```

- **Add documents from a CSV file**:
```
main.py --csv COLLECTION_NAME CSV_FILE_PATH
```

- **Query a collection**:
```
main.py --query COLLECTION_NAME FIELD1 OPERATOR1 VALUE1 FIELD2 OPERATOR2 VALUE2 ...
```

## Dependencies

- Ensure you have the `google-cloud-firestore` Python library installed.
- The CLI also requires `argparse`, `csv`, and `pathlib` which are standard libraries in Python.

## Conclusion

This Firestore CLI utility simplifies the process of interacting with Fires
"# firestoreCLI" 
