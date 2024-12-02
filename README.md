# Team 3
Group project (Team 3) for CS4570 Machine Learning for Software Engineering. This repository serves as a basis for research into prompt engineering for automated commit message generation. Currently makes use of the DeepInfra model for commit message generation.

## Prerequisites
- Python 3.8+
- API key from DeepInfra (add to `.env`)

## Setup
- (Optional) Create virtual environment
- Install dependencies: `pip install -r requirements.txt`
- Create a `.env` file and add the following keys:
```
USERNAME=<your_username>
DEEPINFRA_API_KEY=<your_api_key>
```

## Usage
- Check `.env` variables are defined
- Run `python src/main.py`
- See the results in `output/output.csv`, containing the original commit message and the message generated by the model.

## Example output
```
Original Message, Model Output
"Refactor atomic fraction calculation", "Optimize element fraction calculation using pd_coords."
"Update simplex intersection logic", "Simplify simplex calculations with pd_coords method."
```