import sys
path = r'C:\Users\Asus ExpertBook\.gemini\antigravity\scratch\AdamZeinAslam.github.io\_layouts\default.html'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
start = -1
end = -1
for i, line in enumerate(lines):
    if '<div class="social-links">' in line:
        start = i
    if start != -1 and '</div>' in line:
        end = i
        break
if start != -1 and end != -1:
    new_content = '        <div class="social-links">\n          <a href="https://github.com/AdamZeinAslam" target="_blank" rel="noopener noreferrer">GitHub</a>\n          <a href="https://www.linkedin.com/" target="_blank" rel="noopener noreferrer">LinkedIn</a>\n          <a href="mailto:YOUR_EMAIL@gmail.com">Email</a>\n          <a href="tel:+62XXXXXXXXXX" class="phone-link">Phone</a>\n        </div>\n'
    lines = lines[:start] + [new_content] + lines[end+1:]
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print('Updated successfully')
else:
    print('Tags not found')
