import argparse
import json
from recon.collector import collect_info

def main():
    parser = argparse.ArgumentParser(description = "AI-OSINT Recon Scanner CLI")
    parser.add_argument("--url", required=True, help="Target URL for scanning")
    args = parser.parse_args()

    result = collect_info(args.url)
    print(json.dumps(result, indent=4))  
      
if __name__ == "__main__":
    main()