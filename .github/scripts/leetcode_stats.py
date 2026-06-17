# -*- coding: utf-8 -*-
# 掃描 leetcode repo 的解題檔，產生每月刷題統計寫進 README。
# 解題月份判定：檔名有 YYYYMMDD_ 前綴就用前綴，否則用 git 第一次加入該檔的日期。
# 由 .github/workflows/leetcode-stats.yml 在每次 push *.py 時自動執行。
import os, re, subprocess, collections, sys

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

REPO = os.environ.get('REPO_DIR') or '.'
START = '<!-- LEETCODE-STATS:START -->'
END = '<!-- LEETCODE-STATS:END -->'
date_pat = re.compile(r'^(\d{4})(\d{2})\d{2}_')

def git_first_month(relpath):
    """回傳該檔最早一次被加入的 YYYY-MM；查不到回 'unknown'。"""
    try:
        out = subprocess.run(
            ['git', '-C', REPO, 'log', '--diff-filter=A', '--format=%ad',
             '--date=format:%Y-%m', '--', relpath],
            capture_output=True, text=True)
        rows = [r for r in out.stdout.strip().splitlines() if r.strip()]
        return rows[-1] if rows else 'unknown'
    except Exception:
        return 'unknown'

entries = []  # (ym, problem, filename)
for name in sorted(os.listdir(REPO)):
    p = os.path.join(REPO, name)
    if not os.path.isdir(p) or name.startswith('.'):
        continue
    for f in sorted(os.listdir(p)):
        if not f.endswith('.py'):
            continue
        m = date_pat.match(f)
        ym = (m.group(1) + '-' + m.group(2)) if m else git_first_month(name + '/' + f)
        entries.append((ym, name, f))

by_month = collections.defaultdict(list)
for ym, prob, f in entries:
    by_month[ym].append(prob)
problems = sorted(set(prob for _, prob, _ in entries))

lines = [START,
         '## 刷題統計（GitHub Action 自動產生，請勿手改此區）',
         '',
         '- 解題數（不同題目）：{}'.format(len(problems)),
         '- 解答檔總數：{}'.format(len(entries)),
         '',
         '| 月份 | 題數 | 題目 |',
         '| --- | --- | --- |']
for ym in sorted(by_month, reverse=True):
    probs = sorted(set(by_month[ym]))
    lines.append('| {} | {} | {} |'.format(ym, len(probs), ', '.join(probs)))
lines.append('')
lines.append('_共 {} 題；本表每次 push 解題檔時自動更新。_'.format(len(problems)))
lines.append(END)
block = '\n'.join(lines)

readme = os.path.join(REPO, 'README.md')
content = open(readme, encoding='utf-8').read() if os.path.exists(readme) else '# leetcode\n'
if START in content and END in content:
    content = re.sub(re.escape(START) + r'.*?' + re.escape(END), lambda mm: block, content, flags=re.S)
else:
    content = content.rstrip() + '\n\n' + block + '\n'
with open(readme, 'w', encoding='utf-8', newline='\n') as fh:
    fh.write(content)

print('problems:', len(problems), '| files:', len(entries), '| months:', sorted(by_month, reverse=True))
