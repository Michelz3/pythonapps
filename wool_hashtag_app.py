
import streamlit as st
import random

HASHTAG_POOL = [
    "#knitting", "#knittersofinstagram", "#yarn", "#handdyed", "#wool", "#knitstagram", "#handknit",
    "#knitwear", "#knit", "#yarnaddict", "#knittingaddict", "#knittinglove", "#knitlife", "#knitspiration",
    "#knittingproject", "#knitpicks", "#handmade", "#knitting_inspiration", "#yarnlove", "#knittersoftheworld",
    "#woollove", "#knitknitknit", "#knittingfun", "#knittingdaily", "#knittingislove", "#wooladdict",
    "#knittingtime", "#knittingmakesmehappy", "#woolyarn", "#knittingpattern", "#knittingjoy", "#knittingtherapy",
    "#knittingcommunity", "#knittingstudio", "#knittingaddiction", "#knittingprocess", "#wooladdiction",
    "#knittinglifestyle", "#knittingideas", "#knittinggoals", "#knittinghappiness"
]

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

def main():
    st.title("Wool Hashtag Generator")
    try:
        if st.button("Generate Hashtags"):
            hashtags = generate_hashtags()
            st.write(hashtags)
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

