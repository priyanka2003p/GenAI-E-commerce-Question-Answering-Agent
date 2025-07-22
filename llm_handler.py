def generate_sql_from_question(q):
    q = q.lower()
    
    if "total sales" in q:
        # From TotalSales table
        return "SELECT SUM(total_sales) FROM TotalSales;"
    
    elif "roas" in q or "return on ad spend" in q:
        # RoAS = ad_sales / ad_spend
        return "SELECT SUM(ad_sales)/SUM(ad_spend) AS RoAS FROM AdSales;"
    
    elif "highest cpc" in q:
        # CPC = ad_spend / clicks → we calculate it
        return """
        SELECT item_id, 
               (ad_spend * 1.0 / clicks) AS CPC 
        FROM AdSales 
        WHERE clicks > 0 
        ORDER BY CPC DESC 
        LIMIT 1;
        """
    
    else:
        return "SELECT 'Query not recognized';"
