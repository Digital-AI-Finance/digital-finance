# BSc Course Syllabus: Blockchain, Cryptocurrencies & DeFi
## Digital Finance Program

---

# PART I: COURSE INFORMATION

## Basic Information

| Field | Details |
|-------|---------|
| **Course Title** | Blockchain, Cryptocurrencies, and Decentralized Finance |
| **Program** | BSc Digital Finance / BSc Business Administration |
| **Credits** | 6 ECTS |
| **Total Contact Hours** | 36 hours (48 lessons x 45 minutes) |
| **Prerequisites** | None (introductory level) |
| **Language** | English |

## Course Description

This course provides a comprehensive introduction to blockchain technology, cryptocurrencies, and decentralized finance (DeFi). Students will gain both theoretical understanding and practical skills, from cryptographic fundamentals to smart contract development and DeFi protocol interaction. The course emphasizes hands-on learning through testnet exercises while maintaining academic rigor in analyzing real-world case studies and regulatory frameworks.

By the end of this course, students will understand how blockchain systems work at a technical level, be capable of developing basic smart contracts, and be able to critically evaluate blockchain projects and protocols.

---

## Learning Outcomes

Upon successful completion of this course, students will be able to:

| # | Learning Outcome | Assessment |
|---|-----------------|------------|
| LO1 | **Explain** core blockchain concepts (cryptographic hashes, digital signatures, consensus mechanisms) using appropriate technical terminology | Quizzes, Exam |
| LO2 | **Execute** cryptocurrency transactions safely, including wallet setup, testnet transactions, and block explorer navigation | Practical 1 |
| LO3 | **Interact** with major DeFi protocols on testnets, performing swaps, liquidity provision, and lending/borrowing operations | Practical 3 |
| LO4 | **Develop** basic smart contracts using Solidity, including ERC-20 tokens with appropriate testing | Practical 2, Project |
| LO5 | **Identify** common smart contract vulnerabilities (reentrancy, access control) and apply security best practices | Practical 4 |
| LO6 | **Evaluate** blockchain projects using fundamental analysis criteria: tokenomics, technology, team, and risk assessment | Project |
| LO7 | **Analyze** case studies of blockchain successes and failures, extracting lessons about design, security, and systemic risk | Exam, Project |
| LO8 | **Compare** consensus mechanisms and Layer 2 solutions, articulating trade-offs for specific use cases | Quizzes, Exam |
| LO9 | **Navigate** regulatory frameworks, understanding token classification, KYC/AML, and jurisdictional differences | Exam, Project |
| LO10 | **Communicate** blockchain concepts to non-technical stakeholders through presentations and documentation | Project |

---

## Assessment Structure

| Component | Weight | Description | Due |
|-----------|--------|-------------|-----|
| **Module Quizzes** | 20% | 8 online quizzes (best 7 count), 10 questions each | After each module |
| **Mid-course Exam** | 20% | Written exam covering Modules 1-4 | After Lesson 24 |
| **Practical Assignments** | 25% | 4 hands-on tasks with documented outputs | See schedule |
| **Final Project** | 35% | Comprehensive project (3 track options) | End of course |

### Grading Scale

| Grade | Percentage | Description |
|-------|------------|-------------|
| A | 90-100% | Excellent - Exceeds expectations |
| B | 80-89% | Good - Meets all expectations |
| C | 70-79% | Satisfactory - Meets basic expectations |
| D | 60-69% | Passing - Minimum acceptable |
| F | <60% | Failing - Does not meet expectations |

---

## Required Materials

### Software (Free)
- **MetaMask** - Browser wallet extension (metamask.io)
- **Remix IDE** - Browser-based Solidity development (remix.ethereum.org)
- **Modern Web Browser** - Chrome, Firefox, or Brave

### Textbooks (Free/Open Access)
1. **Mastering Ethereum** by Antonopoulos & Wood - github.com/ethereumbook/ethereumbook
2. **How to DeFi** by CoinGecko - Available on CoinGecko website
3. **Bitcoin Whitepaper** by Satoshi Nakamoto - bitcoin.org/bitcoin.pdf

### Online Resources
- Solidity Documentation (docs.soliditylang.org)
- Ethereum.org Learning Hub
- CryptoZombies Interactive Tutorial (cryptozombies.io)

---

# PART II: 48-LESSON SCHEDULE

## MODULE 1: Blockchain Foundations (Lessons 1-6)

**Module Learning Objectives:**
- Understand the historical context and motivation for blockchain technology
- Explain how cryptographic primitives enable blockchain security
- Describe the structure of blocks and how they form an immutable chain

---

### Lesson 1: What is Blockchain? History & Motivation
**Duration:** 45 minutes

**Description:**
This introductory lesson establishes the historical context for blockchain technology, tracing its origins from early digital cash attempts (DigiCash, e-gold, Hashcash) to the 2008 Bitcoin whitepaper. Students will understand the fundamental problem blockchain solves: achieving trust and consensus in a distributed system without central authority. The lesson introduces the concept of a shared, immutable ledger and its revolutionary implications for finance, governance, and data management.

**Topics Covered:**
- The trust problem in digital systems
- History of digital cash: Chaum, Szabo, Finney
- Satoshi Nakamoto and the Bitcoin whitepaper (2008)
- Core properties: decentralization, transparency, immutability
- Use cases beyond cryptocurrency

**Key Concepts:** Decentralization, trustless systems, peer-to-peer networks, digital scarcity

**Preparation:** Read Bitcoin whitepaper abstract and introduction (2 pages)

---

### Lesson 2: Blocks, Chains, and Immutability
**Duration:** 45 minutes

**Description:**
This lesson examines the fundamental data structure of blockchain: how individual blocks are constructed and linked together to form an immutable chain. Students will learn about block headers (containing metadata, timestamps, and hash pointers) and block bodies (containing transactions). The lesson demonstrates why altering any historical block requires recomputing all subsequent blocks, making tampering computationally impractical.

**Topics Covered:**
- Block structure: header vs. body
- Hash pointers and chain linking
- Genesis block and block height
- Why immutability matters for trust
- Fork types: soft forks vs. hard forks

**Key Concepts:** Block header, previous hash, chain linking, computational immutability, forks

**Activity:** Visual blockchain building exercise using paper blocks

---

### Lesson 3: Hash Functions: Properties and Applications
**Duration:** 45 minutes

**Description:**
Hash functions are the cryptographic building blocks of blockchain technology. This lesson explores SHA-256 and other cryptographic hash functions, demonstrating their essential properties: deterministic output, avalanche effect, one-way computation, and collision resistance. Students will understand how these properties enable blockchain security, from linking blocks to mining puzzles.

**Topics Covered:**
- What is a hash function?
- SHA-256: the Bitcoin hash function
- Properties: deterministic, one-way, avalanche effect
- Collision resistance and birthday attacks
- Applications: block linking, mining, commitments

