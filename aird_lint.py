import os
import re
import sys
from pathlib import Path

# --- CONFIGURATION ---
L1_FILE = "llms.txt"
L3_MARKER = "ai-context:"

class AIRDLinter:
    def __init__(self, root_dir="."):
        self.root = Path(root_dir)
        self.report = {
            "L1": {"status": "PASS", "issues": []},
            "L2": {"status": "PASS", "issues": []},
            "L3": {"status": "PASS", "issues": []},
        }

    def check_l1(self):
        """Check Discovery Layer: Existence of llms.txt"""
        if not (self.root / L1_FILE).exists():
            self.report["L1"]["status"] = "FAIL"
            self.report["L1"]["issues"].append(f"Missing {L1_FILE} in root directory.")

    def check_l2_and_l3(self, file_path):
        """Check Structure and Context Layers for a markdown file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines()

            # L3: Check AI-Context Block (YAML frontmatter)
            if L3_MARKER not in content[:500]: # Look in the first 500 chars
                self.report["L3"]["status"] = "FAIL"
                self.report["L3"]["issues"].append(f"[{file_path}] Missing AI-Context Block at the top.")

            # L2: Check Heading Hierarchy (Simple jump check)
            last_level = 0
            for line in lines:
                if line.startswith('#'):
                    level = len(line) - len(line.lstrip('#'))
                    if level > 1 and (level - last_level > 1):
                        self.report["L2"]["status"] = "WARN"
                        self.report["L2"]["issues"].append(f"[{file_path}] Heading jump detected: H{last_level} -> H{level}")
                    last_level = level

    def run(self):
        self.check_l1()
        
        # Scan all .md files
        for md_file in self.root.rglob("*.md"):
            if "node_modules" in str(md_file) or ".git" in str(md_file):
                continue
            self.check_l2_and_l3(md_file)

        self.print_report()

    def print_report(self):
        print("\n" + "="*40)
        print(" 🦞 AIRD Compliance Report v1.0")
        print("="*40)
        
        for layer, data in self.report.items():
            status_icon = "✅" if data["status"] == "PASS" else "⚠️" if data["status"] == "WARN" else "❌"
            print(f"\n{status_icon} {layer} Layer: {data['status']}")
            for issue in data["issues"]:
                print(f"   - {issue}")
        
        print("\n" + "="*40)
        if self.report["L1"]["status"] == "PASS" and \
           self.report["L2"]["status"] == "PASS" and \
           self.report["L3"]["status"] == "PASS":
            print("RESULT: 🌟 FULLY AIRD-COMPLIANT")
        else:
            print("RESULT: 🛠 Improvements needed.")
        print("="*40 + "\n")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    linter = AIRDLinter(target)
    linter.run()
