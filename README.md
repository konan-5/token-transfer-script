# Token Transfer Script

A Python script for transferring ERC20 tokens to multiple addresses using the Ethereum network.

## Table of Contents

- [Description](#description)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)

## Description

The Token Transfer Script is a Python script that leverages the Web3 Python library to transfer ERC20 tokens to multiple addresses on the Ethereum network. It reads a list of recipient addresses from a file, connects to the Ethereum network using an RPC provider, and sends the specified amount of tokens to each address.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/konan-5/token-transfer-script.git
   ```

2. Navigate to the project directory:

   ```shell
   cd token-transfer-script
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

### Configuration

1. Rename the `.env.example` file to `.env`.

2. Open the `.env` file and provide the following configuration:

   ```shell
   PRIVATE_KEY=<your-private-key>
   RPC_URL=<ethereum-rpc-url>
   AMOUNT=<token-amount>
   TOKEN_CONTRACT_ADDRESS=<usdt-contract-address>
   ```

   - `PRIVATE_KEY`: The private key of the Ethereum address from which the tokens will be sent.
   - `RPC_URL`: The URL of the Ethereum RPC provider.
   - `AMOUNT`: The amount of tokens to transfer to each address.
   - `TOKEN_CONTRACT_ADDRESS`: The address of the ERC20 token contract.

## Usage

1. Prepare a file named `addresses.txt` that contains the list of recipient addresses, with each address on a new line.

2. Run the script:

   ```shell
   python transfer_tokens.py
   ```

   The script will connect to the Ethereum network, transfer tokens to each address in `addresses.txt`, and display the transaction hash for each transfer.