**Key Concepts:** Cryptographic hash, SHA-256, avalanche effect, preimage resistance, collision resistance

**Activity:** Online hash calculator experiments - observe avalanche effect

---

### Lesson 4: Public Key Cryptography Basics
**Duration:** 45 minutes

**Description:**
Public key cryptography enables secure communication and authentication without shared secrets. This lesson introduces asymmetric encryption concepts: key pairs (public/private), the mathematical relationship between keys, and the security assumptions underlying modern cryptographic systems. Students will understand how public key cryptography enables blockchain addresses and transaction authorization.

**Topics Covered:**
- Symmetric vs. asymmetric encryption
- Key pairs: public key and private key
- Elliptic Curve Cryptography (ECC) overview
- From private key to public key to address
- Security: why private keys must stay secret

**Key Concepts:** Key pair, asymmetric encryption, elliptic curves, ECDSA, key derivation

**Analogy:** Mailbox (public key = address anyone can send to, private key = only you can open)

---

### Lesson 5: Digital Signatures and Wallet Addresses
**Duration:** 45 minutes

**Description:**
Digital signatures prove ownership and authorize transactions without revealing private keys. This lesson explains how signing works mathematically, why signatures are unforgeable, and how verification works. Students will understand the connection between private keys, public keys, and wallet addresses, and why "not your keys, not your crypto" is the fundamental principle of self-custody.

**Topics Covered:**
- What is a digital signature?
- Signing process: private key + message = signature
- Verification process: public key + message + signature = valid/invalid
- Address derivation: hashing public keys
- Wallet types: hot, cold, hardware, custodial

**Key Concepts:** Digital signature, ECDSA, signature verification, wallet address, self-custody

**Activity:** Generate key pairs and sign/verify messages using online tools

---

### Lesson 6: Merkle Trees and Data Verification
**Duration:** 45 minutes

**Description:**
Merkle trees enable efficient verification of large data sets using minimal information. This lesson explains how transactions in a block are organized into a Merkle tree structure, producing a single root hash that summarizes all transactions. Students will understand how light clients can verify transaction inclusion without downloading entire blocks, enabling blockchain scalability.

**Topics Covered:**
- Tree data structures review
- Merkle tree construction from transactions
- Merkle root: summarizing all transactions
- Merkle proofs: efficient verification
- Light clients and SPV (Simplified Payment Verification)

**Key Concepts:** Merkle tree, Merkle root, Merkle proof, light client, SPV

**Preparation:** Read Mastering Ethereum Chapter 1 (Introduction)

---

### Module 1 Resources

| Resource | Type | Required |
|----------|------|----------|
| Bitcoin Whitepaper | Reading | Yes |
| 3Blue1Brown: "How Bitcoin Works" | Video (26 min) | Yes |
| Mastering Ethereum Ch. 1 | Reading | Yes |
| Anders Brownworth Blockchain Demo | Interactive | Recommended |

**Quiz 1:** Due after Lesson 6 (covers Lessons 1-6)

---

## MODULE 2: Consensus Mechanisms (Lessons 7-12)

**Module Learning Objectives:**
- Understand why consensus is necessary in distributed systems
- Compare Proof of Work and Proof of Stake mechanisms
- Analyze the economic incentives that secure blockchain networks

---

### Lesson 7: The Double-Spending Problem
**Duration:** 45 minutes

**Description:**
The double-spending problem is the fundamental challenge that blockchain technology solves. This lesson explains why digital money, unlike physical cash, can potentially be copied and spent multiple times. Students will understand why previous digital cash systems required trusted third parties and how Bitcoin's innovation was solving this problem in a decentralized manner.

**Topics Covered:**
- Why digital goods can be copied
- The double-spending problem explained
- Traditional solution: trusted intermediaries (banks)
- Bitcoin's innovation: decentralized consensus
- Transaction ordering and conflict resolution

**Key Concepts:** Double-spending, transaction ordering, race condition, confirmation

**Case Study:** Early digital cash failures (DigiCash, e-gold)

---

### Lesson 8: Byzantine Generals Problem
**Duration:** 45 minutes

**Description:**
The Byzantine Generals Problem is a classic distributed systems challenge that illustrates the difficulty of achieving consensus among unreliable participants. This lesson uses the military analogy to explain how nodes in a blockchain network must agree on the state of the ledger despite potentially malicious actors. Students will understand the theoretical foundations underlying consensus mechanisms.

**Topics Covered:**
- The Byzantine Generals thought experiment
- Byzantine Fault Tolerance (BFT)
- Honest vs. malicious nodes
- Threshold requirements for consensus
- Practical BFT and blockchain consensus

**Key Concepts:** Byzantine fault, fault tolerance, consensus threshold, honest majority

**Activity:** Classroom role-play of Byzantine Generals scenario

---

### Lesson 9: Proof of Work: Mining Explained
**Duration:** 45 minutes

**Description:**
Proof of Work (PoW) is Bitcoin's groundbreaking consensus mechanism. This lesson explains how miners compete to find valid block hashes by iterating through nonce values, creating a computational lottery that secures the network. Students will understand the mining puzzle, difficulty targeting, and why PoW makes attacks economically infeasible.

**Topics Covered:**
- The mining puzzle: finding valid hashes
- Nonce iteration and computational work
- Difficulty target and leading zeros
- Block reward: coinbase transaction
- Mining pools: combining computational power

**Key Concepts:** Mining, nonce, difficulty target, block reward, mining pool

**Activity:** Dice-rolling mining simulation to demonstrate probability

---

### Lesson 10: PoW Economics: Difficulty & Rewards
**Duration:** 45 minutes

**Description:**
Mining economics determines the security budget of Proof of Work blockchains. This lesson analyzes the relationship between hash rate, difficulty, and profitability. Students will understand difficulty adjustment algorithms, the halving mechanism, and ongoing debates about long-term security funding as block rewards diminish.

**Topics Covered:**
- Difficulty adjustment: maintaining 10-minute blocks
- Hash rate and network security
- Mining profitability: revenue vs. costs
- Halving events and supply schedule
- Energy consumption debate

**Key Concepts:** Difficulty adjustment, hash rate, halving, mining economics, energy consumption

**Data Analysis:** Bitcoin difficulty and hash rate charts over time

---

### Lesson 11: Proof of Stake: Validators & Staking
**Duration:** 45 minutes

**Description:**
Proof of Stake (PoS) offers an alternative consensus mechanism based on economic stake rather than computational work. This lesson explains how validators are selected based on staked tokens, how blocks are proposed and attested, and how PoS achieves security through economic incentives rather than energy expenditure.

**Topics Covered:**
- PoS vs. PoW: fundamental differences
- Staking: locking tokens as collateral
- Validator selection: random weighted by stake
- Block proposal and attestation
- Finality: when transactions become irreversible

**Key Concepts:** Staking, validator, attestation, finality, nothing-at-stake problem

**Case Study:** Ethereum's transition from PoW to PoS (The Merge, 2022)

---

