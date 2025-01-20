from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mypal_database"]
courses_collection = db["courses"]

# Define the course metadata
courses = [
    {
        "course_name": "Cloud Foundations",
        "namespace": "cloud_foundations",
        "description": "Learn the basics of cloud computing, including core services and use cases.",
        "chapters": [
            {
                "chapter_name": "History of Cloud",
                "pdf_path": "data/courses/cloud_foundations/Chapitre1.pdf"
            },
            {
                "chapter_name": "Elastic Compute",
                "pdf_path": "data/courses/cloud_foundations/Chapitre2.pdf"
            },
            {
                "chapter_name": "Types of Cloud",
                "pdf_path": "data/courses/cloud_foundations/Chapitre3.pdf"
            },
            {
                "chapter_name": "Data Center Infrastructure",
                "pdf_path": "data/courses/cloud_foundations/Chapitre4.pdf"
            }
        ]
    }
]

# Insert into MongoDB
courses_collection.insert_many(courses)
print("Courses added successfully!")
