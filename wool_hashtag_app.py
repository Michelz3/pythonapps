
import streamlit as st
import random

HASHTAG_POOL = set([
    "#knitting", "#knittersofinstagram", "#yarn", "#handdyed", "#wool", "#knitstagram", "#handknit",
    "#knitwear", "#knit", "#yarnaddict", "#knittingaddict", "#knittinglove", "#knitlife", "#knitspiration",
    "#knittingproject", "#knitpicks", "#handmade", "#knitting_inspiration", "#yarnlove", "#knittersoftheworld",
    "#woollove", "#knitknitknit", "#knittingfun", "#knittingdaily", "#knittingislove", "#wooladdict",
    "#knittingtime", "#knittingmakesmehappy", "#woolyarn", "#knittingpattern", "#knittingjoy", "#knittingtherapy",
    "#knittingcommunity", "#knittingstudio", "#knittingaddiction", "#knittingprocess", "#wooladdiction",
    "#knittinglifestyle", "#knittingideas", "#knittinggoals", "#knittinghappiness"
])

def generate_hashtags(count=30):
    return random.sample(list(HASHTAG_POOL), count)

def add_one_hashtag(current_list):
    available = HASHTAG_POOL - set(current_list)
    if available:
        selected = random.choice(list(available))
        current_list.append(selected)
        return selected
    else:
        return None

def non_interactive_demo():
    hashtags = generate_hashtags()
    added_tag = add_one_hashtag(hashtags)
    removed_tag = hashtags.pop(0) if hashtags else None
    return {
        "hashtags": hashtags,
        "added_tag": added_tag,
        "removed_tag": removed_tag
    }

if __name__ == "__main__":
    result = non_interactive_demo()
    print("\n--- Wool Hashtag App Demo ---")
    print(f"Added hashtag: {result['added_tag']}")
    print(f"Removed hashtag: {result['removed_tag']}")
    print(f"\nCurrent hashtag list ({len(result['hashtags'])} hashtags):")
    for idx, tag in enumerate(result['hashtags']):
        print(f"{idx}: {tag}")

