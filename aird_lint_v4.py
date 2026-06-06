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
    "apikey": "API Key Management",
    "secret": "API Key Management",
    "permission": "Permission Management",
    "acl": "Permission Management",
    "install": "Environment Installation",
    "setup": "Initial Configuration",
    "requirements": "Environment Installation",
    "prerequisites": "Environment Installation",
    "environment": "Environment Installation",
    "deploy": "Deployment Guide",
    "docker": "Deployment Guide",
    "kubernetes": "Deployment Guide",
    "ci/cd": "Deployment Guide",
    "database": "Database Schema",
    "sql": "Database Schema",
    "schema": "Database Schema",
    "migration": "Database Schema",
    "api": "API Fundamentals",
    "endpoint": "API Fundamentals",
    "request": "API Fundamentals",
    "response": "API Fundamentals",
    "webhook": "API Fundamentals",
    "sdk": "API Fundamentals",
    "architecture": "System Architecture",
    "design": "System Architecture",
    "flow": "System Architecture",
    "diagram": "System Architecture",
    "error": "Troubleshooting Guide",
    "debug": "Troubleshooting Guide",
    "troubleshoot": "Troubleshooting Guide",
}

class AIRDLinterV4:
    def __init__(self, root_dir=".", suggest=False, fix=False, badge=False):
        self.root = Path(root_dir)
        self.suggest = suggest
        self.fix = fix
        self.badge = badge
        self.report = {
            "L1": {"status": "PASS", "issues": []},
            "L2": {"status": "PASS", "issues": []},
            "L3": {"status": "PASS", "issues": []},
        }

    def _get_suggested_prereqs(self, content):
        found = set()
        lower_content = content.lower()
        for kw, val in KEYWORD_MAP.items():
            if kw in lower_content:
                found.add(val)
        return list(found)

    def check_l1(self):
        l1_path = self.root / L1_FILE
        if not l1_path.exists():
            self.report["L1"]["status"] = "FAIL"
            md_files = [f.name for f in self.root.rglob("*.md")]
            links = "\n".join([f"- {f} (https://{self.root.name}/{f})" for f in md_files])
            scaffold = f"# {self.root.name} AI-Ready Docs\n\n## Core Documentation\n{links}"
            
            self.report["L1"]["issues"].append({"msg": f"Missing {L1_FILE}", "suggestion": f"Create {L1_FILE} with:\n\n{scaffold}"})
            if self.fix:
                with open(l1_path, 'w', encoding='utf-8') as f:
                    f.write(scaffold)
                self.report["L1"]["status"] = "FIXED"

    def check_l2_and_l3(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines()

        if L3_MARKER not in content[:500]:
            self.report["L3"]["status"] = "FAIL"
            topic = "General"
            for line in lines:
                if line.startswith('# '):
                    topic = line[2:].strip()
                    break
            prereqs = self._get_suggested_prereqs(content)
            context_block = f"---\nai-context:\n  topic: \"{topic}\"\n  prerequisites: {prereqs}\n  critical-warning: \"\"\n---\n\n"
            self.report["L3"]["issues"].append({"msg": f"[{file_path}] Missing AI-Context", "suggestion": context_block})
            if self.fix:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(context_block + content)
                self.report["L3"]["status"] = "FIXED"

        last_level = 0
        for idx, line in enumerate(lines):
            if line.startswith('#'):
                level = len(line) - len(line.lstrip('#'))
                if level > 1 and (level - last_level > 1):
                    self.report["L2"]["status"] = "WARN"
                    self.report["L2"]["issues"].append({"msg": f"[{file_path}] Heading jump H{last_level}->H{level} at line {idx+1}", "suggestion": "Insert intermediate heading."})
                last_level = level

    def generate_badge_url(self):
        """Generate a Shields.io badge URL based on current status."""
        # Logic: FULL (All PASS/FIXED), BASIC (L1+L3 PASS/FIXED), IN-PROGRESS (Else)
        l1_ok = self.report["L1"]["status"] in ["PASS", "FIXED"]
        l2_ok = self.report["L2"]["status"] in ["PASS", "FIXED"]
        l3_ok = self.report["L3"]["status"] in ["PASS", "FIXED"]
        
        if l1_ok and l2_ok and l3_ok:
            label, color, status = "AI-Ready", "brightgreen", "FULL"
        elif l1_ok and l3_ok:
            label, color, status = "AI-Ready", "yellow", "BASIC"
        else:
            label, color, status = "AI-Ready", "orange", "IN-PROGRESS"
            
        return f"https://img.shields.io/badge/{label}-{status}-{color}"

    def run(self):
        self.check_l1()
        for md_file in self.root.rglob("*.md"):
            if "node_modules" in str(md_file) or ".git" in str(md_file): continue
            self.check_l2_and_l3(md_file)
        self.print_report()

    def print_report(self):
        print("\n" + "="*60)
        print(" 🦞 AIRD Compliance Report v4.0 (Badge Edition)")
        print("="*60)
        for layer, data in self.report.items():
            icon = "✅" if data["status"] == "PASS" else "🔧" if data["status"] == "FIXED" else "⚠️" if data["status"] == "WARN" else "❌"
            print(f"\n{icon} {layer} Layer: {data['status']}")
            for issue in data["issues"]:
                print(f"   - {issue['msg']}")
                if self.suggest: print(f"     💡 {issue['suggestion']}")
        
        if self.badge:
            print(f"\n🌟 Recommended Badge: {self.generate_badge_url()}")
        
        print("\n" + "="*60)
        print(f"RESULT: {'🌟 FULLY AIRD-COMPLIANT' if all(d['status'] in ['PASS', 'FIXED'] for d in self.report.values()) else '🛠 Improvements needed.'}")
        print("="*60 + "\n")

if __name__ == "__main__":
    args = sys.argv[1:]
    target, suggest, fix, badge = ".", False, False, False
    if args:
        for arg in args:
            if arg == "--suggest": suggest = True
            elif arg == "--fix": fix = True
            elif arg == "--badge": badge = True
            elif not arg.startswith("-"): target = arg
    AIRDLinterV4(target, suggest, fix, badge).run()
