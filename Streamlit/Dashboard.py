import streamlit as st 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud
import urllib.request

all_df = pd.read_csv("./Data/all_df.csv")
sellers = pd.read_csv("./Data/sellers_dataset.csv")
customer_location = pd.read_csv('./Data/customer_location.csv')
order_reviews = pd.read_csv("./Data/order_reviews_dataset.csv")
st.title('E-Commerce Dashboard :sparkles:')
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://media.licdn.com/dms/image/D5603AQFjPhmlcNvdNg/profile-displayphoto-shrink_800_800/0/1701944152755?e=2147483647&v=beta&t=s5LvU64NwwiRKYHkEj6sy7uWkdnAbbdjLZcZHMu6Obc")
    st.write("Alvin Fajar Permana")
    st.write("github: https://github.com/Alvinnxyz")
    st.write("LinkedIn: https://linkedin.com/in/alvinfp/")
st.subheader("Best & Worst Performing Product")
tab1, tab2 = st.tabs(["sales amount", "Revenue"])

with tab1:
    st.subheader("Performing Product by sales amount")
    st.markdown("This plot shows the comparison of the top 10 and bottom 10 products based on sales amount.")
    product_counts = all_df['product_category_name_english'].value_counts().sort_values(ascending=False)

    top_10_products_count = product_counts.head(10)
    bottom_10_products_count = product_counts.tail(10)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    top_10_products_count.plot(kind='bar', color='skyblue', label='Top 10')
    plt.title('Top 10 Highest Sales Products')
    plt.xlabel('Product Category (English)')
    plt.ylabel('Total Sales (Count)')
    plt.xticks(rotation=45, ha='right')

    plt.subplot(1, 2, 2)
    bottom_10_products_count.plot(kind='bar', color='salmon', label='Bottom 10')
    plt.title('Bottom 10 Lowest Sales Products')  
    plt.xlabel('Product Category (English)')
    plt.ylabel('Total Sales (Count)')
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    st.pyplot(plt.gcf())  
    
with tab2:
    st.subheader("Performing Product by Revenue")
    st.markdown("This plot shows the comparison of the top 10 and bottom 10 products based on total revenue.")

    product_revenue = all_df.groupby('product_category_name_english')['price'].sum().sort_values(ascending=False)

    top_10_products_count = product_revenue.head(10)
    bottom_10_products_count = product_revenue.tail(10)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    top_10_products_count.plot(kind='bar', color='skyblue', label='Top 10')
    plt.title('Top 10 Highest Sales Products')
    plt.xlabel('Product Category (English)')
    plt.ylabel('Total Revenue')
    plt.xticks(rotation=45, ha='right')

    plt.subplot(1, 2, 2)
    bottom_10_products_count.plot(kind='bar', color='salmon', label='Bottom 10')
    plt.title('Bottom 10 Lowest Sales Products')  
    plt.xlabel('Product Category (English)')
    plt.ylabel('Total Total Revenue')
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    st.pyplot(plt.gcf())  
    
st.subheader("Total monthly orders in 2017 and 2018")
all_df['order_purchase_timestamp'] = pd.to_datetime(all_df['order_purchase_timestamp'])

# Filter data for the year 2017
data_2017 = all_df[all_df['order_purchase_timestamp'].dt.year == 2017]
order_counts_per_month_2017 = data_2017.resample('M', on='order_purchase_timestamp')['order_id'].count()
order_counts_per_month_2017.index = order_counts_per_month_2017.index.strftime('%B')

# Filter data for the year 2018
data_2018 = all_df[all_df['order_purchase_timestamp'].dt.year == 2018]
order_counts_per_month_2018 = data_2018.resample('M', on='order_purchase_timestamp')['order_id'].count()
order_counts_per_month_2018.index = order_counts_per_month_2018.index.strftime('%B')

# Convert index and data to lists
months_2017 = list(order_counts_per_month_2017.index)
months_2018 = list(order_counts_per_month_2018.index)
order_counts_array_2017 = order_counts_per_month_2017.values
order_counts_array_2018 = order_counts_per_month_2018.values

# Plot
plt.figure(figsize=(18, 8))

plt.plot(months_2017, order_counts_array_2017, marker='o', linewidth=2, color="#72BCD4", label='2017')
plt.plot(months_2018, order_counts_array_2018, marker='o', linewidth=2, color="#FF5733", label='2018')

