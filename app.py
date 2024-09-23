import streamlit as st
import anthropic
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API key from environment variable
api_key = os.getenv('Claude_api_key')

# Initialize Anthropic client with API key
client = anthropic.Anthropic(api_key=api_key)

# Define the functions for generating game content
def generate_game_environment(description):
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=150,
        temperature=0.7,
        system="You are a creative game designer. Generate a detailed and imaginative game environment based on the provided description.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Create a game environment based on the following description: {description}"
                    }
                ]
            }
        ]
    )
    return message.content[0].text  # Return relevant text

def generate_game_story(environment, protagonist, antagonist):
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=150,
        temperature=0.7,
        system="You are a skilled storyteller. Craft a compelling game story that connects the environment, protagonist, and antagonist.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Create a game story that takes place in the following environment: {environment}. "
                                f"The protagonist is: {protagonist}. The antagonist is: {antagonist}. "
                                "Please craft a detailed and engaging game story."
                    }
                ]
            }
        ]
    )
    return message.content[0].text  # Return relevant text

def generate_protagonist(description):
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=150,
        temperature=0.7,
        system="You are an expert in character development. Create a well-defined and relatable protagonist based on the provided description.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Create a protagonist based on the following description: {description}"
                    }
                ]
            }
        ]
    )
    return message.content[0].text  # Return relevant text

def generate_antagonist(description):
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=150,
        temperature=0.7,
        system="You are an expert in creating antagonists. Generate a compelling and complex antagonist based on the provided description.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Create an antagonist based on the following description: {description}"
                    }
                ]
            }
        ]
    )
    return message.content[0].text  # Return relevant text

# Sidebar Inputs
st.sidebar.title("StoryForge")
st.sidebar.subheader("Please enter the details for your game:")

game_environment = st.sidebar.text_input("Game Environment", 
                                         "Enter the setting or world where your game takes place. For example, a post-apocalyptic city, a fantasy kingdom, or a sci-fi space station.")

protagonist = st.sidebar.text_input("Protagonist", 
                                    "Enter the main character of your game, including their role and key characteristics. For example, a brave knight, a resourceful hacker, or a mystical sorcerer.")

antagonist = st.sidebar.text_input("Antagonist", 
                                   "Enter the main antagonist of your game, describing their role and motivations. For example, an evil warlord, a corrupt corporation, or a malevolent AI.")

# Generate content when the user clicks the button
if st.sidebar.button("Generate Game Design Document"):
    if game_environment and protagonist and antagonist:
        # Generate each part of the game design document
        generated_environment = generate_game_environment(game_environment)
        generated_protagonist = generate_protagonist(protagonist)
        generated_antagonist = generate_antagonist(antagonist)
        generated_story = generate_game_story(generated_environment, generated_protagonist, generated_antagonist)
        
        # Main App Title and Description
        st.title("StoryForge")
        st.write("""
        StoryForge is a powerful tool for game developers to generate comprehensive Game Design Documents (GDD). 
        Simply input key elements of your game, and StoryForge will help you organize and structure your ideas into a professional document.
        """)

        # Layout with Columns
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Game Environment")
            st.write(generated_environment)

            st.subheader("Protagonist")
            st.write(generated_protagonist)

        with col2:
            st.subheader("Game Story")
            st.write(generated_story)

            st.subheader("Antagonist")
            st.write(generated_antagonist)
    else:
        st.error("Please fill out all fields in the sidebar to generate the Game Design Document.")
else:
    # Main App Title and Description
    st.title("StoryForge")
    st.write("""
    StoryForge is a powerful tool for game developers to generate comprehensive Game Design Documents (GDD). 
    Simply input key elements of your game, and StoryForge will help you organize and structure your ideas into a professional document.
    """)

    # Layout with Columns and placeholders for when no content is generated
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Game Environment")
        st.write("Enter game environment details to generate content.")

        st.subheader("Protagonist")
        st.write("Enter protagonist details to generate content.")

    with col2:
        st.subheader("Game Story")
        st.write("Enter game environment, protagonist, and antagonist to generate the story.")

        st.subheader("Antagonist")
        st.write("Enter antagonist details to generate content.")
