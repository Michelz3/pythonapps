import streamlit as st
import random

# Wool hashtags
HASHTAG_POOL = [
    "#knitting", "#knittersofinstagram", "#yarn", "#handdyed", "#wool", "#knitstagram", "#handknit",
    "#knitwear", "#knit", "#yarnaddict", "#knittingaddict", "#knittinglove", "#knitlife", "#knitspiration",
    "#knittingproject", "#knitpicks", "#handmade", "#knitting_inspiration", "#yarnlove", "#knittersoftheworld",
    "#woollove", "#knitknitknit", "#knittingfun", "#knittingdaily", "#knittingislove", "#wooladdict",
    "#knittingtime", "#knittingmakesmehappy", "#woolyarn", "#knittingpattern", "#knittingjoy", "#knittingtherapy",
    "#knittingcommunity", "#knittingstudio", "#knittingaddiction", "#knittingprocess", "#wooladdiction",
    "#knittinglifestyle", "#knittingideas", "#knittinggoals", "#knittinghappiness"
]

# Rainbow hashtags
HASHTAG_RAINBOW = [
    "#Rainbowyarn", "#Regenboogwol", "#Ringelwolle", "#Iloverainbows", "#Selfstripingrainbowyarn",
    "#Rainbowsocks"
]

def generate_hashtags(nr_regenboog, nr_wol):
    wool_tags = random.sample(HASHTAG_POOL, min(nr_wol, len(HASHTAG_POOL)))
    rainbow_tags = random.sample(HASHTAG_RAINBOW, min(nr_regenboog, len(HASHTAG_RAINBOW)))
    hashtags = wool_tags + rainbow_tags
    hashtag_types = ["wool"] * len(wool_tags) + ["rainbow"] * len(rainbow_tags)
    return hashtags, hashtag_types

def format_hashtags(hashtags):
    return ' '.join(hashtags)

def main():
    st.title("🧶 Wool Hashtag Generator")

    if 'hashtags' not in st.session_state:
        st.session_state.hashtags = []
        st.session_state.hashtag_types = []

    nr_regenboog = st.number_input("Aantal #regenboog", min_value=0, max_value=len(HASHTAG_RAINBOW), value=0)
    nr_wol = st.number_input("Aantal #wol", min_value=0, max_value=len(HASHTAG_POOL), value=30)

    if st.button("Generate Hashtags"):
        hashtags, hashtag_types = generate_hashtags(nr_regenboog, nr_wol)
        st.session_state.hashtags = hashtags
        st.session_state.hashtag_types = hashtag_types

    if st.session_state.hashtags:
        st.write("### Click a hashtag to replace it with a new one of the same type:")

        cols = st.columns(5)
        for i, hashtag in enumerate(st.session_state.hashtags):
            if cols[i % 5].button(hashtag, key=f"tag_{i}"):
                tag_type = st.session_state.hashtag_types[i]

                if tag_type == "wool":
                    available_pool = set(HASHTAG_POOL) - set(st.session_state.hashtags)
                elif tag_type == "rainbow":
                    available_pool = set(HASHTAG_RAINBOW) - set(st.session_state.hashtags)
                else:
                    available_pool = set()

                if available_pool:
                    st.session_state.hashtags[i] = random.choice(list(available_pool))
                else:
                    st.warning(f"No more unique {tag_type} hashtags available for replacement.")

        formatted = format_hashtags(st.session_state.hashtags)
        st.text_area("Your hashtags (copy below):", formatted, height=150)

if __name__ == "__main__":
    main()

