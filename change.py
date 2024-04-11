print("ASD Percentage:", asd_percentage)

# Define categories and corresponding recommended video links
categories = ["Mild", "Moderate", "Severe"]
video_links = [
    "https://example.com/mild_video",
    "https://example.com/moderate_video",
    "https://example.com/severe_video"
]

# Categorize based on ASD percentage
if asd_percentage < 50:
    print("Category: No Autism (ASD Percentage < 50%)")
elif 50 <= asd_percentage < 75:
    print("Category: Mild Autism (ASD Percentage 50-75%)")
    print("Recommended Video Link:", video_links[0])
elif 75 <= asd_percentage < 90:
    print("Category: Moderate Autism (ASD Percentage 75-90%)")
    print("Recommended Video Link:", video_links[1])
else:
    print("Category: Severe Autism (ASD Percentage >= 90%)")
    print("Recommended Video Link:", video_links[2])