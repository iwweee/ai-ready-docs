import os
import re
import sys
from pathlib import Path

# --- CONFIGURATION ---
L1_FILE = "llms.txt"
L3_MARKER = "ai-context:"
L4_FILE = ".ai-feedback.md"

# Weight mapping for AI-Ready Score
WEIGHTS = {
    "L1": 0.3,
    "L2": 0.2,
    "L3": 0.4,
    "L4": 0.1
}

class AIRDLinterV5:
    def __init__(self, root_dir=".", suggest=False, fix=False):
        self.root = Path(root_dir)
        self.suggest = suggest
        self.fix = fix
        self.report = {
            "L1": {"score": 0.0, "status": "PASS", "issues": []},
            "L2": {"score": 0.0, "status": "PASS", "issues": []},
            "L3": {"score": 0.0, "status": "PASS", "issues": []},
            "L4": {"score": 0.0, "status": "PASS", "issues": []},
        }
        self.all_files = list(self.root.rglob("*"))

    def _check_file_exists(self, path_str):
        clean_path = path_str.strip().strip("/")
        target = self.root / clean_path
        return target.exists()

    def check_l1(self):
        l1_path = self.root / L1_FILE
        if not l1_path.exists():
            self.report["L1"]["status"] = "FAIL"
            self.report["L1"]["score"] = 0.0
            self.report["L1"]["issues"].append({"msg": f"Missing {L1_FILE}", "suggestion": "Create llms.txt to provide a map for AI."})
            if self.fix:
                with open(l1_path, 'w', encoding='utf-8') as f:
                    f.write(f"# {self.root.name} AI-Ready Docs\n\n## Core Documentation\n- Documentation: [README.md](./README.md)")
                self.report["L1"]["status"] = "FIXED"
                self.report["L1"]["score"] = 1.0
        else:
            self.report["L1"]["score"] = 1.0

    def check_l2_and_l3(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines()

        if L3_MARKER not in content[:500]:
            self.report["L3"]["status"] = "FAIL"
            self.report["L3"]["issues"].append({"msg": f"[{file_path}] Missing AI-Context block", "suggestion": "Add ai-context block at the top."})
        else:
            prereq_match = re.search(r"prerequisites:\s*\[(.*?)\]", content)
            if prereq_match:
                prereqs = [p.strip().strip('"\'') for p in prereq_match.group(1).split(',') if p.strip()]
                for p in prereqs:
                    if not self._check_file_exists(p):
                        self.report["L3"]["status"] = "WARN"
                        self.report["L3"]["issues"].append({"msg": f"[{file_path}] Broken prerequisite: {p} not found", "suggestion": f"Ensure {p} exists or correct the path."})

        last_level = 0
        for idx, line in enumerate(lines):
            if line.startswith('#'):
                level = len(line) - len(line.lstrip('#'))
                if level > 1 and (level - last_level > 1):
                    self.report["L2"]["status"] = "WARN"
                    self.report["L2"]["issues"].append({"msg": f"[{file_path}] Heading jump H{last_level}->H{level} at line {idx+1}", "suggestion": "Insert intermediate heading."})
                last_level = level

    def check_l4(self):
        l4_path = self.root / L4_FILE
        if not l4_path.exists():
            self.report["L4"]["status"] = "FAIL"
            self.report["L4"]["score"] = 0.0
            self.report["L4"]["issues"].append({"msg": f"Missing {L4_FILE}", "suggestion": "Create .ai-feedback.md to enable L4 evolution."})
        else:
            self.report["L4"]["score"] = 1.0
            if l4_path.stat().st_size < 10:
                self.report["L4"]["status"] = "WARN"
                self.report["L4"]["issues"].append({"msg": f"{L4_FILE} is empty", "suggestion": "Start recording AI failure points."})

    def run(self):
        self.check_l1()
        md_files = [f for f in self.root.rglob("*.md") if not any(x in str(f) for x in [".git", "node_modules"])]
        total_md = len(md_files)
        l3_valid_count = 0
        for md_file in md_files:
            self.check_l2_and_l3(md_file)
            with open(md_file, 'r', encoding='utf-8') as f:
                if L3_MARKER in f.read(500):
                    l3_valid_count += 1
        self.check_l4()
        self.report["L3"]["score"] = (l3_valid_count / total_md) if total_md > 0 else 1.0
        l2_warns = len(self.report["L2"]["issues"])
        self.report["L2"]["score"] = max(0.0, 1.0 - (l2_warns * 0.1)) if total_md > 0 else 1.0
        final_score = sum(self.report[layer]["score"] * WEIGHTS[layer] for layer in WEIGHTS) * 100
        self.print_report(final_score)

    def print_report(self, score):
        print("\n" + "═"*60)
        print(f" 🦞 AIRD Compliance Report v5.0 | Score: {score:.1f}/100")
        print("═"*60)
        rank = "Elite" if score >= 90 else "High" if score >= 70 else "Medium" if score >= 50 else "Low"
        print(f"Overall Readiness Rank: {rank}")
        for layer, data in self.report.items():
            icon = "✅" if data["status"] == "PASS" else "⚠️" if data["status"] == "WARN" else "❌"
            print(f"\n{icon} {layer} Layer ({int(WEIGHTS[layer]*100)}%): {data['status']}")
            for issue in data["issues"]:
                print(f"   - {issue['msg']}")
                if self.suggest: print(f"     💡 {issue['suggestion']}")
        print("\n" + "═"*60)
        if score >= 90:
            print("🌟 RESULT: FULLY AI-READY (Evolutionary Stage)")
        elif score >= 70:
            print("🛠 RESULT: AI-COMPATIBLE (Minor optimizations needed)")
        else:
            print("⚠️ RESULT: HUMAN-CENTRIC (Significant AIRD upgrade required)")
        print("═"*60 + "\n")

if __name__ == "__main__":
    args = sys.argv[1:]
    target, suggest, fix = ".", False, False
    if args:
        for arg in args:
            if arg == "--suggest": suggest = True
            elif arg == "--fix": fix = True
            elif not arg.startswith("-"): target = arg
    AIRDLinterV5(target, suggest, fix).run()
