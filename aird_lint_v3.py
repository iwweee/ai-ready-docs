import os
import re
import sys
from pathlib import Path

# --- CONFIGURATION ---
L1_FILE = "llms.txt"
L3_MARKER = "ai-context:"

# Intelligence keywords for L3 prerequisites
KEYWORD_MAP = {
    "auth": "Authentication Setup",
    "login": "Authentication Setup",
    "token": "API Key Management",
    "install": "Environment Installation",
    "setup": "Initial Configuration",
    "deploy": "Deployment Guide",
    "database": "Database Schema",
    "sql": "Database Schema",
    "api": "API Fundamentals",
    "endpoint": "API Fundamentals",
}

class AIRDLinterV3:
    def __init__(self, root_dir=".", suggest=False, fix=False):
        self.root = Path(root_dir)
        self.suggest = suggest
        self.fix = fix
        self.report = {
            "L1": {"status": "PASS", "issues": []},
            "L2": {"status": "PASS", "issues": []},
            "L3": {"status": "PASS", "issues": []},
        }

    def _get_suggested_prereqs(self, content):
        """Intelligently suggest prerequisites based on keywords."""
        found = set()
        lower_content = content.lower()
        for kw, val in KEYWORD_MAP.items():
            if kw in lower_content:
                found.add(val)
        return list(found)

    def check_l1(self):
        """Check Discovery Layer: Existence of llms.txt"""
        l1_path = self.root / L1_FILE
        if not l1_path.exists():
            self.report["L1"]["status"] = "FAIL"
            issue = f"Missing {L1_FILE} in root directory."
            
            # Build content for suggestion/fix
            md_files = [f.name for f in self.root.rglob("*.md")]
            links = "\n".join([f"- {f} (https://{self.root.name}/{f})" for f in md_files])
            scaffold = f"# {self.root.name} AI-Ready Docs\n\n## Core Documentation\n{links}"
            
            suggestion = f"Create {L1_FILE} with following content:\n\n{scaffold}"
            self.report["L1"]["issues"].append({"msg": issue, "suggestion": suggestion})
            
            if self.fix:
                with open(l1_path, 'w', encoding='utf-8') as f:
                    f.write(scaffold)
                self.report["L1"]["status"] = "FIXED"

    def check_l2_and_l3(self, file_path):
        """Check Structure and Context Layers for a markdown file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines()

        # L3: AI-Context Block
        if L3_MARKER not in content[:500]:
            self.report["L3"]["status"] = "FAIL"
            
            # Guess topic from the first H1
            topic = "General"
            for line in lines:
                if line.startswith('# '):
                    topic = line[2:].strip()
                    break
            
            prereqs = self._get_suggested_prereqs(content)
            
            context_block = f"---\nai-context:\n  topic: \"{topic}\"\n  prerequisites: {prereqs}\n  critical-warning: \"\"\n---\n\n"
            
            issue = f"[{file_path}] Missing AI-Context Block at the top."
            suggestion = f"Add following block to the top of {file_path}:\n\n{context_block}"
            self.report["L3"]["issues"].append({"msg": issue, "suggestion": suggestion})
            
            if self.fix:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(context_block + content)
                self.report["L3"]["status"] = "FIXED"

        # L2: Heading Hierarchy
        last_level = 0
        for idx, line in enumerate(lines):
            if line.startswith('#'):
                level = len(line) - len(line.lstrip('#'))
                if level > 1 and (level - last_level > 1):
                    self.report["L2"]["status"] = "WARN"
                    issue = f"[{file_path}] Heading jump detected at line {idx+1}: H{last_level} -> H{level}"
                    suggestion = f"Insert an H{last_level+1} heading above line {idx+1}, or change line {idx+1} to H{last_level+1}."
                    self.report["L2"]["issues"].append({"msg": issue, "suggestion": suggestion})
                    # Fixing L2 automatically is risky as it changes content structure, 
                    # so we only warn/suggest for L2.
                last_level = level

    def run(self):
        self.check_l1()
        for md_file in self.root.rglob("*.md"):
            if "node_modules" in str(md_file) or ".git" in str(md_file):
                continue
            self.check_l2_and_l3(md_file)
        self.print_report()

    def print_report(self):
        print("\n" + "="*60)
        print(" 🦞 AIRD Compliance Report v3.0 (Pro Mode)")
        print("="*60)
        
        for layer, data in self.report.items():
            status_icon = "✅" if data["status"] == "PASS" else "🔧" if data["status"] == "FIXED" else "⚠️" if data["status"] == "WARN" else "❌"
            print(f"\n{status_icon} {layer} Layer: {data['status']}")
            for issue in data["issues"]:
                print(f"   - {issue['msg']}")
                if self.suggest and issue['suggestion']:
                    print(f"     💡 Suggestion: {issue['suggestion']}")
        
        print("\n" + "="*60)
        final_status = "🌟 FULLY AIRD-COMPLIANT" if all(d["status"] in ["PASS", "FIXED"] for d in self.report.values()) else "🛠 Improvements needed."
        print(f"RESULT: {final_status}")
        print("="*60 + "\n")

if __name__ == "__main__":
    args = sys.argv[1:]
    target = "."
    suggest = False
    fix = False
    
    if args:
        # Simple parser
        for arg in args:
            if arg == "--suggest": suggest = True
            elif arg == "--fix": fix = True
            elif not arg.startswith("-"): target = arg
            
    linter = AIRDLinterV3(target, suggest=suggest, fix=fix)
    linter.run()
