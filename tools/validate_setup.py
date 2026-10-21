#!/usr/bin/env python3
"""No-dependency static check for the Codex IT-company template. Python 3.11+."""
from __future__ import annotations
from pathlib import Path
import re
import sys
import tomllib

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ["AGENTS.md", "README.md", ".codex/config.toml", "workspace/STATUS.md",
            "playbooks/OPERATING_MODEL.md", "references/ROLE_ROUTING.md",
            "prompts/01-discovery.md", "templates/04_DETAILED_SRS.md"]
ERRORS = []

def error(message: str): ERRORS.append(message)

for item in REQUIRED:
    if not (ROOT / item).is_file(): error(f"Missing {item}")

agents = sorted((ROOT / ".codex/agents").glob("*.toml"))
skills = sorted((ROOT / ".agents/skills").glob("*/SKILL.md"))
if len(agents) < 12: error(f"Expected >=12 agents, got {len(agents)}")
if len(skills) < 10: error(f"Expected >=10 skills, got {len(skills)}")

names = set()
for f in [ROOT / ".codex/config.toml", *agents]:
    try:
        content=tomllib.loads(f.read_text(encoding="utf-8"))
        if f in agents:
            name=content.get("name")
            if not isinstance(name,str) or not name: error(f"Agent has no name: {f}")
            if name in names: error(f"Duplicate agent: {name}")
            names.add(name)
            if not content.get("developer_instructions"): error(f"No instructions: {f}")
    except Exception as ex:
        error(f"Invalid TOML {f.relative_to(ROOT)}: {ex}")

skill_names=set()
for f in skills:
    data=f.read_text(encoding="utf-8")
    if not data.startswith("---\n"):
        error(f"Missing YAML frontmatter {f}")
        continue
    front=data.split("---",2)[1]
    name=re.search(r"^name:\s*(\S+)",front,re.M)
    description=re.search(r"^description:\s*(.+)",front,re.M)
    if not name or not description: error(f"Missing name/description in {f}")
    elif name.group(1) != f.parent.name: error(f"Skill folder/name mismatch {f}")
    elif name.group(1) in skill_names: error(f"Duplicate skill {name.group(1)}")
    else: skill_names.add(name.group(1))

agent_root=(ROOT/'AGENTS.md').read_text(encoding='utf-8')
for mention in set(re.findall(r"\$([a-z][a-z0-9-]+)",agent_root)):
    if mention not in skill_names: error(f"AGENTS.md refers to missing skill ${mention}")

if ERRORS:
    print("INVALID TEMPLATE:")
    for err in ERRORS: print(" -",err)
    sys.exit(1)
print(f"OK: {len(agents)} agents, {len(skills)} skills, {len(list((ROOT/'templates').glob('*.md')))} templates, ")
print(f"    {len(list((ROOT/'prompts').glob('*.md')))} prompts. TOML, frontmatter and core references checked.")
print("NOTE: static validation does not simulate Codex multi-agent behavior or verify external service integrations.")
