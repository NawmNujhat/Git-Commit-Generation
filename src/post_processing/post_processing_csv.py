import os
import pandas as pd

from .evaluate import (evaluate_metrics)

def read_and_evaluate_files(input_files: str='./cleaned_output', output_files: str='./results'):
    average_results = {
        'model':[],
        'prompt':[],
        'temperature':[],
        'bleu_mean':[],
        'meteor_mean':[],
        'rouge_l_mean':[],
        'cleaned_bleu_mean':[],
        'cleaned_meteor_mean':[],
        'cleaned_rouge_l_mean':[],
        'cleaned_blue_std': [],
        'cleaned_meteor_std': [],
        'cleaned_rouge_l_std': [],
        'cleaned_blue_p2': [],
        'cleaned_meteor_p2': [],
        'cleaned_rouge_l_p2': [],
        'cleaned_blue_p25': [],
        'cleaned_meteor_p25': [],
        'cleaned_rouge_l_p25': [],
        'cleaned_blue_p50': [],
        'cleaned_meteor_p50': [],
        'cleaned_rouge_l_p50': [],
        'cleaned_blue_p75': [],
        'cleaned_meteor_p75': [],
        'cleaned_rouge_l_p75': [],
        'cleaned_blue_p98': [],
        'cleaned_meteor_p98': [],
        'cleaned_rouge_l_p98': [],
    }

    for filename in os.listdir(input_files):
        if filename.endswith('.csv'):
            parts=filename.replace('.csv','').split('_')
            model=parts[0]
            prompt_type=parts[2]
            temperature=parts[3]
            df = pd.read_csv(os.path.join(input_files,filename),usecols=['true_message','generated_message','cleaned_generated_message'])

            for i in range(len(df)):
                item = df.iloc[i]

                if not isinstance(item['true_message'], str):
                    df.loc[i,'true_message'] = ""
                if not isinstance(item['generated_message'], str):
                    df.loc[i,'generated_message'] = ""
                if not isinstance(item['cleaned_generated_message'], str):
                    df.loc[i,'cleaned_generated_message'] = ""
                
                item = df.iloc[i]
            
                bleu, meteor, rouge_l = evaluate_metrics(item['true_message'], item['generated_message'])
                df.loc[i,'bleu'] = bleu
                df.loc[i,'meteor'] = meteor
                df.loc[i,'rouge_l'] = rouge_l

                cleaned_bleu, cleaned_meteor, cleaned_rouge_l = evaluate_metrics(item['true_message'], item['cleaned_generated_message'])
                df.loc[i,'cleaned_bleu'] = cleaned_bleu
                df.loc[i,'cleaned_meteor'] = cleaned_meteor
                df.loc[i,'cleaned_rouge_l'] = cleaned_rouge_l

                if i % 100 == 0:
                    print(f"{filename}: {i}/{len(df)}")

            average_results['model'].append(model)
            average_results['prompt'].append(prompt_type)
            average_results['temperature'].append(temperature)
            average_results['bleu_mean'].append(df['bleu'].mean())
            average_results['meteor_mean'].append(df['meteor'].mean())
            average_results['rouge_l_mean'].append(df['rouge_l'].mean())
            average_results['cleaned_bleu_mean'].append(df['cleaned_bleu'].mean())
            average_results['cleaned_meteor_mean'].append(df['cleaned_meteor'].mean())
            average_results['cleaned_rouge_l_mean'].append(df['cleaned_rouge_l'].mean())
            average_results['cleaned_blue_std'].append(df['cleaned_bleu'].std())
            average_results['cleaned_meteor_std'].append(df['cleaned_meteor'].std())
            average_results['cleaned_rouge_l_std'].append(df['cleaned_rouge_l'].std())
            average_results['cleaned_blue_p2'].append(df['cleaned_bleu'].quantile(0.02))
            average_results['cleaned_meteor_p2'].append(df['cleaned_meteor'].quantile(0.02))
            average_results['cleaned_rouge_l_p2'].append(df['cleaned_rouge_l'].quantile(0.02))
            average_results['cleaned_blue_p25'].append(df['cleaned_bleu'].quantile(0.25))
            average_results['cleaned_meteor_p25'].append(df['cleaned_meteor'].quantile(0.25))
            average_results['cleaned_rouge_l_p25'].append(df['cleaned_rouge_l'].quantile(0.25))
            average_results['cleaned_blue_p50'].append(df['cleaned_bleu'].quantile(0.50))
            average_results['cleaned_meteor_p50'].append(df['cleaned_meteor'].quantile(0.50))
            average_results['cleaned_rouge_l_p50'].append(df['cleaned_rouge_l'].quantile(0.50))
            average_results['cleaned_blue_p75'].append(df['cleaned_bleu'].quantile(0.75))
            average_results['cleaned_meteor_p75'].append(df['cleaned_meteor'].quantile(0.75))
            average_results['cleaned_rouge_l_p75'].append(df['cleaned_rouge_l'].quantile(0.75))
            average_results['cleaned_blue_p98'].append(df['cleaned_bleu'].quantile(0.98))
            average_results['cleaned_meteor_p98'].append(df['cleaned_meteor'].quantile(0.98))
            average_results['cleaned_rouge_l_p98'].append(df['cleaned_rouge_l'].quantile(0.98))
    
    results = pd.DataFrame(average_results)
    results.to_csv(f'{output_files}/evaluation_results.csv',index=False)
    print(results.to_string())

    
