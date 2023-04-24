# Ephemeral Astroturfing & Fake Trends Bots

This repository contains the data, the annotations and the code for the paper "Analyzing Activity and Suspension Patterns of Twitter Bots Attacking Turkish Twitter Trends by a Longitudinal Dataset" and "Ephemeral Astroturfing Attacks: The Case of Fake Twitter Trends". 

Please cite the papers if you use our data or the code in this repository.

Please also contact us if you use data for research purposes, we would like to learn your experience!: tugrulcanelmas@gmail.com

The tweet data was extracted from the Internet Archive's Twitter Stream Grab. 

## Folders & Files

- `2019`: The annotations from our earlier paper Ephemeral Astroturfing Attack The Case of Fake Twitter Trends (see below)

- `botstream`: 2 week real-time tweets from a sample of bots. You can easily see the anomalies in tweeting and deleting behavior. For the longer dataset, please contact us, as it is a bit big.

- `longitudinal_data`: all the bots found between 2013-2023, the tweets that made us detect them (attack_data.csv.bz2), and their profile information. 
The data here is for statistical purposes and the accounts that are active before 2022 are mostly removed, it's better to use the data below

- `search_api_results`: the bots here are detected real-time in late 2022, hence the recall is higher and the classifications are noise-free. (hence the name "past_search")
- `bot_scores.csv`: the Botometer results of the accounts detected
- `past_search_all_bot_tweets.csv`: The tweets that made us detect those bots
- `past_search_all_bots_user.csv`: The basic profile and the statistics of the bots. The total attacks mean how many times we detect that bot being a bot.
- `profile_info`: The profile info of bots downloaded in January 2023. The files inside have the same data but in different formats

- `trends`: The data related to trends
- `all_trend_stats`.csv: Trends between 2013-2022 and their statistics
- `fake_trends_20202122.csv`: Only the fake trends between 2020-2022

### Important Caveat for Bot Detection Researchers:
We advise you to use bots that attacked multiple times (e.g., at least 4). We put total_attacks field to indicate this. 
This is to ensure that there is no noisy accounts, such as those who were 
- compromised accounts that were briefly included in the bot-net and acted as a bot but then saved themselves 
- Twitter removed them immediately so they were not very succesful at being bots.

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

