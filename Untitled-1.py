<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>A. Sai Kali Chakravarthi | CSE Student &amp; Developer Portfolio</title>
  <meta name="description" content="Portfolio of A. Sai Kali Chakravarthi — B.Tech Computer Science &amp; Engineering student at Jain University, Bengaluru. Interested in Software Development and Web Development." />
  <style>
    :root {
      --bg: #0b1120;
      --bg-elevated: #111827;
      --bg-card: rgba(17, 24, 39, 0.78);
      --bg-glass: rgba(15, 23, 42, 0.75);
      --border: rgba(148, 163, 184, 0.16);
      --border-hover: rgba(56, 189, 248, 0 .45);
      --text: #f1f5f9;
      --text-muted: #94a3b8;
      --text-soft: #cbd5e1;
      --accent: #38bdf8;
      --accent-2: #f59e0b;
      --accent-glow: rgba(56, 189, 248, 0.18);
      --success: #34d399;
      --shadow: 0 20px 50px rgba(2, 6, 23, 0.55);
      --radius: 18px;
      --radius-sm: 12px;
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Inter, "Helvetica Neue", Arial, sans-serif;
      --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
    }

    [data-theme="light"] {
      --bg: #f8fafc;
      --bg-elevated: #ffffff;
      --bg-card: rgba(255, 255, 255, 0.9);
      --bg-glass: rgba(248, 250, 252, 0.85);
      --border: rgba(15, 23, 42, 0.1);
      --border-hover: rgba(2, 132, 199, 0.45);
      --text: #0f172a;
      --text-muted: #475569;
      --text-soft: #334155;
      --accent: #0284c7;
      --accent-2: #d97706;
      --accent-glow: rgba(2, 132, 199, 0.14);
      --success: #059669;
      --shadow: 0 18px 40px rgba(15, 23, 42, 0.08);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      font-family: var(--font-sans);
      background: var(--bg);
      color: var(--text);
      line-height: 1.65;
      overflow-x: hidden;
      transition: background 0.3s ease, color 0.3s ease;
    }

    /* Ambient Background */
    .bg-grid {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: -2;
      background-image:
        linear-gradient(to right, var(--border) 1px, transparent 1px),
        linear-gradient(to bottom, var(--border) 1px, transparent 1px);
      background-size: 48px 48px;
      mask-image: radial-gradient(circle at 50% 20%, black 20%, transparent 78%);
      opacity: 0.45;
    }

    .bg-orb {
      position: fixed;
      border-radius: 50%;
      filter: blur(90px);
      pointer-events: none;
      z-index: -1;
      opacity: 0.35;
    }
    .bg-orb-1 {
      width: 420px;
      height: 420px;
      background: var(--accent);
      top: -120px;
      right: -80px;
    }
    .bg-orb-2 {
      width: 360px;
      height: 360px;
      background: var(--accent-2);
      bottom: -120px;
      left: -80px;
      opacity: 0.2;
    }

    a {
      color: inherit;
      text-decoration: none;
    }

    .container {
      width: min(1120px, 92%);
      margin: 0 auto;
    }

    /* Navigation */
    .navbar {
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      background: var(--bg-glass);
      border-bottom: 1px solid var(--border);
    }

    .nav-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 68px;
      gap: 16px;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 700;
      letter-spacing: -0.02em;
      font-size: 1.05rem;
    }

    .brand-badge {
      width: 34px;
      height: 34px;
      border-radius: 10px;
      display: grid;
      place-items: center;
      background: linear-gradient(135deg, var(--accent), var(--accent-2));
      color: #0b1120;
      font-weight: 800;
      font-family: var(--font-mono);
      font-size: 0.9rem;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 8px;
      list-style: none;
    }

    .nav-links a {
      padding: 8px 14px;
      border-radius: 10px;
      font-size: 0.92rem;
      font-weight: 500;
      color: var(--text-muted);
      transition: all 0.2s ease;
    }

    .nav-links a:hover,
    .nav-links a.active {
      color: var(--text);
      background: var(--accent-glow);
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .icon-btn {
      width: 40px;
      height: 40px;
      border-radius: 11px;
      border: 1px solid var(--border);
      background: var(--bg-elevated);
      color: var(--text);
      display: grid;
      place-items: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .icon-btn:hover {
      border-color: var(--border-hover);
      transform: translateY(-1px);
    }

    .menu-toggle {
      display: none;
    }

    /* Hero */
    .hero {
      padding: 72px 0 56px;
    }

    .hero-grid {
      display: grid;
      grid-template-columns: 1.25fr 0.85fr;
      gap: 48px;
      align-items: center;
    }

    .status-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      border-radius: 999px;
      border: 1px solid var(--border);
      background: var(--bg-card);
      font-size: 0.85rem;
      color: var(--text-soft);
      margin-bottom: 20px;
    }

    .status-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--success);
      box-shadow: 0 0 0 4px rgba(52, 211, 153, 0.2);
      animation: pulse 2s infinite;
    }

    @keyframes pulse {
      0%, 100% { box-shadow: 0 0 0 3px rgba(52, 211, 153, 0.2); }
      50% { box-shadow: 0 0 0 7px rgba(52, 211, 153, 0.05); }
    }

    .hero h1 {
      font-size: clamp(2.1rem, 4.3vw, 3.35rem);
      line-height: 1.12;
      letter-spacing: -0.03em;
      margin-bottom: 14px;
    }

    .gradient-text {
      background: linear-gradient(120deg, var(--accent), var(--accent-2));
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
    }

    .role-line {
      font-family: var(--font-mono);
      font-size: 1.05rem;
      color: var(--accent);
      min-height: 28px;
      margin-bottom: 18px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .cursor {
      display: inline-block;
      width: 2px;
      height: 1.1em;
      background: var(--accent);
      animation: blink 0.9s infinite;
    }

    @keyframes blink {
      0%, 49% { opacity: 1; }
      50%, 100% { opacity: 0; }
    }

    .hero-summary {
      color: var(--text-muted);
      font-size: 1.03rem;
      max-width: 58ch;
      margin-bottom: 28px;
    }

    .hero-ctas {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 28px;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 12px 20px;
      border-radius: 12px;
      font-weight: 600;
      font-size: 0.94rem;
      cursor: pointer;
      border: 1px solid transparent;
      transition: all 0.22s ease;
    }

    .btn-primary {
      background: linear-gradient(135deg, var(--accent), #0ea5e9);
      color: #081221;
      box-shadow: 0 10px 25px rgba(56, 189, 248, 0.25);
    }

    .btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 14px 30px rgba(56, 189, 248, 0.35);
    }

    .btn-secondary {
      background: var(--bg-elevated);
      border-color: var(--border);
      color: var(--text);
    }

    .btn-secondary:hover {
      border-color: var(--border-hover);
      transform: translateY(-2px);
    }

    .hero-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 18px;
      color: var(--text-muted);
      font-size: 0.9rem;
    }

    .hero-meta span {
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    /* Portrait Card */
    .portrait-wrap {
      position: relative;
      display: flex;
      justify-content: center;
    }

    .portrait-card {
      position: relative;
      width: min(360px, 100%);
      border-radius: 24px;
      padding: 12px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      transition: transform 0.35s ease;
    }

    .portrait-card:hover {
      transform: translateY(-4px);
    }

    .portrait-frame {
      position: relative;
      border-radius: 18px;
      overflow: hidden;
      aspect-ratio: 4 / 5;
      background: linear-gradient(145deg, #1e293b, #0f172a);
    }

    .portrait-frame img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 20%;
      display: block;
    }

    .portrait-fallback {
      position: absolute;
      inset: 0;
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 24px;
      background: radial-gradient(circle at top, rgba(56, 189, 248, 0.2), transparent 65%), #0f172a;
      color: #e2e8f0;
    }

    .portrait-fallback.visible {
      display: flex;
    }

    .fallback-initials {
      width: 88px;
      height: 88px;
      border-radius: 24px;
      display: grid;
      place-items: center;
      font-size: 2rem;
      font-weight: 800;
      font-family: var(--font-mono);
      background: linear-gradient(135deg, var(--accent), var(--accent-2));
      color: #0b1120;
      margin-bottom: 14px;
    }

    .portrait-caption {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 14px 8px 4px;
      font-size: 0.86rem;
      color: var(--text-muted);
    }

    .portrait-caption strong {
      color: var(--text);
      display: block;
      font-size: 0.94rem;
    }

    .float-chip {
      position: absolute;
      bottom: 84px;
      left: -18px;
      background: var(--bg-elevated);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 10px 14px;
      box-shadow: var(--shadow);
      font-size: 0.82rem;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .float-chip strong {
      display: block;
      color: var(--text);
      font-size: 0.9rem;
    }

    /* Sections */
    section {
      padding: 58px 0;
    }

    .section-header {
      display: flex;
      flex-wrap: wrap;
      align-items: flex-end;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 30px;
    }

    .section-tag {
      font-family: var(--font-mono);
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--accent);
      margin-bottom: 6px;
      display: block;
    }

    .section-title {
      font-size: clamp(1.55rem, 2.8vw, 2.1rem);
      letter-spacing: -0.02em;
    }

    .section-sub {
      color: var(--text-muted);
      max-width: 54ch;
      font-size: 0.95rem;
    }

    .card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 26px;
      box-shadow: var(--shadow);
      transition: border-color 0.25s ease, transform 0.25s ease;
    }

    .card:hover {
      border-color: var(--border-hover);
    }

    /* Quick Stats */
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-top: 12px;
    }

    .stat-box {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 18px 20px;
    }

    .stat-num {
      font-size: 1.65rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: var(--accent);
      font-family: var(--font-mono);
    }

    .stat-label {
      font-size: 0.86rem;
      color: var(--text-muted);
      margin-top: 4px;
    }

    /* Education */
    .edu-grid {
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      gap: 24px;
    }

    .edu-badge {
      display: inline-block;
      padding: 4px 10px;
      border-radius: 8px;
      font-size: 0.8rem;
      font-family: var(--font-mono);
      background: var(--accent-glow);
      color: var(--accent);
      margin-bottom: 12px;
    }

    .edu-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 14px;
      color: var(--text-soft);
      font-size: 0.92rem;
    }

    .progress-track {
      height: 10px;
      background: rgba(148, 163, 184, 0.16);
      border-radius: 999px;
      overflow: hidden;
      margin-top: 14px;
    }

    .progress-fill {
      height: 100%;
      border-radius: 999px;
      background: linear-gradient(90deg, var(--accent), var(--accent-2));
      width: 0;
      transition: width 1s ease;
    }

    .sgpa-bars {
      display: flex;
      flex-direction: column;
      gap: 16px;
      margin-top: 14px;
    }

    .sgpa-row-top {
      display: flex;
      justify-content: space-between;
      font-size: 0.92rem;
      margin-bottom: 6px;
    }

    .sgpa-row-top strong {
      font-family: var(--font-mono);
      color: var(--accent);
    }

    /* Skills */
    .filter-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .filter-btn {
      padding: 8px 15px;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: var(--bg-elevated);
      color: var(--text-muted);
      font-size: 0.88rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .filter-btn.active,
    .filter-btn:hover {
      background: var(--accent-glow);
      border-color: var(--border-hover);
      color: var(--text);
    }

    .skills-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(235px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }

    .skill-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 18px;
      transition: all 0.22s ease;
    }

    .skill-card:hover {
      border-color: var(--border-hover);
      transform: translateY(-2px);
    }

    .skill-card.hidden {
      display: none;
    }

    .skill-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }

    .skill-name {
      font-weight: 700;
      font-size: 1rem;
    }

    .level-pill {
      font-size: 0.74rem;
      font-family: var(--font-mono);
      padding: 3px 9px;
      border-radius: 999px;
      border: 1px solid var(--border);
    }

    .level-intermediate {
      color: var(--success);
      border-color: rgba(52, 211, 153, 0.35);
      background: rgba(52, 211, 153, 0.1);
    }

    .level-beginner {
      color: var(--accent);
      border-color: rgba(56, 189, 248, 0.35);
      background: rgba(56, 189, 248, 0.1);
    }

    .skill-cat {
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-bottom: 10px;
    }

    .mini-bar {
      height: 6px;
      background: rgba(148, 163, 184, 0.15);
      border-radius: 999px;
      overflow: hidden;
    }

    .mini-bar > span {
      display: block;
      height: 100%;
      border-radius: 999px;
      background: linear-gradient(90deg, var(--accent), var(--accent-2));
    }

    /* Core Knowledge Interactive Pills */
    .core-box {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      align-items: center;
    }

    .pill-group {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }

    .topic-pill {
      padding: 9px 14px;
      border-radius: 999px;
      border: 1px solid var(--border);
      background: var(--bg-elevated);
      color: var(--text-soft);
      font-size: 0.88rem;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .topic-pill.active,
    .topic-pill:hover {
      border-color: var(--accent);
      background: var(--accent-glow);
      color: var(--text);
    }

    .topic-detail {
      padding: 18px;
      border-radius: var(--radius-sm);
      background: var(--bg-elevated);
      border: 1px dashed var(--border-hover);
    }

    .topic-detail h4 {
      margin-bottom: 6px;
      color: var(--accent);
      font-size: 1rem;
    }

    .topic-detail p {
      font-size: 0.9rem;
      color: var(--text-muted);
    }

    /* Project Showcase */
    .project-card {
      display: grid;
      grid-template-columns: 1.05fr 0.95fr;
      gap: 28px;
      align-items: start;
    }

    .stage-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      border-radius: 999px;
      font-size: 0.78rem;
      font-family: var(--font-mono);
      background: rgba(245, 158, 11, 0.14);
      color: var(--accent-2);
      border: 1px solid rgba(245, 158, 11, 0.35);
      margin-bottom: 14px;
    }

    .tech-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin: 18px 0 22px;
    }

    .tech-tag {
      font-family: var(--font-mono);
      font-size: 0.8rem;
      padding: 5px 11px;
      border-radius: 8px;
      background: var(--bg-elevated);
      border: 1px solid var(--border);
      color: var(--text-soft);
    }

    .arch-explorer {
      background: var(--bg-elevated);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 18px;
    }

    .arch-tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 14px;
    }

    .arch-tab {
      padding: 7px 12px;
      border-radius: 8px;
      border: 1px solid var(--border);
      background: transparent;
      color: var(--text-muted);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .arch-tab.active {
      background: var(--accent-glow);
      border-color: var(--accent);
      color: var(--text);
    }

    .arch-panel {
      display: none;
      animation: fadeUp 0.25s ease;
    }

    .arch-panel.active {
      display: block;
    }

    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .arch-panel h4 {
      font-size: 1rem;
      margin-bottom: 6px;
      color: var(--accent);
    }

    .arch-panel p {
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-bottom: 10px;
    }

    .arch-list {
      list-style: none;
      display: grid;
      gap: 6px;
      font-size: 0.87rem;
      color: var(--text-soft);
    }

    .arch-list li::before {
      content: "→ ";
      color: var(--accent);
      font-family: var(--font-mono);
    }

    /* Achievements & Profile Info */
    .info-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
    }

    .info-card h3 {
      font-size: 1.08rem;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .chip-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 12px;
    }

    .chip {
      padding: 6px 12px;
      border-radius: 999px;
      background: var(--bg-elevated);
      border: 1px solid var(--border);
      font-size: 0.85rem;
      color: var(--text-soft);
    }

    /* Contact */
    .contact-grid {
      display: grid;
      grid-template-columns: 0.95fr 1.05fr;
      gap: 24px;
    }

    .contact-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding: 14px 16px;
      border-radius: var(--radius-sm);
      background: var(--bg-elevated);
      border: 1px solid var(--border);
      margin-bottom: 12px;
    }

    .contact-item small {
      display: block;
      color: var(--text-muted);
      font-size: 0.78rem;
    }

    .contact-item strong {
      font-size: 0.93rem;
      word-break: break-all;
    }

    .copy-btn {
      padding: 7px 12px;
      border-radius: 8px;
      border: 1px solid var(--border);
      background: transparent;
      color: var(--accent);
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
    }

    .copy-btn:hover {
      background: var(--accent-glow);
      border-color: var(--accent);
    }

    .form-group {
      margin-bottom: 14px;
    }

    .form-group label {
      display: block;
      font-size: 0.85rem;
      color: var(--text-soft);
      margin-bottom: 6px;
      font-weight: 500;
    }

    .form-group input,
    .form-group textarea {
      width: 100%;
      padding: 11px 14px;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: var(--bg-elevated);
      color: var(--text);
      font-family: inherit;
      font-size: 0.94rem;
      outline: none;
      transition: border-color 0.2s ease;
    }

    .form-group input:focus,
    .form-group textarea:focus {
      border-color: var(--accent);
    }

    /* Footer */
    footer {
      border-top: 1px solid var(--border);
      padding: 28px 0 40px;
      margin-top: 30px;
      color: var(--text-muted);
      font-size: 0.88rem;
    }

    .footer-inner {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }

    /* Toast */
    .toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--bg-elevated);
      color: var(--text);
      border: 1px solid var(--accent);
      padding: 12px 18px;
      border-radius: 12px;
      box-shadow: var(--shadow);
      font-size: 0.9rem;
      opacity: 0;
      transform: translateY(12px);
      pointer-events: none;
      transition: all 0.25s ease;
      z-index: 200;
    }

    .toast.show {
      opacity: 1;
      transform: translateY(0);
    }

    /* Scroll Reveal */
    .reveal {
      opacity: 0;
      transform: translateY(18px);
      transition: opacity 0.6s ease, transform 0.6s ease;
    }
    .reveal.visible {
      opacity: 1;
      transform: translateY(0);
    }

    /* Responsive */
    @media (max-width: 920px) {
      .hero-grid,
      .edu-grid,
      .core-box,
      .project-card,
      .contact-grid {
        grid-template-columns: 1fr;
      }
      .info-grid {
        grid-template-columns: 1fr;
      }
      .stats-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .portrait-wrap {
        order: -1;
      }
      .float-chip {
        left: 10px;
        bottom: 72px;
      }
    }

    @media (max-width: 720px) {
      .menu-toggle {
        display: grid;
      }
      .nav-links {
        position: absolute;
        top: 68px;
        left: 0;
        right: 0;
        flex-direction: column;
        background: var(--bg-elevated);
        border-bottom: 1px solid var(--border);
        padding: 14px;
        display: none;
      }
      .nav-links.open {
        display: flex;
      }
      .nav-links a {
        width: 100%;
        text-align: center;
      }
    }
  </style>
