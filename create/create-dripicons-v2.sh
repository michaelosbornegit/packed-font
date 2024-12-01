# using package/project manager uv https://docs.astral.sh/uv/
# No idea why and don't want to spend more time on it, character code 173 errors. So I just skip it.
uv run create-font.py ../fonts/dripicons-16/dripicons-v2.ttf ../fonts/dripicons-16/dripicons-v2-16.json --size 16 --chars 0-172,174-200 --verbose
uv run pack-font.py ../fonts/dripicons-16/dripicons-v2-16.json