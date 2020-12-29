from itertools import chain
import streamlit as st

# NLP packages
import spacy
from textblob import TextBlob
from gensim.summarization import summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


def tokenize_and_analyze(text_to_tokenize):
    import en_core_web_sm
    nlp = en_core_web_sm.load()
    docx = nlp(text_to_tokenize)
    tokens = [token.text for token in docx]
    token_data = [
        f"'Token' : {token.text} 'Lemma' : {token.lemma_} " for token in docx]
    return token_data


def obtain_named_entities(text_to_analyze):
    import en_core_web_sm
    nlp = en_core_web_sm.load()
    docx = nlp(text_to_analyze)
    # entity_data = []
    # if docx.ents:
    #     for ent in docx.ents:
    #         entity_data += f"'Token' : {ent.text}   'Entity' : {ent.label_}"
    entities = [{"Text": entity.text, "Entity": entity.label_}
                for entity in docx.ents]
    return entities


def obtain_sentiment_from_text(text_to_find_sentiment):
    default = {"1": "anu", "2": "priya"}
    return default


def sumy_summarizer(docx):
    parser = PlaintextParser.from_string(docx, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, 3)
    summary_list = [str(sentence) for sentence in summary]
    result_summary = " ".join(summary_list)
    return result_summary


def main():
    """NLP App with Streamlit"""
    st.title("NLP Web Application with Streamlit")
    st.header("Natural Language Processing Application")
    st.subheader("")
    st.info("Tokenization")

    # Tokenization
    if st.checkbox("Click to perform Tokenization and display tokens with lemma."):
        st.subheader("Tokenize your Text")
        message_token = st.text_area(
            "(Enter text to tokenize)")

        if st.button("Analyze text to Tokenize"):
            tokens = tokenize_and_analyze(message_token)
            st.json(tokens)

    st.write("  ***********  ")
    st.subheader("")
    # Named Entity Recognition
    st.info("Named Entity Recognition")

    if st.checkbox("Click to obtain Named Entitites "):
        st.subheader("Obtain Named Entites")
        message_entites = st.text_area(
            "(Enter text to obtain named entities)")

        if st.button("Analyze text to otain named entities"):
            entities = obtain_named_entities(message_entites)
            st.json(entities)

    st.write("  ***********  ")
    st.subheader("    ")

    # Sentiment Analysis
    st.info("Sentiment Analysis")
    if st.checkbox("Click to perform Sentiment Analysis"):
        st.subheader("Perform sentiment analysis")
        message_sentiment = st.text_area(
            "(Enter text to find sentiment from )")

        if st.button("Analyze text to find sentiment"):
            blob = TextBlob(message_sentiment)
            result_sentiment = blob.sentiment
            st.success(result_sentiment)

    st.write("  ***********  ")
    st.subheader("    ")

    # Text Summarization
    st.info("Text Summarization")
    if st.checkbox("Click to summarize your text"):
        st.subheader("Summarize your text")
        message_summarize = st.text_area("(Enter text to summarize)")
        summary_options = st.selectbox(
            "Select your summarizer", ("gensim", "sumy"))
        if st.button("Click to summarize text"):
            if summary_options == "gensim":
                st.text("Using gensim package")
                summary_gensim = summarize(message_summarize)
                st.success(summary_gensim)
            elif summary_options == "sumy":
                st.text(f"Using {summary_options} package")
                summary_result = sumy_summarizer(message_summarize)
                st.success(summary_result)
            else:
                st.warning("Using Default Summarizer : 'Gensim'")
                st.text("Using gensim package")
                summary_result = summarize(message_summarize)
                st.success(summary_result)
    st.write("  ***********  ")
    st.subheader("    ")
    st.subheader(
        "Tokenization : Named Entity : Sentiment Analysis : Text Summarization")
    st.write(" ********* ")


if __name__ == "__main__":
    main()