</head>
<body>
  <div class="bg-grid" aria-hidden="true"></div>
  <div class="bg-orb bg-orb-1" aria-hidden="true"></div>
  <div class="bg-orb bg-orb-2" aria-hidden="true"></div>

  <!-- Navbar -->
  <header class="navbar">
    <div class="container nav-inner">
      <a href="#top" class="brand">
        <span class="brand-badge">SC</span>
        <span>Sai Chakravarthi</span>
      </a>

      <ul class="nav-links" id="navLinks">
        <li><a href="#education">Education</a></li>
        <li><a href="#skills">Skills</a></li>
        <li><a href="#projects">Projects</a></li>
        <li><a href="#achievements">Achievements</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>

      <div class="nav-actions">
        <button class="icon-btn" id="themeToggle" aria-label="Toggle dark or light theme" title="Toggle theme">
          <span id="themeIcon">☀️</span>
        </button>
        <button class="icon-btn menu-toggle" id="menuToggle" aria-label="Toggle navigation menu">
          ☰
        </button>
      </div>
    </div>
  </header>

  <main id="top">
    <!-- Hero -->
    <section class="hero">
      <div class="container hero-grid">
        <div>
          <div class="status-pill">
            <span class="status-dot"></span>
            <span>B.Tech CSE (2nd Year, Sem 3) • Jain University</span>
          </div>

          <h1>Hi, I'm <span class="gradient-text">A. Sai Kali Chakravarthi</span></h1>

          <div class="role-line" aria-live="polite">
            <span id="typedRole"></span><span class="cursor"></span>
          </div>

          <p class="hero-summary">
            Second-year Computer Science and Engineering student at Jain University, Bengaluru.
            Interested in software development and web development, with foundational skills in
            Python, Java, SQL, and web technologies—eager to build practical skills through hands-on projects.
          </p>

          <div class="hero-ctas">
            <a href="#projects" class="btn btn-primary">Explore Project Architecture</a>
            <a href="#contact" class="btn btn-secondary">Get in Touch</a>
            <a href="https://github.com/chakravarthi000087-byte" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">GitHub ↗</a>
          </div>

          <div class="hero-meta">
            <span>📍 Hyderabad, Telangana</span>
            <span>🎓 Bengaluru (Jain University)</span>
            <span>🏆 Celestia Hackathon Finalist</span>
          </div>
        </div>

        <!-- Portrait -->
        <div class="portrait-wrap">
          <div class="portrait-card">
            <div class="portrait-frame">
              <img
                id="profilePhoto"
                src="profile.jpg"
                alt="Portrait of A. Sai Kali Chakravarthi"
                onerror="this.style.display='none'; document.getElementById('photoFallback').classList.add('visible');"
              />
              <div class="portrait-fallback" id="photoFallback">
                <div class="fallback-initials">AS</div>
                <strong>A. Sai Kali Chakravarthi</strong>
                <small style="color:#94a3b8; margin-top:6px;">
                  Place your photo as <code>profile.jpg</code> in the same folder as <code>index.html</code> to display it here.
                </small>
              </div>
            </div>

            <div class="float-chip">
              <span>⚡</span>
              <div>
                <strong>8.65 / 8.20 SGPA</strong>
                <span style="color:var(--text-muted)">Sem 1 &amp; Sem 2</span>
              </div>
            </div>

            <div class="portrait-caption">
              <div>
                <strong>A. Sai Kali Chakravarthi</strong>
                <span>B.Tech CSE • 2025–2029</span>
              </div>
              <a href="https://www.linkedin.com/in/anupati-sai-kali-chakravarthi-097178449" target="_blank" rel="noopener noreferrer" class="copy-btn">LinkedIn ↗</a>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Stats -->
      <div class="container stats-grid reveal">
        <div class="stat-box">
          <div class="stat-num">8.65</div>
          <div class="stat-label">Semester 1 SGPA</div>
        </div>
        <div class="stat-box">
          <div class="stat-num">8.20</div>
          <div class="stat-label">Semester 2 SGPA</div>
        </div>
        <div class="stat-box">
          <div class="stat-num">Finalist</div>
          <div class="stat-label">Celestia Hackathon</div>
        </div>
        <div class="stat-box">
          <div class="stat-num">3 Langs</div>
          <div class="stat-label">English • Telugu • Hindi</div>
        </div>
      </div>
    </section>

    <!-- Education -->
    <section id="education">
      <div class="container">
        <div class="section-header reveal">
          <div>
            <span class="section-tag">Academic Foundation</span>
            <h2 class="section-title">Education &amp; Performance</h2>
          </div>
          <p class="section-sub">Building strong computer science fundamentals alongside hands-on development practice.</p>
        </div>

        <div class="edu-grid reveal">
          <div class="card">
            <span class="edu-badge">2025 – 2029 (Expected)</span>
            <h3>Jain University, Bengaluru</h3>
            <p style="color:var(--text-soft); margin-top:4px; font-weight:500;">
              B.Tech in Computer Science and Engineering
            </p>
            <div class="edu-meta">
              <span>📘 Currently in 2nd Year, 3rd Semester</span>
              <span>💻 Focus: Software &amp; Web Development</span>
            </div>

            <div style="margin-top:22px;">
              <div style="display:flex; justify-content:space-between; font-size:0.86rem; color:var(--text-muted);">
                <span>Degree Progress (Semester 3 of 8)</span>
                <strong style="color:var(--text); font-family:var(--font-mono);">37.5%</strong>
              </div>
              <div class="progress-track">
                <div class="progress-fill" data-width="37.5%"></div>
              </div>
            </div>
          </div>

          <div class="card">
            <h3>Semester SGPA Breakdown</h3>
            <p style="font-size:0.88rem; color:var(--text-muted);">Consistent academic performance across core engineering semesters.</p>

            <div class="sgpa-bars">
              <div>
                <div class="sgpa-row-top">
                  <span>Semester 1</span>
                  <strong>8.65 / 10</strong>
                </div>
                <div class="progress-track" style="margin-top:0;">
                  <div class="progress-fill" data-width="86.5%"></div>
                </div>
              </div>

              <div>
                <div class="sgpa-row-top">
                  <span>Semester 2</span>
                  <strong>8.20 / 10</strong>
                </div>
                <div class="progress-track" style="margin-top:0;">
                  <div class="progress-fill" data-width="82%"></div>
                </div>
              </div>

              <div>
                <div class="sgpa-row-top">
                  <span>Semester 3</span>
                  <strong style="color:var(--accent-2);">In Progress</strong>
                </div>
                <div class="progress-track" style="margin-top:0;">
                  <div class="progress-fill" data-width="45%"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Skills -->
    <section id="skills">
      <div class="container">
        <div class="section-header reveal">
          <div>
            <span class="section-tag">Technical Stack</span>
            <h2 class="section-title">Skills &amp; Core Knowledge</h2>
          </div>

          <div class="filter-bar" role="tablist" aria-label="Filter skills by category">
            <button class="filter-btn active" data-filter="all">All</button>
            <button class="filter-btn" data-filter="languages">Languages</button>
            <button class="filter-btn" data-filter="web">Web</button>
            <button class="filter-btn" data-filter="tools">Dev Tools</button>
          </div>
        </div>

        <div class="skills-grid reveal" id="skillsGrid">
          <div class="skill-card" data-category="languages">
            <div class="skill-top">
              <span class="skill-name">Python</span>
              <span class="level-pill level-beginner">Beginner</span>
            </div>
            <div class="skill-cat">Programming Language</div>
            <div class="mini-bar"><span style="width:45%"></span></div>
          </div>

          <div class="skill-card" data-category="languages">
            <div class="skill-top">
              <span class="skill-name">Java</span>
              <span class="level-pill level-beginner">Beginner</span>
            </div>
            <div class="skill-cat">Programming Language</div>
            <div class="mini-bar"><span style="width:45%"></span></div>
          </div>

          <div class="skill-card" data-category="languages">
            <div class="skill-top">
              <span class="skill-name">SQL</span>
              <span class="level-pill level-beginner">Beginner</span>
            </div>
            <div class="skill-cat">Database Querying</div>
            <div class="mini-bar"><span style="width:45%"></span></div>
          </div>

          <div class="skill-card" data-category="web">
            <div class="skill-top">
              <span class="skill-name">HTML</span>
              <span class="level-pill level-beginner">Beginner</span>
            </div>
            <div class="skill-cat">Web Technologies</div>
            <div class="mini-bar"><span style="width:50%"></span></div>
          </div>

          <div class="skill-card" data-category="web">
            <div class="skill-top">
              <span class="skill-name">CSS</span>
              <span class="level-pill level-beginner">Beginner</span>
            </div>
            <div class="skill-cat">Web Technologies</div>
            <div class="mini-bar"><span style="width:48%"></span></div>
          </div>

          <div class="skill-card" data-category="tools">
            <div class="skill-top">
              <span class="skill-name">VS Code</span>
              <span class="level-pill level-intermediate">Intermediate</span>
            </div>
            <div class="skill-cat">Development Tool</div>
            <div class="mini-bar"><span style="width:76%"></span></div>
          </div>

          <div class="skill-card" data-category="tools">
            <div class="skill-top">
              <span class="skill-name">Git / GitHub</span>
              <span class="level-pill level-intermediate">Intermediate</span>
            </div>
            <div class="skill-cat">Version Control</div>
            <div class="mini-bar"><span style="width:74%"></span></div>
          </div>

          <div class="skill-card" data-category="tools">
            <div class="skill-top">
              <span class="skill-name">Google Colab</span>
              <span class="level-pill level-intermediate">Intermediate</span>
            </div>
            <div class="skill-cat">Cloud Notebook Environment</div>
            <div class="mini-bar"><span style="width:72%"></span></div>
          </div>
        </div>

        <!-- Core CS Knowledge Interactive Explorer -->
        <div class="card core-box reveal">
          <div>
            <h3 style="margin-bottom:8px;">Core Computer Science Knowledge</h3>
            <p style="font-size:0.9rem; color:var(--text-muted); margin-bottom:14px;">
              Click any subject to explore how it supports my software &amp; web engineering journey.
            </p>
            <div class="pill-group" id="corePills">
              <button class="topic-pill active" data-topic="oop">Object-Oriented Programming (OOP)</button>
              <button class="topic-pill" data-topic="dsa">Data Structures</button>
              <button class="topic-pill" data-topic="os">Operating Systems</button>
              <button class="topic-pill" data-topic="stats">Statistics</button>
              <button class="topic-pill" data-topic="prob">Probability</button>
            </div>
          </div>

          <div class="topic-detail" id="topicDetail">
            <h4>Object-Oriented Programming (OOP)</h4>
            <p>Designing modular, reusable code using classes, encapsulation, inheritance, and polymorphism—applied with Java and Python.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Projects -->
    <section id="projects">
      <div class="container">
        <div class="section-header reveal">
          <div>
            <span class="section-tag">Featured Project</span>
            <h2 class="section-title">Projects &amp; System Design</h2>
          </div>
          <p class="section-sub">Interactive breakdown of the planned architecture and foundation for Trip Guide.</p>
        </div>

        <div class="card project-card reveal">
          <div>
            <span class="stage-badge">🛠️ Stage: Architecture &amp; Foundation</span>
            <h3 style="font-size:1.5rem; margin-bottom:10px;">Trip Guide – Travel Planning Platform</h3>
            <p style="color:var(--text-muted); font-size:0.97rem;">
              Designed a travel-planning platform to help users organize trips, create structured itineraries,
              and manage travel budgets and expenses. Planned with a modern full-stack architecture combining
              Next.js, FastAPI, and PostgreSQL alongside map and weather integrations.
            </p>

            <div class="tech-tags">
              <span class="tech-tag">Next.js (Planned)</span>
              <span class="tech-tag">FastAPI (Planned)</span>
              <span class="tech-tag">PostgreSQL (Planned)</span>
              <span class="tech-tag">Map Integration</span>
              <span class="tech-tag">Weather API</span>
            </div>

            <div style="display:flex; flex-wrap:wrap; gap:12px;">
              <a href="https://jainsmartnavigation.ai.studio" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
                Visit Project Website ↗
              </a>
              <a href="https://github.com/chakravarthi000087-byte" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">
                GitHub Profile
              </a>
            </div>
          </div>

          <!-- Interactive Architecture Explorer -->
          <div class="arch-explorer">
            <div style="font-size:0.8rem; font-family:var(--font-mono); color:var(--text-muted); margin-bottom:10px;">
              INTERACTIVE ARCHITECTURE EXPLORER
            </div>
            <div class="arch-tabs" role="tablist">
              <button class="arch-tab active" data-arch="overview">Overview</button>
              <button class="arch-tab" data-arch="frontend">Frontend</button>
              <button class="arch-tab" data-arch="backend">Backend</button>
              <button class="arch-tab" data-arch="data">Database &amp; APIs</button>
            </div>

            <div class="arch-panel active" id="arch-overview">
              <h4>Core Platform Capabilities</h4>
              <p>End-to-end trip organization tailored for travelers managing schedules and costs in one place.</p>
              <ul class="arch-list">
                <li>Trip organization &amp; day-by-day itinerary builder</li>
                <li>Travel budget planning and expense tracking</li>
                <li>Unified architecture foundation ready for iterative buildout</li>
              </ul>
            </div>

            <div class="arch-panel" id="arch-frontend">
              <h4>Next.js Frontend Layer (Planned)</h4>
              <p>Responsive client experience for itinerary creation, budget dashboards, and interactive views.</p>
              <ul class="arch-list">
                <li>Clean route-based navigation for trips and expenses</li>
                <li>Interactive itinerary cards and expense summaries</li>
                <li>Responsive layout for desktop &amp; mobile travelers</li>
              </ul>
            </div>

            <div class="arch-panel" id="arch-backend">
              <h4>FastAPI Backend Layer (Planned)</h4>
              <p>Lightweight, structured Python API service handling core business logic and validation.</p>
              <ul class="arch-list">
                <li>REST endpoints for trips, itinerary items, and budgets</li>
                <li>Schema validation and modular service structure</li>
                <li>Proxy integration for external weather &amp; map services</li>
              </ul>
            </div>

            <div class="arch-panel" id="arch-data">
              <h4>PostgreSQL + Map &amp; Weather Integrations</h4>
              <p>Relational data persistence paired with location and live forecast context.</p>
              <ul class="arch-list">
                <li>PostgreSQL relational schema for users, trips, and expenses</li>
                <li>Map integration for destination &amp; route visualization</li>
                <li>Weather integration for smarter itinerary planning</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Achievements & Info -->
    <section id="achievements">
      <div class="container">
        <div class="section-header reveal">
          <div>
            <span class="section-tag">Beyond Academics</span>
            <h2 class="section-title">Achievements &amp; Profile</h2>
          </div>
        </div>

        <div class="info-grid reveal">
          <div class="card info-card">
            <h3>🏆 Celestia Hackathon</h3>
            <p style="color:var(--text-muted); font-size:0.93rem;">
              Participated in the <strong>Celestia Hackathon</strong>, advanced to the <strong>final round</strong>,
              and earned a participation certificate—strengthening rapid problem-solving and teamwork under deadlines.
            </p>
            <div class="chip-row">
              <span class="chip" style="border-color:rgba(245,158,11,0.4); color:var(--accent-2);">Final Round</span>
              <span class="chip">Certificate Earned</span>
            </div>
          </div>

          <div class="card info-card">
            <h3>🎯 Areas of Interest &amp; Soft Skills</h3>
            <p style="color:var(--text-muted); font-size:0.92rem;">
              Focused on turning foundational computer science concepts into clean, user-friendly software.
            </p>
            <div class="chip-row">
              <span class="chip">Software Development</span>
              <span class="chip">Web Development</span>
              <span class="chip">Communication</span>
              <span class="chip">Adaptability</span>
              <span class="chip">Time Management</span>
            </div>
          </div>

          <div class="card info-card">
            <h3>🌐 Languages Spoken</h3>
            <p style="color:var(--text-muted); font-size:0.92rem;">
              Comfortable collaborating in multilingual academic and team environments.
            </p>
            <div class="chip-row">
              <span class="chip">English</span>
              <span class="chip">Telugu</span>
              <span class="chip">Hindi</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact -->
    <section id="contact">
      <div class="container">
        <div class="section-header reveal">
          <div>
            <span class="section-tag">Connect</span>
            <h2 class="section-title">Get in Touch</h2>
          </div>
          <p class="section-sub">Open to internships, student collaborations, hackathons, and learning opportunities.</p>
        </div>

        <div class="contact-grid reveal">
          <div class="card">
            <div class="contact-item">
              <div>
                <small>Email</small>
                <strong>chakravarthi000087@gmail.com</strong>
              </div>
              <button class="copy-btn" data-copy="chakravarthi000087@gmail.com">Copy</button>
            </div>

            <div class="contact-item">
              <div>
                <small>Phone</small>
                <strong>+91 8143211120</strong>
              </div>
              <button class="copy-btn" data-copy="8143211120">Copy</button>
            </div>

            <div class="contact-item">
              <div>
                <small>LinkedIn</small>
                <strong>anupati-sai-kali-chakravarthi-097178449</strong>
              </div>
              <a class="copy-btn" href="https://www.linkedin.com/in/anupati-sai-kali-chakravarthi-097178449" target="_blank" rel="noopener noreferrer">Open ↗</a>
            </div>

            <div class="contact-item" style="margin-bottom:0;">
              <div>
                <small>GitHub</small>
                <strong>github.com/chakravarthi000087-byte</strong>
              </div>
              <a class="copy-btn" href="https://github.com/chakravarthi000087-byte" target="_blank" rel="noopener noreferrer">Open ↗</a>
            </div>
          </div>

          <form class="card" id="contactForm">
            <h3 style="margin-bottom:14px;">Send a Quick Message</h3>
            <div class="form-group">
              <label for="senderName">Your Name</label>
              <input id="senderName" type="text" placeholder="Enter your name" required />
            </div>
            <div class="form-group">
              <label for="senderEmail">Your Email</label>
              <input id="senderEmail" type="email" placeholder="you@example.com" required />
            </div>
            <div class="form-group">
              <label for="senderMessage">Message</label>
              <textarea id="senderMessage" rows="4" placeholder="Hi Sai, I'd love to connect about..." required></textarea>
            </div>
            <button type="submit" class="btn btn-primary" style="width:100%;">Compose Email to Sai</button>
          </form>
        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="container footer-inner">
      <span>© <span id="year"></span> A. Sai Kali Chakravarthi • Hyderabad, Telangana</span>
      <span>Built with clean HTML, CSS &amp; JavaScript</span>
    </div>
  </footer>

  <div class="toast" id="toast" role="status" aria-live="polite"></div>

  <script>
    // Year
    document.getElementById("year").textContent = new Date().getFullYear();

    // Theme Toggle
    const html = document.documentElement;
    const themeToggle = document.getElementById("themeToggle");
    const themeIcon = document.getElementById("themeIcon");
    const savedTheme = localStorage.getItem("sai-portfolio-theme");
    if (savedTheme) {
      html.setAttribute("data-theme", savedTheme);
      themeIcon.textContent = savedTheme === "light" ? "🌙" : "☀️";
    }

    themeToggle.addEventListener("click", () => {
      const next = html.getAttribute("data-theme") === "dark" ? "light" : "dark";
      html.setAttribute("data-theme", next);
      localStorage.setItem("sai-portfolio-theme", next);
      themeIcon.textContent = next === "light" ? "🌙" : "☀️";
    });

    // Mobile Menu
    const menuToggle = document.getElementById("menuToggle");
    const navLinks = document.getElementById("navLinks");
    menuToggle.addEventListener("click", () => navLinks.classList.toggle("open"));
    navLinks.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => navLinks.classList.remove("open"));
    });

    // Role Typing Effect
    const roles = [
      "B.Tech CSE Student @ Jain University",
      "Aspiring Software Developer",
      "Web Development Enthusiast",
      "Celestia Hackathon Finalist"
    ];
    const typedEl = document.getElementById("typedRole");
    let roleIdx = 0;
    let charIdx = 0;
    let deleting = false;

    function typeLoop() {
      const current = roles[roleIdx];
      if (!deleting) {
        typedEl.textContent = current.slice(0, ++charIdx);
        if (charIdx === current.length) {
          deleting = true;
          setTimeout(typeLoop, 1700);
          return;
        }
      } else {
        typedEl.textContent = current.slice(0, --charIdx);
        if (charIdx === 0) {
          deleting = false;
          roleIdx = (roleIdx + 1) % roles.length;
        }
      }
      setTimeout(typeLoop, deleting ? 36 : 62);
    }
    typeLoop();

    // Skills Filter
    const filterBtns = document.querySelectorAll(".filter-btn");
    const skillCards = document.querySelectorAll(".skill-card");

    filterBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        filterBtns.forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        const filter = btn.dataset.filter;
        skillCards.forEach((card) => {
          const match = filter === "all" || card.dataset.category === filter;
          card.classList.toggle("hidden", !match);
        });
      });
    });

    // Core Knowledge Interactive Switcher
    const coreTopics = {
      oop: {
        title: "Object-Oriented Programming (OOP)",
        desc: "Designing modular, reusable code using classes, encapsulation, inheritance, and polymorphism—applied with Java and Python."
      },
      dsa: {
        title: "Data Structures",
        desc: "Understanding arrays, linked lists, stacks, queues, trees, and algorithmic efficiency to solve programming challenges cleanly."
      },
      os: {
        title: "Operating Systems",
        desc: "Core concepts of processes, threads, scheduling, memory management, and file systems that power backend and application software."
      },
      stats: {
        title: "Statistics",
        desc: "Analyzing distributions, variance, and data patterns—helpful for reasoning about metrics, budgets, and computational models."
      },
      prob: {
        title: "Probability",
        desc: "Foundational mathematical reasoning for uncertainty, event modeling, and analytical problem solving in computer science."
      }
    };

    const topicDetail = document.getElementById("topicDetail");
    document.querySelectorAll(".topic-pill").forEach((pill) => {
      pill.addEventListener("click", () => {
        document.querySelectorAll(".topic-pill").forEach((p) => p.classList.remove("active"));
        pill.classList.add("active");
        const data = coreTopics[pill.dataset.topic];
        topicDetail.innerHTML = `<h4>${data.title}</h4><p>${data.desc}</p>`;
      });
    });

    // Project Architecture Tabs
    document.querySelectorAll(".arch-tab").forEach((tab) => {
      tab.addEventListener("click", () => {
        document.querySelectorAll(".arch-tab").forEach((t) => t.classList.remove("active"));
        document.querySelectorAll(".arch-panel").forEach((p) => p.classList.remove("active"));
        tab.classList.add("active");
        document.getElementById(`arch-${tab.dataset.arch}`).classList.add("active");
      });
    });

    // Toast + Copy to Clipboard
    const toast = document.getElementById("toast");
    let toastTimer;
    function showToast(msg) {
      toast.textContent = msg;
      toast.classList.add("show");
      clearTimeout(toastTimer);
      toastTimer = setTimeout(() => toast.classList.remove("show"), 2600);
    }

    document.querySelectorAll("[data-copy]").forEach((btn) => {
      btn.addEventListener("click", async () => {
        const value = btn.dataset.copy;
        try {
          await navigator.clipboard.writeText(value);
          showToast(`Copied: ${value}`);
        } catch {
          showToast(`Copy manually: ${value}`);
        }
      });
    });

    // Contact Form -> mailto
    document.getElementById("contactForm").addEventListener("submit", (e) => {
      e.preventDefault();
      const name = document.getElementById("senderName").value.trim();
      const email = document.getElementById("senderEmail").value.trim();
      const msg = document.getElementById("senderMessage").value.trim();
      const subject = encodeURIComponent(`Portfolio Inquiry from ${name}`);
      const body = encodeURIComponent(`Name: ${name}\nEmail: ${email}\n\n${msg}`);
      window.location.href = `mailto:chakravarthi000087@gmail.com?subject=${subject}&body=${body}`;
      showToast("Opening your email client...");
    });

    // Scroll Reveal & Animated Progress Bars
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          entry.target.querySelectorAll(".progress-fill[data-width]").forEach((bar) => {
            bar.style.width = bar.dataset.width;
          });
        }
      });
    }, { threshold: 0.14 });

    document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));
  </script>
</body>
</html>