### Lesson 12: PoS Economics: Slashing & Rewards
**Duration:** 45 minutes

**Description:**
The economic design of PoS systems determines their security properties. This lesson examines staking yields, slashing conditions, and the game theory that incentivizes honest validator behavior. Students will understand how PoS achieves security parity with PoW through different economic mechanisms.

**Topics Covered:**
- Staking rewards: inflation vs. fees
- Slashing conditions: double-signing, inactivity
- Minimum stake requirements
- Liquid staking and delegation
- Comparing PoW vs. PoS security models

**Key Concepts:** Slashing, staking yield, liquid staking, delegation, economic security

**Analysis:** Compare validator economics across PoS chains (Ethereum, Cardano, Solana)

---

### Module 2 Resources

| Resource | Type | Required |
|----------|------|----------|
| Ethereum.org: Proof of Stake | Reading | Yes |
| "The Merge" documentation | Reading | Yes |
| beaconcha.in validator explorer | Interactive | Recommended |
| Cambridge Bitcoin Energy Index | Data | Recommended |

**Quiz 2:** Due after Lesson 12 (covers Lessons 7-12)

**Practical Assignment 1:** Create wallet, execute testnet transaction (due after Module 2)

---

## MODULE 3: Bitcoin (Lessons 13-18)

**Module Learning Objectives:**
- Understand Bitcoin's technical architecture and transaction model
- Analyze Bitcoin's monetary policy and economic properties
- Evaluate Bitcoin scaling solutions and limitations

---

### Lesson 13: Bitcoin Network Architecture
**Duration:** 45 minutes

**Description:**
Bitcoin operates as a peer-to-peer network of nodes with different roles and responsibilities. This lesson examines the network topology, node types (full nodes, mining nodes, SPV clients), and how transactions and blocks propagate across the network. Students will understand the decentralized infrastructure that maintains the Bitcoin blockchain.

**Topics Covered:**
- Peer-to-peer network topology
- Node types: full, mining, SPV
- Transaction propagation and mempool
- Block propagation and orphan blocks
- Network discovery and bootstrapping

**Key Concepts:** Full node, mempool, block propagation, peer discovery, network topology

---

### Lesson 14: UTXO Model Explained
**Duration:** 45 minutes

**Description:**
Bitcoin uses the Unspent Transaction Output (UTXO) model rather than account balances. This lesson explains how UTXOs work as discrete units of value, how transactions consume and create UTXOs, and why this model provides privacy and parallelization benefits. Students will learn to trace Bitcoin transactions through the UTXO graph.

**Topics Covered:**
- UTXO vs. account model
- Transaction inputs and outputs
- Change addresses and UTXO splitting
- Coin selection algorithms
- Privacy implications of UTXO model

**Key Concepts:** UTXO, transaction input, transaction output, change address, coin selection

**Activity:** Trace real Bitcoin transactions on blockchain explorer

---

### Lesson 15: Transaction Lifecycle
**Duration:** 45 minutes

**Description:**
A Bitcoin transaction goes through multiple stages from creation to final confirmation. This lesson follows a transaction's journey: construction, signing, broadcasting, mempool waiting, block inclusion, and confirmation accumulation. Students will understand transaction fees, confirmation reliability, and when to consider a transaction "final."

**Topics Covered:**
- Transaction construction and signing
- Broadcasting to the network
- Mempool: waiting for confirmation
- Fee market and fee estimation
- Confirmation depth and finality

**Key Concepts:** Transaction fee, mempool, confirmation, fee rate (sat/vB), replace-by-fee (RBF)

**Data Analysis:** Mempool visualization (mempool.space)

---

### Lesson 16: Bitcoin Scripting Basics
**Duration:** 45 minutes

**Description:**
Bitcoin transactions include programmable locking and unlocking scripts. This lesson introduces Bitcoin Script: a stack-based, intentionally limited scripting language. Students will understand standard transaction types (P2PKH, P2SH, P2WPKH) and how scripts enable features like multi-signature wallets and time-locked transactions.

**Topics Covered:**
- Bitcoin Script: stack-based language
- Locking scripts (scriptPubKey)
- Unlocking scripts (scriptSig)
- Standard transaction types
- Multi-signature and time-locks

**Key Concepts:** Bitcoin Script, scriptPubKey, scriptSig, P2PKH, multi-sig

---

### Lesson 17: Scaling: Lightning Network
**Duration:** 45 minutes

**Description:**
The Lightning Network is Bitcoin's primary Layer 2 scaling solution. This lesson explains payment channels, how they enable instant, low-fee transactions off-chain, and how channels can be linked to route payments across the network. Students will understand the trade-offs between on-chain security and off-chain scalability.

**Topics Covered:**
- Bitcoin's scalability limitations
- Payment channels: off-chain transactions
- Channel opening and closing
- Multi-hop payments and routing
- Lightning Network adoption and challenges

**Key Concepts:** Layer 2, payment channel, routing, liquidity, channel capacity

**Demo:** Lightning Network node visualization

---

### Lesson 18: Bitcoin Economics & Halving
**Duration:** 45 minutes

**Description:**
Bitcoin's fixed supply and predictable issuance schedule create unique monetary properties. This lesson analyzes Bitcoin's economics: the 21 million cap, halving schedule, stock-to-flow model, and the transition from block rewards to fee-based security. Students will evaluate Bitcoin's "digital gold" thesis and long-term sustainability.

**Topics Covered:**
- Fixed supply: 21 million BTC
- Halving schedule and issuance curve
- Stock-to-flow model
- Security budget: rewards vs. fees
- Bitcoin as "digital gold"

**Key Concepts:** Halving, fixed supply, deflation, stock-to-flow, security budget

**Data Analysis:** Bitcoin supply schedule and halving impact on price

---

### Module 3 Resources

| Resource | Type | Required |
|----------|------|----------|
| Mastering Bitcoin Ch. 6-7 | Reading | Recommended |
| blockchain.com explorer | Interactive | Yes |
| mempool.space | Interactive | Yes |
| Lightning Network whitepaper | Reading | Recommended |

**Quiz 3:** Due after Lesson 18 (covers Lessons 13-18)

---

## MODULE 4: Ethereum & Smart Contracts (Lessons 19-24)

**Module Learning Objectives:**
- Understand Ethereum's architecture and differences from Bitcoin
- Write and deploy basic smart contracts using Solidity
- Analyze gas economics and transaction execution

---

### Lesson 19: Ethereum vs Bitcoin: Key Differences
**Duration:** 45 minutes

**Description:**
Ethereum extended blockchain technology beyond simple value transfer to programmable smart contracts. This lesson compares Ethereum and Bitcoin architecturally: account model vs. UTXO, Turing-complete scripting vs. limited scripting, and general-purpose vs. specialized use cases. Students will understand why Ethereum became the foundation for DeFi and NFTs.

