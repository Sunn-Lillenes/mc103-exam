# Cryptography and Blockchain

MC103 academic portfolio covering classical cryptanalysis, hashing, digital
signatures and Ethereum smart contracts.

## Code to explore

| Directory | Topic |
| --- | --- |
| [oppgave1](oppgave1) | Caesar and extended-alphabet substitution experiments |
| [oppgave2](oppgave2) | XOR and ASCII cipher analysis |
| [oppgave3](oppgave3) | Rail Fence transposition |
| [oppgave4](oppgave4) | Digest identification and hash comparisons |
| [oppgave10](oppgave10) | Solidity ERC-20 contract, Hardhat configuration and deployment scripts |

The repository also contains selected screenshots from the original exercises.
Python cryptanalysis examples use the standard library.

```bash
python3 oppgave1/oppgave1.py
python3 oppgave2/XOR.py
python3 oppgave3/rail_fence.py
python3 oppgave4/hash_checks.py
```

## Ethereum component

The `oppgave10` folder contains `SJLToken.sol`, an OpenZeppelin-based token,
alongside deployment and transfer scripts. RPC endpoints and signing keys are
read from environment variables.

Use a local Hardhat network for development. The included Lock files are starter
template material. The token and deployment configuration form the exam-specific
extension. The existing package's test command is a scaffold and is not a
validated token test suite.

This repository records educational experiments and demonstrations.
