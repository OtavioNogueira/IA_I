with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the duplicate button
content = content.replace(
    '<button class="tab-btn" onclick="openTab(event, \'pmc2\')">PMC 2</button>\n        <button class="tab-btn" onclick="openTab(event, \'pmc2\')">PMC 2</button>',
    '<button class="tab-btn" onclick="openTab(event, \'pmc2\')">PMC 2</button>'
)

# Fix the duplicate tab content
# There are two blocks of <!-- TAB PMC 2 -->. We want to remove the first one entirely.
import re
# Find all occurrences of the PMC 2 block
pattern = re.compile(r'<!-- TAB PMC 2 -->.*?</div>\n\n\n    <!-- TAB PMC 2 -->', re.DOTALL)
content = pattern.sub('<!-- TAB PMC 2 -->', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Duplication fixed.")
