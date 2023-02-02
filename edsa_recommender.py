"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
from PIL import Image

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')



# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Exploratory Data Analysis", "Business Model","Algorithm Overview",  "Meet The Team"]
    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    
    if page_selection == "Algorithm Overview":
        st.snow()
        st.title("Algorithm Overview")
        st.write("")
        st.write("Content Based Filtering")
        st.write("")
        st.write("In Content-Based Filtering, the recommender system filters the item according to the item’s content and suggests it to a user. For example, if a user likes a book, then the recommender system recommends a book that is never read by the user but this book is similar to the user’s previously liked book. ")
        st.image('resources/imgs/image1.png',use_column_width=True)
        st.write("")
        st.write("")
        st.write("Collaborative Filtering")
        st.write("")
        st.write("Collaborative filtering can be divided into two parts:")
        st.write("Item-based collaborative filtering:- In this type of collaborative filtering, items are suggested according to their similarity calculated based on the user’s interaction with other items.")
        st.write("User-based collaborative filtering:- In this type of collaborative filtering, items are suggested according to the similarity between users which I illustrate before.")
        st.write("In Content-based filtering, we don’t need any User information while recommending an item. But on the other side, Item-based collaborative filtering needs the user’s interaction with the other items, i.e. ratings. It is all about data. If we see that our collected data contains the item’s feature rather than the user interaction, we simply go for content-based filtering. But if we see that the data contains the information about the user ratings, userId, and movieId, just like the Movielens Dataset, then we go for the collaborative filtering.")
        st.image('resources/imgs/image2.png',use_column_width=True)

    if page_selection == "Exploratory Data Analysis":
        
        base="light"
        st.balloons()
        st.title("Exploratory Data Analysis")
        st.write("")
        st.subheader("What Does Exploratory Data Analysis (EDA) Mean?")
        st.write("")
        st.write("Exploratory data analysis (EDA) is a term for certain kinds of initial analysis and findings done with data sets, usually early on in an analytical process. Some experts describe it as “taking a peek” at the data to understand more about what it represents and how to apply it. Exploratory data analysis is often a precursor to other kinds of work with statistics and data.")
        st.write("Professionals will often use various visual tools to do exploratory data analysis, for example, to test an intuitive hypothesis, and figure out in what ways data sets are similar or different. One excellent example is the use of a scatter plot graph – this simple bit of exploratory data analysis can show analysts whether there is a trend or major difference between two or more data sets, by making numbers, which are relatively hard for the human brain to analyze as a whole, into easy visuals.")
        st.write("")
        st.write("")
        st.title("So Let's Get Started!")
        st.write("")
        st.subheader("Popularity")
        st.write("")
        st.write("As we can see below, drama is the most commonly occuring genre with almost half of the movies identifying itself as a drama film. Comedy comes in at a distant second with 25% of the movies having adequate doses of humor. Other major genres in the top 10 are Thriller, Romance,Action, Horror, Documentary and Crime.")
        st.write("")
        st.image('resources/imgs/Image3.png',use_column_width=True)
        st.write("")
        st.write("")
        st.write("")
        st.subheader("Annual Releases")
        st.write("")
        st.write("The dataset has 48213 movies available to us. it is reasonable to assume that it does include almost every major film released during those years. With this assumptions in mind, let us take a look at the number of movies produced by the year.")
        st.write("By looking at the below graph, we can see that over 8000 Sci-Fi movies were produced annually, with a steady decline from atmospheric movies with 6500 movies per year, to the least amount of movies with 3800 belonging to classic movies.")
        st.write("")
        st.image('resources/imgs/Image4.png',use_column_width=True)
        st.write("")
        st.write("")
        st.write("")
        st.subheader("15 Best And Worst Rated Movies")
        st.write("")
        st.write("Let's take a look at the 15 best performing movies with ratings higher than 10 000. We can see that the top 3 movies are Shawshank Redemption(1994) with a rating of 4.46, Pulp Fiction(1994) with a rating of 4.32, and Usual Suspects with a rating of 4.28. The 3 movies that barely made the top 10 cut are Star Wars: Episode 5 (1980), The Matrix (1999), and Inception (2010) with ratings higher than 4.15.")
        st.write("")
        st.image('resources/imgs/Image5.png',use_column_width=True)
        st.write("")
        st.write("")
        st.write("")
        st.write("By taking a look at the 15 worst performing movies, we can see that the 3 worst movies are Battlefield Earth (2000) with a rating less than 1.6. Baby Geniuses (1999) with a rating less than 1.75, and Dumb and Dumberer: When Harry Met Lloyd (2003) with a rating less than 1.75. ")
        st.write("")
        st.image('resources/imgs/Image6.png',use_column_width=True)
        st.write("")
        st.write("")
        st.write("")
        st.subheader("User Ratings")
        st.write("")
        st.write("Here we can analyse how many users or viewers give different rated scores. By looking at the below graph, we can see tha only 14.45% of users gave a 5 star rating, and over 26% of users gave a rating of 4.0. This is a rather curious graph that would tend to make a person wonder why certain ratings are given towards certain movies, especially when the ratings differ by 3 or 4 points.  ")
        st.write("")
        st.image('resources/imgs/Image7.png',use_column_width=True)
        st.write("")
        st.write("")
        st.write("")
        st.write("By looking at the below graph, we find it interesting that the ratings are left-skewed. It was expected that there would be a normal distrubtion with a mean rating of 3. Instead, we observe that users tend to rate movies quite favourably and tend to avoid negative ratings. This skew might be explained by the tendency of users to rate movies they liked. In other words, if a user doesn't like a movie, it is unlikely that they will watch it through to the end, let alone rate it.")
        st.write("")
        st.image('resources/imgs/Image8.png',use_column_width=True)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.title("That's All For Now")
        st.subheader("Look what we have to offer on the next page. Cheers!")

    if page_selection == "Business Model":
        st.subheader("Why Should You Even Consider Us?")
        st.write("Well, the least we can do is to try and convince you, but we are pretty certain that won't be too difficult")
        st.write("")
        st.subheader("Scenario")
        st.write("Let us give a scenario as to why a streaming service would need a movie recommendation feature such as ours. Let's say, for example, that your company has spent a tiny fortune on the development of an appealing, user-friendly, efficient, and reliable streaming service similar to that of Netflix or Showmax. However, your streaming service has an edge over all other streaming services because it is:")
        st.write("")
        st.write("###### 1. Less Expensive")
        st.write("###### 2. Much Faster  ")
        st.write("###### 3. Has Much More Movies and Series to Watch")
        st.write("###### 4. Requires Less Bandwidth")
        st.write("###### 5. Is Available on all Devices")
        st.write("")
        st.write("In Addition, you have already started your marketing campaigns and have a fast growing client-base that strongly promotes your product's potential. Now, a few months later and your clients have started to watched most of the movies and shows they wished to watch. Here and there they find something interesting to watch, perhaps you have a few banners showing trending films, but now you start to notice a decline on your service usages and you start to wonder what may be the cause of this.")
        st.write("")
        st.write("Well, this is where we come in. Your clients are suffering from 'too much of a good thing' syndrome, and they no longer can find anything interesting that's worth their time to watch. This will all be over in a second, or at least as soon as our recommender is deployed. Now your streaming service is capable of using all your historic streaming data and analyzing every account seperately, whereafter it will create an effective strategy and display, according to historic data, every show that it thinks the users will be the most interested in. As soon as a user thinks that there are no more satisfying movies to watch, then the Recommender will jump in and save the day.")
        st.write("")
        st.write("")
        st.write("Let's take a look at one of the most popular streaming services and it's performances:")
        st.write("")
        st.write("")
        st.subheader("NETFLIX")
        st.write("Netflix is synonymous to most people in this day and age as the go-to streaming service for movies and tv shows. What most people do not know, however, is that Netflix started out in the late 1990s with a subscription-based model, posting DVDs to people’s homes in the US. In 2000, Netflix introduced personalised movie recommendations with a recommender system, which back then had a root mean squared error (RMSE) of 0.9525 and was called Cinematch.")
        st.write("Fast forward to 2020, Netflix has transformed from a mail service posting DVDs in the US to a global streaming service with 182.8 million subscribers. Consequently, its recommender system transformed from a regression problem predicting ratings to a ranking problem, to a page-generation problem, to a problem maximising user experience (defined as maximising number of hours streamed i.e. personalising everything that can be personalised).")
        st.write("Well, how important is this recommender system to Netflix? Approximately 80% of their stream time is achieved through Netflix’s recommender system, which is a highly impressive number. Moreover, Netflix believes in creating a user experience that will seek to improve retention rate, which in turn translates to savings on customer acquisition (estimated $1B per year as of 2016).")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image('resources/imgs/image9.jpg',use_column_width=True)
        st.write("")
        st.write("")
        st.image('resources/imgs/image10.png',use_column_width=True)

    if page_selection =="Meet The Team":

        st.header("Company Name:")
        st.write(" Tech Refined Software Solutions Pty Ltd")
        st.write("Location: San Francisco, CA")
        st.subheader("Mission Statement: ")
        st.write("To deliver innovative and cutting-edge software solutions that simplify the digital landscape for businesses and individuals.About Us: NextGen Software Solutions is a technology company specializing in the development of software applications for various industries. Our team of experts has extensive experience in developing and implementing customized software solutions that meet the specific needs of our clients.")
        st.subheader("Products and Services: ")
        st.write("Our services include custom software development, machine learning, web application development, mobile app development, software maintenance and support, and consulting services. Our products include project management software, customer relationship management (CRM) software, and enterprise resource planning (ERP) software.")
        st.subheader("Values:")
        st.write("At Tech Refined Software Solutions, we believe in the power of technology to drive progress and transform lives. We are committed to providing excellent customer service, promoting diversity and inclusiveness, and fostering a culture of innovation and continuous improvement.")
        st.subheader("Why Choose Us: ")
        st.write("We are a dedicated and experienced team of software developers and designers who work together to deliver quality results. Our focus on innovation and our commitment to excellence sets us apart from the competition, and our strong track record of delivering successful software solutions speaks to our expertise and experience.")



        col1, col2 = st.columns([2, 1])
    

        member1, member2, member3, member4, member5 = st.columns(5)

       
        member1.image('resources/imgs/image11.png', use_column_width=True)
        member1.markdown("<p class='name'> Werner Stander </p>", unsafe_allow_html=True)
        member1.markdown("<p class='role'> CEO </p>", unsafe_allow_html=True)

        member2.image('resources/imgs/image11.png', use_column_width=True)
        member2.markdown("<p class='name'> Solomon Nwokoro </p>", unsafe_allow_html=True)
        member2.markdown("<p class='role'> Director </p>", unsafe_allow_html=True)

        member3.image('resources/imgs/image11.png', use_column_width=True)
        member3.markdown("<p class='name'> Eze Ajali </p>", unsafe_allow_html=True)
        member3.markdown("<p class='role'> Chief Data Scientist </p>", unsafe_allow_html=True)

        member4.image('resources/imgs/image11.png', use_column_width=True)
        member4.markdown("<p class='name'> Deborah Obafemi </p>", unsafe_allow_html=True)
        member4.markdown("<p class='role'> Data Analyst </p>", unsafe_allow_html=True)

        member5.image('resources/imgs/image11.png', use_column_width=True)
        member5.markdown("<p class='name'> Aloy </p>", unsafe_allow_html=True)
        member5.markdown("<p class='role'> Data Engineer </p>", unsafe_allow_html=True)

     
     


if __name__ == '__main__':
    main()
