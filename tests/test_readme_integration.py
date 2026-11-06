import os
import sys

def test_readme_references_cyber_bonsai():
    readme_path = "README.md"
    assert os.path.exists(readme_path), "README.md not found"
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    assert "assets/cyber-bonsai.svg" in content, "README does not reference assets/cyber-bonsai.svg"
    assert "media.giphy.com" not in content, "README still references external media.giphy.com"
    assert 'alt="Pixel-Art Cyber Bonsai"' in content, "Missing alt attribute 'Pixel-Art Cyber Bonsai'"

if __name__ == "__main__":
    try:
        test_readme_references_cyber_bonsai()
        print("PASS")
    except AssertionError as e:
        print(f"FAIL: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(2)
