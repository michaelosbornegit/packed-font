# using package/project manager uv https://docs.astral.sh/uv/
# No idea why and don't want to spend more time on it, character code 173 errors. So I just skip it.
# size 16
# split 1
uv run create-font.py ../fonts/dripicons/dripicons-v2-split1.ttf ../fonts/dripicons/dripicons-v2-16-split1.json --size 16 --chars 33-126 --verbose
uv run pack-font.py ../fonts/dripicons/dripicons-v2-16-split1.json
uv run generate-font-reference-image.py ../fonts/dripicons/ dripicons-v2-16-split1.tff
# split 2
uv run create-font.py ../fonts/dripicons/dripicons-v2-split2.ttf ../fonts/dripicons/dripicons-v2-16-split2.json --size 16 --chars 33-126 --verbose
uv run pack-font.py ../fonts/dripicons/dripicons-v2-16-split2.json
uv run generate-font-reference-image.py ../fonts/dripicons/ dripicons-v2-16-split2.tff
# split 3
uv run create-font.py ../fonts/dripicons/dripicons-v2-split3.ttf ../fonts/dripicons/dripicons-v2-16-split3.json --size 16 --chars 33-44 --verbose
uv run pack-font.py ../fonts/dripicons/dripicons-v2-16-split3.json
uv run generate-font-reference-image.py ../fonts/dripicons/ dripicons-v2-16-split3.tff

# size 24
# split 1
uv run create-font.py ../fonts/dripicons/dripicons-v2-split1.ttf ../fonts/dripicons/dripicons-v2-24-split1.json --size 24 --chars 33-126 --verbose
uv run pack-font.py ../fonts/dripicons/dripicons-v2-24-split1.json
uv run generate-font-reference-image.py ../fonts/dripicons/ dripicons-v2-24-split1.tff
# split 2
uv run create-font.py ../fonts/dripicons/dripicons-v2-split2.ttf ../fonts/dripicons/dripicons-v2-24-split2.json --size 24 --chars 33-126 --verbose
uv run pack-font.py ../fonts/dripicons/dripicons-v2-24-split2.json
uv run generate-font-reference-image.py ../fonts/dripicons/ dripicons-v2-24-split2.tff
# split 3
uv run create-font.py ../fonts/dripicons/dripicons-v2-split3.ttf ../fonts/dripicons/dripicons-v2-24-split3.json --size 24 --chars 33-44 --verbose
uv run pack-font.py ../fonts/dripicons/dripicons-v2-24-split3.json
uv run generate-font-reference-image.py ../fonts/dripicons/ dripicons-v2-24-split3.tff

# size 32
# split 1
uv run create-font.py ../fonts/dripicons/dripicons-v2-split1.ttf ../fonts/dripicons/dripicons-v2-32-split1.json --size 32 --chars 33-126 --verbose
uv run pack-font.py ../fonts/dripicons/dripicons-v2-32-split1.json
uv run generate-font-reference-image.py ../fonts/dripicons/ dripicons-v2-32-split1.tff
# split 2
uv run create-font.py ../fonts/dripicons/dripicons-v2-split2.ttf ../fonts/dripicons/dripicons-v2-32-split2.json --size 32 --chars 33-126 --verbose
uv run pack-font.py ../fonts/dripicons/dripicons-v2-32-split2.json
uv run generate-font-reference-image.py ../fonts/dripicons/ dripicons-v2-32-split2.tff
# split 3
uv run create-font.py ../fonts/dripicons/dripicons-v2-split3.ttf ../fonts/dripicons/dripicons-v2-32-split3.json --size 32 --chars 33-44 --verbose
uv run pack-font.py ../fonts/dripicons/dripicons-v2-32-split3.json
uv run generate-font-reference-image.py ../fonts/dripicons/ dripicons-v2-32-split3.tff