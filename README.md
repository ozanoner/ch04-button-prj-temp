
# button-prj

This repository contains an ESP-IDF app under `button-ex`, with its pytest target test script colocated in the same folder.

## Prerequisites

- ESP-IDF `v6.0` environment exported
- Python packages:
	- `idf-ci`
	- `pytest-embedded-idf`
	- `pytest-embedded-wokwi`
- `WOKWI_CLI_TOKEN` set for Wokwi simulation tests

Example package install:

```bash
python -m pip install idf-ci pytest-embedded-idf pytest-embedded-wokwi
```

## Build with idf-ci

Build all CI sdkconfig variants for one target (according to `.idf_build_apps.toml`):

Note: with the pytest script now inside `button-ex`, build and test discovery can use the same path.

```bash
idf-ci build run -p button-ex --target esp32
```

```bash
idf-ci build run -p button-ex --target esp32c3
```

This produces build directories like:

- `button-ex/build_esp32_config1`
- `button-ex/build_esp32_config2`
- `button-ex/build_esp32c3_config1`
- `button-ex/build_esp32c3_config2`

## Run pytest target tests manually

Run tests for one target with Wokwi (the test script parameterizes both `config1` and `config2`):

```bash
export WOKWI_CLI_TOKEN=your_token_here

python -m pytest button-ex/test_button_ex.py \
	--target esp32 \
	--wokwi-diagram button-ex/diagram.esp32.json \
	--embedded-services idf,wokwi
```

```bash
python -m pytest button-ex/test_button_ex.py \
	--target esp32c3 \
	--wokwi-diagram button-ex/diagram.esp32c3.json \
	--embedded-services idf,wokwi
```

Generate JUnit reports:

```bash
python -m pytest button-ex/test_button_ex.py \
	--target esp32 \
	--wokwi-diagram button-ex/diagram.esp32.json \
	--embedded-services idf,wokwi \
	--junitxml report_esp32.xml
```

## Optional: collect tests only

```bash
python -m pytest button-ex/test_button_ex.py --collect-only -q
```

## Optional: Wokwi CLI scenario run

For manual scenario execution inside `button-ex`:

```bash
wokwi-cli --diagram diagram.esp32.json --scenario wokwi-scenario.yaml
```