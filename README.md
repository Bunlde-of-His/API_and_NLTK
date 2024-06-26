# Text Processing API using Flask and NLTK

This project provides a REST API for text processing using the NLTK (Natural Language Toolkit) library. The API can be used by a frontend application to perform various text processing operations such as tokenization, part-of-speech tagging, and named entity recognition.

## Requirements

- Python 3
- Virtual environment (venv)
- Flask
- NLTK

## Installation

1. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Download necessary NLTK data:**

    ```sh
    python app/nltk_setup.py
    ```

## Running the Application

1. **Start the Flask server:**

    ```sh
    python run.py
    ```

2. The API will be available at `http://127.0.0.1:5000`.

# API Testing with Postman

To test the API using Postman, follow these steps:

1. Open Postman and create a new request.

2. Set the request method to `POST`.

3. Enter the API endpoint URL (e.g., `http://127.0.0.1:5000/tokenize`).

4. Navigate to the "Body" tab and select `raw`. Then choose `JSON` from the dropdown menu.

5. Enter the JSON payload in the request body. For example:

    ```json
    {
        "text": "Some text - bla_bla"
    }
    ```

6. Click "Send" to send the request and view the response.

## Example Requests Using Postman

### Tokenization

**Endpoint:** `/tokenize`

**Method:** `POST`

**Request Body:**

```json
{
    "text": "Barack Obama was born in Hawaii."
}
```

**Example Response:**

```json
[
    "Barack",
    "Obama",
    "was",
    "born",
    "in",
    "Hawaii",
    "."
]
```

### Part-of-Speech Tagging

**Endpoint:** `/pos_tag`

**Method:** `POST`

**Request Body:**

```json
{
    "text": "Barack Obama was born in Hawaii."
}
```

**Example Response:**

```json
[
    [
        "Barack",
        "NNP"
    ],
    [
        "Obama",
        "NNP"
    ],
    [
        "was",
        "VBD"
    ],
    [
        "born",
        "VBN"
    ],
    [
        "in",
        "IN"
    ],
    [
        "Hawaii",
        "NNP"
    ],
    [
        ".",
        "."
    ]
]
```

### Named Entity Recognition

**Endpoint:** `/ner`

**Method:** `POST`

**Request Body:**

```json
{
    "text": "Barack Obama was born in Hawaii."
}
```

**Example Response:**

```json
[
    [
        "Barack Obama",
        "PERSON"
    ],
    [
        "Hawaii",
        "GPE"
    ]
]
```