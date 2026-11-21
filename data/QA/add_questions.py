
import json
import shutil
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
dataset_path = project_root / "data" / "QA" / "cybersecurity_qa.json"
backup_path = project_root / "data" / "QA" / "cybersecurity_qa_backup.json"

# Batch 6: Digital Forensics and Evidence Analysis
new_questions = [
    {
        "id": 101,
        "category": "Digital Forensics",
        "question": "What is digital forensics?",
        "answer": "Digital forensics is the process of identifying, collecting, preserving, examining, and presenting digital evidence from computers, mobile devices, networks, and other digital systems. It supports cybercrime investigations and incident response."
    },
    {
        "id": 102,
        "category": "Digital Forensics",
        "question": "What are the main phases of digital forensics?",
        "answer": "Common phases include identification, preservation, collection or acquisition, examination, analysis, and reporting. These phases help investigators handle digital evidence systematically while maintaining its integrity and documenting their actions."
    },
    {
        "id": 103,
        "category": "Digital Forensics",
        "question": "What is digital evidence?",
        "answer": "Digital evidence is information stored or transmitted in digital form that may be relevant to an investigation. Examples include emails, documents, photographs, browser history, system logs, network captures, and mobile device data."
    },
    {
        "id": 104,
        "category": "Digital Forensics",
        "question": "What is the chain of custody?",
        "answer": "Chain of custody is the documented record of how evidence is collected, transferred, stored, accessed, and handled throughout an investigation. It identifies the people responsible, dates, times, and actions performed to help establish evidence integrity and accountability."
    },
    {
        "id": 105,
        "category": "Digital Forensics",
        "question": "Why is evidence preservation important in digital forensics?",
        "answer": "Evidence preservation helps prevent accidental or intentional alteration, deletion, or contamination of digital evidence. Investigators document the original state, use appropriate acquisition methods, restrict access, and maintain integrity checks throughout the investigation."
    },
    {
        "id": 106,
        "category": "Digital Forensics",
        "question": "What is forensic imaging?",
        "answer": "Forensic imaging is the creation of a bit-by-bit copy of a digital storage device or specified media. It aims to preserve the original evidence, including allocated and unallocated areas, so investigators can examine the copy rather than unnecessarily modifying the original."
    },
    {
        "id": 107,
        "category": "Digital Forensics",
        "question": "What is a write blocker?",
        "answer": "A write blocker is a hardware or software mechanism that prevents data from being written to a storage device during forensic acquisition. It helps protect original evidence from accidental modification while allowing investigators to read and copy its contents."
    },
    {
        "id": 108,
        "category": "Digital Forensics",
        "question": "What is file hashing in digital forensics?",
        "answer": "File hashing generates a fixed-length digest from digital data using a hash algorithm such as SHA-256. Investigators calculate hashes before and after acquisition or examination to check whether the data has changed. Matching hashes provide evidence that the compared data is identical with respect to that hash algorithm."
    },
    {
        "id": 109,
        "category": "Digital Forensics",
        "question": "What is the difference between MD5 and SHA-256?",
        "answer": "MD5 produces a 128-bit hash, while SHA-256 produces a 256-bit hash. MD5 is vulnerable to collision attacks and should not be relied upon for modern security-sensitive integrity verification. SHA-256 is generally preferred for forensic integrity checks."
    },
    {
        "id": 110,
        "category": "Digital Forensics",
        "question": "What is disk forensics?",
        "answer": "Disk forensics is the examination of data stored on storage devices such as hard drives and solid-state drives. Investigators may examine file systems, deleted files, partitions, metadata, timestamps, and other artifacts to reconstruct user or system activity."
    },
    {
        "id": 111,
        "category": "Digital Forensics",
        "question": "What is memory forensics?",
        "answer": "Memory forensics involves analyzing volatile memory, commonly RAM, to investigate running processes, active network connections, loaded modules, command history, and possible malware activity. It can reveal evidence that may not be available from disk analysis alone."
    },
    {
        "id": 112,
        "category": "Digital Forensics",
        "question": "What is volatile data?",
        "answer": "Volatile data is information that can disappear when a system loses power or changes state. Examples include RAM contents, active network connections, running processes, and temporary system information. Investigators may collect it early because it can be lost quickly."
    },
    {
        "id": 113,
        "category": "Digital Forensics",
        "question": "What is non-volatile data?",
        "answer": "Non-volatile data is information that generally remains stored after a system is powered off. Examples include files on hard drives, solid-state drives, and other persistent storage. It can be collected and examined during a forensic investigation."
    },
    {
        "id": 114,
        "category": "Digital Forensics",
        "question": "What is file system analysis?",
        "answer": "File system analysis is the examination of how a storage device organizes and manages files and directories. Investigators inspect file metadata, timestamps, directory structures, deleted entries, and file allocation information to understand system activity."
    },
    {
        "id": 115,
        "category": "Digital Forensics",
        "question": "What are file metadata and why are they important?",
        "answer": "File metadata is information describing a file, such as its name, size, type, creation time, modification time, and ownership. Metadata can help investigators establish timelines and understand how files were created, accessed, or changed, although timestamps must be interpreted carefully."
    },
    {
        "id": 116,
        "category": "Digital Forensics Tools",
        "question": "What is Autopsy in digital forensics?",
        "answer": "Autopsy is an open-source digital forensics platform that provides a graphical interface for examining hard drives and forensic disk images. It supports file analysis, keyword searching, deleted-file recovery, timeline examination, and other investigative tasks."
    },
    {
        "id": 117,
        "category": "Digital Forensics Tools",
        "question": "What is The Sleuth Kit?",
        "answer": "The Sleuth Kit is an open-source collection of command-line tools and libraries used to investigate disk images and file systems. It helps forensic analysts examine partitions, file metadata, directory structures, and deleted file entries."
    },
    {
        "id": 118,
        "category": "Digital Forensics Tools",
        "question": "What is Volatility used for?",
        "answer": "Volatility is an open-source memory forensics framework used to analyze RAM captures. Investigators can examine processes, network connections, loaded modules, command-line activity, and other memory artifacts that may indicate malicious behavior."
    },
    {
        "id": 119,
        "category": "Digital Forensics",
        "question": "What is a forensic timeline?",
        "answer": "A forensic timeline is a chronological representation of relevant digital events, such as file creation, modification, access, logins, and system activity. It helps investigators reconstruct sequences of events and identify suspicious behavior."
    },
    {
        "id": 120,
        "category": "Digital Forensics",
        "question": "What should a digital forensic investigation report contain?",
        "answer": "A digital forensic report should include the investigation scope, case details, evidence identifiers, acquisition methods, tools and versions used, integrity verification results, examination procedures, findings, limitations, conclusions, and supporting documentation. It should be clear, objective, and reproducible."
    }
]


def main():
    if not dataset_path.exists():
        print("Error: Dataset file was not found.")
        return

    with dataset_path.open("r", encoding="utf-8") as file:
        existing_questions = json.load(file)

    existing_ids = {item["id"] for item in existing_questions}
    new_ids = [item["id"] for item in new_questions]

    if len(new_ids) != len(set(new_ids)):
        print("Error: Duplicate IDs inside Batch 6.")
        return

    duplicates = existing_ids.intersection(new_ids)

    if duplicates:
        print(f"Error: These IDs already exist: {sorted(duplicates)}")
        print("Dataset has not been modified.")
        return

    shutil.copy2(dataset_path, backup_path)

    updated_questions = existing_questions + new_questions
    temp_path = dataset_path.with_suffix(".tmp")

    with temp_path.open("w", encoding="utf-8") as file:
        json.dump(updated_questions, file, indent=4, ensure_ascii=False)

    with temp_path.open("r", encoding="utf-8") as file:
        json.load(file)

    temp_path.replace(dataset_path)

    print("Batch 6 added successfully!")
    print("Questions added:", len(new_questions))
    print("Total questions:", len(updated_questions))
    print("Backup created:", backup_path.name)


if __name__ == "__main__":
    main()
