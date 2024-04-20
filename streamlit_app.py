import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
# Set the primary color to green
st.set_page_config(page_title="OM", page_icon=":four_leaf_clover:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# ---- LOAD ASSETS ----

lottie_me = load_lottieurl("https://lottie.host/3fec572b-5677-49a3-ab24-73d54bb596b8/ZYGFobmZoC.json")
lottie_exp = load_lottieurl("https://lottie.host/08acf049-652d-4c97-80ee-7f81e4eb5c42/PCsu9sBxRh.json")
lottie_goal = load_lottieurl("https://lottie.host/03ea3e55-6e3d-4b6f-b4f3-dfe12e21f310/Nj25FzBr3w.json")
lottie_p1 = load_lottieurl("https://lottie.host/d4379d65-5f67-4210-9965-b6ec74e15a75/DpujVTeuH2.json")
lottie_p2 = load_lottieurl("https://lottie.host/fbde61d6-bce7-4bbd-a552-7f82f3bb4e59/WrB0knelzK.json")
lottie_p3 = load_lottieurl("https://lottie.host/218487af-45f2-4b80-a325-2c1ac28b8e8d/Zk1BmPVMZi.json")
lottie_coding = load_lottieurl("https://lottie.host/4ccc97a1-4af5-48ed-90c7-bd9d30febdda/HLu8RIPbmK.json")
your_image=Image.open("om.png")

# ---- HEADER SECTION ----
with st.container():
    # Create a row layout
    header_col1, header_col2 = st.columns([10, 3])

    # Add "Hi, I am Om" text to the second column
    with header_col1:
        st.subheader("Hi, I am Om :wave:")
        st.title("Coding Odyssey: A Student's Tech Journey")
        st.write(
            "I'm currently immersed in learning Data Structures and Algorithms while simultaneously crafting projects aligned with my passions and interests."
        )

    # Add the image to the first column
    with header_col2:
        # Style the image as a circle
        st.image(your_image, width=3000, use_column_width='always', output_format='PNG', channels='RGB', clamp=False)
        st.markdown(
            """
            <style>
                img {
                    border-radius: 50%;
                    overflow: hidden;
                }
            </style>
            """,
            unsafe_allow_html=True
        )


# ---- About Me ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("##")
        st.write(
            """
            Hello, I'm Om Bharti, a passionate student currently pursuing a Bachelor's degree in Electronics and Communication Engineering (ECE). For me, coding is not merely a skill; it's a journey of exploration and problem-solving. I derive joy from delving deep into Data Structures and Algorithms (DSA) and Competitive Programming (CP), continuously pushing myself to improve and innovate.
            """
        )
    with right_column:
        st_lottie(lottie_me, height=200, key="me")

# ---- Area of Interest and Skills: ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Area of Interest and Skills")
        st.write("##")
        st.write(
            """
           My primary focus lies in mastering programming languages like Python, C, and SQL, with a keen interest in exploring the depths of C++. I'm committed to staying updated in the ever-evolving tech landscape through continuous learning and practical application.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=200, key="coding")

# ---- Experience ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Experience")
        st.write("##")
        st.write(
            """
           I've developed a weather forecasting application by harnessing Weather APIs, demonstrating my ability to integrate real-world data into innovative solutions. Additionally, I've explored AI with a generative chat project, showcasing my curiosity in emerging technologies. Furthermore, I've embarked on a To-Do project, aiming to create a task management application that enhances productivity and organization, highlighting my commitment to practical problem-solving and software development.
            """
        )
    with right_column:
        st_lottie(lottie_exp, height=200, key="exp")        


# ---- Future Goals: ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Future Goals")
        st.write("##")
        st.write(
            """
           Building upon my foundation in Data Structures and Algorithms with C++, I plan to advance my expertise in Python, JavaScript,SQL and MongoDB. Additionally, I aim to explore the realms of graphic design and 3D modeling using Blender, integrating technical skills with creative pursuits to drive innovation and contribute positively to diverse fields.
            """
        )
    with right_column:
        st_lottie(lottie_goal, height=200, key="goal")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Projects")
        st.write("##")
        st.subheader("Weather Forecasting Application")
        st.write(
            """
           The Weather Forecasting Web Application is a user-friendly platform designed to provide accurate and real-time weather forecasts to users. It offers a seamless experience accessible through web browsers on various devices, including desktops, laptops, tablets, and smartphones.
            """
        )
    with right_column:
        st_lottie(lottie_p1, height=200, key="weather")

    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.subheader("To-Do Application")
        st.write(
            """
           A To-Do Application is a productivity tool designed to help individuals organize tasks, manage priorities, and track progress effectively. It provides a digital platform for creating, scheduling, and completing tasks efficiently, thereby enhancing productivity and time management skills.
            """
        )
    with right_column:
        st_lottie(lottie_p2, height=200, key="to-do")

    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.subheader("AI Chatbot")
        st.write(
            """
           An AI Chatbot is an artificial intelligence-powered conversational agent designed to interact with users via text or speech interfaces. It simulates human-like conversation, providing assistance, information, or performing tasks based on user queries or commands. AI techniques to understand and respond to user input effectively.
            """
        )
    with right_column:
        st_lottie(lottie_p3, height=200, key="ai")

# ---- SOCIAL MEDIA LINKS ----
with st.container():
    st.write("---")
    st.subheader("Connect with me on Social Media")
    st.write("##")

    # Define columns for social media links
    col1, col2, col3, col4 = st.columns(4)

    # Define social media icons
    social_icons = {
        "Instagram": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/1200px-Instagram_icon.png",
        "GitHub": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
        "LinkedIn": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png",
        "Twitter": "https://cdn.icon-icons.com/icons2/2429/PNG/512/twitter_logo_icon_147217.png"
    }

    # Define social media links
    social_links = {
        "Instagram": "https://www.instagram.com/0m.bharti?igshid=MTd0NXJpN3YyZGszOA==",
        "GitHub": "https://github.com/Om-Bharti",
        "LinkedIn": "https://www.linkedin.com/in/om-bharti-0b7777282",  # Updated LinkedIn URL if necessary
        "Twitter": "https://twitter.com/Om__Bharti"
    }

    # Display social media links with icons
    for platform, icon_url in social_icons.items():
        with globals()[f'col{len(platform) % 4 + 1}']:
            st.markdown(
                f'<a href="{social_links[platform]}" target="_blank"><img src="{icon_url}" alt="{platform}" width="50"></a>',
                unsafe_allow_html=True
            )