**Topics Covered:**
- Bitcoin's limitations for complex applications
- Vitalik Buterin and Ethereum's vision
- Account model vs. UTXO model
- Turing-complete smart contracts
- Ethereum's evolution: PoW to PoS

**Key Concepts:** Smart contract, account model, Turing completeness, world computer

---

### Lesson 20: Ethereum Virtual Machine (EVM)
**Duration:** 45 minutes

**Description:**
The Ethereum Virtual Machine (EVM) is the runtime environment for smart contracts. This lesson explains how the EVM executes bytecode, manages state, and ensures deterministic computation across all nodes. Students will understand the EVM's stack-based architecture, memory model, and storage system.

**Topics Covered:**
- What is a virtual machine?
- EVM architecture: stack, memory, storage
- Bytecode execution
- Determinism: same input = same output
- EVM compatibility and alternative chains

**Key Concepts:** EVM, bytecode, stack machine, state, determinism

---

### Lesson 21: Gas Mechanics & EIP-1559
**Duration:** 45 minutes

**Description:**
Gas is Ethereum's mechanism for metering computation and preventing abuse. This lesson explains gas costs, gas limits, and the EIP-1559 fee market reform. Students will understand how to estimate transaction costs, why gas prices fluctuate, and the relationship between network congestion and fees.

**Topics Covered:**
- Why gas exists: preventing infinite loops
- Gas costs for different operations
- Gas limit and out-of-gas errors
- EIP-1559: base fee and priority fee
- Gas optimization techniques

**Key Concepts:** Gas, gas limit, base fee, priority fee, gas estimation

**Activity:** Analyze gas costs of different transactions on Etherscan

---

### Lesson 22: Smart Contracts: Concept & Use Cases
**Duration:** 45 minutes

**Description:**
Smart contracts are self-executing programs that run on the blockchain. This lesson explores what smart contracts can and cannot do, their key properties (trustless, transparent, immutable), and major use cases across DeFi, NFTs, DAOs, and gaming. Students will understand both the potential and limitations of smart contract technology.

**Topics Covered:**
- Nick Szabo and smart contract origins
- Properties: trustless, transparent, immutable
- Use cases: DeFi, NFTs, DAOs, gaming
- Limitations: oracle problem, immutability risks
- Upgradability patterns

**Key Concepts:** Smart contract, trustless execution, oracle problem, immutability

**Case Studies:** Uniswap, Aave, CryptoKitties

---

### Lesson 23: Solidity Basics: Data Types & Functions
**Duration:** 45 minutes

**Description:**
Solidity is the primary programming language for Ethereum smart contracts. This lesson introduces Solidity syntax, data types (uint, address, mapping), visibility modifiers, and function declarations. Students will write their first smart contract code, understanding the differences between Solidity and other programming languages.

**Topics Covered:**
- Solidity syntax overview
- Data types: uint, address, bool, string, mapping
- Variables: state vs. local vs. memory
- Functions: visibility (public, private, internal, external)
- View and pure functions

**Key Concepts:** Solidity, data types, visibility modifier, state variable, view function

**Code Example:** Simple storage contract

---

### Lesson 24: Deploying Your First Contract
**Duration:** 45 minutes

**Description:**
This hands-on lesson guides students through deploying their first smart contract using Remix IDE. Students will compile Solidity code, connect MetaMask to the Sepolia testnet, deploy the contract, and interact with it through both Remix and Etherscan. This lesson synthesizes all Module 4 concepts into practical experience.

**Topics Covered:**
- Remix IDE orientation
- Compilation and bytecode generation
- Connecting MetaMask to Remix
- Deployment to Sepolia testnet
- Contract verification on Etherscan

**Key Concepts:** Compilation, deployment, contract address, verification

**Activity:** Deploy "HelloWorld" storage contract to Sepolia

---

### Module 4 Resources

| Resource | Type | Required |
|----------|------|----------|
| Mastering Ethereum Ch. 2-4 | Reading | Yes |
| Solidity Documentation | Reference | Yes |
| Remix IDE | Tool | Yes |
| CryptoZombies Lessons 1-3 | Interactive | Recommended |

**Quiz 4:** Due after Lesson 24 (covers Lessons 19-24)

**Practical Assignment 2:** Deploy smart contract to testnet (due after Module 4)

**MID-COURSE EXAM:** After Lesson 24 (covers Modules 1-4)

---

## MODULE 5: Tokens & Tokenomics (Lessons 25-30)

**Module Learning Objectives:**
- Understand token standards and their implementation
- Create ERC-20 and ERC-721 tokens
- Analyze tokenomics and token valuation frameworks

---

### Lesson 25: Token Standards: ERC-20
**Duration:** 45 minutes

**Description:**
ERC-20 is the most widely adopted token standard on Ethereum. This lesson examines the ERC-20 interface: required functions (totalSupply, balanceOf, transfer, approve, allowance, transferFrom), events, and how this standardization enabled the explosion of token-based applications. Students will understand why standards matter for ecosystem interoperability.

**Topics Covered:**
- What is a token standard?
- ERC-20 interface specification
- Required functions and events
- Decimal handling (18 decimals standard)
- Token compatibility and wallets

**Key Concepts:** ERC-20, token standard, interface, decimals, events

**Analysis:** Examine USDC, WETH contracts on Etherscan

---

### Lesson 26: Creating an ERC-20 Token
**Duration:** 45 minutes

**Description:**
This practical lesson guides students through creating their own ERC-20 token using OpenZeppelin libraries. Students will write a token contract with custom name, symbol, and initial supply, deploy it to testnet, and add the token to their MetaMask wallet. This demonstrates the accessibility of token creation.

**Topics Covered:**
- OpenZeppelin Contracts library
- Inheriting from ERC-20
- Constructor parameters: name, symbol, supply
- Minting and initial distribution
- Adding custom token to MetaMask

**Key Concepts:** OpenZeppelin, inheritance, minting, token deployment

**Activity:** Create and deploy custom ERC-20 token to Sepolia

---

### Lesson 27: NFTs: ERC-721 & ERC-1155
**Duration:** 45 minutes

**Description:**
Non-fungible tokens (NFTs) represent unique digital assets using the ERC-721 standard. This lesson explains the difference between fungible (ERC-20) and non-fungible (ERC-721) tokens, examines the ERC-721 interface, and introduces ERC-1155 (multi-token standard). Students will understand NFT use cases beyond digital art.

**Topics Covered:**
- Fungible vs. non-fungible tokens
- ERC-721 interface and functions
- Token URI and metadata standards
- ERC-1155: multi-token efficiency
- NFT use cases: art, gaming, identity, tickets

**Key Concepts:** NFT, ERC-721, ERC-1155, tokenURI, metadata

**Case Studies:** Bored Apes, CryptoPunks, ENS domains

---

### Lesson 28: Tokenomics: Supply & Distribution
**Duration:** 45 minutes

