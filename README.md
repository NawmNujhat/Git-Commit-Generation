# Team 3
Group project (Team 3) for CS4570 Machine Learning for Software Engineering. This repository serves as a basis for research into prompt engineering for automated commit message generation. Currently makes use of the DeepInfra model for commit message generation.

## Prerequisites
- Python 3.8+
- API key from [DeepInfra](https://deepinfra.com/) (add to `.env`)
- For CodeLlama: [Ollama](https://ollama.com/)

## Setup
- (Optional) Create virtual environment
- Install dependencies: `pip install -r requirements.txt`
- Create a `.env` file and add the following keys:
```
USERNAME=<your_username>
DEEPINFRA_API_KEY=<your_api_key>
```

### For use of CodeLlama
- CodeLlama requires Ollama to be running locally. See [installation instructions](https://ollama.com/).

### For use of Mistral-7b-instruct and Phi-3.5-mini-instruct
- Both of these model require llama.cpp for running the quantized version locally. See [installation instructions](https://github.com/ggerganov/llama.cpp/blob/master/docs/build.md) for downloading llama.cpp locally. Make sure to clone it inside the project repository.
- Before installing llama.cpp, make sure to install 'pkgconfig' and 'make' command
- Next, install the required versions of Mistral-7b-instruct and Phi-3.5-mini-instruct through the following commands:
   `cd llama.cpp`
   `cd models`
For Mistral Ai, use `huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.2-GGUF mistral-7b-instruct-v0.2.Q6.gguf --local-dir . --local-dir-use-symlinks False`
For Phi-3.5-mini, use `huggingface-cli download bartowski/Phi-3.5-mini-instruct-GGUF --include "Phi-3.5-mini-instruct-Q8_0.gguf" --local-dir ./`
Depending on the system spec of your local setup, you can use other quantized versions based on the provided links: 
- Phi-3.5-mini-instruct : [https://huggingface.co/bartowski/Phi-3.5-mini-instruct-GGUF]
- Mistral-7b-instructL: [https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF]

Note: In the `.env` file set the value of following environment variables depending on your setup specs: 
`CONTEXT_WINDOW_FOR_MISTRAL`=2048
`CONTEXT_WINDOW_FOR_PHI`=2048
`GPU_LAYERS`=48

## Usage
- Check `.env` variables are defined
- Run `python src/main.py`
- Input the model to use (choose from `deepinfra`, `codet5` or `codellama`)
- See the results in `output/output.csv`, containing the original commit message and the message generated by the model.

## Example output
Using DeepInfra/dbrx:
```
Original Message, Model Output
"Refactor atomic fraction calculation", "Optimize element fraction calculation using pd_coords."
"Update simplex intersection logic", "Simplify simplex calculations with pd_coords method."
```
Using Mistral-7b-instruct,
```
Original Message, Model Output
"Bumped version number and fixed a blocking issue where users without config file had crashes,Updated application version to 2.0.0a5 and modified config file loading."
```
Using Phi-3.5-mini-instruct,
```
Original Message,Model Output
Code cleanup based on Sonar inspection,Update ScottAgent package summary with additional documentation link.
```
