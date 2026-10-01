# 🛡️ BIP39 Seed Rescuer

<p align="center">
  <img src="https://img.shields.io/badge/Security-Air--Gapped%20Safe-10b981?style=for-the-badge&logo=shield" alt="Air-Gapped Safe" />
  <img src="https://img.shields.io/badge/Dependencies-Zero%20(Single%20HTML)-38bdf8?style=for-the-badge&logo=html5" alt="Zero Dependencies" />
  <img src="https://img.shields.io/badge/Multi--Threading-Web%20Workers-f59e0b?style=for-the-badge&logo=speedtest" alt="Multi-Threaded" />
  <img src="https://img.shields.io/badge/License-MIT-a855f7?style=for-the-badge" alt="MIT License" />
</p>

**BIP39 Seed Rescuer** is an ultra-fast, 100% offline, browser-based seed phrase recovery tool. If you lost 1 or 2 words from your 12 or 24-word recovery phrase, or made a typo in a word, this tool recovers your exact seed phrase and derives your wallet addresses using multi-threaded Web Workers and BIP39 checksum pruning.

**[TR]** *Kayıp veya hatalı 1-2 kelime içeren BIP39 tohum cümlenizi (seed phrase) %100 çevrimdışı, hava boşluklu (air-gapped) güvenlik protokolüyle tarayıcınızda saniyeler içinde kurtaran açık kaynaklı cüzdan kurtarma aracı.*

---

## ⚡ Highlights & Key Features

- 🔒 **100% Offline & Cold Storage Safe**: Zero network calls, zero telemetry, zero analytics, zero external CDNs. Packaged into a single self-contained `index.html` file that you can copy to an offline USB flash drive and run on an air-gapped machine.
- 🚀 **Multi-Core Parallelism (Web Workers)**: Automatically detects and utilizes all available CPU cores via parallel Web Workers for maximum derivation speed.
- 🎯 **Mathematical Checksum Pruning**: Utilizes BIP39 checksum validation bits to discard 93.75% (15 out of 16) of candidate combinations before calculating PBKDF2 hashes, resulting in up to **16x faster recovery**.
- 🔠 **Smart Typo Auto-Correction (Levenshtein Distance)**: Misspelled words (e.g. `aple` instead of `apple`, `lenght` instead of `length`) are automatically highlighted with 1-click fuzzy correction suggestions.
- 🌐 **Comprehensive Multi-Chain & Derivation Paths**:
  - **Bitcoin Native SegWit (Bech32)**: `m/84'/0'/0'/0/0` (`bc1q...`)
  - **Bitcoin Nested SegWit (P2SH-P2WPKH)**: `m/49'/0'/0'/0/0` (`3...`)
  - **Bitcoin Legacy (P2PKH)**: `m/44'/0'/0'/0/0` (`1...`)
  - **Ethereum / EVM Compatible Chains**: `m/44'/60'/0'/0/0` (`0x...`)
  - **Auto Detect**: Derives and tests against all standard formats simultaneously.
- 📦 **Zero Installation**: No `npm`, `node_modules`, `python`, or compilation steps needed. Simply double-click `index.html` in Chrome, Brave, Edge, Firefox, or Safari.

---

## 🖥️ Quick Start / Nasıl Kullanılır?

### 1. Download & Run Offline
1. Download `index.html` (or clone this repository).
2. *(Highly Recommended)* Disconnect your internet connection or transfer `index.html` to a clean, offline computer via USB.
3. Double-click `index.html` to open it in your browser.

### 2. Enter Your Seed Phrase
- Select your seed length (**12**, **15**, **18**, **21**, or **24** words).
- Type known words into the grid.
- For unknown / lost words, type `?` or leave the input empty.
- Enter your known public address in **"Hedef Cüzdan Adresi"** (e.g. `bc1q...` or `0x...`).
- Select your CPU thread count and click **"Kurtarmayı Başlat" (Start Recovery)**.

### 3. Recovery
- **1 Missing Word**: Instant recovery (typically < 0.1 seconds).
- **2 Missing Words**: Multi-threaded parallel brute-force (typically 5–90 seconds depending on CPU and thread count).
- Once found, the **Victory Modal** appears with your recovered full mnemonic seed phrase, derived address, derivation path, and private key.

---

## 🔐 Security Architecture

```
[ Air-Gapped Machine / Cold Browser ]
               │
   ┌───────────┴───────────┐
   │      index.html       │ (Self-contained, Embedded Crypto Libraries)
   └───────────┬───────────┘
               │
   ┌───────────▼───────────┐
   │  BIP39 Checksum Filter│ ──> Discards 15/16 combinations instantly
   └───────────┬───────────┘
               │
   ┌───────────▼───────────┐
   │ Parallel Web Workers  │ ──> PBKDF2 (2048 iter HMAC-SHA512)
   └───────────┬───────────┘
               │
   ┌───────────▼───────────┐
   │ BIP32/44/49/84 Paths  │ ──> Secp256k1 Curve + Bech32 / Base58Check
   └───────────┬───────────┘
               │
   ┌───────────▼───────────┐
   │    Address Match?     │ ──> YES: Victory Modal (Zero Data Saved)
   └───────────────────────┘
```

- **Ephemeral Storage**: All processing resides exclusively in volatile browser RAM. Closing the tab permanently erases all traces.
- **No LocalStorage**: No keys or seed words are written to disk, cookies, or `localStorage`.

---

## ☕ Support the Project / Geliştiriciye Destek

If this tool helped you recover your locked cryptocurrency and saved your assets, please consider supporting the project with a voluntary donation:

- **Bitcoin (BTC)**:
```text
bc1qxf5cfrxasshlkt79x0q805l9t3feer868en68nhlxmwetlr6sv4qdfda5s
```

Your contributions help maintain this tool and build more open-source cryptographic security utilities.

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.
