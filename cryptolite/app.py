from flask import Flask, render_template, request, redirect, url_for
from blockchain import Blockchain
from wallet import Wallet

app = Flask(__name__)

blockchain = Blockchain()
wallets = {}
current_wallet = None


def get_wallet_address():
    """Return the current wallet address if exists."""
    return current_wallet.address if current_wallet else None


def get_balance(wallet_address):
    """Return balance for given wallet address."""
    if not wallet_address:
        return 0
    return blockchain.get_balance(wallet_address)


@app.route('/')
def index():
    wallet_created = current_wallet is not None
    wallet_address = get_wallet_address()
    balance = get_balance(wallet_address)
    return render_template('index.html', wallet_created=wallet_created, wallet_address=wallet_address, balance=balance)


@app.route('/create_wallet', methods=['POST'])
def create_wallet():
    global current_wallet
    if current_wallet:
        # If already created, redirect to home
        return redirect(url_for('home'))

    current_wallet = Wallet()
    wallets[current_wallet.address] = current_wallet

    # ✅ Give new wallet 20 BTC initial balance
    blockchain.add_transaction("SYSTEM", current_wallet.address, 20.0)
    blockchain.mine_block()

    balance = blockchain.get_balance(current_wallet.address)
    return render_template('create_wallet.html', wallet=current_wallet, balance=balance, wallet_created=True)


@app.route('/home')
def home():
    wallet_address = get_wallet_address()
    wallet_created = bool(wallet_address)
    balance = get_balance(wallet_address)
    return render_template('home.html', wallet_created=wallet_created, wallet_address=wallet_address, balance=balance)


@app.route('/send', methods=['POST'])
def send():
    if not current_wallet:
        return redirect(url_for('index'))

    receiver = request.form['receiver']
    amount = float(request.form['amount'])

    blockchain.add_transaction(current_wallet.address, receiver, amount)
    balance = blockchain.get_balance(current_wallet.address)
    return render_template(
        'home.html',
        wallet=current_wallet,
        balance=balance,
        wallet_created=True,
        message=f"✅ Sent {amount} CLT to {receiver}"
    )


@app.route('/mine_block')
def mine_block():
    if not current_wallet:
        return redirect(url_for('index'))

    if len(blockchain.pending_transactions) == 0:
        return render_template(
            'home.html',
            wallet=current_wallet,
            balance=blockchain.get_balance(current_wallet.address),
            wallet_created=True,
            message="❌ No transactions found to mine."
        )

    blockchain.mine_block()
    balance = blockchain.get_balance(current_wallet.address)
    return render_template(
        'home.html',
        wallet=current_wallet,
        balance=balance,
        wallet_created=True,
        message="✅ Block mined successfully!"
    )


@app.route('/view_chain')
def view_chain():
    chain_data = blockchain.chain
    wallet_address = get_wallet_address()
    wallet_created = bool(wallet_address)
    return render_template('view_chain.html', chain=chain_data, wallet_created=wallet_created, wallet_address=wallet_address)


@app.route('/view_balance')
def view_balance():
    if not current_wallet:
        return redirect(url_for('index'))

    balance = blockchain.get_balance(current_wallet.address)
    transactions = []

    for block in blockchain.chain:
        for tx in block['transactions']:
            if tx['sender'] == current_wallet.address or tx['receiver'] == current_wallet.address:
                transactions.append(tx)

    return render_template(
        'view_balance.html',
        wallet=current_wallet,
        balance=balance,
        transactions=transactions,
        wallet_created=True
    )


if __name__ == '__main__':
    app.run(debug=True)
