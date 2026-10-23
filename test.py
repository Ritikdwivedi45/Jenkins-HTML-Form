from pathlib import Path

html = Path("index.html").read_text()

assert "<form" in html, "Form is missing"
assert 'name="name"' in html, "Name field is missing"
assert 'name="email"' in html, "Email field is missing"
assert 'name="contact"' in html, "Contact field is missing"
assert 'type="submit"' in html, "Submit button is missing"

print("All HTML form tests passed successfully!")