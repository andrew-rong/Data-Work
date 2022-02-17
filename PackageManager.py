import importlib.util
import sys

packages = ['bs4', 'pandas', 'numpy','matplotlib', 'plotly', 'seaborn', 'statsmodels', 'sklearn']

for package in packages:
    if package in sys.modules:
        print(f"{package!r} already in sys.modules")
    elif (spec := importlib.util.find_spec(package)) is not None:
        module = importlib.util.module_from_spec(spec)
        sys.modules[package] = module
        spec.loader.exec_module(module)
        print(f"{package!r} has been imported")
    else:
        print(f"can't find the {package!r} module")
        