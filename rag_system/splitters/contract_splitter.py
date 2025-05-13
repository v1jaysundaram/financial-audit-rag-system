from rag_system.loaders.contract_loader import load_contracts

# load contracts
contracts = load_contracts()

print(f"Loaded {len(contracts)} contracts.")