**Description:**
Tokenomics is the economic design of token systems. This lesson analyzes supply dynamics (fixed, inflationary, deflationary), distribution mechanisms (fair launch, ICO, airdrop), and vesting schedules. Students will learn to evaluate whether a token's economic design aligns with its stated goals.

**Topics Covered:**
- Token supply: fixed vs. inflationary vs. deflationary
- Distribution methods: ICO, IEO, airdrop, fair launch
- Vesting and lock-up periods
- Token burns and buybacks
- Circulating vs. total vs. max supply

**Key Concepts:** Tokenomics, supply schedule, vesting, burn mechanism, distribution

**Analysis:** Compare tokenomics of BTC, ETH, UNI, MKR

---

### Lesson 29: Token Valuation Frameworks
**Duration:** 45 minutes

**Description:**
How do you value a token? This lesson introduces frameworks for token valuation: network value metrics (NVT ratio), discounted cash flow for fee-generating tokens, comparable analysis, and qualitative assessment. Students will understand the challenges of crypto valuation and common analytical approaches.

**Topics Covered:**
- Traditional valuation vs. crypto valuation
- Network Value to Transactions (NVT) ratio
- Fee-generating protocol valuation
- Comparable analysis across protocols
- Red flags and due diligence

**Key Concepts:** Valuation, NVT, fee revenue, market cap, fully diluted valuation

**Framework:** Token evaluation checklist

---

### Lesson 30: Case Study: Token Launch Analysis
**Duration:** 45 minutes

**Description:**
This lesson applies tokenomics concepts to analyze real token launches: successful examples and cautionary tales. Students will examine initial distributions, vesting unlocks, price dynamics, and governance transitions. The goal is developing critical analysis skills for evaluating new token projects.

**Topics Covered:**
- Successful launch analysis: UNI airdrop
- Failed launch analysis: Various ICO failures
- Analyzing token distribution charts
- Identifying red flags
- Due diligence checklist

**Key Concepts:** Token launch, airdrop, ICO failure, due diligence

**Activity:** Group analysis of a recent token launch

---

### Module 5 Resources

| Resource | Type | Required |
|----------|------|----------|
| OpenZeppelin ERC-20 docs | Reference | Yes |
| "How to DeFi" Ch. on Tokens | Reading | Yes |
| CoinGecko token pages | Data | Recommended |
| Token Terminal | Data | Recommended |

**Quiz 5:** Due after Lesson 30 (covers Lessons 25-30)

---

## MODULE 6: Decentralized Finance - DeFi (Lessons 31-38)

**Module Learning Objectives:**
- Understand DeFi protocols and their mechanisms
- Interact with DEXs and lending protocols on testnets
- Analyze DeFi risks and historical failures

---

### Lesson 31: What is DeFi? CeFi vs DeFi
**Duration:** 45 minutes

**Description:**
Decentralized Finance (DeFi) recreates traditional financial services using smart contracts. This lesson compares centralized finance (CeFi) with decentralized alternatives, examining the advantages (permissionless, transparent, composable) and disadvantages (complexity, risks, limited customer protection) of DeFi. Students will understand the DeFi vision and its current state.

**Topics Covered:**
- Traditional finance infrastructure
- Centralized exchanges and custodians
- DeFi principles: permissionless, non-custodial, composable
- DeFi primitives overview
- TVL and DeFi metrics

**Key Concepts:** DeFi, CeFi, TVL, permissionless, composability

**Data:** DeFi Llama TVL charts and protocol breakdown

---

### Lesson 32: AMMs: Constant Product Formula
**Duration:** 45 minutes

**Description:**
Automated Market Makers (AMMs) revolutionized decentralized trading. This lesson explains the constant product formula (x * y = k), how liquidity pools replace order books, and the mathematical mechanics of token swaps. Students will calculate swap outputs and understand price impact.

**Topics Covered:**
- Order books vs. liquidity pools
- Constant product formula: x * y = k
- Price determination in AMMs
- Swap mechanics and price impact
- Slippage tolerance

**Key Concepts:** AMM, liquidity pool, constant product, price impact, slippage

**Math Exercise:** Calculate swap outputs and price impact

---

### Lesson 33: Uniswap Deep Dive
**Duration:** 45 minutes

**Description:**
Uniswap is the leading decentralized exchange and the reference implementation for AMMs. This lesson examines Uniswap's evolution (V1, V2, V3), concentrated liquidity, and governance. Students will understand how Uniswap contracts work and the protocol's impact on DeFi.

**Topics Covered:**
- Uniswap V1: proof of concept
- Uniswap V2: ERC-20 pairs, flash swaps
- Uniswap V3: concentrated liquidity
- UNI token and governance
- Uniswap's role in DeFi ecosystem

**Key Concepts:** Uniswap, concentrated liquidity, LP position, governance

**Activity:** Analyze Uniswap contracts on Etherscan

---

### Lesson 34: Liquidity & Impermanent Loss
**Duration:** 45 minutes

**Description:**
Liquidity providers (LPs) earn fees but face impermanent loss risk. This lesson explains what impermanent loss is, when it occurs, how to calculate it, and strategies for managing LP risk. Students will understand the trade-offs of providing liquidity to AMM pools.

**Topics Covered:**
- Liquidity provision: depositing to pools
- LP tokens and pool shares
- Impermanent loss: definition and causes
- Calculating impermanent loss
- Strategies for LP risk management

**Key Concepts:** Liquidity provider, LP token, impermanent loss, fee APY

**Calculator:** Impermanent loss calculator exercise

---

### Lesson 35: Lending Protocols: Aave & Compound
**Duration:** 45 minutes

**Description:**
DeFi lending protocols enable permissionless borrowing and lending. This lesson examines Aave and Compound: how supply/borrow rates are determined algorithmically, how collateralization works, and how protocols earn revenue. Students will understand the mechanics of DeFi lending markets.

**Topics Covered:**
- Traditional lending vs. DeFi lending
- Supply and borrow mechanics
- Interest rate models
- Utilization rate and rate curves
- Governance and protocol revenue

**Key Concepts:** Lending protocol, supply APY, borrow APY, utilization rate

**Analysis:** Compare Aave and Compound rate models

---

### Lesson 36: Collateralization & Liquidation
**Duration:** 45 minutes

**Description:**
DeFi loans require overcollateralization to manage risk. This lesson explains collateral factors, health factors, liquidation mechanics, and the role of liquidators. Students will understand how DeFi protocols maintain solvency and the risks borrowers face.

**Topics Covered:**
- Overcollateralization requirement
- Loan-to-Value (LTV) ratios
- Health factor and liquidation threshold
- Liquidation mechanics and incentives
- Flash liquidations

**Key Concepts:** Collateral factor, health factor, liquidation, LTV, overcollateralization

**Simulation:** Calculate liquidation prices for various positions

---

### Lesson 37: Stablecoins: Types & Mechanisms
**Duration:** 45 minutes