plt.title('Number of Orders per Month (2017 vs 2018)', loc="center", fontsize=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Order Count', fontsize=14)
plt.xticks(fontsize=10, rotation=45, ha='right')
plt.yticks(fontsize=10)
plt.legend()
plt.tight_layout()
st.pyplot(plt.gcf())  

st.subheader("Customer and seller city")
customer_by_city = all_df.groupby('customer_city')['customer_unique_id'].nunique().sort_values(ascending=False)
top_10_customer_cities = customer_by_city.head(10).reset_index()

# Count the number of sellers by city
seller_by_city = sellers.groupby('seller_city')['seller_id'].nunique().sort_values(ascending=False)
top_10_seller_cities = seller_by_city.head(10).reset_index()

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(45, 25))

colors = ["#068DA9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="customer_unique_id", y="customer_city", data=top_10_customer_cities, palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Number of Customers", fontsize=30)
ax[0].set_title("Top 10 Customer Cities", loc="center", fontsize=50)
ax[0].tick_params(axis ='y', labelsize=35)
ax[0].tick_params(axis ='x', labelsize=30)

sns.barplot(x="seller_id", y="seller_city", data=top_10_seller_cities, palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Number of Sellers", fontsize=30)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Top 10 Seller Cities", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)

st.pyplot(fig)

st.subheader("Common Word Review")
tab1, tab2 = st.tabs(["Common words in review", "Top words in review score 5 and review score 1"])
with tab1:
    
    text = ' '.join(order_reviews['review_comment_title'].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    st.image(wordcloud.to_array())
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    word_freq = Counter(text.split())
    top_10_words = word_freq.most_common(10)

    words, frequencies = zip(*top_10_words)
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 10 Most Frequent Words in Reviews')
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())
with tab2:
    score_1_comments = order_reviews[order_reviews['review_score'] == 1]['review_comment_title']
    score_5_comments = order_reviews[order_reviews['review_score'] == 5]['review_comment_title']
    def count_words(comments):
        words = ' '.join(map(str, comments)).split()
        return Counter(words).most_common(5)

    
    top_5_words_score_1 = count_words(score_1_comments)
    top_5_words_score_5 = count_words(score_5_comments)

  
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    
    axs[0].bar(*zip(*top_5_words_score_1), color='salmon')
    axs[0].set_title('Top 5 Words in Review Titles (Score = 1)')
    axs[0].set_xlabel('Words')
    axs[0].set_ylabel('Frequency')


    axs[1].bar(*zip(*top_5_words_score_5), color='skyblue')
    axs[1].set_title('Top 5 Words in Review Titles (Score = 5)')
    axs[1].set_xlabel('Words')
    axs[1].set_ylabel('Frequency')

  
    plt.legend()
    plt.tight_layout()
    st.pyplot(plt.gcf())  

st.subheader("Customer geolocation")
def plot_map(data):
    # Validate data
    if 'geolocation_lng' not in data.columns or 'geolocation_lat' not in data.columns:
        raise ValueError("Data must contain 'geolocation_lng' and 'geolocation_lat' columns")

    # Download and read Brazil map image
    try:
        response = urllib.request.urlopen('https://i.pinimg.com/originals/3a/0c/e1/3a0ce18b3c842748c255bc0aa445ad41.jpg')
        brazil_image = plt.imread(response, format='jpg')  # Specify format to avoid potential errors
    except urllib.error.URLError as e:
        st.error(f"Error downloading map image: {e}")
        return

# Create the plot
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.scatter(data['geolocation_lng'], data['geolocation_lat'], alpha=0.3, s=0.3, c='maroon', zorder=2)  # Scatter points on top of map
    ax.axis('off')

    # Display Brazil map image
    extent = [-73.98283055, -33.8, -33.75116944, 5.4]  # Adjust extent as needed to match image dimensions
    ax.imshow(brazil_image, extent=extent, zorder=1)  # Place map image behind scatter points

    plt.title('Customer Locations')
    st.pyplot(fig)
if 'customer_location' in globals():
    # Plot the map
    plot_map(customer_location)
else:
    st.error("Please load your customer data first.")

with st.expander("See Explanation"):
        st.write('''Based on the generated graph, there's a higher concentration of customers in the southeast and southern regions. Furthermore, there's a tendency for more customers to be located in capital cities such as São Paulo, Rio de Janeiro, Porto Alegre, and others.).''')

st.caption('Copyright (C) Alvin Fajar Permana 2024')