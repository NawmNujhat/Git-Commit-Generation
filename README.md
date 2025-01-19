# Team 3
Group project (Team 3) for CS4570 Machine Learning for Software Engineering. This repository serves as a basis for research into prompt engineering for automated commit message generation. 

## Requirements

- Python 3.10 or higher
- [Ollama](https://github.com/jmorganca/ollama) (for model serving)
- A supported Ollama model (e.g. `mistral`, `codellama`, `phi3.5`)

## Installation

### 1. Install Python and Dependencies

1. **Python**  
   Make sure you have Python 3.10 or higher installed. If you are on a Unix-like system (Linux/MacOS), run:
   ```bash
   python3 --version
   ```
   If Python is not installed, visit [python.org](https://www.python.org/downloads/) to download and install it.

2. **Python Dependencies**  
   Install the required Python libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

### 2. Install Ollama

Ollama is required to run and manage the models. Download and install Ollama from [ollama.com](https://ollama.com/).

### 3. Install a Model

Ollama requires a model to be installed before you can generate text. Some possible models include:
- `mistral`
- `codellama`
- `phi3.5`

To install a model (for example, `mistral`), run:
```bash
ollama pull mistral
```

## Usage
- Check `.env` variables are defined
- Run `python src/main.py`
- Input the model to use (choose from `deepinfra`, `phi_mini`,`mistral` or `codellama`)
- See the results in `output/output.csv`, containing the original commit message and the message generated by the model.
- After obtained outputs from a model, run `python src/evaluate.py` to see the evaluation results.

Before usage make sure Ollama is running using:
```bash
ollama serve
```

Below is an example of how to run the main file:
```bash
python src/main.py \
    --model mistral \
    --prompt baseline \
```

## Man page

Below is the placeholder for the detailed manual page of the main file and how to use it:

```
sage: main.py [-h] [--model {mistral,codellama,phi3.5}] [--prompt {baseline,fewshot,cot}] [--input_size INPUT_SIZE] [--process_amount PROCESS_AMOUNT] [--sequential] [--input_folder INPUT_FOLDER] [--output_folder OUTPUT_FOLDER] [--temperature TEMPERATURE] [--workers WORKERS]

Run one of the experiments with the specified model.

options:
  -h, --help            show this help message and exit
  --model {mistral,codellama,phi3.5}
                        The model to use.
  --prompt {baseline,fewshot,cot}
                        The prompt to use.
  --input_size INPUT_SIZE
                        The size of the input.
  --process_amount PROCESS_AMOUNT
                        The number of items to process.
  --sequential          Run the experiment sequentially instead of in parallel.
  --input_folder INPUT_FOLDER
                        The folder containing the input files.
  --output_folder OUTPUT_FOLDER
                        The folder to save the output files.
  --temperature TEMPERATURE
                        The temperature for the model generation.
  --workers WORKERS     The number of workers to use for parallel processing.
```

## Extension
>Notice: We used WSL2 and macOS as the testing environment, some adaptions for Windows are also implemented. However, they are not tested thoroughly. The current extension can be seen as a Proof of Concept.

To test if the extension is running properly, you need to follow the instructions below:

1. Open `extension/commit-generation` as the root project in Visual Studio Code.

2. Press `F5` to open the visual debugger, then press `Ctrl` + `Shift` + `P`, search and select `Generate commit message` in the list.

3. You should see the process by print statements in the console terminal, ignore the visual studio pop-ups - they are redundant for now.

4. After that you should see the console outputs(below is an example)：
```
Initializing virtual environments...
Virtual environment created. Now installing dependencies...
Pulling Mistral model via Ollama...
Dependencies installed. Now fetching git diff...
Git diff fetched:  Now write diff to temp file...
Diff file is written to temp file, located at /home/weicheng/.vscode-server/data/User/globalStorage/undefined_publisher.commit-generation/staged_diff.txt , now running the model to generate messages....
Message automatically copied to the file location: [.../my_messages.txt]
```
If you can see the last line, then messages should be copied to the file location, which is typically in the root folder of your repository.

### Model running on the extension
The extension runs on `src/runExtension.py`. The current model it is running:
```
Model: Mistral7b
Applied technique(s): few-shot
Temperature: 0.7
```

To adjust the parameters for the model, modify `src/runExtension.py`. Alternatively, you can put your own model in.

## Other scripts


### Input preperation
Run `prepare_input.py` to transform the dataset `csv` files into input files, by generating the prompts from them. The input files are generated as `{model}_{size}_{technique}.csv`.
```bash
python src/prepare_input.py
```

### Run similar search
Run `run_similar_search.py` to find similar commits as few shot examples for samples in the dataset. Warning: this script will download full repositories to find similar commits and so will usage a large amount of storage.
```bash
python src/few_shot/run_similar_search.py
```