**Description:**
Stablecoins maintain price stability relative to fiat currencies, enabling DeFi to function. This lesson categorizes stablecoins by mechanism: fiat-backed (USDC, USDT), crypto-collateralized (DAI), and algorithmic (UST). Students will understand the trade-offs between decentralization, capital efficiency, and stability.

**Topics Covered:**
- Why stablecoins matter for DeFi
- Fiat-backed: USDC, USDT
- Crypto-collateralized: DAI, MakerDAO
- Algorithmic: UST, FRAX
- Regulatory considerations

**Key Concepts:** Stablecoin, fiat-backed, crypto-collateralized, algorithmic, peg

**Comparison:** Stablecoin trilemma analysis

---

### Lesson 38: Case Study: Terra/Luna Collapse
**Duration:** 45 minutes

**Description:**
The Terra/Luna collapse in May 2022 was the largest DeFi failure, destroying over $40 billion. This lesson analyzes the algorithmic stablecoin mechanism, why the death spiral occurred, the contagion effects, and lessons for DeFi design. Students will understand the risks of under-collateralized systems.

**Topics Covered:**
- Terra/Luna ecosystem overview
- UST algorithmic mechanism
- The de-peg and death spiral
- Anchor Protocol and unsustainable yields
- Contagion: 3AC, Celsius, FTX

**Key Concepts:** Death spiral, de-peg, reflexivity, contagion

**Lesson:** Why "too good to be true" yields are dangerous

---

### Module 6 Resources

| Resource | Type | Required |
|----------|------|----------|
| "How to DeFi" (CoinGecko) | Reading | Yes |
| DeFi Llama | Data | Yes |
| Finematics YouTube channel | Video | Recommended |
| Uniswap documentation | Reference | Recommended |

**Quiz 6:** Due after Lesson 38 (covers Lessons 31-38)

**Practical Assignment 3:** DeFi interaction (swap, liquidity) on testnet (due after Module 6)

---

## MODULE 7: Security (Lessons 39-44)

**Module Learning Objectives:**
- Identify common smart contract vulnerabilities
- Apply security best practices in contract development
- Analyze real-world exploit case studies

---

### Lesson 39: Smart Contract Security Principles
**Duration:** 45 minutes

**Description:**
Smart contract bugs can result in irreversible financial losses. This lesson introduces security principles: defense in depth, fail-safe defaults, the principle of least privilege, and the Checks-Effects-Interactions pattern. Students will understand why security is not optional and how to think adversarially.

**Topics Covered:**
- Why smart contract security matters
- Security mindset: think like an attacker
- Defense in depth
- Checks-Effects-Interactions (CEI) pattern
- Security development lifecycle

**Key Concepts:** Security principles, CEI pattern, adversarial thinking, defense in depth

---

### Lesson 40: Reentrancy Attacks (The DAO)
**Duration:** 45 minutes

**Description:**
Reentrancy is the most famous smart contract vulnerability, responsible for The DAO hack in 2016. This lesson explains how reentrancy works, demonstrates the attack vector, and shows how to prevent it using the CEI pattern and reentrancy guards. Students will implement both vulnerable and secure code.

**Topics Covered:**
- The DAO: history and vision
- Reentrancy vulnerability explained
- The DAO hack: step-by-step
- Prevention: CEI pattern
- ReentrancyGuard modifier

**Key Concepts:** Reentrancy, external call, CEI pattern, ReentrancyGuard

**Code Exercise:** Identify and fix reentrancy vulnerability

---

### Lesson 41: Access Control Vulnerabilities
**Duration:** 45 minutes

**Description:**
Access control vulnerabilities allow unauthorized users to execute restricted functions. This lesson examines common patterns: missing modifiers, incorrect visibility, centralization risks, and privilege escalation. Students will learn to implement proper access control using OpenZeppelin's Ownable and AccessControl.

**Topics Covered:**
- Access control patterns
- Ownable: single administrator
- AccessControl: role-based permissions
- Common mistakes: missing modifiers
- Centralization vs. decentralization trade-offs

**Key Concepts:** Access control, Ownable, role-based access, modifier, visibility

**Code Exercise:** Implement role-based access control

---

### Lesson 42: Integer Overflow & Other Bugs
**Duration:** 45 minutes

**Description:**
This lesson covers additional common vulnerabilities: integer overflow/underflow (mitigated in Solidity 0.8+), front-running, oracle manipulation, and denial of service. Students will understand the variety of attack vectors and how to defend against them.

**Topics Covered:**
- Integer overflow and underflow
- Solidity 0.8+ built-in protection
- Front-running and MEV
- Oracle manipulation attacks
- Denial of service vectors

**Key Concepts:** Integer overflow, front-running, MEV, oracle manipulation, DoS

---

### Lesson 43: Security Tools: Slither & Audits
**Duration:** 45 minutes

**Description:**
Security tools and audits help identify vulnerabilities before deployment. This lesson introduces static analysis tools (Slither, Mythril), symbolic execution, formal verification, and the professional audit process. Students will run Slither on sample contracts and interpret results.

**Topics Covered:**
- Static analysis: Slither
- Symbolic execution: Mythril
- Formal verification overview
- Professional security audits
- Bug bounty programs

**Key Concepts:** Static analysis, Slither, audit, bug bounty, formal verification

**Activity:** Run Slither on vulnerable contracts

---

### Lesson 44: Case Study: Major DeFi Hacks
**Duration:** 45 minutes

**Description:**
Learning from past exploits is essential for security awareness. This lesson analyzes major DeFi hacks: Ronin Bridge ($625M), Wormhole ($320M), Nomad Bridge ($190M), and others. Students will understand attack patterns, post-mortem analysis, and how the industry responds to security incidents.

**Topics Covered:**
- Ronin Bridge hack analysis
- Wormhole hack analysis
- Flash loan attacks
- Bridge vulnerabilities
- Industry response and insurance

**Key Concepts:** Post-mortem, bridge hack, flash loan attack, multi-sig compromise

**Analysis:** Read and discuss actual post-mortem reports

---

### Module 7 Resources

| Resource | Type | Required |
|----------|------|----------|
| SWC Registry | Reference | Yes |
| Ethernaut | Interactive | Recommended |
| Damn Vulnerable DeFi | Interactive | Recommended |
| Rekt News | Reading | Recommended |

**Quiz 7:** Due after Lesson 44 (covers Lessons 39-44)

**Practical Assignment 4:** Security vulnerability analysis (due after Module 7)

---

## MODULE 8: Advanced Topics & Future (Lessons 45-48)

**Module Learning Objectives:**
- Understand Layer 2 scaling solutions
- Analyze the regulatory landscape
- Explore career pathways in blockchain

---

### Lesson 45: Layer 2: Rollups Explained
**Duration:** 45 minutes

**Description:**
Layer 2 solutions scale blockchains by processing transactions off-chain while inheriting security from Layer 1. This lesson explains rollup technology: the difference between optimistic rollups (Arbitrum, Optimism) and ZK-rollups (zkSync, StarkNet), and how they achieve scalability without sacrificing security.

