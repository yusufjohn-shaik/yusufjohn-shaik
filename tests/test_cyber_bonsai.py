import xml.etree.ElementTree as ET
import os
import sys

def test_svg_validity_and_structure():
    svg_path = "assets/cyber-bonsai.svg"
    assert os.path.exists(svg_path), f"{svg_path} does not exist"
    
    # Check valid XML parse
    tree = ET.parse(svg_path)
    root = tree.getroot()
    
    # Check root attributes
    assert root.tag.endswith('svg'), f"Expected svg root, got {root.tag}"
    assert "0 0 320 280" in root.attrib.get('viewBox', ''), f"Unexpected viewBox: {root.attrib.get('viewBox')}"
    
    # Check style and keyframes present
    with open(svg_path, 'r', encoding='utf-8') as f:
        content = f.read()
    assert "@keyframes" in content, "Missing @keyframes in SVG"
    assert "petal-drift" in content or "petal" in content, "Missing petal animation keyframes"
    assert "#38bdf8" in content, "Missing neon cyan palette (#38bdf8)"
    assert 'shape-rendering="crispEdges"' in content or 'crispEdges' in content, "Missing crispEdges rendering"

if __name__ == "__main__":
    try:
        test_svg_validity_and_structure()
        print("PASS")
    except AssertionError as e:
        print(f"FAIL: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(2)
