# EphemeralAstroturfing

This repository contains the data, the annotations and the code for the paper "Ephemeral Astroturfing Attacks: The Case of Fake Twitter Trends".

Please cite our paper if you use our data or the code in this repository.

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

## Files 

- `fake_trends.csv`: Keywords targeted in all succesful attacks between January 2019 and September 2019 and their labels.
- `astrobot_annotations.csv`: Annotations of the astrobots.
- `attack_annotations.csv`: Annotations of the attacks. 

The attack number column denotes if the tweet is used in the same attack within the other tweets targeting the same keyword or not.

## Code

- `lexicon_classifier.py`: Rule based classifier to detect lexicon tweets. 

## Access to more data

Twitter allows sharing Tweet / User objects via non-automated means, i.e. communication in person. Thus, you can contact us for the data we cannot publicly distribute, such as tweet and user objects or content of the lexicon tweets.

Contact: tugrulcan dot elmas at epfl dot ch