**Topics Covered:**
- Scalability trilemma
- Layer 2 approaches overview
- Optimistic rollups: fraud proofs
- ZK-rollups: validity proofs
- Comparing L2 solutions (L2Beat)

**Key Concepts:** Layer 2, rollup, fraud proof, validity proof, data availability

**Data:** L2Beat metrics and comparison

---

### Lesson 46: Cross-Chain & Bridges
**Duration:** 45 minutes

**Description:**
Blockchain interoperability requires bridges to transfer assets across chains. This lesson examines bridge architectures (lock-and-mint, burn-and-mint), trust assumptions, and security considerations. Students will understand why bridges are high-value targets and the trade-offs between different bridge designs.

**Topics Covered:**
- Why cross-chain interoperability matters
- Bridge mechanisms: lock-and-mint
- Trust assumptions and security models
- Bridge hacks and vulnerabilities
- Future: native interoperability

**Key Concepts:** Bridge, cross-chain, interoperability, lock-and-mint, trust assumptions

**Case Study:** Bridge hacks (Ronin, Wormhole, Nomad)

---

### Lesson 47: Regulation: MiCA, SEC, Global
**Duration:** 45 minutes

**Description:**
Regulatory frameworks are evolving rapidly across jurisdictions. This lesson examines the European MiCA regulation, US SEC and CFTC approaches, and global regulatory trends. Students will understand token classification (security vs. utility), compliance requirements, and the impact of regulation on innovation.

**Topics Covered:**
- Why regulation matters
- EU Markets in Crypto-Assets (MiCA)
- US: SEC vs. CFTC jurisdiction
- Howey Test and security classification
- Global regulatory landscape

**Key Concepts:** MiCA, SEC, Howey Test, security token, regulatory compliance

**Analysis:** Classify tokens under different frameworks

---

### Lesson 48: Future Trends & Career Paths
**Duration:** 45 minutes

**Description:**
The final lesson looks forward: emerging trends (account abstraction, intents, AI+blockchain) and career pathways in the blockchain industry. Students will understand how to continue learning, contribute to the ecosystem, and build careers in this rapidly evolving field.

**Topics Covered:**
- Emerging trends: account abstraction, intents
- Real-world assets (RWA) tokenization
- AI and blockchain convergence
- Career paths: technical and non-technical
- Building a portfolio and networking

**Key Concepts:** Account abstraction, intents, RWA, career development

**Resources:** Hackathons, communities, continued learning paths

---

### Module 8 Resources

| Resource | Type | Required |
|----------|------|----------|
| L2Beat | Data | Yes |
| MiCA regulation summary | Reading | Recommended |
| Developer DAO | Community | Recommended |
| ETHGlobal hackathons | Events | Recommended |

**Quiz 8:** Due after Lesson 48 (covers Lessons 45-48)

---

# PART III: ASSESSMENTS

## Module Quizzes (20% Total)

- 8 quizzes, one after each module
- 10 multiple choice/short answer questions per quiz
- 15-minute time limit
- Best 7 of 8 count toward final grade
- Available on LMS for one week after module completion

### Sample Quiz Questions

**Module 1 (Blockchain Foundations):**
1. What property of hash functions ensures that changing one character in the input completely changes the output?
2. Explain in 2-3 sentences why blockchain immutability depends on computational cost.

**Module 4 (Ethereum):**
1. What happens when a transaction runs out of gas during execution?
2. What is the difference between a "view" function and a regular function in Solidity?

**Module 6 (DeFi):**
1. In an AMM with reserves of 100 ETH and 200,000 USDC, what is the current price of ETH?
2. Explain why impermanent loss is called "impermanent."

---

## Mid-Course Exam (20%)

**Timing:** After Lesson 24 (after Module 4)
**Duration:** 90 minutes
**Format:** Written exam (closed book, cheat sheet allowed)

### Exam Structure

| Section | Points | Description |
|---------|--------|-------------|
| Multiple Choice | 30 | 15 questions x 2 points |
| Short Answer | 40 | 4 questions x 10 points |
| Problem Solving | 30 | 2 problems x 15 points |

### Topics Covered
- Module 1: Blockchain fundamentals, cryptography
- Module 2: Consensus mechanisms (PoW, PoS)
- Module 3: Bitcoin architecture, UTXO model
- Module 4: Ethereum, EVM, Solidity basics

### Sample Exam Questions

**Multiple Choice:**
"Which of the following is NOT a property of cryptographic hash functions?"
a) Deterministic output
b) Reversible computation
c) Collision resistance
d) Avalanche effect

**Short Answer:**
"Explain the difference between Proof of Work and Proof of Stake in terms of how validators are selected and what economic resources are at risk."

**Problem Solving:**
"Given a Solidity contract that stores user balances, identify the security vulnerability and write the corrected code."

---

## Practical Assignments (25% Total)

### Practical 1: Wallet Setup & Transaction (After Module 2)
**Weight:** 6%
**Due:** 1 week after Lesson 12

**Tasks:**
1. Install MetaMask and create a new wallet
2. Connect to Sepolia testnet
3. Obtain testnet ETH from a faucet
4. Send a transaction to a provided address
5. Document the process with screenshots

**Deliverables:**
- Your wallet address
- Transaction hash of the sent transaction
- Screenshots of MetaMask showing balance and transaction
- Written reflection: 200 words on what you learned

**Grading Rubric:**

| Criterion | Points | Description |
|-----------|--------|-------------|
| Wallet Setup | 2 | MetaMask installed, connected to Sepolia |
| Transaction Execution | 2 | Successful transaction sent |
| Documentation | 1.5 | Clear screenshots and transaction hash |
| Reflection | 0.5 | Thoughtful reflection on learning |

---

### Practical 2: Smart Contract Deployment (After Module 4)
**Weight:** 7%
**Due:** 1 week after Lesson 24

**Tasks:**
1. Write a simple storage contract in Solidity
2. Compile and deploy to Sepolia testnet
3. Interact with the deployed contract
4. Verify the contract on Sepolia Etherscan

**Deliverables:**
- Solidity source code
- Deployed contract address
- Transaction hashes for deployment and interactions
- Link to verified contract on Etherscan
- Written explanation: 300 words on how the contract works

**Grading Rubric:**

| Criterion | Points | Description |
|-----------|--------|-------------|
| Code Quality | 2 | Correct Solidity syntax, clean code |
| Deployment | 2 | Successfully deployed to testnet |
| Interaction | 1.5 | Demonstrated read/write functions |
| Verification | 1 | Contract verified on Etherscan |
| Explanation | 0.5 | Clear technical explanation |

---

### Practical 3: DeFi Interaction (After Module 6)
**Weight:** 6%
**Due:** 1 week after Lesson 38

**Tasks:**
1. Connect wallet to Uniswap (testnet mode)
2. Execute a token swap
3. Provide liquidity to a pool (optional for bonus)
4. Document all transactions with analysis

