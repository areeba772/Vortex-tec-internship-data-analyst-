import pandas as pd
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="VortexTech Superstore Dashboard",
    page_icon="📊",
    layout="wide",
)


# 2. Load Dataset
@st.cache_data
def load_data():
  return pd.read_csv("cleaned_superstore.csv")


df = load_data()

# 3. Dashboard Title
st.title("📊 VortexTech Superstore Interactive Dashboard - Week 3")
st.markdown(
    "Explore the superstore dataset dynamically using the sidebar filters below."
)

# 4. Sidebar Filters
st.sidebar.header("🔍 Filter Options")

# Filter 1: Dropdown for Category Selection
if "Category" in df.columns:
  categories = ["All"] + list(df["Category"].unique())
  selected_category = st.sidebar.selectbox("Select Category", categories)
else:
  selected_category = "All"

# Filter 2: Numeric Slider for Sales or Profit
numeric_col = (
    "Sales" if "Sales" in df.columns else df.select_dtypes(include=["number"]).columns[0]
)
min_val = float(df[numeric_col].min())
max_val = float(df[numeric_col].max())
selected_range = st.sidebar.slider(
    f"Select {numeric_col} Range", min_val, max_val, (min_val, max_val)
)

# Apply Filters to DataFrame
filtered_df = df.copy()

if selected_category != "All" and "Category" in df.columns:
  filtered_df = filtered_df[filtered_df["Category"] == selected_category]

filtered_df = filtered_df[
    (filtered_df[numeric_col] >= selected_range[0])
    & (filtered_df[numeric_col] <= selected_range[1])
]

# 5. Display Summary Metrics
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label="Total Records", value=len(filtered_df))
with col2:
  total_numeric = (
      filtered_df[numeric_col].sum() if not filtered_df.empty else 0
  )
  st.metric(label=f"Total {numeric_col}", value=f"${total_numeric:,.2f}")
with col3:
  avg_numeric = (
      filtered_df[numeric_col].mean() if not filtered_df.empty else 0
  )
  st.metric(label=f"Average {numeric_col}", value=f"${avg_numeric:,.2f}")

# 6. Visualizations (3 Visualizations)
st.subheader("📈 Visualizations")

if filtered_df.empty:
  st.warning(
      "No data matches your selected filters. Please adjust the sidebar filters."
  )
else:
  # Visualization 1: Bar Chart
  st.markdown("### 1. Bar Chart Overview")
  if "Category" in df.columns:
    bar_data = (
        filtered_df.groupby("Category")[numeric_col].sum().reset_index()
    )
  else:
    bar_data = filtered_df.head(10)
  st.bar_chart(bar_data)

  # Visualization 2 & 3: Line Chart and Area Chart side-by-side
  ch1, ch2 = st.columns(2)
  with ch1:
    st.markdown("### 2. Line Chart Trend")
    if len(filtered_df) > 1:
      st.line_chart(filtered_df.select_dtypes(include=["number"]).head(30))
    else:
      st.write("Not enough data.")

  with ch2:
    st.markdown("### 3. Area Chart Distribution")
    if len(filtered_df) > 1:
      st.area_chart(filtered_df.select_dtypes(include=["number"]).head(30))
    else:
      st.write("Not enough data.")

# 7. Raw Data Table View
st.subheader("📋 Filtered Raw Data View")
st.dataframe(filtered_df, use_container_width=True)