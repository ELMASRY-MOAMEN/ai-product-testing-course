import importlib.util
from pathlib import Path
P=Path(__file__).parents[1]/"scripts"/"validate_manifest.py"; s=importlib.util.spec_from_file_location("vm",P); vm=importlib.util.module_from_spec(s); s.loader.exec_module(vm)
def test_template_has_required_sections(): assert vm.validate(Path(__file__).parents[1]/"templates"/"evaluation-manifest.yaml")==[]
