# using package/project manager uv https://docs.astral.sh/uv/
uv run create-font.py ../fonts/dripicons-16/dripicons-v2.ttf ../fonts/dripicons-16/dripicons-v2-16.json --size 16 --verbose
uv run pack-font.py ../fonts/dripicons-16/dripicons-v2-16.json