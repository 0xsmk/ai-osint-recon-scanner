
#  AI-OSINT Recon Scanner

**AI-OSINT Recon Scanner** is an intelligent vulnerability scanner that uses OSINT fingerprinting and AI analysis to select relevant security checks.  
Unlike classic scanners, it does not just run through a CVE database, but dynamically adapts tests to the specific technology stack of the target site.

---

##  Features
- Collect target information (HTML, headers, favicon, title).
- AI-based analysis of collected data → recommendations for security checks.
- Basic vulnerability tests: SQLi, XSS, weak security headers.
- CLI interface for running in the terminal.

---

##  Project Structure
```

ai-osint-recon-scanner/
│── cli/            # command-line interface entry point
│── recon/          # data collection (collector, parser)
│── ai/             # AI-based analysis and reporting
│── scanner/        # vulnerability tests
│── utils/          # helper utilities
│── webui/          # (optional) web interface

````

---

##  Installation
```bash
git clone https://github.com/<your-username>/ai-osint-recon-scanner.git
cd ai-osint-recon-scanner
pip install -r requirements.txt
````

---

##  Usage

Example:

```bash
python -m cli.main --url https://example.com
```

Output (JSON):

```json
{
    "url": "https://example.com",
    "status_code": 200,
    "title": "Example Domain",
    "favicon_hash": "abc123...",
    "headers": { ... }
}
```

AI analysis:

```
[AI Analyzer] Recommended tests:
- Check for Path Traversal
- Check for SQL Injection
```

---

##  Roadmap

* [x] CLI and data collection
* [ ] Basic AI analysis (if-logic)
* [ ] Add first tests (SQLi, XSS, headers)
* [ ] Integrate open-source LLM (Mistral 7B)
* [ ] Fine-tune model on CVE/Wappalyzer dataset
* [ ] Web interface for reports

---

##  Disclaimer

This project is created for educational purposes only.
The author is not responsible for any misuse of the tool against systems without explicit permission.

