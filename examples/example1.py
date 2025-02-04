from algojig import get_suggested_params, generate_accounts, dump
from algojig.ledger import JigLedger
from algosdk.future.transaction import PaymentTxn

secrets, addresses = generate_accounts(2)

sp = get_suggested_params()

ledger = JigLedger()
ledger.set_account_balance(addresses[0], 1_000_000)

transactions = [
    PaymentTxn(
        sender=addresses[0],
        sp=sp,
        receiver=addresses[1],
        amt=200_000,
    ).sign(secrets[0]),
    PaymentTxn(
        sender=addresses[1],
        sp=sp,
        receiver=addresses[0],
        amt=1,
    ).sign(secrets[1]),
]
block = ledger.eval_transactions(transactions)
dump(block[b'txns'])
print('Algo Balance 0:', ledger.get_account_balance(addresses[0]))
print('Algo Balance 1:', ledger.get_account_balance(addresses[1]))
print()
print('Account 0:', addresses[0])
dump(ledger.get_raw_account(addresses[0]))
print()
print('Account 1:', addresses[1])
dump(ledger.get_raw_account(addresses[1]))