**Deliverables:**
- Transaction hashes for all DeFi interactions
- Screenshots of Uniswap interface
- Analysis document: Explain what happened in each transaction, including gas costs and slippage
- Reflection: 300 words comparing DeFi to traditional finance

**Grading Rubric:**

| Criterion | Points | Description |
|-----------|--------|-------------|
| Swap Execution | 2 | Successfully completed swap |
| Documentation | 2 | Clear transaction records and screenshots |
| Analysis | 1.5 | Accurate explanation of mechanics |
| Reflection | 0.5 | Thoughtful CeFi vs DeFi comparison |
| Bonus: LP | +1 | Successfully provided liquidity |

---

### Practical 4: Security Analysis (After Module 7)
**Weight:** 6%
**Due:** 1 week after Lesson 44

**Tasks:**
1. Analyze a provided vulnerable contract
2. Identify at least 3 security issues
3. Explain how each vulnerability could be exploited
4. Provide fixed code for each issue

**Deliverables:**
- Security analysis report (1-2 pages)
- For each vulnerability: description, exploitation scenario, fix
- Fixed contract code with comments

**Grading Rubric:**

| Criterion | Points | Description |
|-----------|--------|-------------|
| Issue Identification | 2 | Found at least 3 vulnerabilities |
| Exploitation Analysis | 2 | Clear explanation of attack vectors |
| Code Fixes | 1.5 | Correct and secure solutions |
| Report Quality | 0.5 | Well-organized, clear writing |

---

## Final Project (35%)

**Due:** End of course
**Format:** Individual or team (2-3 members)

### Option A: Smart Contract Development (Technical Track)

**Deliverables:**
1. Deployed smart contract(s) on testnet
2. Source code with comments
3. Technical documentation (5-7 pages)
4. Test suite with at least 10 test cases
5. 10-minute video demonstration

**Project Scope Examples:**
- Voting system with delegation
- Simple NFT marketplace
- Crowdfunding platform
- Multi-signature wallet

**Grading Rubric:**

| Criterion | Points | Weight |
|-----------|--------|--------|
| Functionality | 30 | All features work correctly |
| Code Quality | 20 | Clean, well-structured, commented |
| Security | 20 | No obvious vulnerabilities |
| Testing | 15 | Comprehensive test coverage |
| Documentation | 15 | Clear technical documentation |

---

### Option B: DeFi Protocol Analysis (Analytical Track)

**Deliverables:**
1. Written report (12-15 pages)
2. On-chain data analysis with visualizations
3. Presentation slides (15 slides)
4. 10-minute presentation (live or recorded)

**Analysis Requirements:**
- Protocol mechanics and architecture
- Tokenomics analysis
- Competitive positioning
- Risk assessment
- Investment thesis (bull and bear case)

**Grading Rubric:**

| Criterion | Points | Weight |
|-----------|--------|--------|
| Technical Understanding | 25 | Deep understanding of mechanics |
| Data Analysis | 25 | Original on-chain analysis |
| Critical Evaluation | 20 | Balanced risk assessment |
| Research Quality | 15 | Proper sources and citations |
| Presentation | 15 | Clear communication |

---

### Option C: Regulatory Case Study (Policy Track)

**Deliverables:**
1. Written report (10-12 pages)
2. Regulatory analysis framework
3. Presentation to "policy makers" (10 minutes)

**Analysis Requirements:**
- Case background and timeline
- Regulatory response analysis
- Jurisdictional comparison
- Policy recommendations
- Industry impact assessment

**Grading Rubric:**

| Criterion | Points | Weight |
|-----------|--------|--------|
| Case Analysis | 25 | Comprehensive case coverage |
| Regulatory Framework | 25 | Accurate regulatory analysis |
| Communication | 20 | Accessible to non-technical audience |
| Recommendations | 15 | Actionable, specific proposals |
| Research Quality | 15 | Proper sources and citations |

---

# PART IV: COURSE POLICIES

## Attendance and Participation

- Attendance is expected but not mandatory
- Active participation enhances learning
- Discord/forum participation counts toward participation grade

## Late Submission Policy

- Practical assignments: 10% penalty per day, up to 3 days
- Quizzes: No late submissions accepted
- Final project: 5% penalty per day, up to 5 days
- Extensions granted for documented emergencies only

## Academic Integrity

### Allowed:
- Discussing concepts with classmates
- Using official documentation and tutorials
- Referencing Stack Overflow (with citation)
- Using OpenZeppelin libraries

### Not Allowed:
- Copying code from classmates
- Submitting AI-generated code without understanding
- Plagiarizing written reports
- Sharing quiz answers

### Code Attribution:
All external code must be cited with source URL and date accessed.

## Technology Requirements

- Laptop with modern web browser
- Stable internet connection
- MetaMask browser extension
- For Module 4+: Node.js (optional but recommended)

---

# PART V: INSTRUCTOR INFORMATION

## Office Hours
- By appointment
- Virtual office hours available

## Communication
- Primary: Discord server / LMS announcements
- Email: For private matters only
- Response time: Within 48 hours

## Support Resources
- Course Discord server
- Weekly Q&A sessions
- Peer tutoring (arranged through LMS)

---

# APPENDICES

## Appendix A: Glossary of Terms

| Term | Definition |
|------|------------|
| AMM | Automated Market Maker - DEX using liquidity pools |
| DeFi | Decentralized Finance - financial services on blockchain |
| ERC-20 | Ethereum token standard for fungible tokens |
| EVM | Ethereum Virtual Machine - runtime for smart contracts |
| Gas | Unit measuring computational effort on Ethereum |
| Hash | Fixed-size output from cryptographic hash function |
| LP | Liquidity Provider - deposits assets to AMM pools |
| NFT | Non-Fungible Token - unique digital asset |
| PoS | Proof of Stake - consensus based on staked tokens |
| PoW | Proof of Work - consensus based on computational work |
| Slippage | Difference between expected and actual trade price |
| TVL | Total Value Locked - assets deposited in DeFi protocols |
| UTXO | Unspent Transaction Output - Bitcoin's transaction model |

## Appendix B: Tool Installation Guides

### MetaMask Installation
1. Visit metamask.io
2. Install browser extension
3. Create new wallet
4. WRITE DOWN seed phrase on paper
5. Never share seed phrase

### Sepolia Testnet Setup
1. Open MetaMask settings
2. Enable "Show test networks"
3. Select Sepolia network
4. Get test ETH from faucet

## Appendix C: Recommended Learning Path After Course

### Technical Track:
1. CryptoZombies advanced lessons
2. Damn Vulnerable DeFi
3. Foundry/Hardhat deep dive
4. Security auditing courses

### Analytical Track:
1. Token Terminal analysis
2. Dune Analytics dashboards
3. Research reports (Messari, Delphi)
4. Governance participation

### Career Development:
1. Build GitHub portfolio
2. Participate in hackathons
3. Join Developer DAO / Bankless
4. Contribute to open source
