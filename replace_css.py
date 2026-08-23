import sys
import re

path = r'C:\Users\Asus ExpertBook\.gemini\antigravity\scratch\AdamZeinAslam.github.io\assets\css\style.css'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace profile-name font-size
content = re.sub(r'\.profile-name\s*\{\s*margin:\s*0\s*0\s*16px\s*0;\s*font-size:\s*36px;', r'.profile-name {\n  margin: 0 0 16px 0;\n\n  font-size: 28px;', content)

# Replace social links section
social_links_pattern = r'/\*\s*=========================================================\s*SOCIAL LINKS\s*=========================================================\s*\*/.*?/\*\s*=========================================================\s*PHONE ICON\s*=========================================================\s*\*/'

new_social_links = '''/* =========================================================
   SOCIAL LINKS
   ========================================================= */

.social-links {
  display: flex !important;
  flex-direction: row !important;
  flex-wrap: wrap !important;
  align-items: center !important;
  justify-content: flex-start !important;
  gap: 10px !important;
  margin: 10px 0 0 0 !important;
  padding: 0 !important;
}

.social-links a {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 6px 12px !important;
  border: 1px solid #d5d5d5 !important;
  border-radius: 4px !important;
  text-decoration: none !important;
  font-size: 12px !important;
  font-weight: 600 !important;
  color: #555555 !important;
  background: #ffffff !important;
  transition: all 0.2s ease !important;
}

.social-links a:hover {
  background: #f5f5f5 !important;
  border-color: #bcbcbc !important;
  color: #111111 !important;
}

/* =========================================================
   PHONE ICON
   ========================================================= */'''

content = re.sub(social_links_pattern, new_social_links, content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated CSS successfully')
