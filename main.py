import argparse
import csv
from pathlib import Path
from google.cloud import firestore

db = firestore.Client()

def sync_collection(collection_name: str) -> None:
    """
    Sync documents from a Firestore collection to a local text file.

    Args:
    - collection_name (str): The name of the Firestore collection.

    """
    collections_dir = Path("collections")
    collections_dir.mkdir(exist_ok=True)
    file_path = collections_dir / f"{collection_name}.txt"
    
    docs = db.collection(collection_name).stream()
    with open(file_path, 'w') as f:
        for doc in docs:
            f.write(f'{doc.id}: {doc.to_dict()}\n')

def delete_document(collection_name: str, doc_id: str) -> None:
    """
    Delete a document from a Firestore collection.

    Args:
    - collection_name (str): The name of the Firestore collection.
    - doc_id (str): The ID of the document to be deleted.

    """
    db.collection(collection_name).document(doc_id).delete()

def add_document(collection_name: str, fields: list[str]) -> None:
    """
    Add a new document to a Firestore collection.

    Args:
    - collection_name (str): The name of the Firestore collection.
    - fields (list[str]): List of field-value pairs to be added.

    """
    data = dict(zip(fields[::2], fields[1::2]))
    db.collection(collection_name).add(data)

def update_document(collection_name: str, doc_id: str, fields: list[str]) -> None:
    """
    Update a document in a Firestore collection.

    Args:
    - collection_name (str): The name of the Firestore collection.
    - doc_id (str): The ID of the document to be updated.
    - fields (list[str]): List of field-value pairs to update.

    """
    data = dict(zip(fields[::2], fields[1::2]))
    db.collection(collection_name).document(doc_id).set(data, merge=True)

def add_from_csv(collection_name: str, csv_path: str) -> None:
    """
    Add documents to a Firestore collection from a CSV file.

    Args:
    - collection_name (str): The name of the Firestore collection.
    - csv_path (str): Path to the CSV file.

    """
    with open(csv_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            db.collection(collection_name).add(row)

def query_collection(collection_name: str, conditions: list[str]) -> None:
    """
    Query a Firestore collection based on provided conditions.

    Args:
    - collection_name (str): The name of the Firestore collection.
    - conditions (list[str]): List of field, operator, value sets to filter documents.

    """
    query = db.collection(collection_name)
    for i in range(0, len(conditions), 3):
        field, operator, value = conditions[i:i+3]
        query = query.where(field, operator, value)

    for doc in query.stream():
        print(f'{doc.id}: {doc.to_dict()}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Firestore CLI operations.')
    parser.add_argument('--sync', help='Sync a collection to file')
    parser.add_argument('--delete', nargs=2, help='Delete a document from collection. Args: collectionName, docID')
    parser.add_argument('--add', nargs='+', help='Add a document to collection. Args: collectionName, field1, value1, ...')
    parser.add_argument('--update', nargs='+', help='Update a document in collection. Args: collectionName, docID, field1, value1, ...')
    parser.add_argument('--csv', nargs=2, help='Add records to collection from CSV. Args: collectionName, csvFilePath')
    parser.add_argument('--query', nargs='+', help='Query a collection. Args: collectionName, field1, operator1, value1, ...')
    
    args = parser.parse_args()

    if args.sync:
        sync_collection(args.sync)
    elif args.delete:
        delete_document(args.delete[0], args.delete[1])
    elif args.add:
        add_document(args.add[0], args.add[1:])
    elif args.update:
        update_document(args.update[0], args.update[1], args.update[2:])
    elif args.csv:
        add_from_csv(args.csv[0], args.csv[1])
    elif args.query:
        query_collection(args.query[0], args.query[1:])