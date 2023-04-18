from tech_news.database import db


# Requisito 10
def top_5_categories():
    pipeline = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$project": {"categoria": "$_id", "count": 1, "_id": 0}},
        {"$sort": {"count": -1, "categoria": 1}},
        {"$limit": 5}
    ]

    news = db.news.aggregate(pipeline)
    categories = [new["categoria"] for new in news]
    return categories
