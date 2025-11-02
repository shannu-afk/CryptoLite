# 💎 Cryptolite – A Simple Blockchain & Wallet System

> A beginner-friendly blockchain simulation built with **Python** and **Flask**, allowing you to create wallets, mine blocks, and make crypto-style transactions on a local blockchain.

---

## 🧠 Overview

**Cryptolite** is a lightweight blockchain project designed to help developers understand how blockchain, mining, and wallet transactions work in a simple way — without needing external dependencies like Ethereum or Bitcoin networks.

---

## 🚀 Features

- 🔗 **Blockchain Core** – Implements block creation, proof-of-work, and chain validation.  
- 💰 **Transactions** – Simulated crypto transactions between wallets.  
- 🧾 **Wallet System** – Generate wallets with public/private keys.  
- ⛏️ **Mining** – Reward miners with new tokens for validating transactions.  
- 🌐 **Flask API** – Interact with the blockchain via RESTful endpoints.  
- 🧱 **Data Integrity** – Uses SHA-256 hashing to ensure block immutability.

---

## 🧩 Project Structure

```
cryptolite/
│
├── app.py                 # Main Flask application
├── blockchain.py          # Core blockchain logic
├── wallet.py              # Wallet generation and transactions
├── static/                # Static files (CSS, JS, images)
├── templates/             # HTML templates for the web interface
├── requirements.txt       # Python dependencies
└── README.md              # Documentation
```

---

## ⚙️ Installation & Setup

### 🪄 Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/cryptolite.git
cd cryptolite
```

### 🧰 Step 2: Create a Virtual Environment
```bash
python -m venv venv
```

Activate it:
- **Windows:** `venv\Scripts\activate`
- **macOS/Linux:** `source venv/bin/activate`

### 📦 Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

Example `requirements.txt`:
```
Flask==3.0.3
requests==2.31.0
ecdsa==0.18.0
```

---

## 🧑‍💻 Running the App

Start the Flask server:
```bash
python app.py
```

Then open your browser and visit:
```
http://127.0.0.1:5000/
```

You should see the **Cryptolite Wallet** interface running locally.

---

## 🧭 API Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `GET` | `/mine_block` | Mines a new block and adds it to the chain |
| `POST` | `/create_wallet` | Creates a new wallet (returns address & keys) |
| `POST` | `/add_transaction` | Adds a transaction between two wallets |
| `GET` | `/get_chain` | Returns the full blockchain |
| `GET` | `/is_valid` | Checks if the blockchain is valid |

---

## 💸 Example Usage

1️⃣ **Create Wallets**
```bash
POST /create_wallet
```
Response:
```json
{
  "address": "abc123...",
  "private_key": "xyz789..."
}
```

2️⃣ **Add a Transaction**
```bash
POST /add_transaction
{
  "sender": "SYSTEM",
  "receiver": "wallet_address_here",
  "amount": 20
}
```

3️⃣ **Mine a Block**
```bash
GET /mine_block
```

4️⃣ **View the Blockchain**
```bash
GET /get_chain
```

---

## 📚 How It Works

1. **New Transactions** are added to the pending transaction list.  
2. **Mining** runs a proof-of-work algorithm to find a valid hash.  
3. **Reward** is given to the miner’s wallet.  
4. **New Block** is added to the chain and verified.  

Every block includes:
```json
{
  "index": 1,
  "timestamp": "2025-11-02T10:00:00",
  "transactions": [],
  "proof": 12345,
  "previous_hash": "0"
}
```

---

## 🧩 Concepts Covered

- Blockchain data structure  
- Proof-of-Work algorithm  
- Cryptographic hashing (SHA-256)  
- Flask REST APIs  
- Wallet generation using public/private key pairs  

---

## 🧠 Future Improvements

- 🪙 Real-time wallet balance tracking  
- 🔐 Enhanced transaction signatures  
- 🌍 Peer-to-peer network nodes  
- 🖥️ Web UI dashboard for mining & transactions  

---


## 👨‍💻 Author

**👋 K.Shanmukh**

## 🪪 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it for learning or development.
