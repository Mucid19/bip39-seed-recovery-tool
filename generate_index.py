import os, sys, json

target_dir = r'c:\Users\Nova\Desktop\bip39-seed-rescuer'

# 1. Read BIP39 words
with open(os.path.join(target_dir, 'bip39_english.txt'), 'r', encoding='utf-8') as f:
    bip39_words = [line.strip() for line in f if line.strip()]

words_json = json.dumps(bip39_words)

# 2. Read core-libs from B_t_C/index.html (CryptoJS, RIPEMD160, Elliptic)
with open(r'c:\Users\Nova\Desktop\B_t_C\index.html', 'r', encoding='utf-8') as f:
    btc_html = f.read()

s_marker = '<script id="core-libs">'
e_marker = '</script>'
s_idx = btc_html.find(s_marker)
e_idx = btc_html.find(e_marker, s_idx)
core_libs_code = btc_html[s_idx + len(s_marker):e_idx].strip()

html_template = '''<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔑 KeyRescuer — Çevrimdışı BIP39 Cüzdan & Seed Kurtarıcı (Air-Gapped)</title>
    <!-- 100% Bağımsız Çevrimdışı Kriptografi Kütüphaneleri -->
    <script id="core-libs">
''' + core_libs_code + '''
    </script>
    <style>
        :root {
            --bg: #070a13;
            --surface: #0e1526;
            --surface-hover: #162038;
            --card-border: #1e293b;
            --accent-cyan: #06b6d4;
            --accent-green: #10b981;
            --accent-gold: #f59e0b;
            --accent-rose: #f43f5e;
            --text-main: #f8fafc;
            --text-dim: #94a3b8;
            --text-muted: #64748b;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            background-color: var(--bg);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding-bottom: 60px;
            overflow-x: hidden;
        }

        /* Top Security Banner */
        .shield-banner {
            width: 100%;
            padding: 8px 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.3px;
            transition: all 0.3s ease;
        }
        .shield-banner.offline {
            background: rgba(16, 185, 129, 0.15);
            border-bottom: 1px solid rgba(16, 185, 129, 0.4);
            color: #34d399;
        }
        .shield-banner.online {
            background: rgba(245, 158, 11, 0.15);
            border-bottom: 1px solid rgba(245, 158, 11, 0.4);
            color: #fbbf24;
        }

        /* Header */
        header {
            width: 100%;
            max-width: 980px;
            padding: 24px 20px 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 12px;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .brand-icon {
            width: 44px;
            height: 44px;
            background: linear-gradient(135deg, #0284c7, #0d9488);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            box-shadow: 0 0 20px rgba(6, 182, 212, 0.4);
        }

        .brand-title {
            font-size: 20px;
            font-weight: 800;
            background: linear-gradient(90deg, #38bdf8, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
        }

        .brand-subtitle {
            font-size: 11px;
            color: var(--text-dim);
            font-weight: 600;
        }

        .header-actions {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .btn-top {
            background: var(--surface);
            border: 1px solid var(--card-border);
            color: var(--text-dim);
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
        }
        .btn-top:hover {
            border-color: var(--accent-cyan);
            color: var(--text-main);
        }
        .btn-donate {
            background: rgba(245, 158, 11, 0.12);
            border-color: rgba(245, 158, 11, 0.35);
            color: #fbbf24;
        }
        .btn-donate:hover {
            background: rgba(245, 158, 11, 0.22);
            border-color: #f59e0b;
            color: #fff;
            box-shadow: 0 0 12px rgba(245, 158, 11, 0.4);
        }

        /* Main Container */
        .container {
            width: 100%;
            max-width: 980px;
            padding: 0 16px;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        /* Cards */
        .card {
            background: var(--surface);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 18px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
        }

        .card-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 14px;
            padding-bottom: 10px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }

        .card-title {
            font-size: 14px;
            font-weight: 700;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        /* Mode Tabs */
        .mode-tabs {
            display: flex;
            gap: 6px;
            background: rgba(0, 0, 0, 0.3);
            padding: 4px;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.06);
            margin-bottom: 14px;
        }
        .mode-tab {
            flex: 1;
            padding: 8px 12px;
            text-align: center;
            font-size: 12px;
            font-weight: 700;
            color: var(--text-dim);
            background: transparent;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s;
        }
        .mode-tab.active {
            background: var(--surface-hover);
            color: var(--accent-cyan);
            box-shadow: 0 2px 8px rgba(0,0,0,0.4);
            border: 1px solid rgba(6, 182, 212, 0.3);
        }

        /* Quick Controls Row */
        .controls-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 12px;
        }

        .word-count-select, .threads-select {
            background: #090e1a;
            border: 1px solid var(--card-border);
            color: var(--text-main);
            padding: 6px 10px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 600;
            outline: none;
            cursor: pointer;
        }

        /* Words Grid */
        .words-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
            gap: 8px;
            margin-bottom: 14px;
        }

        .word-box {
            position: relative;
            background: #090e1a;
            border: 1px solid var(--card-border);
            border-radius: 8px;
            padding: 6px 8px;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
        }
        .word-box:focus-within {
            border-color: var(--accent-cyan);
            box-shadow: 0 0 10px rgba(6, 182, 212, 0.3);
        }
        .word-box.missing {
            border-color: var(--accent-gold);
            background: rgba(245, 158, 11, 0.05);
        }
        .word-box.invalid {
            border-color: var(--accent-rose);
            background: rgba(244, 63, 94, 0.05);
        }
        .word-box.valid {
            border-color: rgba(16, 185, 129, 0.4);
        }

        .word-num {
            font-size: 10px;
            font-weight: 800;
            color: var(--text-muted);
            min-width: 18px;
            text-align: right;
            user-select: none;
        }

        .word-input {
            width: 100%;
            background: transparent;
            border: none;
            color: var(--text-main);
            font-size: 12px;
            font-weight: 600;
            outline: none;
            text-transform: lowercase;
        }
        .word-input::placeholder {
            color: var(--text-muted);
            font-weight: 400;
        }

        .word-status {
            font-size: 11px;
            user-select: none;
        }

        /* Target Address Input */
        .target-section {
            background: #090e1a;
            border: 1px solid var(--card-border);
            border-radius: 8px;
            padding: 12px;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .target-input {
            width: 100%;
            background: #070a13;
            border: 1px solid rgba(255, 255, 255, 0.08);
            color: #38bdf8;
            font-family: 'Consolas', 'Courier New', monospace;
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
            outline: none;
        }
        .target-input:focus {
            border-color: var(--accent-cyan);
        }

        /* Action Buttons */
        .action-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            flex-wrap: wrap;
            margin-top: 14px;
        }

        .btn-start {
            background: linear-gradient(135deg, #0284c7, #059669);
            border: none;
            color: #ffffff;
            padding: 12px 28px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 800;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 4px 16px rgba(6, 182, 212, 0.4);
            transition: all 0.2s;
        }
        .btn-start:hover {
            box-shadow: 0 6px 22px rgba(6, 182, 212, 0.6);
            transform: translateY(-1px);
        }
        .btn-start:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }
        .btn-stop {
            background: rgba(239, 68, 68, 0.2);
            border: 1px solid #ef4444;
            color: #f87171;
            padding: 12px 20px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            display: none;
        }

        /* Live Dashboard */
        .dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 10px;
            margin-top: 14px;
        }
        .stat-box {
            background: #090e1a;
            border: 1px solid var(--card-border);
            border-radius: 8px;
            padding: 10px 14px;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }
        .stat-label {
            font-size: 10px;
            font-weight: 700;
            color: var(--text-dim);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .stat-value {
            font-size: 16px;
            font-weight: 800;
            color: var(--text-main);
            font-family: 'Consolas', monospace;
        }

        /* Progress Bar */
        .progress-bar-wrap {
            width: 100%;
            height: 8px;
            background: #090e1a;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 10px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        .progress-bar-fill {
            height: 100%;
            width: 0%;
            background: linear-gradient(90deg, #0284c7, #10b981);
            transition: width 0.2s ease;
        }

        /* Autocomplete Suggestions */
        .suggestions-dropdown {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: #0e1526;
            border: 1px solid var(--accent-cyan);
            border-radius: 6px;
            max-height: 160px;
            overflow-y: auto;
            z-index: 1000;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6);
            display: none;
        }
        .suggestion-item {
            padding: 6px 10px;
            font-size: 11px;
            font-weight: 600;
            color: var(--text-main);
            cursor: pointer;
        }
        .suggestion-item:hover, .suggestion-item.active {
            background: #1e293b;
            color: var(--accent-cyan);
        }

        /* Modals */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(8px);
            z-index: 2000;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 16px;
        }
        .modal-card {
            background: var(--surface);
            border: 1px solid var(--accent-green);
            border-radius: 16px;
            max-width: 620px;
            width: 100%;
            padding: 24px;
            box-shadow: 0 0 40px rgba(16, 185, 129, 0.35);
            position: relative;
            max-height: 90vh;
            overflow-y: auto;
        }
        .modal-card.donate-modal {
            border-color: var(--accent-gold);
            box-shadow: 0 0 40px rgba(245, 158, 11, 0.3);
        }
        .modal-close {
            position: absolute;
            top: 16px;
            right: 16px;
            background: transparent;
            border: none;
            color: var(--text-muted);
            font-size: 20px;
            cursor: pointer;
        }
        .modal-close:hover {
            color: var(--text-main);
        }

        /* Recovered Seed Display Box */
        .recovered-box {
            background: #090e1a;
            border: 1px solid rgba(16, 185, 129, 0.4);
            border-radius: 10px;
            padding: 14px;
            margin: 14px 0;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .recovered-seed-text {
            font-family: 'Consolas', monospace;
            font-size: 13px;
            font-weight: 700;
            color: #34d399;
            line-height: 1.6;
            word-break: break-word;
            user-select: all;
        }

        /* Donation Address Rows */
        .donate-row {
            background: #090e1a;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 8px;
            padding: 10px 12px;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 8px;
        }
        .donate-label {
            font-size: 11px;
            font-weight: 700;
            color: #fbbf24;
            min-width: 90px;
        }
        .donate-addr {
            font-family: 'Consolas', monospace;
            font-size: 11px;
            color: var(--text-dim);
            word-break: break-all;
        }
        .btn-copy {
            background: #1e293b;
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: var(--text-main);
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 10px;
            font-weight: 600;
            cursor: pointer;
            white-space: nowrap;
        }
        .btn-copy:hover {
            background: #334155;
            color: #38bdf8;
        }

        /* Results table when no target address provided */
        .results-table-wrap {
            max-height: 240px;
            overflow-y: auto;
            border: 1px solid var(--card-border);
            border-radius: 8px;
            margin-top: 12px;
        }
        .results-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 11px;
        }
        .results-table th, .results-table td {
            padding: 6px 10px;
            text-align: left;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }
        .results-table th {
            background: #090e1a;
            color: var(--text-dim);
            font-weight: 700;
            position: sticky;
            top: 0;
        }
        .results-table tr:hover {
            background: rgba(255, 255, 255, 0.03);
        }
    </style>
</head>
<body>

    <!-- Güvenlik / Çevrimdışı Durum Çubuğu -->
    <div id="shieldBanner" class="shield-banner online">
        <span id="shieldIcon">⚠️</span>
        <span id="shieldText">GÜVENLİK TAVSİYESİ: Maksimum güvenlik için internetinizi (Wi-Fi) kesip bu aracı tamamen çevrimdışı (Air-Gapped) çalıştırın.</span>
    </div>

    <!-- Üst Başlık -->
    <header>
        <div class="brand">
            <div class="brand-icon">🔑</div>
            <div>
                <div class="brand-title">KeyRescuer</div>
                <div class="brand-subtitle">Çevrimdışı BIP39 Cüzdan & Seed Kurtarma Aracı (%100 Air-Gapped)</div>
            </div>
        </div>
        <div class="header-actions">
            <button class="btn-top" onclick="fillTestSeed(1)">🧪 1 Eksikli Test</button>
            <button class="btn-top" onclick="fillTestSeed(2)">🧪 2 Eksikli Test</button>
            <button class="btn-top btn-donate" onclick="openDonateModal()">☕ Geliştiriciye Destek</button>
        </div>
    </header>

    <div class="container">

        <!-- Mod Seçimi -->
        <div class="mode-tabs">
            <button class="mode-tab active" onclick="setMode('MISSING')">🧩 1-2 Eksik Kelime Kurtarma (?)</button>
            <button class="mode-tab" onclick="setMode('TYPO')">✏️ Harf Hatası & Yazım Düzeltme</button>
            <button class="mode-tab" onclick="setMode('SCRAMBLE')">🔀 Karışık Sıra Permütasyon</button>
        </div>

        <!-- Ana Kontrol Kartı -->
        <div class="card">
            <div class="card-header">
                <div class="card-title">
                    <span>📝 Tohum Kelimelerini Girin</span>
                    <span id="seedValidBadge" style="font-size:10px; font-weight:700; padding:2px 8px; border-radius:4px; background:rgba(245,158,11,0.15); color:#fbbf24; border:1px solid rgba(245,158,11,0.3);">Eksik Var</span>
                </div>
                <div style="display:flex; align-items:center; gap:8px;">
                    <button class="btn-top" onclick="togglePasteArea()" style="padding:4px 8px; font-size:10px;">📋 Toplu Yapıştır</button>
                    <button class="btn-top" onclick="clearAllWords()" style="padding:4px 8px; font-size:10px;">🗑️ Temizle</button>
                    <select id="wordCountSelect" class="word-count-select" onchange="changeWordCount(this.value)">
                        <option value="12" selected>12 Kelime</option>
                        <option value="15">15 Kelime</option>
                        <option value="18">18 Kelime</option>
                        <option value="21">21 Kelime</option>
                        <option value="24">24 Kelime</option>
                    </select>
                </div>
            </div>

            <!-- Toplu Yapıştırma Kutusu (Gizli/Açılır) -->
            <div id="pasteArea" style="display:none; margin-bottom:12px;">
                <textarea id="bulkPasteInput" placeholder="Tüm kelimeleri boşluk bırakarak buraya yapıştırın. Bilmediğiniz kelimeler için '?' veya '*' koyun..." style="width:100%; height:60px; background:#070a13; border:1px solid var(--card-border); border-radius:6px; color:#fff; padding:8px; font-size:12px; font-family:monospace; resize:none;"></textarea>
                <div style="display:flex; justify-content:flex-end; gap:6px; margin-top:4px;">
                    <button class="btn-top" onclick="applyBulkPaste()" style="background:#0284c7; color:#fff; border:none; padding:4px 10px;">Uygula</button>
                </div>
            </div>

            <!-- 12/24 Kelime Izgarası -->
            <div class="words-grid" id="wordsGrid"></div>

            <!-- Hedef Adres & Türetme Seçimi -->
            <div class="target-section">
                <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:8px;">
                    <label style="font-size:11px; font-weight:700; color:var(--text-dim);">🎯 Bilinen Cüzdan Adresi (Eşleştirme İçin):</label>
                    <div style="display:flex; align-items:center; gap:6px;">
                        <span style="font-size:10px; color:var(--text-muted);">Türetme Yolu:</span>
                        <select id="pathSelect" class="word-count-select" style="font-size:10px; padding:3px 6px;">
                            <option value="AUTO" selected>🔄 Otomatik Algıla</option>
                            <option value="BIP84">Bitcoin Native SegWit (bc1q... BIP84)</option>
                            <option value="BIP49">Bitcoin Nested SegWit (3... BIP49)</option>
                            <option value="BIP44">Bitcoin Legacy (1... BIP44)</option>
                            <option value="ETH">Ethereum / EVM (0x... BIP44)</option>
                        </select>
                    </div>
                </div>
                <input type="text" id="targetAddressInput" class="target-input" placeholder="Örnek: bc1qcr8te4kr609gcawutmrza0j4xv80jy8z306fyu veya 0x... veya 1... veya 3...">
                <div style="display:flex; align-items:center; justify-content:space-between; font-size:10px; color:var(--text-muted);">
                    <span>* Hedef adresi bilmiyorsanız boş bırakabilirsiniz (1 eksikte olası tüm geçerli kombinasyonları listeler).</span>
                    <span id="detectedTypeBadge" style="color:var(--accent-cyan); font-weight:700;"></span>
                </div>
            </div>

            <!-- Opsiyonel BIP39 Parolası (Passphrase / 13. Kelime) -->
            <div style="margin-top:10px; display:flex; align-items:center; gap:8px;">
                <label style="font-size:11px; font-weight:600; color:var(--text-dim); white-space:nowrap;">🔒 Ek Parola (Passphrase / 13./25. Kelime):</label>
                <input type="text" id="passphraseInput" class="target-input" placeholder="Cüzdanınızda ek parola yoksa boş bırakın (çoğu cüzdanda boştur)" style="flex:1; padding:6px 10px; font-size:11px;">
            </div>

            <!-- Eylem Butonları & Thread Seçimi -->
            <div class="action-row">
                <div style="display:flex; align-items:center; gap:8px;">
                    <label style="font-size:11px; font-weight:600; color:var(--text-dim);">⚡ İş Parçacığı (Threads):</label>
                    <select id="threadSelect" class="threads-select"></select>
                </div>
                <div style="display:flex; align-items:center; gap:8px;">
                    <button id="btnStopSearch" class="btn-stop" onclick="stopRecovery()">⏹️ Durdur</button>
                    <button id="btnStartSearch" class="btn-start" onclick="startRecovery()">
                        <span>🚀 Kurtarmayı Başlat</span>
                    </button>
                </div>
            </div>

            <!-- Canlı İlerleme ve Hız Paneli -->
            <div class="dashboard" id="dashboard" style="display:none;">
                <div class="stat-box">
                    <span class="stat-label">Hız</span>
                    <span class="stat-value" id="statSpeed" style="color:#38bdf8;">0 tohum/s</span>
                </div>
                <div class="stat-box">
                    <span class="stat-label">Denenen / Toplam</span>
                    <span class="stat-value" id="statTested">0 / 0</span>
                </div>
                <div class="stat-box">
                    <span class="stat-label">Geçen Süre</span>
                    <span class="stat-value" id="statTime">00:00</span>
                </div>
                <div class="stat-box">
                    <span class="stat-label">Tahmini Kalan</span>
                    <span class="stat-value" id="statETA" style="color:#f59e0b;">Hesaplanıyor...</span>
                </div>
            </div>

            <div class="progress-bar-wrap" id="progressWrap" style="display:none;">
                <div class="progress-bar-fill" id="progressBar"></div>
            </div>

            <!-- Adressiz 1 Eksikli Bulunan Kombinasyonlar Listesi -->
            <div id="resultsTableContainer" style="display:none;">
                <div style="font-size:12px; font-weight:700; color:#34d399; margin-top:14px; display:flex; justify-content:space-between;">
                    <span>📋 Bulunan Geçerli BIP39 Kombinasyonları</span>
                    <span id="resultsCount">0 adet</span>
                </div>
                <div class="results-table-wrap">
                    <table class="results-table">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Tamamlanan Kelime</th>
                                <th>Tam Seed (Mnemonic)</th>
                                <th>Adres (SegWit / bc1q)</th>
                                <th>İşlem</th>
                            </tr>
                        </thead>
                        <tbody id="resultsTableBody"></tbody>
                    </table>
                </div>
            </div>

        </div>

    </div>

    <!-- 🎉 ZAFER & KURTARMA BAŞARI MODALI -->
    <div id="victoryModal" class="modal-overlay">
        <div class="modal-card">
            <button class="modal-close" onclick="closeVictoryModal()">✕</button>
            <div style="text-align:center; margin-bottom:14px;">
                <div style="font-size:40px; margin-bottom:4px;">🎉</div>
                <h2 style="font-size:20px; font-weight:800; color:#34d399;">Cüzdanınız Başarıyla Kurtarıldı!</h2>
                <p style="font-size:12px; color:var(--text-dim); margin-top:4px;">Kayıp kelimeler eksiksiz olarak tespit edildi ve hedef adresle doğrulandı.</p>
            </div>

            <div class="recovered-box">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11px; font-weight:700; color:var(--text-dim);">🔑 KURTARILAN TAM SEED PHRASE:</span>
                    <button class="btn-copy" onclick="copyToClipboard(document.getElementById('recoveredSeedText').innerText, this)">📋 Kopyala</button>
                </div>
                <div id="recoveredSeedText" class="recovered-seed-text"></div>
            </div>

            <div style="background:#090e1a; border:1px solid var(--card-border); border-radius:8px; padding:10px; font-size:11px; margin-bottom:14px;">
                <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                    <span style="color:var(--text-muted);">Eşleşen Adres:</span>
                    <span id="recoveredAddrText" style="color:#38bdf8; font-family:monospace; font-weight:700;"></span>
                </div>
                <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                    <span style="color:var(--text-muted);">Türetme Yolu:</span>
                    <span id="recoveredPathText" style="color:#fbbf24; font-family:monospace;">m/84'/0'/0'/0/0</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span style="color:var(--text-muted);">Özel Anahtar (Hex):</span>
                    <span id="recoveredPrivText" style="color:#a855f7; font-family:monospace;"></span>
                </div>
            </div>

            <!-- Gönüllü Bağış Bölümü -->
            <div style="background:rgba(245,158,11,0.08); border:1px solid rgba(245,158,11,0.3); border-radius:10px; padding:12px; text-align:center;">
                <h4 style="font-size:13px; font-weight:800; color:#fbbf24; margin-bottom:4px;">☕ Geliştiriciye Destek Olmak İster misiniz?</h4>
                <p style="font-size:11px; color:var(--text-dim); line-height:1.4; margin-bottom:10px;">
                    Bu araç tamamen ücretsiz ve açık kaynaklıdır. Eğer bu araç fonlarınızı kurtarmanızı sağladıysa, projeyi ayakta tutmak için küçük bir bağışla destek olabilirsiniz.
                </p>
                <div class="donate-row">
                    <span class="donate-label">🪙 Bitcoin (BTC):</span>
                    <span class="donate-addr">bc1qxf5cfrxasshlkt79x0q805l9t3feer868en68nhlxmwetlr6sv4qdfda5s</span>
                    <button class="btn-copy" onclick="copyToClipboard('bc1qxf5cfrxasshlkt79x0q805l9t3feer868en68nhlxmwetlr6sv4qdfda5s', this)">Kopyala</button>
                </div>
            </div>
        </div>
    </div>

    <!-- ☕ BAĞIŞ MODALI (İstenildiği zaman açılan) -->
    <div id="donateModal" class="modal-overlay">
        <div class="modal-card donate-modal">
            <button class="modal-close" onclick="closeDonateModal()">✕</button>
            <div style="text-align:center; margin-bottom:16px;">
                <div style="font-size:36px; margin-bottom:4px;">☕</div>
                <h3 style="font-size:18px; font-weight:800; color:#fbbf24;">Açık Kaynak Geliştiriciye Destek</h3>
                <p style="font-size:11px; color:var(--text-dim); margin-top:4px;">
                    KeyRescuer, hiçbir ücret talep etmeyen, sıfır dış bağımlılıklı ve %100 yerel çalışan bağımsız bir güvenlik projesidir. Katkılarınız yeni kriptografik kurtarma araçlarının geliştirilmesini sağlar.
                </p>
            </div>

            <div class="donate-row">
                <span class="donate-label">🪙 Bitcoin (BTC):</span>
                <span class="donate-addr">bc1qxf5cfrxasshlkt79x0q805l9t3feer868en68nhlxmwetlr6sv4qdfda5s</span>
                <button class="btn-copy" onclick="copyToClipboard('bc1qxf5cfrxasshlkt79x0q805l9t3feer868en68nhlxmwetlr6sv4qdfda5s', this)">Kopyala</button>
            </div>

            <div style="text-align:center; margin-top:14px; font-size:11px; color:var(--text-muted);">
                Tüm bağışlar için kalpten teşekkür ederiz! 🙏
            </div>
        </div>
    </div>

    <!-- BIP39 KELİME LİSTESİ VE UYGULAMA MOTORU -->
    <script>
        const BIP39_WORDS = ''' + words_json + ''';
        const BIP39_MAP = new Map();
        BIP39_WORDS.forEach((w, i) => BIP39_MAP.set(w, i));

        let currentWordCount = 12;
        let currentMode = 'MISSING';
        let activeWorkers = [];
        let searchStartTime = 0;
        let searchInterval = null;
        let totalTested = 0;
        let totalToTest = 0;
        let isSearching = false;

        // İnternet Bağlantısı Durumunu İzle
        function updateNetworkStatus() {
            const banner = document.getElementById('shieldBanner');
            const icon = document.getElementById('shieldIcon');
            const text = document.getElementById('shieldText');
            if (navigator.onLine) {
                banner.className = 'shield-banner online';
                icon.innerText = '⚠️';
                text.innerText = 'GÜVENLİK TAVSİYESİ: Maksimum güvenlik için internetinizi (Wi-Fi) kesip bu aracı tamamen çevrimdışı (Air-Gapped) çalıştırın.';
            } else {
                banner.className = 'shield-banner offline';
                icon.innerText = '🔒';
                text.innerText = 'GÜVENLİ ÇEVRİMDISI MOD (Air-Gapped): İnternet bağlantısı yok, tüm işlemler yerel RAM belleğinizde çalışıyor.';
            }
        }
        window.addEventListener('online', updateNetworkStatus);
        window.addEventListener('offline', updateNetworkStatus);
        updateNetworkStatus();

        // İş parçacığı (Threads) listesini doldur
        function initThreads() {
            const sel = document.getElementById('threadSelect');
            const cores = navigator.hardwareConcurrency || 4;
            sel.innerHTML = '';
            for (let i = 1; i <= Math.max(16, cores); i++) {
                const opt = document.createElement('option');
                opt.value = i;
                opt.text = i + (i === cores ? ' Çekirdek (Önerilen)' : ' Çekirdek');
                if (i === cores) opt.selected = true;
                sel.appendChild(opt);
            }
        }
        initThreads();

        // Kelime Izgarasını Oluştur
        function renderWordGrid() {
            const grid = document.getElementById('wordsGrid');
            grid.innerHTML = '';
            for (let i = 1; i <= currentWordCount; i++) {
                const box = document.createElement('div');
                box.className = 'word-box';
                box.id = `wordBox_${i}`;
                box.innerHTML = `
                    <span class="word-num">${i}</span>
                    <input type="text" class="word-input" id="wordInput_${i}" data-index="${i}" placeholder="kelime..." autocomplete="off" spellcheck="false" oninput="onWordInput(${i})" onkeydown="onWordKeydown(event, ${i})">
                    <span class="word-status" id="wordStatus_${i}"></span>
                    <div class="suggestions-dropdown" id="sugg_${i}"></div>
                `;
                grid.appendChild(box);
            }
            validateAllWords();
        }
        renderWordGrid();

        function changeWordCount(val) {
            currentWordCount = parseInt(val, 10);
            renderWordGrid();
        }

        function setMode(mode) {
            currentMode = mode;
            document.querySelectorAll('.mode-tab').forEach(t => t.classList.remove('active'));
            event.target.classList.add('active');
        }

        // Kelime Girişi Kontrolü
        function onWordInput(idx) {
            const input = document.getElementById(`wordInput_${idx}`);
            const val = input.value.trim().toLowerCase();
            const box = document.getElementById(`wordBox_${idx}`);
            const status = document.getElementById(`wordStatus_${idx}`);
            const sugg = document.getElementById(`sugg_${idx}`);

            if (!val || val === '?' || val === '*') {
                box.className = 'word-box missing';
                status.innerText = val ? '❓' : '';
                sugg.style.display = 'none';
            } else if (BIP39_MAP.has(val)) {
                box.className = 'word-box valid';
                status.innerText = '✓';
                status.style.color = '#34d399';
                sugg.style.display = 'none';
            } else {
                box.className = 'word-box invalid';
                status.innerText = '✗';
                status.style.color = '#f43f5e';
                showSuggestions(idx, val);
            }
            validateAllWords();
        }

        function showSuggestions(idx, val) {
            const sugg = document.getElementById(`sugg_${idx}`);
            if (val.length < 2) { sugg.style.display = 'none'; return; }
            const matches = BIP39_WORDS.filter(w => w.startsWith(val)).slice(0, 5);
            if (matches.length === 0) { sugg.style.display = 'none'; return; }
            sugg.innerHTML = '';
            matches.forEach(m => {
                const item = document.createElement('div');
                item.className = 'suggestion-item';
                item.innerText = m;
                item.onclick = () => selectSuggestion(idx, m);
                sugg.appendChild(item);
            });
            sugg.style.display = 'block';
        }

        function selectSuggestion(idx, word) {
            const input = document.getElementById(`wordInput_${idx}`);
            input.value = word;
            document.getElementById(`sugg_${idx}`).style.display = 'none';
            onWordInput(idx);
            // Bir sonraki kelimeye odaklan
            if (idx < currentWordCount) {
                const next = document.getElementById(`wordInput_${idx + 1}`);
                if (next) next.focus();
            }
        }

        function onWordKeydown(e, idx) {
            if (e.key === 'Enter' || e.key === 'Tab') {
                const sugg = document.getElementById(`sugg_${idx}`);
                if (sugg && sugg.style.display === 'block') {
                    const first = sugg.querySelector('.suggestion-item');
                    if (first) {
                        e.preventDefault();
                        selectSuggestion(idx, first.innerText);
                    }
                }
            }
        }

        function validateAllWords() {
            let missingCount = 0;
            let invalidCount = 0;
            let filledCount = 0;

            for (let i = 1; i <= currentWordCount; i++) {
                const input = document.getElementById(`wordInput_${i}`);
                const val = input ? input.value.trim().toLowerCase() : '';
                if (!val || val === '?' || val === '*') {
                    missingCount++;
                } else if (BIP39_MAP.has(val)) {
                    filledCount++;
                } else {
                    invalidCount++;
                }
            }

            const badge = document.getElementById('seedValidBadge');
            if (invalidCount > 0) {
                badge.style.background = 'rgba(244,63,94,0.15)';
                badge.style.color = '#f43f5e';
                badge.style.borderColor = 'rgba(244,63,94,0.3)';
                badge.innerText = `${invalidCount} Geçersiz Kelime`;
            } else if (missingCount > 0) {
                badge.style.background = 'rgba(245,158,11,0.15)';
                badge.style.color = '#fbbf24';
                badge.style.borderColor = 'rgba(245,158,11,0.3)';
                badge.innerText = `${missingCount} Eksik Kelime (?)`;
            } else {
                // Checksum geçerli mi kontrol et
                const words = [];
                for (let i = 1; i <= currentWordCount; i++) {
                    words.push(document.getElementById(`wordInput_${i}`).value.trim().toLowerCase());
                }
                const isValidCS = validateBip39Checksum(words);
                if (isValidCS) {
                    badge.style.background = 'rgba(16,185,129,0.15)';
                    badge.style.color = '#34d399';
                    badge.style.borderColor = 'rgba(16,185,129,0.3)';
                    badge.innerText = '✓ Geçerli BIP39 Tohumu';
                } else {
                    badge.style.background = 'rgba(244,63,94,0.15)';
                    badge.style.color = '#f43f5e';
                    badge.style.borderColor = 'rgba(244,63,94,0.3)';
                    badge.innerText = '✗ Hatalı Checksum';
                }
            }
        }

        // BIP39 Checksum Doğrulayıcı
        function validateBip39Checksum(words) {
            const count = words.length;
            if (![12, 15, 18, 21, 24].includes(count)) return false;
            const csBitsLen = count / 3;
            const entropyBitsLen = count * 11 - csBitsLen;

            // Bit array
            const bitArray = [];
            for (let w of words) {
                const idx = BIP39_MAP.get(w);
                if (idx === undefined) return false;
                for (let b = 10; b >= 0; b--) {
                    bitArray.push((idx >> b) & 1);
                }
            }

            // Entropy bytes
            const entropyBytes = [];
            for (let i = 0; i < entropyBitsLen; i += 8) {
                let byteVal = 0;
                for (let b = 0; b < 8; b++) {
                    byteVal = (byteVal << 1) | bitArray[i + b];
                }
                entropyBytes.push(byteVal);
            }

            // SHA256 of entropy
            const entropyHex = entropyBytes.map(b => b.toString(16).padStart(2, '0')).join('');
            const hashWA = CryptoJS.SHA256(CryptoJS.enc.Hex.parse(entropyHex));
            const hashHex = hashWA.toString();
            const firstHashByte = parseInt(hashHex.substring(0, 2), 16);

            // Compare checksum bits
            let expectedCS = 0;
            for (let i = 0; i < csBitsLen; i++) {
                expectedCS = (expectedCS << 1) | bitArray[entropyBitsLen + i];
            }
            const actualCS = firstHashByte >> (8 - csBitsLen);
            return expectedCS === actualCS;
        }

        // Toplu Yapıştırma Kutusu
        function togglePasteArea() {
            const el = document.getElementById('pasteArea');
            el.style.display = el.style.display === 'none' ? 'block' : 'none';
        }

        function applyBulkPaste() {
            const raw = document.getElementById('bulkPasteInput').value.trim();
            if (!raw) return;
            const tokens = raw.split(/[\\s,;]+/).filter(Boolean);
            if ([12, 15, 18, 21, 24].includes(tokens.length)) {
                currentWordCount = tokens.length;
                document.getElementById('wordCountSelect').value = currentWordCount;
                renderWordGrid();
            }
            tokens.slice(0, currentWordCount).forEach((w, i) => {
                const inp = document.getElementById(`wordInput_${i + 1}`);
                if (inp) {
                    inp.value = (w === '?' || w === '*' || !BIP39_MAP.has(w.toLowerCase())) ? (BIP39_MAP.has(w.toLowerCase()) ? w.toLowerCase() : '?') : w.toLowerCase();
                    onWordInput(i + 1);
                }
            });
            document.getElementById('pasteArea').style.display = 'none';
        }

        function clearAllWords() {
            for (let i = 1; i <= currentWordCount; i++) {
                const inp = document.getElementById(`wordInput_${i}`);
                if (inp) { inp.value = ''; onWordInput(i); }
            }
        }

        // Test Tohumu Doldur
        function fillTestSeed(missingCount = 1) {
            // Bilinen BIP84 Test Vektörü:
            // "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
            // Adres: bc1qcr8te4kr609gcawutmrza0j4xv80jy8z306fyu
            currentWordCount = 12;
            document.getElementById('wordCountSelect').value = '12';
            renderWordGrid();

            const testSeed = ['abandon','abandon','abandon','abandon','abandon','abandon','abandon','abandon','abandon','abandon','abandon','about'];
            if (missingCount === 1) {
                testSeed[11] = '?'; // Son kelime eksik
            } else if (missingCount === 2) {
                testSeed[0] = '?';  // 1. kelime eksik
                testSeed[11] = '?'; // 12. kelime eksik
            }

            testSeed.forEach((w, i) => {
                const inp = document.getElementById(`wordInput_${i + 1}`);
                if (inp) { inp.value = w; onWordInput(i + 1); }
            });

            document.getElementById('targetAddressInput').value = 'bc1qcr8te4kr609gcawutmrza0j4xv80jy8z306fyu';
            document.getElementById('pathSelect').value = 'BIP84';
        }

        // ============================================================
        // 🚀 WEB WORKER VE HIZLANDIRILMIŞ KURTARMA MOTORU
        // ============================================================

        // Worker Script Kodu (Blob URL olarak üretilir)
        const workerScriptSource = `
            const BIP39_WORDS = ${words_json};
            const BIP39_MAP = new Map();
            BIP39_WORDS.forEach((w, i) => BIP39_MAP.set(w, i));

            // Core-libs içinde secp256k1 ve hash kütüphaneleri mevcuttur
            ${core_libs_code}

            // Bech32 encode
            const CHARSET = 'qpzry9x8gf2tvdw0s3jn54khce6mua7l';
            function bech32Polymod(values) {
                const GEN = [0x3b6a57b2, 0x26508e6d, 0x1ea119fa, 0x3d4233dd, 0x2a1462b3];
                let chk = 1;
                for (let v of values) {
                    let b = chk >> 25;
                    chk = ((chk & 0x1ffffff) << 5) ^ v;
                    for (let i = 0; i < 5; i++) chk ^= (b >> i) & 1 ? GEN[i] : 0;
                }
                return chk;
            }
            function bech32HrpExpand(hrp) {
                let r = [];
                for (let i = 0; i < hrp.length; i++) r.push(hrp.charCodeAt(i) >> 5);
                r.push(0);
                for (let i = 0; i < hrp.length; i++) r.push(hrp.charCodeAt(i) & 31);
                return r;
            }
            function bech32Checksum(hrp, data) {
                let values = bech32HrpExpand(hrp).concat(data);
                let poly = bech32Polymod(values.concat([0,0,0,0,0,0])) ^ 1;
                let chk = [];
                for (let i = 0; i < 6; i++) chk.push((poly >> (5 * (5 - i))) & 31);
                return chk;
            }
            function convertBits(data, from, to, pad = true) {
                let acc = 0, bits = 0, ret = [];
                let maxv = (1 << to) - 1;
                for (let v of data) {
                    acc = ((acc << from) | v) & ((1 << (from + to - 1)) - 1);
                    bits += from;
                    while (bits >= to) {
                        bits -= to;
                        ret.push((acc >> bits) & maxv);
                    }
                }
                if (pad && bits) ret.push((acc << (to - bits)) & maxv);
                return ret;
            }
            function encodeSegwitBech32(hash160Hex) {
                let bytes = [];
                for (let i = 0; i < hash160Hex.length; i += 2) bytes.push(parseInt(hash160Hex.substr(i, 2), 16));
                let data5 = [0].concat(convertBits(bytes, 8, 5));
                let chk = bech32Checksum('bc', data5);
                let res = 'bc1';
                for (let d of data5.concat(chk)) res += CHARSET[d];
                return res;
            }

            // Base58 encode
            const B58_CHARS = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz';
            function base58Encode(buffer) {
                let digits = [0];
                for (let i = 0; i < buffer.length; i++) {
                    let carry = buffer[i];
                    for (let j = 0; j < digits.length; j++) {
                        carry += digits[j] << 8;
                        digits[j] = carry % 58;
                        carry = (carry / 58) | 0;
                    }
                    while (carry > 0) {
                        digits.push(carry % 58);
                        carry = (carry / 58) | 0;
                    }
                }
                for (let i = 0; i < buffer.length && buffer[i] === 0; i++) digits.push(0);
                let str = '';
                for (let i = digits.length - 1; i >= 0; i--) str += B58_CHARS[digits[i]];
                return str;
            }
            function base58Check(prefixByte, hash160Hex) {
                let full = prefixByte + hash160Hex;
                let sha1 = CryptoJS.SHA256(CryptoJS.enc.Hex.parse(full));
                let sha2 = CryptoJS.SHA256(sha1).toString();
                let checksum = sha2.substring(0, 8);
                let finalHex = full + checksum;
                let bytes = [];
                for (let i = 0; i < finalHex.length; i += 2) bytes.push(parseInt(finalHex.substr(i, 2), 16));
                return base58Encode(bytes);
            }

            // Fast Checksum validator for 12/24 words
            function fastValidateChecksum(wordIndices, count) {
                let csLen = count / 3;
                let entLen = count * 11 - csLen;
                let bits = [];
                for (let idx of wordIndices) {
                    for (let b = 10; b >= 0; b--) bits.push((idx >> b) & 1);
                }
                let bytes = [];
                for (let i = 0; i < entLen; i += 8) {
                    let b = 0;
                    for (let j = 0; j < 8; j++) b = (b << 1) | bits[i + j];
                    bytes.push(b);
                }
                let hex = bytes.map(b => b.toString(16).padStart(2, '0')).join('');
                let sha = CryptoJS.SHA256(CryptoJS.enc.Hex.parse(hex)).toString();
                let actualByte = parseInt(sha.substring(0, 2), 16) >> (8 - csLen);
                let expectedByte = 0;
                for (let i = 0; i < csLen; i++) expectedByte = (expectedByte << 1) | bits[entLen + i];
                return expectedByte === actualByte;
            }

            // BIP32 Derivation
            const secp256k1 = new elliptic.ec('secp256k1');
            const G = secp256k1.g;
            const N = secp256k1.n;

            function ckdPriv(kHex, cHex, index) {
                let isHardened = (index >= 0x80000000);
                let ser32 = (index >>> 0).toString(16).padStart(8, '0');
                let dataHex = '';
                if (isHardened) {
                    dataHex = '00' + kHex + ser32;
                } else {
                    let key = secp256k1.keyFromPrivate(kHex, 'hex');
                    let pubComp = key.getPublic(true, 'hex');
                    dataHex = pubComp + ser32;
                }
                let I = CryptoJS.HmacSHA512(CryptoJS.enc.Hex.parse(dataHex), CryptoJS.enc.Hex.parse(cHex)).toString();
                let Il = I.substring(0, 64);
                let Ir = I.substring(64, 128);
                let ilBN = new secp256k1.curve.conf.BigInteger(Il, 16);
                let kBN = new secp256k1.curve.conf.BigInteger(kHex, 16);
                let childK = ilBN.add(kBN).mod(N).toString(16).padStart(64, '0');
                return { k: childK, c: Ir };
            }

            // PBKDF2 Mnemonic to Seed
            async function deriveSeed(mnemonic, passphrase = '') {
                const pw = new TextEncoder().encode(mnemonic.normalize('NFKD'));
                const salt = new TextEncoder().encode(('mnemonic' + passphrase).normalize('NFKD'));
                const key = await self.crypto.subtle.importKey('raw', pw, { name: 'PBKDF2' }, false, ['deriveBits']);
                const bits = await self.crypto.subtle.deriveBits({
                    name: 'PBKDF2',
                    salt: salt,
                    iterations: 2048,
                    hash: 'SHA-512'
                }, key, 512);
                let hex = '';
                let u8 = new Uint8Array(bits);
                for (let b of u8) hex += b.toString(16).padStart(2, '0');
                return hex;
            }

            // Derive Target Addresses for a seed
            function deriveAddressesForPath(seedHex, pathMode) {
                let I = CryptoJS.HmacSHA512(CryptoJS.enc.Hex.parse(seedHex), 'Bitcoin seed').toString();
                let k = I.substring(0, 64);
                let c = I.substring(64, 128);

                let pathsToTest = [];
                if (pathMode === 'BIP84') pathsToTest.push({ name: 'm/84\\'/0\\'/0\\'/0/0', type: 'SEGWIT', path: [84|0x80000000, 0|0x80000000, 0|0x80000000, 0, 0] });
                else if (pathMode === 'BIP49') pathsToTest.push({ name: 'm/49\\'/0\\'/0\\'/0/0', type: 'P2SH', path: [49|0x80000000, 0|0x80000000, 0|0x80000000, 0, 0] });
                else if (pathMode === 'BIP44') pathsToTest.push({ name: 'm/44\\'/0\\'/0\\'/0/0', type: 'LEGACY', path: [44|0x80000000, 0|0x80000000, 0|0x80000000, 0, 0] });
                else if (pathMode === 'ETH') pathsToTest.push({ name: 'm/44\\'/60\\'/0\\'/0/0', type: 'ETH', path: [44|0x80000000, 60|0x80000000, 0|0x80000000, 0, 0] });
                else {
                    // AUTO: test all primary paths
                    pathsToTest.push({ name: 'm/84\\'/0\\'/0\\'/0/0', type: 'SEGWIT', path: [84|0x80000000, 0|0x80000000, 0|0x80000000, 0, 0] });
                    pathsToTest.push({ name: 'm/49\\'/0\\'/0\\'/0/0', type: 'P2SH', path: [49|0x80000000, 0|0x80000000, 0|0x80000000, 0, 0] });
                    pathsToTest.push({ name: 'm/44\\'/0\\'/0\\'/0/0', type: 'LEGACY', path: [44|0x80000000, 0|0x80000000, 0|0x80000000, 0, 0] });
                    pathsToTest.push({ name: 'm/44\\'/60\\'/0\\'/0/0', type: 'ETH', path: [44|0x80000000, 60|0x80000000, 0|0x80000000, 0, 0] });
                }

                let results = [];
                for (let p of pathsToTest) {
                    let curK = k, curC = c;
                    for (let idx of p.path) {
                        let step = ckdPriv(curK, curC, idx);
                        curK = step.k;
                        curC = step.c;
                    }
                    let key = secp256k1.keyFromPrivate(curK, 'hex');
                    let compPub = key.getPublic(true, 'hex');
                    let sha = CryptoJS.SHA256(CryptoJS.enc.Hex.parse(compPub));
                    let rip = CryptoJS.RIPEMD160(sha).toString();

                    let addr = '';
                    if (p.type === 'SEGWIT') {
                        addr = encodeSegwitBech32(rip);
                    } else if (p.type === 'LEGACY') {
                        addr = base58Check('00', rip);
                    } else if (p.type === 'P2SH') {
                        let redeem = '0014' + rip;
                        let rSha = CryptoJS.SHA256(CryptoJS.enc.Hex.parse(redeem));
                        let rRip = CryptoJS.RIPEMD160(rSha).toString();
                        addr = base58Check('05', rRip);
                    } else if (p.type === 'ETH') {
                        let uncompPub = key.getPublic(false, 'hex').substring(2); // 64 bytes
                        // keccak256
                        let kHash = CryptoJS.SHA3(CryptoJS.enc.Hex.parse(uncompPub), { outputLength: 256 }).toString();
                        addr = '0x' + kHash.substring(24);
                    }
                    results.push({ pathName: p.name, addr: addr, privKeyHex: curK });
                }
                return results;
            }

            self.onmessage = async function(e) {
                const { workerId, missingIndices, knownIndices, wordCount, targetAddr, pathMode, passphrase, sliceStart, sliceEnd } = e.data;
                const targetClean = (targetAddr || '').trim().toLowerCase();
                const isSingleMissing = (missingIndices.length === 1);
                let localTested = 0;

                if (isSingleMissing) {
                    const mPos = missingIndices[0];
                    const testArray = [...knownIndices];
                    for (let w = sliceStart; w <= sliceEnd; w++) {
                        testArray[mPos] = w;
                        if (!fastValidateChecksum(testArray, wordCount)) continue;

                        localTested++;
                        const mnemonic = testArray.map(idx => BIP39_WORDS[idx]).join(' ');
                        const seedHex = await deriveSeed(mnemonic, passphrase);
                        const addrs = deriveAddressesForPath(seedHex, pathMode);

                        if (targetClean) {
                            for (let a of addrs) {
                                if (a.addr.toLowerCase() === targetClean) {
                                    self.postMessage({ type: 'FOUND', mnemonic, pathName: a.pathName, addr: a.addr, privKeyHex: a.privKeyHex });
                                    return;
                                }
                            }
                        } else {
                            // Hedef adres yoksa bulunan adayı ana thread'e bildir
                            self.postMessage({ type: 'CANDIDATE', mnemonic, word: BIP39_WORDS[w], addr: addrs[0].addr, privKeyHex: addrs[0].privKeyHex });
                        }

                        if (localTested % 10 === 0) {
                            self.postMessage({ type: 'PROGRESS', count: 10 });
                        }
                    }
                    self.postMessage({ type: 'DONE', count: localTested });
                } else if (missingIndices.length === 2) {
                    const p1 = missingIndices[0];
                    const p2 = missingIndices[1];
                    const testArray = [...knownIndices];

                    for (let w1 = sliceStart; w1 <= sliceEnd; w1++) {
                        testArray[p1] = w1;
                        for (let w2 = 0; w2 < 2048; w2++) {
                            testArray[p2] = w2;
                            if (!fastValidateChecksum(testArray, wordCount)) continue;

                            localTested++;
                            const mnemonic = testArray.map(idx => BIP39_WORDS[idx]).join(' ');
                            const seedHex = await deriveSeed(mnemonic, passphrase);
                            const addrs = deriveAddressesForPath(seedHex, pathMode);

                            if (targetClean) {
                                for (let a of addrs) {
                                    if (a.addr.toLowerCase() === targetClean) {
                                        self.postMessage({ type: 'FOUND', mnemonic, pathName: a.pathName, addr: a.addr, privKeyHex: a.privKeyHex });
                                        return;
                                    }
                                }
                            }

                            if (localTested % 20 === 0) {
                                self.postMessage({ type: 'PROGRESS', count: 20 });
                            }
                        }
                    }
                    self.postMessage({ type: 'DONE', count: localTested });
                }
            };
        `;

        const workerBlobUrl = URL.createObjectURL(new Blob([workerScriptSource], { type: 'application/javascript' }));

        function startRecovery() {
            if (isSearching) return;

            // 1. Kelimeleri doğrula ve eksikleri bul
            const missingIndices = [];
            const knownIndices = [];
            const invalidWords = [];

            for (let i = 1; i <= currentWordCount; i++) {
                const val = document.getElementById(`wordInput_${i}`).value.trim().toLowerCase();
                if (!val || val === '?' || val === '*') {
                    missingIndices.push(i - 1);
                    knownIndices.push(-1);
                } else if (BIP39_MAP.has(val)) {
                    knownIndices.push(BIP39_MAP.get(val));
                } else {
                    invalidWords.push({ index: i, word: val });
                }
            }

            if (invalidWords.length > 0) {
                alert(`Lütfen önce geçersiz kelimeleri düzeltin: ${invalidWords.map(w => '#' + w.index + ' ' + w.word).join(', ')}`);
                return;
            }

            if (missingIndices.length === 0) {
                alert('Tüm kelimeler zaten dolu! Eğer cüzdanınız açılmıyorsa "Harf Hatası" veya "Karışık Sıra" sekmesini deneyin.');
                return;
            }

            if (missingIndices.length > 2) {
                alert('⚠️ Güvenlik ve performans gereği tarayıcı içi hızlı kurtarma 1 veya 2 eksik kelime için optimize edilmiştir. 3 ve daha fazla eksik kelime trilyonlarca kombinasyon gerektirir.');
                return;
            }

            const targetAddr = document.getElementById('targetAddressInput').value.trim();
            const pathMode = document.getElementById('pathSelect').value;
            const passphrase = document.getElementById('passphraseInput').value;

            if (missingIndices.length === 2 && !targetAddr) {
                alert('⚠️ 2 eksik kelime kurtarırken hedef cüzdan adresini (bc1q..., 0x..., 1... veya 3...) girmelisiniz!');
                return;
            }

            // Başlat
            isSearching = true;
            document.getElementById('btnStartSearch').style.display = 'none';
            document.getElementById('btnStopSearch').style.display = 'inline-block';
            document.getElementById('dashboard').style.display = 'grid';
            document.getElementById('progressWrap').style.display = 'block';

            if (!targetAddr && missingIndices.length === 1) {
                document.getElementById('resultsTableContainer').style.display = 'block';
                document.getElementById('resultsTableBody').innerHTML = '';
            }

            const threadCount = parseInt(document.getElementById('threadSelect').value, 10) || 4;
            const totalPerms = missingIndices.length === 1 ? 2048 : (2048 * 2048);
            totalToTest = Math.round(totalPerms / 16); // Checksum pruning ile geçerli olanlar
            totalTested = 0;
            searchStartTime = Date.now();

            activeWorkers = [];
            const sliceSize = Math.ceil(2048 / threadCount);

            for (let i = 0; i < threadCount; i++) {
                const w = new Worker(workerBlobUrl);
                const sStart = i * sliceSize;
                const sEnd = Math.min(2047, (i + 1) * sliceSize - 1);

                w.onmessage = function(e) {
                    const data = e.data;
                    if (data.type === 'PROGRESS') {
                        totalTested += data.count;
                        updateProgressUI();
                    } else if (data.type === 'FOUND') {
                        stopRecovery();
                        showVictory(data);
                    } else if (data.type === 'CANDIDATE') {
                        addCandidateRow(data);
                    }
                };

                w.postMessage({
                    workerId: i,
                    missingIndices,
                    knownIndices,
                    wordCount: currentWordCount,
                    targetAddr,
                    pathMode,
                    passphrase,
                    sliceStart: sStart,
                    sliceEnd: sEnd
                });
                activeWorkers.push(w);
            }

            searchInterval = setInterval(updateStatsTimer, 500);
        }

        function stopRecovery() {
            isSearching = false;
            activeWorkers.forEach(w => w.terminate());
            activeWorkers = [];
            clearInterval(searchInterval);
            document.getElementById('btnStartSearch').style.display = 'inline-block';
            document.getElementById('btnStopSearch').style.display = 'none';
        }

        function updateProgressUI() {
            const pct = Math.min(100, Math.round((totalTested / totalToTest) * 100));
            document.getElementById('progressBar').style.width = pct + '%';
            document.getElementById('statTested').innerText = `${totalTested.toLocaleString()} / ~${totalToTest.toLocaleString()}`;
        }

        function updateStatsTimer() {
            const elapsed = Math.max(1, Math.floor((Date.now() - searchStartTime) / 1000));
            const speed = Math.round(totalTested / elapsed);
            document.getElementById('statSpeed').innerText = `${speed.toLocaleString()} tohum/s`;

            const m = Math.floor(elapsed / 60).toString().padStart(2, '0');
            const s = (elapsed % 60).toString().padStart(2, '0');
            document.getElementById('statTime').innerText = `${m}:${s}`;

            if (speed > 0 && totalToTest > totalTested) {
                const remSec = Math.round((totalToTest - totalTested) / speed);
                const rm = Math.floor(remSec / 60).toString().padStart(2, '0');
                const rs = (remSec % 60).toString().padStart(2, '0');
                document.getElementById('statETA').innerText = `${rm}:${rs}`;
            } else {
                document.getElementById('statETA').innerText = '00:00';
            }
        }

        function showVictory(data) {
            document.getElementById('recoveredSeedText').innerText = data.mnemonic;
            document.getElementById('recoveredAddrText').innerText = data.addr;
            document.getElementById('recoveredPathText').innerText = data.pathName || "m/84'/0'/0'/0/0";
            document.getElementById('recoveredPrivText').innerText = '0x' + data.privKeyHex;
            document.getElementById('victoryModal').style.display = 'flex';
        }

        function closeVictoryModal() {
            document.getElementById('victoryModal').style.display = 'none';
        }

        function openDonateModal() {
            document.getElementById('donateModal').style.display = 'flex';
        }
        function closeDonateModal() {
            document.getElementById('donateModal').style.display = 'none';
        }

        let candCount = 0;
        function addCandidateRow(data) {
            candCount++;
            document.getElementById('resultsCount').innerText = `${candCount} adet`;
            const tbody = document.getElementById('resultsTableBody');
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${candCount}</td>
                <td><strong style="color:#fbbf24;">${data.word}</strong></td>
                <td style="font-family:monospace; color:#34d399;">${data.mnemonic}</td>
                <td style="font-family:monospace; color:#38bdf8;">${data.addr}</td>
                <td><button class="btn-copy" onclick="copyToClipboard('${data.mnemonic}', this)">Kopyala</button></td>
            `;
            tbody.appendChild(tr);
        }

        function copyToClipboard(text, btn) {
            navigator.clipboard.writeText(text).then(() => {
                const orig = btn.innerText;
                btn.innerText = '✓ Kopyalandı!';
                btn.style.color = '#34d399';
                setTimeout(() => {
                    btn.innerText = orig;
                    btn.style.color = '';
                }, 2000);
            });
        }
    </script>
</body>
</html>'''

with open(os.path.join(target_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Successfully generated index.html ({len(html_template):,} bytes) in {target_dir}")
