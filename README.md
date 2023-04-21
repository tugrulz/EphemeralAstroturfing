# Ephemeral Astroturfing & Fake Trends Bots

This repository contains the data, the annotations and the code for the paper "Analyzing Activity and Suspension Patterns of Twitter Bots Attacking Turkish Twitter Trends by a Longitudinal Dataset" and "Ephemeral Astroturfing Attacks: The Case of Fake Twitter Trends". 

Please cite the papers if you use our data or the code in this repository.

Please also contact us if you use data for research purposes, we would like to learn your experience!: tugrulcanelmas@gmail.com

The tweet data was extracted from the Internet Archive's Twitter Stream Grab. 

## Files 

All following files will be ready by the end of April 2023:

attack_data.csv.zip: All lexicon tweets & astrobots & their activity data.
all_trend_stats.csv: Trends between 2013-2022 and their statistics
fake_trends_20202122.csv: Only the fake trends between 2020-2022

(To come very soon!)
Botstream: Full activity of a sample of astrobots
Search: Tweets mentioning a trend, collected when the bots attacked

### Important Caveat for Bot Detection Researchers:
Please use bots that attacked multiple times (e.g., at least 4). 
This is to ensure that there is no noisy accounts, such as those who were 
- compromised accounts that were briefly included in the bot-net and acted as a bot but then saved themselves 
- Twitter removed them immediately so they were not very succesful at being bots.

2019: Only the data and the annotations from the study "Ephemeral Astroturfing Attacks: The Case of Fake Twitter Trends"


## Citation reference:

```
@article{elmas2023analyzing,
  title={Analyzing Activity and Suspension Patterns of Twitter Bots Attacking Turkish Twitter Trends by a Longitudinal Dataset},
  author={Elmas, Tu{\u{g}}rulcan},
  journal={arXiv preprint arXiv:2304.07907},
  year={2023}
}
```
```
@inproceedings{elmas2021ephemeral,
  title={Ephemeral astroturfing attacks: The case of fake twitter trends},
  author={Elmas, Tu{\u{g}}rulcan and Overdorf, Rebekah and {\"O}zkalay, Ahmed Furkan and Aberer, Karl},
  booktitle={2021 IEEE European Symposium on Security and Privacy (EuroS\&P)},
  pages={403--422},
  year={2021},
  organization={IEEE}
}
```

## 2019 (old) Files 

- `fake_trends.csv`: Keywords targeted in all succesful attacks between January 2019 and September 2019 and their labels.
- `astrobot_annotations.csv`: Annotations of the astrobots.
- `attack_annotations.csv`: Annotations of the attacks. 

The attack number column denotes if the tweet is used in the same attack within the other tweets targeting the same keyword or not.

### Code

- `lexicon_classifier.py`: Rule based classifier to detect lexicon tweets. 

